"""
Import Hood CT Chest definitions from CDEStaging repository.

This script processes Markdown and JSON definitions from the hood_CT_chest directory,
matches them with existing models in the database, and either generates new models
or merges with existing ones.
"""

import argparse
import asyncio
import logging
import os
from pathlib import Path
from typing import Tuple, Optional, Dict, List

from dotenv import load_dotenv
from findingmodel import FindingModelFull
from findingmodel.common import model_file_name
from findingmodel.index import Index

from findingmodels.hood import (
    should_process_file,
    load_definition,
    generate_new_model,
    ensure_required_attributes,
    find_existing_model_with_specificity_check,
    merge_with_existing,
    apply_formatting_guidelines,
    extract_sub_findings
)

# Load environment variables
load_dotenv()

# Logger setup
logger = logging.getLogger(__name__)


async def process_single_file(
    file_path: Path,
    index: Index,
    output_dir: Path
) -> Tuple[bool, str, Optional[Dict], Optional[Dict], Optional[Dict], Optional[List[str]]]:
    """Process a single definition file.
    
    Args:
        file_path: Path to the definition file
        index: Database index
        output_dir: Output directory for generated models
        
    Returns:
        Tuple of (success, message, tracking_info, sub_finding_tracking_info, merge_tracking_info, missing_attributes)
    """
    try:
        filename = file_path.name
        logger.info(f"\nProcessing {filename}...")
        
        # Load definition - returns (data, markdown_content, file_type)
        data, markdown_content, file_type = await load_definition(file_path)
        
        # Generate model from definition: returns (FindingModelFull, missing_attributes)
        incoming_model, missing_attributes = await generate_new_model(file_path, data, markdown_content, file_type)
        logger.info(f"Generated model: {incoming_model.name}")
        if missing_attributes:
            logger.info(f"Missing attributes from source: {', '.join(missing_attributes)}")
        
        # Track merge/match information
        merge_tracking_info = {
            'finding_name': incoming_model.name,
            'match_found': False,
            'result': 'created_new',
            'existing_match': None,
            'merge_details': None
        }
        
        # Search for existing model with specificity check to reject too-general matches.
        # Specificity check uses LLM agent that determines if the existing model is too general compared to the incoming model.
        existing_match = await find_existing_model_with_specificity_check(incoming_model, index)
        
        if existing_match:
            logger.info(f"Found existing model: {existing_match.get('name')} ({existing_match.get('oifm_id')})")
            merge_tracking_info['match_found'] = True
            merge_tracking_info['existing_match'] = {
                'name': existing_match.get('name'),
                'oifm_id': existing_match.get('oifm_id')
            }
            
            # Merge with existing - now returns tuple (model, merge_details)
            final_model, merge_details = await merge_with_existing(incoming_model, existing_match, index)
            merge_tracking_info['result'] = 'merged'
            merge_tracking_info['merge_details'] = merge_details
            logger.info("Merged with existing model")
        else:
            logger.info("No match found, creating new model")
            final_model = incoming_model
            merge_tracking_info['result'] = 'created_new'
        
        # Ensure required attributes (returns tuple: model, tracking_info)
        final_model, tracking_info = await ensure_required_attributes(final_model)
        finding_name = final_model.name  # Store finding name for tracking
        
        # Apply formatting guidelines
        final_model = await apply_formatting_guidelines(final_model)
        
        # Extract sub-findings (returns tuple: (list of models, tracking_info))
        # Note: sub-findings are identified and logged but not saved as separate files
        all_models, sub_finding_tracking_info = await extract_sub_findings(final_model)
        
        # Save only the main model (first in list)
        main_model = all_models[0]
        output_file = output_dir / model_file_name(main_model.name)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            main_model.model_dump_json(indent=2, exclude_none=True),
            encoding='utf-8'
        )
        logger.info(f"Saved to {output_file.name}")
        
        # Log sub-findings that would be extracted (but aren't being saved)
        # Count from tracking info since sub-findings aren't returned in all_models
        extracted_count = len(sub_finding_tracking_info.get('extracted', [])) if sub_finding_tracking_info else 0
        kept_count = len(sub_finding_tracking_info.get('kept_with_presence', [])) if sub_finding_tracking_info else 0
        total_sub_findings = extracted_count + kept_count
        
        if total_sub_findings > 0:
            logger.info(f"Identified {total_sub_findings} sub-finding(s) for extraction (logged only, not saved)")
        
        return True, f"Successfully processed {filename}" + (f" (identified {total_sub_findings} sub-finding(s) for extraction)" if total_sub_findings > 0 else ""), tracking_info, sub_finding_tracking_info, merge_tracking_info, missing_attributes
        
    except Exception as e:
        error_msg = f"Error processing {file_path.name}: {str(e)}"
        logger.error(error_msg)
        import traceback
        traceback.print_exc()
        return False, error_msg, None, None, None, None


def generate_attribute_report(
    attribute_tracking: List[Tuple[str, str, Optional[Dict]]],
    merge_tracking: List[Tuple[str, str, Optional[Dict]]],
    missing_attributes_tracking: List[Tuple[str, str, List[str]]],
    input_dir: str,
    output_dir: str
) -> Path:
    """Generate a markdown report for attribute standardization and merge information.
    
    Args:
        attribute_tracking: List of (filename, finding_name, tracking_info) tuples
        merge_tracking: List of (filename, finding_name, merge_tracking_info) tuples
        missing_attributes_tracking: List of (filename, finding_name, missing_attrs) tuples
        input_dir: Input directory path
        output_dir: Output directory path
        
    Returns:
        Path to the generated report file
    """
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = Path(output_dir) / f"processing_report_{timestamp}.md"
    
    # Create lookup dict for merge tracking (use filename as key for better matching)
    merge_lookup = {}
    for filename, finding_name, info in merge_tracking:
        if info:
            # Store by both filename and finding_name for flexibility
            merge_lookup[filename] = info
            merge_lookup[finding_name.lower()] = info
    
    # Calculate statistics
    total_files = len(attribute_tracking)
    files_with_renamed = sum(1 for _, _, info in attribute_tracking 
                             if info and (info.get('presence', {}).get('action') in ['renamed', 'classification_used'] or
                                         info.get('change_from_prior', {}).get('action') in ['renamed', 'classification_used']))
    files_with_added = sum(1 for _, _, info in attribute_tracking 
                          if info and (info.get('presence', {}).get('action') == 'added' or
                                      info.get('change_from_prior', {}).get('action') == 'added'))
    
    # Merge statistics
    matches_found = sum(1 for _, _, info in merge_tracking if info and info.get('match_found'))
    merged_count = sum(1 for _, _, info in merge_tracking if info and info.get('result') == 'merged')
    created_new_count = sum(1 for _, _, info in merge_tracking if info and info.get('result') == 'created_new')
    
    # Presence statistics
    presence_exact = sum(1 for _, _, info in attribute_tracking 
                        if info and info.get('presence', {}).get('action') == 'exact_match')
    presence_renamed_heuristic = sum(1 for _, _, info in attribute_tracking 
                                    if info and info.get('presence', {}).get('action') == 'renamed')
    presence_renamed_classification = sum(1 for _, _, info in attribute_tracking 
                                         if info and info.get('presence', {}).get('action') == 'classification_used')
    presence_added = sum(1 for _, _, info in attribute_tracking 
                        if info and info.get('presence', {}).get('action') == 'added')
    
    # Change from prior statistics
    change_exact = sum(1 for _, _, info in attribute_tracking 
                      if info and info.get('change_from_prior', {}).get('action') == 'exact_match')
    change_renamed_heuristic = sum(1 for _, _, info in attribute_tracking 
                                   if info and info.get('change_from_prior', {}).get('action') == 'renamed')
    change_renamed_classification = sum(1 for _, _, info in attribute_tracking 
                                       if info and info.get('change_from_prior', {}).get('action') == 'classification_used')
    change_added = sum(1 for _, _, info in attribute_tracking 
                      if info and info.get('change_from_prior', {}).get('action') == 'added')
    
    # Build markdown content
    lines = [
        "# Hood Definition Processing Report - Attribute Standardization",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Input Directory:** {input_dir}",
        f"**Output Directory:** {output_dir}",
        "",
        "## Summary Statistics",
        "",
        f"- **Total files processed:** {total_files}",
        f"- **Matches found in database:** {matches_found}",
        f"- **Merged with existing:** {merged_count}",
        f"- **Created new:** {created_new_count}",
        f"- **Files with renamed attributes:** {files_with_renamed}",
        f"- **Files with added attributes:** {files_with_added}",
        "",
        "### Presence Attributes",
        f"- **Exact match (kept as-is):** {presence_exact}",
        f"- **Renamed (heuristic):** {presence_renamed_heuristic}",
        f"- **Renamed (classification agent):** {presence_renamed_classification}",
        f"- **Added (not found):** {presence_added}",
        "",
        "### Change from Prior Attributes",
        f"- **Exact match (kept as-is):** {change_exact}",
        f"- **Renamed (heuristic):** {change_renamed_heuristic}",
        f"- **Renamed (classification agent):** {change_renamed_classification}",
        f"- **Added (not found):** {change_added}",
        "",
    ]
    
    # Missing attributes statistics
    files_with_missing = len(missing_attributes_tracking)
    total_missing = sum(len(missing_attrs) for _, _, missing_attrs in missing_attributes_tracking)
    if files_with_missing > 0:
        lines.extend([
            "### Missing Attributes from Source",
            f"- **Files with missing attributes:** {files_with_missing}",
            f"- **Total missing attributes:** {total_missing}",
            "",
        ])
    
    lines.extend([
        "## Per-Finding Details",
        "",
    ])
    
    # Add per-finding details
    for filename, finding_name, tracking_info in sorted(attribute_tracking, key=lambda x: x[1].lower()):
        lines.append(f"### {finding_name} (`{filename}`)")
        
        # Merge/match information
        merge_info = merge_lookup.get(filename) or merge_lookup.get(finding_name.lower())
        if merge_info:
            if merge_info.get('match_found'):
                existing = merge_info.get('existing_match', {})
                lines.append(f"- **Database match:** Found - `{existing.get('name', 'unknown')}` (ID: {existing.get('oifm_id', 'N/A')})")
                if merge_info.get('result') == 'merged':
                    lines.append(f"- **Result:** Merged with existing model")
                    merge_details = merge_info.get('merge_details', {})
                    if merge_details:
                        lines.append(f"  - Attributes merged: {merge_details.get('attributes_merged', 0)}")
                        lines.append(f"  - Attributes added: {merge_details.get('attributes_added', 0)}")
                        lines.append(f"  - Attributes created: {merge_details.get('attributes_created', 0)}")
                        if merge_details.get('merge_recommendations'):
                            lines.append("  - Merged attributes:")
                            for mr in merge_details['merge_recommendations']:
                                lines.append(f"    - `{mr.get('existing_name')}` ← `{mr.get('incoming_name')}` ({mr.get('relationship')})")
                        if merge_details.get('new_attributes'):
                            lines.append(f"  - New attributes added: {', '.join([f'`{n}`' for n in merge_details['new_attributes']])}")
                else:
                    lines.append(f"- **Result:** {merge_info.get('result', 'unknown')}")
            else:
                lines.append(f"- **Database match:** Not found")
                lines.append(f"- **Result:** Created new model")
        else:
            lines.append(f"- **Database match:** Unknown")
            lines.append(f"- **Result:** Unknown")
        
        # Presence info
        if not tracking_info:
            lines.append("")
            continue
        presence_info = tracking_info.get('presence', {})
        presence_action = presence_info.get('action', 'unknown')
        presence_original = presence_info.get('original_name')
        
        if presence_action == 'exact_match':
            lines.append(f"- **Presence:** exact match (kept as-is)")
        elif presence_action in ['renamed', 'classification_used']:
            action_label = 'renamed (heuristic)' if presence_action == 'renamed' else 'renamed (classification agent)'
            lines.append(f"- **Presence:** {action_label} - Original: `{presence_original}`")
        elif presence_action == 'added':
            lines.append(f"- **Presence:** added (not found)")
        else:
            lines.append(f"- **Presence:** {presence_action}")
        
        # Change from prior info
        change_info = tracking_info.get('change_from_prior', {})
        change_action = change_info.get('action', 'unknown')
        change_original = change_info.get('original_name')
        
        if change_action == 'exact_match':
            lines.append(f"- **Change from prior:** exact match (kept as-is)")
        elif change_action in ['renamed', 'classification_used']:
            action_label = 'renamed (heuristic)' if change_action == 'renamed' else 'renamed (classification agent)'
            lines.append(f"- **Change from prior:** {action_label} - Original: `{change_original}`")
        elif change_action == 'added':
            lines.append(f"- **Change from prior:** added (not found)")
        else:
            lines.append(f"- **Change from prior:** {change_action}")
        
        # Missing attributes info
        missing_attrs_for_file = [missing_attrs for fn, _, missing_attrs in missing_attributes_tracking if fn == filename]
        if missing_attrs_for_file and missing_attrs_for_file[0]:
            lines.append(f"- **Missing attributes from source:** {', '.join(f'`{attr}`' for attr in missing_attrs_for_file[0])}")
        
        lines.append("")
    
    # Add separate section for missing attributes if any
    if missing_attributes_tracking:
        lines.extend([
            "",
            "## Missing Attributes from Source",
            "",
            "The following attributes were found in the source markdown but were not extracted into the final model:",
            "",
        ])
        
        for filename, finding_name, missing_attrs in sorted(missing_attributes_tracking, key=lambda x: x[1].lower()):
            if missing_attrs:
                lines.append(f"### {finding_name} (`{filename}`)")
                for attr in missing_attrs:
                    lines.append(f"- `{attr}`")
                lines.append("")
    
    # Write report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    
    return report_path


def generate_sub_finding_report(
    sub_finding_tracking: List[Tuple[str, str, Optional[Dict]]],
    input_dir: str,
    output_dir: str
) -> Path:
    """Generate markdown report for sub-finding extractions and presence additions.
    
    Args:
        sub_finding_tracking: List of (filename, finding_name, tracking_info) tuples
        input_dir: Input directory path
        output_dir: Output directory path
        
    Returns:
        Path to the generated report file
    """
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = Path(output_dir) / f"sub_finding_report_{timestamp}.md"
    
    # Calculate statistics
    total_files = len(sub_finding_tracking)
    files_with_extractions = sum(1 for _, _, info in sub_finding_tracking 
                                 if info and info.get('extracted'))
    files_with_kept = sum(1 for _, _, info in sub_finding_tracking 
                         if info and info.get('kept_with_presence'))
    total_extracted = sum(len(info.get('extracted', [])) for _, _, info in sub_finding_tracking if info)
    total_kept = sum(len(info.get('kept_with_presence', [])) for _, _, info in sub_finding_tracking if info)
    
    # Build markdown content
    lines = [
        "# Sub-Finding Extraction Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Input Directory:** {input_dir}",
        f"**Output Directory:** {output_dir}",
        "",
        "## Summary Statistics",
        "",
        f"- **Total files processed:** {total_files}",
        f"- **Files with extractions:** {files_with_extractions}",
        f"- **Files with kept components:** {files_with_kept}",
        f"- **Total components extracted:** {total_extracted}",
        f"- **Total components kept with presence:** {total_kept}",
        "",
        "## Per-Finding Details",
        "",
    ]
    
    # Add per-finding details
    for filename, finding_name, tracking_info in sorted(sub_finding_tracking, key=lambda x: x[1].lower()):
        if not tracking_info:
            continue
        
        lines.append(f"### {finding_name} (`{filename}`)")
        
        # Extracted components
        extracted = tracking_info.get('extracted', [])
        if extracted:
            lines.append("- **Extracted Components:**")
            for comp in extracted:
                comp_name = comp.get('component_name', 'unknown')
                new_name = comp.get('new_finding_name', 'unknown')
                attrs_moved = comp.get('attributes_moved', [])
                presence_kept = comp.get('presence_attribute_kept')
                lines.append(f"  - **{comp_name}**: Created separate finding `{new_name}`")
                if attrs_moved:
                    lines.append(f"    - Moved attributes: {', '.join(attrs_moved)}")
                if presence_kept:
                    lines.append(f"    - Kept in main: `{presence_kept}` (pointer/reference)")
        
        # Kept components
        kept = tracking_info.get('kept_with_presence', [])
        if kept:
            lines.append("- **Kept Components:**")
            for comp in kept:
                comp_name = comp.get('component_name', 'unknown')
                action = comp.get('presence_attribute_action', 'unknown')
                presence_name = comp.get('presence_attribute_name', 'unknown')
                if action == 'already_exists':
                    lines.append(f"  - **{comp_name}**: `{presence_name}` attribute already exists")
                elif action == 'added':
                    lines.append(f"  - **{comp_name}**: Added `{presence_name}` attribute")
        
        # No components found
        if tracking_info.get('no_components_found'):
            lines.append("- No components found")
        
        lines.append("")
    
    # Write report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    
    return report_path


async def process_hood_directory(input_dir: str, output_dir: str, limit: Optional[int] = None):
    """Process all definition files in the hood_CT_chest directory.
    
    Args:
        input_dir: Input directory path
        output_dir: Output directory path
        limit: Optional limit on number of files to process (for testing)
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get all files
    all_files = list(input_path.glob("*"))
    all_files = [f for f in all_files if f.is_file()]
    
    # Filter files to process
    files_to_process = [
        f for f in all_files
        if should_process_file(f, all_files)
    ]
    
    # Apply limit if specified (for testing)
    if limit is not None:
        files_to_process = files_to_process[:limit]
        logger.info(f"Limited to processing first {limit} files (testing mode)")
    
    # Track skipped files
    skipped_files = [
        f for f in all_files
        if not should_process_file(f, all_files) and (f.suffix == ".md" or f.suffix == ".json")
    ]
    
    logger.info(f"Starting to process files in: {input_dir}")
    logger.info(f"Total files found: {len(all_files)}")
    logger.info(f"Files to process: {len(files_to_process)}")
    logger.info(f"Files skipped: {len(skipped_files)}")
    if skipped_files:
        logger.info(f"Skipped files (JSON priority): {[f.name for f in skipped_files]}")
    logger.info("=" * 60)
    
    # Setup database index
    if os.getenv("DUCKDB_INDEX_PATH"):
        db_path = os.getenv("DUCKDB_INDEX_PATH")
        logger.info(f"Using database index at: {db_path}")
        index = Index(db_path=db_path)
    else:
        index = Index()
    await index.setup()
    
    # Process files
    successful_count = 0
    failed_count = 0
    results = []
    
    attribute_tracking: List[Tuple[str, str, Optional[Dict]]] = []  # (filename, finding_name, tracking_info)
    sub_finding_tracking: List[Tuple[str, str, Optional[Dict]]] = []  # (filename, finding_name, tracking_info)
    merge_tracking: List[Tuple[str, str, Optional[Dict]]] = []  # (filename, finding_name, merge_tracking_info)
    missing_attributes_tracking: List[Tuple[str, str, List[str]]] = []  # (filename, finding_name, missing_attrs)
    
    for file_path in files_to_process:
        success, message, tracking_info, sub_finding_info, merge_tracking_info, missing_attrs = await process_single_file(file_path, index, output_path)
        results.append((file_path.name, success, message))
        
        if success:
            successful_count += 1
            # Collect attribute tracking info if available
            if tracking_info:
                # Get finding name from tracking_info (it's stored in both presence and change_from_prior)
                finding_name = tracking_info.get('presence', {}).get('finding_name') or tracking_info.get('change_from_prior', {}).get('finding_name', 'unknown')
                attribute_tracking.append((file_path.name, finding_name, tracking_info))
            # Collect sub-finding tracking info if available
            if sub_finding_info:
                finding_name = sub_finding_info.get('finding_name', 'unknown')
                sub_finding_tracking.append((file_path.name, finding_name, sub_finding_info))
            # Collect merge tracking info if available
            if merge_tracking_info:
                finding_name = merge_tracking_info.get('finding_name', 'unknown')
                merge_tracking.append((file_path.name, finding_name, merge_tracking_info))
            # Collect missing attributes if available
            if missing_attrs:
                finding_name = tracking_info.get('presence', {}).get('finding_name') if tracking_info else 'unknown'
                if not finding_name or finding_name == 'unknown':
                    finding_name = merge_tracking_info.get('finding_name', 'unknown') if merge_tracking_info else 'unknown'
                missing_attributes_tracking.append((file_path.name, finding_name, missing_attrs))
        else:
            failed_count += 1
    
    # Generate attribute report (now includes merge info and missing attributes)
    if attribute_tracking:
        report_path = generate_attribute_report(attribute_tracking, merge_tracking, missing_attributes_tracking, input_dir, str(output_path))
        logger.info(f"\nAttribute standardization report saved to: {report_path}")
    
    # Generate sub-finding report
    if sub_finding_tracking:
        sub_report_path = generate_sub_finding_report(sub_finding_tracking, input_dir, str(output_path))
        logger.info(f"Sub-finding extraction report saved to: {sub_report_path}")
    
    # Calculate attribute statistics for console summary
    presence_renamed = sum(1 for _, _, info in attribute_tracking 
                          if info and info.get('presence', {}).get('action') in ['renamed', 'classification_used'])
    presence_added = sum(1 for _, _, info in attribute_tracking 
                        if info and info.get('presence', {}).get('action') == 'added')
    change_renamed = sum(1 for _, _, info in attribute_tracking 
                        if info and info.get('change_from_prior', {}).get('action') in ['renamed', 'classification_used'])
    change_added = sum(1 for _, _, info in attribute_tracking 
                      if info and info.get('change_from_prior', {}).get('action') == 'added')
    
    # Calculate sub-finding statistics for console summary
    total_extracted = sum(len(info.get('extracted', [])) for _, _, info in sub_finding_tracking if info)
    total_kept = sum(len(info.get('kept_with_presence', [])) for _, _, info in sub_finding_tracking if info)
    
    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("PROCESSING SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total files found: {len(all_files)}")
    logger.info(f"Files processed: {len(files_to_process)}")
    logger.info(f"Files skipped: {len(skipped_files)}")
    logger.info(f"Successfully processed: {successful_count}")
    logger.info(f"Failed: {failed_count}")
    logger.info(f"Success rate: {(successful_count/len(files_to_process)*100):.1f}%" if files_to_process else "N/A")
    logger.info("")
    logger.info("Attribute Standardization:")
    logger.info(f"  Presence attributes: {presence_renamed} renamed, {presence_added} added")
    logger.info(f"  Change from prior attributes: {change_renamed} renamed, {change_added} added")
    logger.info("")
    logger.info("Sub-Finding Extraction:")
    logger.info(f"  Components extracted: {total_extracted}")
    logger.info(f"  Components kept with presence: {total_kept}")
    logger.info("=" * 60)
    logger.info("Processing complete!")


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Import Hood CT Chest definitions from CDEStaging repository'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Set the logging level (default: INFO)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output (sets log level to DEBUG)'
    )
    parser.add_argument(
        '--input-dir',
        default='../CDEStaging/definitions/hood_CT_chest',
        help='Input directory containing Hood definitions (default: ../CDEStaging/definitions/hood_CT_chest)'
    )
    parser.add_argument(
        '--output-dir',
        default='defs/hood_final_models',
        help='Output directory for generated models (default: defs/hood_final_models)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Limit the number of files to process (for testing). Example: --limit 10'
    )
    
    args = parser.parse_args()
    
    # Configure logging
    log_level = logging.DEBUG if args.verbose else getattr(logging, args.log_level)
    logging.basicConfig(
        level=log_level,
        format='%(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Suppress noisy HTTP client debug logs
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore.http11").setLevel(logging.WARNING)
    logging.getLogger("httpcore.connection").setLevel(logging.WARNING)
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    limit = args.limit
    
    logger.info(f"Importing Hood definitions from {input_dir}")
    logger.info(f"Output directory: {output_dir}")
    if limit:
        logger.info(f"Processing limited to {limit} files (testing mode)")
    
    await process_hood_directory(input_dir, output_dir, limit=limit)


if __name__ == "__main__":
    asyncio.run(main())
