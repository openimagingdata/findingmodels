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
from typing import Tuple

from dotenv import load_dotenv
from findingmodel import FindingModelFull
from findingmodel.common import model_file_name
from findingmodel.index import Index

from scripts.hood_helpers import (
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
) -> Tuple[bool, str]:
    """Process a single definition file.
    
    Args:
        file_path: Path to the definition file
        index: Database index
        output_dir: Output directory for generated models
        
    Returns:
        Tuple of (success, message)
    """
    try:
        filename = file_path.name
        logger.info(f"\nProcessing {filename}...")
        
        # Load definition - returns (data, markdown_content, file_type)
        data, markdown_content, file_type = await load_definition(file_path)
        
        # Generate model from definition: generated FindingModelFull
        incoming_model = await generate_new_model(file_path, data, markdown_content, file_type)
        logger.info(f"Generated model: {incoming_model.name}")
        
        # Search for existing model with specificity check to reject too-general matches.
        # Specificity check uses LLM agent that determines if the existing model is too general compared to the incoming model.
        existing_match = await find_existing_model_with_specificity_check(incoming_model, index)
        
        if existing_match:
            logger.info(f"Found existing model: {existing_match.get('name')} ({existing_match.get('oifm_id')})")
            # Merge with existing
            final_model = await merge_with_existing(incoming_model, existing_match, index)
            logger.info("Merged with existing model")
        else:
            logger.info("No match found, creating new model")
            final_model = incoming_model
        
        # Ensure required attributes
        final_model = await ensure_required_attributes(final_model)
        
        # Apply formatting guidelines
        final_model = await apply_formatting_guidelines(final_model)
        
        # Extract sub-findings (returns list: [main_model, sub_finding_1, ...])
        all_models = await extract_sub_findings(final_model)
        
        # Save all models (main + any sub-findings)
        saved_count = 0
        for model in all_models:
            output_file = output_dir / model_file_name(model.name)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(
                model.model_dump_json(indent=2, exclude_none=True),
                encoding='utf-8'
            )
            saved_count += 1
            logger.info(f"Saved to {output_file.name}")
        
        if saved_count > 1:
            logger.info(f"Extracted {saved_count - 1} sub-finding(s) from {filename}")
        
        return True, f"Successfully processed {filename}" + (f" (extracted {saved_count - 1} sub-finding(s))" if saved_count > 1 else "")
        
    except Exception as e:
        error_msg = f"Error processing {file_path.name}: {str(e)}"
        logger.error(error_msg)
        import traceback
        traceback.print_exc()
        return False, error_msg


async def process_hood_directory(input_dir: str, output_dir: str):
    """Process all definition files in the hood_CT_chest directory.
    
    Args:
        input_dir: Input directory path
        output_dir: Output directory path
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
    index = Index()
    if os.getenv("DUCKDB_INDEX_PATH"):
        db_path = os.getenv("DUCKDB_INDEX_PATH")
        logger.info(f"Using database index at: {db_path}")
    await index.setup()
    
    # Process files
    successful_count = 0
    failed_count = 0
    results = []
    
    for file_path in files_to_process:
        success, message = await process_single_file(file_path, index, output_path)
        results.append((file_path.name, success, message))
        
        if success:
            successful_count += 1
        else:
            failed_count += 1
    
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
        default='defs/hood_findings',
        help='Output directory for generated models (default: defs/hood_findings)'
    )
    
    args = parser.parse_args()
    
    # Configure logging
    log_level = logging.DEBUG if args.verbose else getattr(logging, args.log_level)
    logging.basicConfig(
        level=log_level,
        format='%(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    logger.info(f"Importing Hood definitions from {input_dir}")
    logger.info(f"Output directory: {output_dir}")
    
    await process_hood_directory(input_dir, output_dir)


if __name__ == "__main__":
    asyncio.run(main())
