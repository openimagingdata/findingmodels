"""
Import Hood CT Chest definitions from CDEStaging repository.

This script processes Markdown and JSON definitions from the hood_CT_chest directory,
matches them with existing models in the database, and either generates new models
or merges with existing ones.
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from findingmodel import FindingModelFull, FindingModelBase, FindingInfo
from findingmodel.common import model_file_name
from findingmodel.tools import (
    find_similar_models,
    create_model_from_markdown,
    add_ids_to_model,
    add_standard_codes_to_model
)
from findingmodel.index import Index

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

# Import from scripts in same directory
try:
    from hood_json_adapter import HoodJsonAdapter
    from markdown_to_finding_model_adapter import MarkdownToFindingModelAdapter
    from merge_findings import (
        find_existing_model,
        get_existing_model_from_db,
        classify_and_group_attributes,
        compare_attributes_within_group
    )
    from merge_findings_helpers import (
        create_presence_element,
        create_change_element,
        build_final_finding,
        ensure_hood_contributor,
        reorder_attributes,
        preserve_existing_ids,
        extract_attr_name
    )
except ImportError:
    # Fallback: try with scripts. prefix
    from scripts.hood_json_adapter import HoodJsonAdapter
    from scripts.markdown_to_finding_model_adapter import MarkdownToFindingModelAdapter
    from scripts.merge_findings import (
        find_existing_model,
        get_existing_model_from_db,
        classify_and_group_attributes,
        compare_attributes_within_group
    )
    from scripts.merge_findings_helpers import (
        create_presence_element,
        create_change_element,
        build_final_finding,
        ensure_hood_contributor,
        reorder_attributes,
        preserve_existing_ids,
        extract_attr_name
    )

# Load environment variables
load_dotenv()

# Initialize the OpenAI model for specificity checking
model = OpenAIChatModel("gpt-4o-mini")

# Pydantic model for specificity check output
class SpecificityCheck(BaseModel):
    """Output from specificity checker"""
    is_too_general: bool = Field(description="True if existing match is too general (hypernym) compared to incoming term")
    confidence: float = Field(description="Confidence score (0.0 to 1.0)")
    reasoning: str = Field(description="Clear explanation of why existing is or isn't too general")


def create_specificity_check_agent() -> Agent[str, SpecificityCheck]:
    """Create agent for checking if an existing match is too general."""
    return Agent(
        model=model,
        output_type=SpecificityCheck,
        system_prompt="""You are a medical imaging expert specializing in radiology finding terminology.

Your task is to determine if an EXISTING finding model name is too general (a hypernym) compared to an INCOMING finding model name.

CRITICAL RULE: An existing match is "too general" if it represents a broader category that encompasses the incoming term, but the incoming term is more specific.

Examples of "too general" (should return is_too_general=True):
- Existing: "detectable hardware on chest X-ray" vs Incoming: "tunneled catheter" → TOO GENERAL
  (tunneled catheter is a specific type of hardware, but "detectable hardware" is too broad)
  
- Existing: "pulmonary finding" vs Incoming: "pulmonary nodule" → TOO GENERAL
  (pulmonary nodule is a specific type of pulmonary finding)

- Existing: "chest abnormality" vs Incoming: "pneumothorax" → TOO GENERAL
  (pneumothorax is a specific chest abnormality)

Examples of NOT "too general" (should return is_too_general=False):
- Existing: "pulmonary nodule" vs Incoming: "pulmonary nodule" → NOT TOO GENERAL (same)
- Existing: "pneumothorax" vs Incoming: "tension pneumothorax" → NOT TOO GENERAL (incoming is more specific, but existing is still appropriate)
- Existing: "mediastinal mass" vs Incoming: "anterior mediastinal mass" → NOT TOO GENERAL (incoming is a subtype, but existing is still specific enough)

KEY PRINCIPLES:
1. If the existing name contains very general terms like "detectable", "hardware", "device", "finding", "abnormality" without specificity, it's likely too general
2. If the existing name is a broad category and incoming is a specific instance, it's too general
3. If both are similarly specific (even if one is slightly more specific), it's NOT too general
4. Consider medical terminology: specific anatomical structures or conditions are preferred over generic terms

Provide a confidence score (0.0 to 1.0) and clear reasoning for your decision."""
    )


def should_process_file(file_path: Path, all_files: List[Path]) -> bool:
    """Determine if a file should be processed, considering JSON priority.
    
    Args:
        file_path: Path to the file to check
        all_files: List of all file paths in the directory
        
    Returns:
        True if file should be processed, False otherwise
    """
    if file_path.suffix == ".json":
        # Skip .cde.json files
        if file_path.name.endswith(".cde.json"):
            return False
        # Process JSON files (they take priority)
        return True
    
    elif file_path.suffix == ".md":
        # Only process MD if no corresponding JSON exists
        json_path = file_path.with_suffix(".json")
        if json_path in all_files:
            return False  # Skip MD, JSON will be processed instead
        return True  # Process MD, no JSON exists
    
    return False


async def load_definition(file_path: Path) -> Tuple[Optional[Dict], Optional[str], str]:
    """Load and parse a definition file (MD or JSON).
    
    Args:
        file_path: Path to the definition file
        
    Returns:
        Tuple of (data_dict, markdown_content, file_type)
        - data_dict: Parsed JSON data (if JSON) or None (if MD)
        - markdown_content: Markdown content (if MD) or None (if JSON)
        - file_type: "json" or "md"
    """
    file_type = file_path.suffix[1:]  # Remove the dot
    
    if file_type == "json":
        # Try multiple encodings to handle Unicode issues
        for encoding in ["utf-8", "latin-1", "cp1252"]:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    data = json.load(f)
                    return data, None, "json"
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        raise ValueError(f"Failed to load JSON file {file_path} with any encoding")
    
    elif file_type == "md":
        # Read markdown content
        for encoding in ["utf-8", "latin-1", "cp1252"]:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return None, content, "md"
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Failed to load Markdown file {file_path} with any encoding")
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


async def is_match_too_general(incoming_name: str, existing_name: str) -> bool:
    """Check if an existing match is too general (hypernym) compared to incoming term.
    
    Uses LLM to determine if existing match is a hypernym of incoming term.
    Example: "tunneled catheter" (specific) vs "detectable hardware on chest X-ray" (general)
    
    Args:
        incoming_name: Name of the incoming finding
        existing_name: Name of the existing finding
        
    Returns:
        True if existing is too general, False otherwise
    """
    try:
        agent = create_specificity_check_agent()
        prompt = f"""Compare these two finding model names:

INCOMING (new finding): "{incoming_name}"
EXISTING (matched finding): "{existing_name}"

Determine if the EXISTING finding name is too general (a hypernym) compared to the INCOMING finding name.
The existing name should be rejected as "too general" if it represents a broad category that encompasses the incoming term, but the incoming term is more specific.

Provide your analysis."""
        
        result = await agent.run(prompt)
        check_result = result.output
        
        if check_result.is_too_general:
            print(f"  [SPECIFICITY] Existing '{existing_name}' is too general for '{incoming_name}' (confidence: {check_result.confidence:.2f})")
            print(f"  [SPECIFICITY] Reasoning: {check_result.reasoning}")
        
        return check_result.is_too_general
        
    except Exception as e:
        print(f"  [WARN] Error in specificity check: {e}, using fallback heuristic")
        # Fallback to simple heuristic
        general_terms = ["detectable", "hardware", "device", "finding", "abnormality"]
        existing_lower = existing_name.lower()
        
        general_count = sum(1 for term in general_terms if term in existing_lower)
        if general_count >= 2:
            incoming_words = len(incoming_name.split())
            existing_words = len(existing_name.split())
            if incoming_words > existing_words:
                return True
        
        return False


async def find_existing_model_with_specificity_check(
    incoming_model: FindingModelFull,
    index: Index
) -> Optional[Dict]:
    """Search for existing model with specificity check to reject too-general matches.
    
    Args:
        incoming_model: The incoming finding model
        index: Database index
        
    Returns:
        Match dict if found and not too general, None otherwise
    """
    # First, find potential matches
    match = await find_existing_model(incoming_model, index)
    
    if match is None:
        return None
    
    # Check if the match is too general
    incoming_name = incoming_model.name
    existing_name = match.get('name', '')
    
    if await is_match_too_general(incoming_name, existing_name):
        print(f"  [SKIP] Rejected match '{existing_name}' as too general for '{incoming_name}'")
        return None
    
    return match


async def generate_new_model(
    file_path: Path,
    data: Optional[Dict],
    markdown_content: Optional[str],
    file_type: str
) -> FindingModelFull:
    """Generate a new finding model from MD or JSON.
    
    Args:
        file_path: Path to the source file
        data: Parsed JSON data (if JSON)
        markdown_content: Markdown content (if MD)
        file_type: "json" or "md"
        
    Returns:
        Generated FindingModelFull
    """
    if file_type == "json":
        # Use HoodJsonAdapter
        filename = file_path.name
        model = await HoodJsonAdapter.adapt_hood_json(data, filename)
        return model
    
    elif file_type == "md":
        # Extract finding name from filename
        filename = file_path.stem
        finding_name = filename.replace('-', ' ').replace('_', ' ').title()
        
        # Create basic finding info
        finding_info = FindingInfo(
            name=finding_name.lower(),
            description=""  # Will be generated by LLM
        )
        
        # Create complete model from markdown
        model = await create_model_from_markdown(
            finding_info,
            markdown_text=markdown_content
        )
        
        # Add IDs and codes
        full_model = add_ids_to_model(model, source="MGB")
        add_standard_codes_to_model(full_model)
        
        # Add contributors
        full_model.contributors = MarkdownToFindingModelAdapter._create_default_contributors()
        
        # Convert to FindingModelFull
        return FindingModelFull(**full_model.model_dump())
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


async def ensure_required_attributes(model: FindingModelFull) -> FindingModelFull:
    """Ensure presence and change_from_prior attributes exist.
    
    Args:
        model: The finding model
        
    Returns:
        Model with required attributes added if missing
    """
    # Convert to dict for easier manipulation
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    
    # Check for presence attribute
    has_presence = any(
        attr.get('name', '').lower() == 'presence'
        for attr in attributes
    )
    
    # Check for change_from_prior attribute
    has_change = any(
        attr.get('name', '').lower() == 'change from prior'
        for attr in attributes
    )
    
    # Add missing attributes
    if not has_presence:
        presence_attr = create_presence_element(model.name)
        attributes.insert(0, presence_attr)
        print(f"  [OK] Added presence attribute")
    
    if not has_change:
        change_attr = create_change_element(model.name)
        # Insert after presence if it exists, otherwise at beginning
        insert_pos = 1 if has_presence else 0
        attributes.insert(insert_pos, change_attr)
        print(f"  [OK] Added change_from_prior attribute")
    
    model_dict['attributes'] = attributes
    
    # Convert back to FindingModelBase, then add IDs, then to FindingModelFull
    from findingmodel import FindingModelBase
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    
    # Recreate model with IDs
    return FindingModelFull(**full_model.model_dump())


def apply_formatting_guidelines(model: FindingModelFull) -> FindingModelFull:
    """Apply formatting guidelines to the model.
    
    Rules:
    1. Lowercase: Convert model name, attribute names, and values to lowercase (except descriptions)
    2. Location attributes: Flag for review (keep but mark)
    3. Eponyms: Keep for now, mark for review
    
    Args:
        model: The finding model
        
    Returns:
        Model with formatting guidelines applied
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    
    # 1. Lowercase model name
    if model_dict.get('name'):
        model_dict['name'] = model_dict['name'].lower()
    
    # 2. Lowercase attribute names and values
    attributes = model_dict.get('attributes', [])
    for attr in attributes:
        # Lowercase attribute name
        if attr.get('name'):
            attr['name'] = attr['name'].lower()
        
        # Lowercase attribute values (if choice type)
        if attr.get('type') == 'choice' and attr.get('values'):
            for value in attr['values']:
                if value.get('name'):
                    value['name'] = value['name'].lower()
    
    # 3. Flag location attributes for review
    location_attrs = []
    for attr in attributes:
        attr_name = attr.get('name', '').lower()
        if 'location' in attr_name or 'anatomical location' in attr_name:
            location_attrs.append(attr_name)
    
    if location_attrs:
        print(f"  [NOTE] Location attributes flagged for review: {', '.join(location_attrs)}")
    
    # Recreate model
    return FindingModelFull(**model_dict)


async def merge_with_existing(
    incoming_model: FindingModelFull,
    existing_match: Dict,
    index: Index
) -> FindingModelFull:
    """Merge incoming model with existing model.
    
    Args:
        incoming_model: The incoming finding model
        existing_match: The existing model match dict
        index: Database index
        
    Returns:
        Merged FindingModelFull
    """
    # Load existing model from database
    existing_model_data = await get_existing_model_from_db(
        existing_match.get('oifm_id'),
        index
    )
    
    if not existing_model_data:
        raise ValueError(f"Failed to load existing model {existing_match.get('oifm_id')}")
    
    finding_name = incoming_model.name
    
    # Get attributes from both models
    incoming_attrs = []
    for attr in incoming_model.attributes or []:
        if isinstance(attr, dict):
            incoming_attrs.append(attr.copy())
        else:
            incoming_attrs.append(attr.model_dump(exclude_unset=False, exclude_none=False))
    
    existing_attrs = existing_model_data.get('attributes', [])
    
    # Classify and group attributes
    incoming_grouped = await classify_and_group_attributes(incoming_attrs, finding_name)
    existing_grouped = await classify_and_group_attributes(existing_attrs, finding_name)
    
    # Compare attributes within each classification group
    all_comparisons = {}
    for classification_type in ['presence', 'change_from_prior', 'other']:
        incoming_attrs_group = incoming_grouped.get(classification_type, [])
        existing_attrs_group = existing_grouped.get(classification_type, [])
        
        if incoming_attrs_group or existing_attrs_group:
            comparisons = await compare_attributes_within_group(
                incoming_attrs_group,
                existing_attrs_group,
                classification_type,
                finding_name
            )
            all_comparisons[classification_type] = comparisons
    
    # Collect merge recommendations
    merge_recommendations = []
    no_merge_comparisons = []
    needs_review_comparisons = []
    new_attributes = []
    ENHANCED_CONFIDENCE_THRESHOLD = 0.7
    
    for classification_type, comparisons in all_comparisons.items():
        for comparison in comparisons:
            relationship = comparison.get('relationship')
            
            if not relationship:
                # No relationship found - all comparisons were no_similarities -> new attribute
                new_attributes.append({
                    'incoming_attribute': comparison.get('incoming_attribute')
                })
                continue
            
            relationship_type = relationship.relationship if hasattr(relationship, 'relationship') else relationship.get('relationship')
            confidence = relationship.confidence if hasattr(relationship, 'confidence') else relationship.get('confidence', 0.0)
            
            if relationship_type == 'enhanced':
                if confidence >= ENHANCED_CONFIDENCE_THRESHOLD:
                    merge_recommendations.append({
                        'incoming_attribute': comparison.get('incoming_attribute'),
                        'existing_attribute': comparison.get('existing_attribute'),
                        'relationship': relationship
                    })
                else:
                    # Enhanced below threshold -> needs review
                    needs_review_comparisons.append({
                        'incoming_attribute': comparison.get('incoming_attribute'),
                        'existing_attribute': comparison.get('existing_attribute'),
                        'relationship': relationship,
                        'reason': f'Enhanced relationship but confidence ({confidence:.2f}) below threshold ({ENHANCED_CONFIDENCE_THRESHOLD})'
                    })
            elif relationship_type in ['identical', 'subset']:
                no_merge_comparisons.append({
                    'incoming_attribute': comparison.get('incoming_attribute'),
                    'existing_attribute': comparison.get('existing_attribute'),
                    'relationship': relationship
                })
            elif relationship_type == 'needs_review':
                needs_review_comparisons.append({
                    'incoming_attribute': comparison.get('incoming_attribute'),
                    'existing_attribute': comparison.get('existing_attribute'),
                    'relationship': relationship,
                    'reason': 'Attributes have shared values but each has unique values'
                })
            elif relationship_type == 'no_similarities':
                new_attributes.append({
                    'incoming_attribute': comparison.get('incoming_attribute')
                })
    
    # Check for presence/change_from_prior
    incoming_has_presence = any(
        attr.get('_classification') == 'presence'
        for attr_list in incoming_grouped.values()
        for attr in attr_list
    )
    existing_has_presence = any(
        attr.get('_classification') == 'presence'
        for attr_list in existing_grouped.values()
        for attr in attr_list
    )
    
    incoming_has_change = any(
        attr.get('_classification') == 'change_from_prior'
        for attr_list in incoming_grouped.values()
        for attr in attr_list
    )
    existing_has_change = any(
        attr.get('_classification') == 'change_from_prior'
        for attr_list in existing_grouped.values()
        for attr in attr_list
    )
    
    # Process new attributes - extract just the attribute dicts
    approved_new_attributes = []
    for new_attr_info in new_attributes:
        approved_new_attributes.append(new_attr_info.get('incoming_attribute'))
    
    # Add missing attributes
    attributes_to_add = []
    if not incoming_has_presence and not existing_has_presence:
        presence_attr = create_presence_element(finding_name)
        attributes_to_add.append(('presence', presence_attr))
    
    if not incoming_has_change and not existing_has_change:
        change_attr = create_change_element(finding_name)
        attributes_to_add.append(('change_from_prior', change_attr))
    
    # Auto-approve needs_review for now (can be enhanced later)
    review_decisions = []
    for review_comp in needs_review_comparisons:
        # Auto-merge for now (can be made interactive later)
        review_decisions.append({
            'incoming_attribute': review_comp.get('incoming_attribute'),
            'existing_attribute': review_comp.get('existing_attribute'),
            'decision': 'merge_values'  # Auto-merge
        })
    
    # Build final finding
    final_finding = build_final_finding(
        existing_model_data=existing_model_data,
        incoming_model=incoming_model,
        merge_recommendations=merge_recommendations,
        attributes_to_add=attributes_to_add,
        approved_new_attributes=approved_new_attributes,
        review_decisions=review_decisions
    )
    
    # Ensure Hood contributor
    final_finding = ensure_hood_contributor(final_finding)
    
    # Reorder attributes
    final_finding = reorder_attributes(final_finding)
    
    # Preserve existing IDs
    final_finding = preserve_existing_ids(final_finding, source="MGB")
    
    # Convert back to FindingModelFull
    return FindingModelFull(**final_finding)


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
        print(f"\nProcessing {filename}...")
        
        # Load definition
        data, markdown_content, file_type = await load_definition(file_path)
        
        # Generate model from definition
        incoming_model = await generate_new_model(file_path, data, markdown_content, file_type)
        print(f"  [OK] Generated model: {incoming_model.name}")
        
        # Lookup existing model with specificity check
        existing_match = await find_existing_model_with_specificity_check(incoming_model, index)
        
        if existing_match:
            print(f"  [OK] Found existing model: {existing_match.get('name')} ({existing_match.get('oifm_id')})")
            # Merge with existing
            final_model = await merge_with_existing(incoming_model, existing_match, index)
            print(f"  [OK] Merged with existing model")
        else:
            print(f"  [OK] No match found, creating new model")
            final_model = incoming_model
        
        # Ensure required attributes
        final_model = await ensure_required_attributes(final_model)
        
        # Apply formatting guidelines
        final_model = apply_formatting_guidelines(final_model)
        
        # Save model
        output_file = output_dir / model_file_name(final_model.name)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            final_model.model_dump_json(indent=2, exclude_none=True),
            encoding='utf-8'
        )
        
        print(f"  [OK] Saved to {output_file.name}")
        return True, f"Successfully processed {filename}"
        
    except Exception as e:
        error_msg = f"Error processing {file_path.name}: {str(e)}"
        print(f"  [ERROR] {error_msg}")
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
    
    print(f"Starting to process files in: {input_dir}")
    print(f"Total files found: {len(all_files)}")
    print(f"Files to process: {len(files_to_process)}")
    print(f"Files skipped: {len(skipped_files)}")
    if skipped_files:
        print(f"Skipped files (JSON priority): {[f.name for f in skipped_files]}")
    print("=" * 60)
    
    # Setup database index
    index = Index()
    if os.getenv("DUCKDB_INDEX_PATH"):
        db_path = os.getenv("DUCKDB_INDEX_PATH")
        print(f"Using database index at: {db_path}")
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
    print("\n" + "=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total files found: {len(all_files)}")
    print(f"Files processed: {len(files_to_process)}")
    print(f"Files skipped: {len(skipped_files)}")
    print(f"Successfully processed: {successful_count}")
    print(f"Failed: {failed_count}")
    print(f"Success rate: {(successful_count/len(files_to_process)*100):.1f}%" if files_to_process else "N/A")
    print("=" * 60)
    print("Processing complete!")


async def main():
    """Main entry point."""
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/hood_findings"
    
    print(f"Importing Hood definitions from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    await process_hood_directory(input_dir, output_dir)


if __name__ == "__main__":
    asyncio.run(main())

