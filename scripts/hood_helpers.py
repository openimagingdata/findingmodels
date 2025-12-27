"""
Helper functions for Hood definition processing.

This module contains all utility functions organized by responsibility:
- File I/O operations
- Model generation and validation
- Model matching and specificity checking
- Merge processing
- Formatting and transformation
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from findingmodel import FindingModelFull, FindingModelBase, FindingInfo
from findingmodel.index import Index
from findingmodel.tools import (
    create_model_from_markdown,
    add_ids_to_model,
    add_standard_codes_to_model
)

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
    preserve_existing_ids
)
from agents.specificity_agents import create_specificity_check_agent
from agents.formatting_agents import (
    create_acronym_expansion_agent,
    create_eponym_minimization_agent,
    create_sub_finding_extraction_agent
)

logger = logging.getLogger(__name__)

# ============================================================================
# CONSTANTS
# ============================================================================

SUPPORTED_ENCODINGS = ["utf-8", "latin-1", "cp1252"]
ENHANCED_CONFIDENCE_THRESHOLD = 0.7
CLASSIFICATION_TYPES = ['presence', 'change_from_prior', 'other']


# ============================================================================
# FILE I/O OPERATIONS
# ============================================================================

def should_process_file(file_path: Path, all_files: List[Path]) -> bool:
    """Determine if a file should be processed, some files have MD and JSON versions.
    
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
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    data = json.load(f)
                    return data, None, "json"
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        raise ValueError(f"Failed to load JSON file {file_path} with any encoding")
    
    elif file_type == "md":
        # Read markdown content
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return None, content, "md"
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Failed to load Markdown file {file_path} with any encoding")
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


# ============================================================================
# MODEL GENERATION AND VALIDATION
# ============================================================================

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
        logger.info("Added presence attribute")
    
    if not has_change:
        change_attr = create_change_element(model.name)
        # Insert after presence if it exists, otherwise at beginning
        insert_pos = 1 if has_presence else 0
        attributes.insert(insert_pos, change_attr)
        logger.info("Added change_from_prior attribute")
    
    model_dict['attributes'] = attributes
    
    # Convert back to FindingModelBase, then add IDs, then to FindingModelFull
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    
    # Recreate model with IDs
    return FindingModelFull(**full_model.model_dump())


# ============================================================================
# MODEL MATCHING AND SPECIFICITY CHECKING
# ============================================================================

async def is_match_too_general(specific_term: str, general_term: str) -> bool:
    """Check if general_term is too general (hypernym) compared to specific_term.
    
    Uses LLM to determine if general_term is a hypernym of specific_term.
    This function works bidirectionally - it checks if the second parameter is
    too general compared to the first parameter.
    
    Example: "tunneled catheter" (specific) vs "detectable hardware on chest X-ray" (general)
    
    Args:
        specific_term: The more specific finding name (reference term)
        general_term: The potentially general finding name (to check)
        
    Returns:
        True if general_term is too general compared to specific_term, False otherwise
    """
    try:
        agent = create_specificity_check_agent()
        prompt = f"""Compare these two finding model names:

TERM 1 (reference): "{specific_term}"
TERM 2 (to check): "{general_term}"

Determine if TERM 2 is too general (a hypernym) compared to TERM 1.
TERM 2 should be considered "too general" if it represents a broad category that encompasses TERM 1, but TERM 1 is more specific.

Provide your analysis."""
        
        result = await agent.run(prompt)
        check_result = result.output
        
        if check_result.is_too_general:
            logger.debug(f"'{general_term}' is too general for '{specific_term}' (confidence: {check_result.confidence:.2f})")
            logger.debug(f"Reasoning: {check_result.reasoning}")
        
        return check_result.is_too_general
        
    except Exception as e:
        logger.warning(f"Error in specificity check: {e}, using fallback heuristic")
        # Fallback to simple heuristic
        general_terms = ["detectable", "hardware", "device", "finding", "abnormality"]
        general_term_lower = general_term.lower()
        
        general_count = sum(1 for term in general_terms if term in general_term_lower)
        if general_count >= 2:
            specific_words = len(specific_term.split())
            general_words = len(general_term.split())
            if specific_words > general_words:
                return True
        
        return False


async def find_existing_model_with_specificity_check(
    incoming_model: FindingModelFull,
    index: Index
) -> Optional[Dict]:
    """Search for existing model with specificity check to reject too-general matches.
    
    Rejects matches if either the existing term is too general for the incoming term,
    or if the incoming term is too general for the existing term. This prevents
    merging specific findings with overly general ones in either direction.
    
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
    
    # Check if the match is too general (bidirectional check)
    incoming_name = incoming_model.name
    existing_name = match.get('name', '')
    
    # Check if existing is too general for incoming
    if await is_match_too_general(incoming_name, existing_name):
        logger.info(f"Rejected match '{existing_name}' as too general for '{incoming_name}'")
        return None
    
    # Check if incoming is too general for existing (reverse check)
    if await is_match_too_general(existing_name, incoming_name):
        logger.info(f"Rejected match: incoming '{incoming_name}' is too general for existing '{existing_name}'")
        return None
    
    return match


# ============================================================================
# MERGE PROCESSING
# ============================================================================

def _collect_merge_recommendations(all_comparisons: Dict) -> Dict:
    """Process comparisons and categorize merge recommendations.
    
    Args:
        all_comparisons: Dict of comparisons by classification type
        
    Returns:
        Dict with keys: merge_recommendations, no_merge_comparisons, 
        needs_review_comparisons, new_attributes
    """
    merge_recommendations = []
    no_merge_comparisons = []
    needs_review_comparisons = []
    new_attributes = []
    
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
    
    return {
        'merge_recommendations': merge_recommendations,
        'no_merge_comparisons': no_merge_comparisons,
        'needs_review_comparisons': needs_review_comparisons,
        'new_attributes': new_attributes
    }


def _check_required_attributes(incoming_grouped: Dict, existing_grouped: Dict) -> Dict:
    """Check for presence and change_from_prior in both models.
    
    Args:
        incoming_grouped: Grouped attributes from incoming model
        existing_grouped: Grouped attributes from existing model
        
    Returns:
        Dict with keys: incoming_has_presence, existing_has_presence,
        incoming_has_change, existing_has_change
    """
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
    
    return {
        'incoming_has_presence': incoming_has_presence,
        'existing_has_presence': existing_has_presence,
        'incoming_has_change': incoming_has_change,
        'existing_has_change': existing_has_change
    }


def _prepare_merge_data(
    new_attributes: List[Dict],
    needs_review_comparisons: List[Dict],
    incoming_has_presence: bool,
    existing_has_presence: bool,
    incoming_has_change: bool,
    existing_has_change: bool,
    finding_name: str
) -> Dict:
    """Prepare data structures for merge.
    
    Args:
        new_attributes: List of new attribute info dicts
        needs_review_comparisons: List of comparisons needing review
        incoming_has_presence: Whether incoming model has presence attribute
        existing_has_presence: Whether existing model has presence attribute
        incoming_has_change: Whether incoming model has change_from_prior attribute
        existing_has_change: Whether existing model has change_from_prior attribute
        finding_name: Name of the finding
        
    Returns:
        Dict with keys: approved_new_attributes, attributes_to_add, review_decisions
    """
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
    
    return {
        'approved_new_attributes': approved_new_attributes,
        'attributes_to_add': attributes_to_add,
        'review_decisions': review_decisions
    }


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
    for classification_type in CLASSIFICATION_TYPES:
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
    merge_data = _collect_merge_recommendations(all_comparisons)
    merge_recommendations = merge_data['merge_recommendations']
    no_merge_comparisons = merge_data['no_merge_comparisons']
    needs_review_comparisons = merge_data['needs_review_comparisons']
    new_attributes = merge_data['new_attributes']
    
    # Check for presence/change_from_prior
    required_attrs = _check_required_attributes(incoming_grouped, existing_grouped)
    incoming_has_presence = required_attrs['incoming_has_presence']
    existing_has_presence = required_attrs['existing_has_presence']
    incoming_has_change = required_attrs['incoming_has_change']
    existing_has_change = required_attrs['existing_has_change']
    
    # Prepare merge data
    merge_prep = _prepare_merge_data(
        new_attributes,
        needs_review_comparisons,
        incoming_has_presence,
        existing_has_presence,
        incoming_has_change,
        existing_has_change,
        finding_name
    )
    approved_new_attributes = merge_prep['approved_new_attributes']
    attributes_to_add = merge_prep['attributes_to_add']
    review_decisions = merge_prep['review_decisions']
    
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


# ============================================================================
# FORMATTING AND TRANSFORMATION
# ============================================================================

async def expand_acronyms_and_add_synonyms(model: FindingModelFull) -> FindingModelFull:
    """Expand acronyms in model name and add synonym forms.
    
    Rule: Model names should have acronyms spelled out, with synonyms
    including the compact form (e.g., "anterior cruciate ligament tear"
    with "ACL tear" as synonym).
    
    Args:
        model: The finding model to process
        
    Returns:
        Model with expanded name and synonyms added
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    original_name = model_dict.get('name', '')
    
    if not original_name:
        return model
    
    try:
        # Use LLM agent to expand acronyms
        agent = create_acronym_expansion_agent()
        prompt = f"""Expand acronyms in this finding model name: "{original_name}"

Detect all medical acronyms, expand them to full terms, and identify compact forms for synonyms."""
        
        result = await agent.run(prompt)
        expansion_result = result.output
        
        # Update model with expanded name
        if expansion_result.expanded_name and expansion_result.expanded_name.lower() != original_name.lower():
            model_dict['name'] = expansion_result.expanded_name.lower()
            
            # Initialize synonyms array if it doesn't exist
            if model_dict.get('synonyms') is None:
                model_dict['synonyms'] = []
            
            # Add compact forms to synonyms
            synonyms = model_dict.get('synonyms', []) or []
            for compact_form in expansion_result.compact_forms:
                compact_lower = compact_form.lower()
                if compact_lower not in [s.lower() for s in synonyms]:
                    synonyms.append(compact_lower)
            
            model_dict['synonyms'] = synonyms
            
            logger.debug(f"Expanded acronyms in '{original_name}' → '{expansion_result.expanded_name}' (confidence: {expansion_result.confidence:.2f})")
        
    except Exception as e:
        logger.warning(f"Error in acronym expansion for '{original_name}': {e}, keeping original name")
        # Fallback: return model unchanged
    
    # Recreate model
    return FindingModelFull(**model_dict)


def transform_location_attributes(model: FindingModelFull) -> FindingModelFull:
    """Transform location attributes to anatomic location subsets.
    
    Rule: Location should be expressed as where the finding could occur
    (subset of anatomic location nodes), not as separate attributes.
    
    Args:
        model: The finding model to process
        
    Returns:
        Model with location attributes transformed
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    
    # Identify and remove location attributes
    # Location should not be a separate attribute per the requirements
    filtered_attributes = []
    for attr in attributes:
        attr_name = attr.get('name', '').lower()
        # Remove attributes with "location" or "anatomical location" in name
        if 'location' not in attr_name and 'anatomical location' not in attr_name:
            filtered_attributes.append(attr)
    
    model_dict['attributes'] = filtered_attributes
    
    # Note: Location information is implicit in the finding name
    # (e.g., "pulmonary nodule" implies lung location)
    # If explicit anatomic location subset representation is needed,
    # it would require schema extension or index_codes mapping
    
    # Recreate model
    return FindingModelFull(**model_dict)


def remove_associated_findings(model: FindingModelFull) -> FindingModelFull:
    """Remove associated findings attributes.
    
    Rule: Avoid "associated findings" attributes; ensure definitions exist
    for associated items separately.
    
    Args:
        model: The finding model to process
        
    Returns:
        Model with associated findings attributes removed
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    
    # Filter out attributes with "associated" in name (case-insensitive)
    filtered_attributes = [
        attr for attr in attributes
        if 'associated' not in attr.get('name', '').lower()
    ]
    
    model_dict['attributes'] = filtered_attributes
    
    # Recreate model
    return FindingModelFull(**model_dict)


async def minimize_eponyms(model: FindingModelFull) -> FindingModelFull:
    """Minimize eponyms and ensure they are not preferred terms.
    
    Rule: Eponyms can be uppercase but should be minimized and should NOT
    be the preferred term if possible.
    
    Args:
        model: The finding model to process
        
    Returns:
        Model with eponyms minimized
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    original_name = model_dict.get('name', '')
    
    if not original_name:
        return model
    
    try:
        # Use LLM agent to minimize eponyms
        agent = create_eponym_minimization_agent()
        prompt = f"""Minimize eponyms in this finding model name: "{original_name}"

Detect any eponyms, replace with descriptive terms if appropriate, and keep original as synonym."""
        
        result = await agent.run(prompt)
        eponym_result = result.output
        
        # Update model if eponym was found and replaced
        if eponym_result.has_eponym and eponym_result.descriptive_name.lower() != original_name.lower():
            model_dict['name'] = eponym_result.descriptive_name.lower()
            
            # Initialize synonyms array if it doesn't exist
            if model_dict.get('synonyms') is None:
                model_dict['synonyms'] = []
            
            # Add original eponym form to synonyms
            if eponym_result.eponym_synonym:
                synonyms = model_dict.get('synonyms', []) or []
                eponym_lower = eponym_result.eponym_synonym.lower()
                if eponym_lower not in [s.lower() for s in synonyms]:
                    synonyms.append(eponym_lower)
                model_dict['synonyms'] = synonyms
            
            logger.debug(f"Minimized eponym in '{original_name}' → '{eponym_result.descriptive_name}' (confidence: {eponym_result.confidence:.2f})")
        
    except Exception as e:
        logger.warning(f"Error in eponym minimization for '{original_name}': {e}, keeping original name")
        # Fallback: return model unchanged
    
    # Recreate model
    return FindingModelFull(**model_dict)


async def extract_sub_findings(model: FindingModelFull) -> List[FindingModelFull]:
    """Extract detailed sub-findings as separate models.
    
    Rule: If something looks like a detailed sub-finding with multiple
    properties, extract it as a separate finding.
    
    Example: "solid component of mixed pulmonary nodule" should be separate
    from "pulmonary nodule".
    
    Args:
        model: The finding model to process
        
    Returns:
        List of finding models (original + extracted sub-findings)
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    finding_name = model_dict.get('name', '')
    attributes = model_dict.get('attributes', [])
    
    try:
        # Use LLM agent to determine if sub-findings should be extracted
        agent = create_sub_finding_extraction_agent()
        
        # Prepare model information for the agent
        attributes_summary = []
        for attr in attributes:
            attr_info = {
                'name': attr.get('name', ''),
                'type': attr.get('type', ''),
                'description': attr.get('description', '')
            }
            if attr.get('type') == 'choice' and attr.get('values'):
                attr_info['values'] = [v.get('name', '') for v in attr.get('values', [])]
            attributes_summary.append(attr_info)
        
        prompt = f"""Analyze this finding model to determine if sub-findings should be extracted:

Finding Name: "{finding_name}"
Description: "{model_dict.get('description', '')}"
Attributes: {json.dumps(attributes_summary, indent=2)}

Determine if any attributes represent detailed sub-findings that should be extracted as separate models."""
        
        result = await agent.run(prompt)
        extraction_result = result.output
        
        # If no extraction needed, return original model
        if not extraction_result.should_extract or not extraction_result.sub_findings:
            logger.debug(f"No sub-findings to extract for '{finding_name}'")
            return [model]
        
        logger.info(f"Extracting {len(extraction_result.sub_findings)} sub-finding(s) from '{finding_name}': {extraction_result.reasoning}")
        
        # Step 1: Create mapping of attribute names to full attribute objects
        attr_name_to_obj = {}
        for attr in attributes:
            attr_name = attr.get('name', '').lower()
            attr_name_to_obj[attr_name] = attr
        
        # Step 2: Create sub-finding models
        sub_finding_models = []
        for sub_finding_def in extraction_result.sub_findings:
            sub_finding_name = sub_finding_def.get('name', '').lower()
            sub_finding_description = sub_finding_def.get('description', '')
            sub_finding_attr_names = sub_finding_def.get('attributes', [])
            
            # Collect attributes for this sub-finding
            sub_finding_attributes = []
            for attr_name in sub_finding_attr_names:
                attr_name_lower = attr_name.lower()
                if attr_name_lower in attr_name_to_obj:
                    # Deep copy the attribute to avoid modifying original
                    attr_copy = json.loads(json.dumps(attr_name_to_obj[attr_name_lower]))
                    sub_finding_attributes.append(attr_copy)
                else:
                    logger.warning(f"Attribute '{attr_name}' not found in original model for sub-finding '{sub_finding_name}'")
            
            # Create sub-finding model dict
            sub_finding_dict = {
                'name': sub_finding_name,
                'description': sub_finding_description,
                'attributes': sub_finding_attributes,
                'contributors': model_dict.get('contributors', []),
                'index_codes': model_dict.get('index_codes'),
                'tags': model_dict.get('tags'),
                'synonyms': model_dict.get('synonyms')
            }
            
            # Convert to FindingModelBase, add IDs, then to FindingModelFull
            try:
                base_model = FindingModelBase(**sub_finding_dict)
                model_with_ids = add_ids_to_model(base_model, source="MGB")
                sub_finding_model = FindingModelFull(**model_with_ids.model_dump())
                
                # Ensure required attributes (presence, change_from_prior)
                sub_finding_model = await ensure_required_attributes(sub_finding_model)
                
                sub_finding_models.append(sub_finding_model)
                logger.info(f"Created sub-finding: '{sub_finding_name}' with {len(sub_finding_attributes)} attributes")
            except Exception as e:
                logger.error(f"Error creating sub-finding '{sub_finding_name}': {e}")
                continue
        
        # Step 3: Modify main model - keep only attributes in main_model_attributes
        main_attr_names_lower = {name.lower() for name in extraction_result.main_model_attributes}
        main_model_attributes = []
        for attr in attributes:
            attr_name_lower = attr.get('name', '').lower()
            if attr_name_lower in main_attr_names_lower:
                main_model_attributes.append(attr)
        
        # Update main model dict
        modified_main_dict = model_dict.copy()
        modified_main_dict['attributes'] = main_model_attributes
        
        # Convert back to FindingModelFull
        try:
            base_model = FindingModelBase(**modified_main_dict)
            model_with_ids = add_ids_to_model(base_model, source="MGB")
            modified_main_model = FindingModelFull(**model_with_ids.model_dump())
            
            logger.info(f"Modified main model '{finding_name}': kept {len(main_model_attributes)} attributes, removed {len(attributes) - len(main_model_attributes)} component-specific attributes")
        except Exception as e:
            logger.error(f"Error modifying main model: {e}, returning original")
            return [model]
        
        # Step 4: Return list with modified main model and all sub-findings
        return [modified_main_model] + sub_finding_models
        
    except Exception as e:
        logger.warning(f"Error in sub-finding extraction for '{finding_name}': {e}, returning original model")
        import traceback
        traceback.print_exc()
        # Fallback: return original model
        return [model]


def _flag_location_attributes(model: FindingModelFull) -> List[str]:
    """Extract location attribute names for flagging.
    
    Args:
        model: The finding model to check
        
    Returns:
        List of location attribute names found
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    location_attrs = []
    for attr in attributes:
        attr_name = attr.get('name', '').lower()
        if 'location' in attr_name or 'anatomical location' in attr_name:
            location_attrs.append(attr_name)
    return location_attrs


async def apply_formatting_guidelines(model: FindingModelFull) -> FindingModelFull:
    """Apply formatting guidelines to the model.
    
    Rules:
    1. Lowercase: Convert model name, attribute names, and values to lowercase (except descriptions)
    2. Remove associated findings attributes
    3. Expand acronyms and add synonyms
    4. Transform location attributes to anatomic location subsets
    5. Minimize eponyms
    
    Args:
        model: The finding model
        
    Returns:
        Model with formatting guidelines applied
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    
    # 1. Lowercase model name, attribute names, and values
    if model_dict.get('name'):
        model_dict['name'] = model_dict['name'].lower()
    
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
    
    # Recreate model for helper functions
    model = FindingModelFull(**model_dict)
    
    # 2. Remove associated findings (clean up first) - simple rule-based
    model = remove_associated_findings(model)
    
    # 3. Expand acronyms and add synonyms - uses LLM agent
    model = await expand_acronyms_and_add_synonyms(model)
    
    # 4. Transform location attributes - simple rule-based
    model = transform_location_attributes(model)
    
    # 5. Minimize eponyms - uses LLM agent
    model = await minimize_eponyms(model)
    
    # Flag location attributes for review (until transformation is fully implemented)
    location_attrs = _flag_location_attributes(model)
    if location_attrs:
        logger.info(f"Location attributes flagged for review: {', '.join(location_attrs)}")
    
    return model

