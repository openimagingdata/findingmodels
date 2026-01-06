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
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

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
    compare_attributes_within_group,
    classify_attribute
)
from scripts.merge_findings_helpers import (
    create_presence_element,
    create_change_element,
    ensure_standard_presence_values,
    ensure_standard_change_values,
    build_final_finding,
    ensure_hood_contributor,
    reorder_attributes,
    preserve_existing_ids,
    extract_attr_name,
    extract_value_names
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

def extract_expected_attributes_from_markdown(markdown_content: str) -> List[str]:
    """Extract expected attribute names from markdown content.
    
    Parses markdown to find attribute definitions in the format:
    - **Attribute Name**: ...
    
    Args:
        markdown_content: The markdown content to parse
        
    Returns:
        List of expected attribute names (normalized to lowercase)
    """
    expected_attrs = []
    
    # Pattern to match bold text followed by colon (attribute definitions)
    # Matches: **Attribute Name**: or **Attribute Name**:
    pattern = r'\*\*([^*]+)\*\*\s*:'
    
    matches = re.findall(pattern, markdown_content)
    for match in matches:
        attr_name = match.strip().lower()
        # Skip common non-attribute patterns
        if attr_name not in ['identification', 'characteristics', 'associated findings', 'description']:
            expected_attrs.append(attr_name)
    
    return expected_attrs


async def generate_new_model(
    file_path: Path,
    data: Optional[Dict],
    markdown_content: Optional[str],
    file_type: str
) -> Tuple[FindingModelFull, List[str]]:
    """Generate a new finding model from MD or JSON.
    
    Args:
        file_path: Path to the source file
        data: Parsed JSON data (if JSON)
        markdown_content: Markdown content (if MD)
        file_type: "json" or "md"
        
    Returns:
        Tuple of (Generated FindingModelFull, list of missing attribute names)
    """
    missing_attributes = []
    
    if file_type == "json":
        # Use HoodJsonAdapter
        filename = file_path.name
        model = await HoodJsonAdapter.adapt_hood_json(data, filename)
        # For JSON, we don't track missing attributes (would need to parse JSON structure)
        return model, missing_attributes
    
    elif file_type == "md":
        # Extract expected attributes from markdown before processing
        expected_attrs = extract_expected_attributes_from_markdown(markdown_content)
        
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
        
        # Extract actual attribute names from generated model
        actual_attrs = {extract_attr_name(attr).lower() for attr in model.attributes}
        
        # Find missing attributes (normalize expected to handle variations)
        # Normalize expected attributes (remove "presence of", "signs of", etc. for comparison)
        expected_normalized = set()
        for exp_attr in expected_attrs:
            # Remove common prefixes that might be normalized
            normalized = exp_attr
            for prefix in ['presence of ', 'signs of ', 'other ']:
                if normalized.startswith(prefix):
                    normalized = normalized[len(prefix):].strip()
            expected_normalized.add(normalized)
        
        # Check which expected attributes are missing
        for exp_attr in expected_attrs:
            # Try exact match first
            if exp_attr not in actual_attrs:
                # Try normalized match
                normalized = exp_attr
                for prefix in ['presence of ', 'signs of ', 'other ']:
                    if normalized.startswith(prefix):
                        normalized = normalized[len(prefix):].strip()
                
                # Check if any actual attribute contains the normalized name
                found = False
                for actual_attr in actual_attrs:
                    if normalized in actual_attr or actual_attr in normalized:
                        found = True
                        break
                
                if not found:
                    missing_attributes.append(exp_attr)
        
        # Add IDs and codes
        full_model = add_ids_to_model(model, source="MGB")
        add_standard_codes_to_model(full_model)
        
        # Add contributors
        full_model.contributors = MarkdownToFindingModelAdapter._create_default_contributors()
        
        # Preserve metadata fields before conversion (use explicit parameters like other functions)
        full_model_dict = full_model.model_dump(exclude_unset=False, exclude_none=False)
        preserved_index_codes = full_model_dict.get('index_codes')
        preserved_locations = full_model_dict.get('locations')
        
        # Convert to FindingModelFull
        result_model = FindingModelFull(**full_model_dict)
        
        # Restore preserved fields if they exist
        if preserved_index_codes:
            result_model.index_codes = preserved_index_codes
        if preserved_locations:
            result_model.locations = preserved_locations
        
        return result_model, missing_attributes
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


def is_about_main_finding(
    attr_description: str, 
    finding_name: str,
    attr_name: str
) -> bool:
    """Verify attribute is about main finding, not sub-feature.
    
    Args:
        attr_description: The attribute's description text
        finding_name: The name of the main finding
        attr_name: The attribute's name
        
    Returns:
        True if attribute is about the main finding, False if it's about a sub-feature
    """
    desc_lower = attr_description.lower()
    name_lower = finding_name.lower()
    attr_name_lower = attr_name.lower()
    
    # Must contain finding name or generic "finding" reference
    has_finding_reference = (
        name_lower in desc_lower or
        'finding' in desc_lower or
        f'the {name_lower}' in desc_lower
    )
    
    if not has_finding_reference:
        return False
    
    # Reject if clearly about sub-feature
    # Patterns that indicate sub-features (unless finding name is also present)
    sub_feature_patterns = [
        r'presence of (calcification|enhancement|thickening|mass|nodule|lesion)',
        r'change in (enhancement|pattern|characteristic)',
        r'within the (finding|nodule|mass)',
        r'component of',
        r'feature of',
    ]
    
    # But allow if finding name is in the pattern (e.g., "presence of nodule" when finding is "nodule")
    for pattern in sub_feature_patterns:
        if re.search(pattern, desc_lower) and name_lower not in desc_lower:
            return False
    
    # Additional check: reject if description mentions specific sub-features
    # but doesn't clearly reference the main finding
    sub_feature_indicators = [
        'calcification', 'enhancement', 'associated', 'within', 
        'component', 'feature', 'characteristic', 'pattern',
    ]
    
    # If description contains sub-feature indicators but doesn't contain finding name,
    # it's likely about a sub-feature
    has_sub_feature_indicator = any(
        indicator in desc_lower and finding_name not in desc_lower
        for indicator in sub_feature_indicators
    )
    
    if has_sub_feature_indicator:
        return False
    
    return True


async def ensure_required_attributes(model: FindingModelFull) -> Tuple[FindingModelFull, Dict]:
    """Ensure presence and change_from_prior attributes exist.
    
    Uses hybrid detection: exact match → heuristic → classification agent.
    Verifies attributes are about the main finding, not sub-features.
    
    Args:
        model: The finding model
        
    Returns:
        Tuple of (model with required attributes, tracking_info dict)
    """
    # Convert to dict for easier manipulation
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    finding_name = model.name
    
    # Tracking info for reporting
    tracking_info = {
        'presence': {'action': None, 'original_name': None, 'finding_name': finding_name},
        'change_from_prior': {'action': None, 'original_name': None, 'finding_name': finding_name}
    }
    
    # Standard value sets for detection
    standard_presence_values = {"present", "absent", "indeterminate", "unknown"}
    standard_change_values = {"unchanged", "stable", "increased", "decreased", "new", "resolved", "no prior"}
    
    # Sub-feature indicators for description verification
    sub_feature_indicators = [
        'calcification', 'enhancement', 'associated', 'within', 
        'component', 'feature', 'characteristic', 'pattern',
        'subcutaneous', 'pleural', 'pulmonary'
    ]
    
    # ========================================================================
    # PRESENCE ATTRIBUTE DETECTION
    # ========================================================================
    found_presence = False
    presence_attr_index = None
    
    # Step 1: Check for exact match
    for i, attr in enumerate(attributes):
        if extract_attr_name(attr).lower() == 'presence':
            found_presence = True
            presence_attr_index = i
            # Ensure all standard values are present
            attributes[i] = ensure_standard_presence_values(attr, finding_name)
            tracking_info['presence'] = {
                'action': 'exact_match',
                'original_name': 'presence',
                'finding_name': finding_name
            }
            logger.debug(f"Found exact match for presence attribute")
            break
    
    # Step 2: Heuristic detection (if no exact match)
    if not found_presence:
        for i, attr in enumerate(attributes):
            attr_name = extract_attr_name(attr)
            attr_name_lower = attr_name.lower()
            
            # Heuristic: name contains "presence" AND values match standard presence values
            if 'presence' in attr_name_lower:
                attr_values = set(extract_value_names(attr))
                
                # Check if values match standard presence values (at least 2 must match)
                matching_values = standard_presence_values.intersection(attr_values)
                if len(matching_values) >= 2:
                    # CRITICAL: Verify it's about the main finding, not a sub-feature
                    description = attr.get('description', '')
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        # Valid presence attribute - rename it
                        original_name = attr_name
                        attr['name'] = 'presence'
                        # Ensure all standard values are present
                        attr = ensure_standard_presence_values(attr, finding_name)
                        attributes[i] = attr
                        found_presence = True
                        presence_attr_index = i
                        tracking_info['presence'] = {
                            'action': 'renamed',
                            'original_name': original_name,
                            'finding_name': finding_name
                        }
                        logger.info(f"Renamed presence attribute: '{original_name}' → 'presence'")
                        break
    
    # Step 3: Classification agent fallback (if still not found)
    if not found_presence:
        for i, attr in enumerate(attributes):
            try:
                classification = await classify_attribute(attr, finding_name)
                
                if classification.classification == 'presence':
                    # CRITICAL: Verify description before accepting
                    description = attr.get('description', '')
                    attr_name = extract_attr_name(attr)
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        # Valid presence attribute - rename it
                        original_name = attr_name
                        attr['name'] = 'presence'
                        # Ensure all standard values are present
                        attr = ensure_standard_presence_values(attr, finding_name)
                        attributes[i] = attr
                        found_presence = True
                        presence_attr_index = i
                        tracking_info['presence'] = {
                            'action': 'classification_used',
                            'original_name': original_name,
                            'finding_name': finding_name
                        }
                        logger.info(f"Renamed presence attribute (via classification): '{original_name}' → 'presence'")
                        break
            except Exception as e:
                logger.warning(f"Error classifying attribute for presence detection: {e}")
                continue
    
    # Step 4: Add if not found
    if not found_presence:
        presence_attr = create_presence_element(finding_name)
        attributes.insert(0, presence_attr)
        tracking_info['presence'] = {
            'action': 'added',
            'original_name': None,
            'finding_name': finding_name
        }
        logger.info("Added presence attribute")
    
    # ========================================================================
    # CHANGE FROM PRIOR ATTRIBUTE DETECTION
    # ========================================================================
    found_change = False
    change_attr_index = None
    
    # Step 1: Check for exact match
    for i, attr in enumerate(attributes):
        if extract_attr_name(attr).lower() == 'change from prior':
            found_change = True
            change_attr_index = i
            # Ensure all standard values are present
            attributes[i] = ensure_standard_change_values(attr, finding_name)
            tracking_info['change_from_prior'] = {
                'action': 'exact_match',
                'original_name': 'change from prior',
                'finding_name': finding_name
            }
            logger.debug(f"Found exact match for change from prior attribute")
            break
    
    # Step 2: Heuristic detection (if no exact match)
    if not found_change:
        for i, attr in enumerate(attributes):
            attr_name = extract_attr_name(attr)
            attr_name_lower = attr_name.lower()
            
            # Heuristic: name contains change-related terms AND values match standard change values
            change_keywords = ['change', 'prior', 'interval', 'progression', 'stability', 'status']
            if any(keyword in attr_name_lower for keyword in change_keywords):
                attr_values = set(extract_value_names(attr))
                
                # Check if values match standard change values (at least 2 must match)
                matching_values = standard_change_values.intersection(attr_values)
                if len(matching_values) >= 2:
                    # CRITICAL: Verify it's about the main finding
                    description = attr.get('description', '')
                    
                    # For change attributes, also check for time-related phrases
                    finding_name_lower = finding_name.lower()
                    is_about_main_finding_check = (
                        finding_name_lower in description.lower() or
                        'finding' in description.lower() or
                        'changed over time' in description.lower() or
                        'compared to prior' in description.lower() or
                        'interval change' in description.lower()
                    )
                    
                    if is_about_main_finding_check:
                        # Additional check: reject if clearly about sub-feature
                        desc_lower = description.lower()
                        is_sub_feature = any(
                            indicator in desc_lower and finding_name_lower not in desc_lower
                            for indicator in sub_feature_indicators
                        )
                        
                        if not is_sub_feature:
                            # Valid change attribute - rename it
                            original_name = attr_name
                            attr['name'] = 'change from prior'
                            # Ensure all standard values are present
                            attr = ensure_standard_change_values(attr, finding_name)
                            attributes[i] = attr
                            found_change = True
                            change_attr_index = i
                            tracking_info['change_from_prior'] = {
                                'action': 'renamed',
                                'original_name': original_name,
                                'finding_name': finding_name
                            }
                            logger.info(f"Renamed change from prior attribute: '{original_name}' → 'change from prior'")
                            break
    
    # Step 3: Classification agent fallback (if still not found)
    if not found_change:
        for i, attr in enumerate(attributes):
            try:
                classification = await classify_attribute(attr, finding_name)
                
                if classification.classification == 'change_from_prior':
                    # CRITICAL: Verify description before accepting
                    description = attr.get('description', '')
                    attr_name = extract_attr_name(attr)
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        # Valid change attribute - rename it
                        original_name = attr_name
                        attr['name'] = 'change from prior'
                        # Ensure all standard values are present
                        attr = ensure_standard_change_values(attr, finding_name)
                        attributes[i] = attr
                        found_change = True
                        change_attr_index = i
                        tracking_info['change_from_prior'] = {
                            'action': 'classification_used',
                            'original_name': original_name,
                            'finding_name': finding_name
                        }
                        logger.info(f"Renamed change from prior attribute (via classification): '{original_name}' → 'change from prior'")
                        break
            except Exception as e:
                logger.warning(f"Error classifying attribute for change detection: {e}")
                continue
    
    # Step 4: Add if not found
    if not found_change:
        change_attr = create_change_element(finding_name)
        # Insert after presence if it exists, otherwise at beginning
        insert_pos = 1 if found_presence else 0
        attributes.insert(insert_pos, change_attr)
        tracking_info['change_from_prior'] = {
            'action': 'added',
            'original_name': None,
            'finding_name': finding_name
        }
        logger.info("Added change_from_prior attribute")
    
    # Remove any duplicate presence/change attributes (keep only the first one we found/added)
    # This handles cases where both the original and a renamed version exist
    seen_names = set()
    filtered_attributes = []
    for attr in attributes:
        attr_name_lower = extract_attr_name(attr).lower()
        if attr_name_lower in ['presence', 'change from prior']:
            if attr_name_lower not in seen_names:
                seen_names.add(attr_name_lower)
                filtered_attributes.append(attr)
            else:
                logger.warning(f"Removed duplicate attribute: {extract_attr_name(attr)}")
        else:
            filtered_attributes.append(attr)
    
    model_dict['attributes'] = filtered_attributes
    
    # Preserve metadata fields before conversion
    preserved_contributors = model_dict.get('contributors', [])
    preserved_index_codes = model_dict.get('index_codes')
    preserved_locations = model_dict.get('locations')
    
    # Convert back to FindingModelBase, then add IDs, then to FindingModelFull
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    
    # Restore preserved metadata fields
    full_model_dict = full_model.model_dump(exclude_unset=False, exclude_none=False)
    if preserved_contributors:
        full_model_dict['contributors'] = preserved_contributors
    if preserved_index_codes:
        full_model_dict['index_codes'] = preserved_index_codes
    if preserved_locations:
        full_model_dict['locations'] = preserved_locations
    
    # Recreate model with IDs and preserved metadata
    return (FindingModelFull(**full_model_dict), tracking_info)


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
    incoming_name = incoming_model.name
    
    # First, find potential matches
    match = await find_existing_model(incoming_model, index)
    
    if match is None:
        return None
    
    existing_name = match.get('name', '')
    logger.info(f"Found potential match: '{existing_name}' (ID: {match.get('oifm_id', 'N/A')}), checking specificity...")
    
    # Check if the match is too general (bidirectional check)
    # Check if existing is too general for incoming
    if await is_match_too_general(incoming_name, existing_name):
        logger.info(f"Rejected match '{existing_name}' as too general for '{incoming_name}'")
        return None
    
    # Check if incoming is too general for existing (reverse check)
    if await is_match_too_general(existing_name, incoming_name):
        logger.info(f"Rejected match: incoming '{incoming_name}' is too general for existing '{existing_name}'")
        return None
    
    logger.info(f"Match accepted: '{existing_name}' is appropriate for '{incoming_name}'")
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
) -> Tuple[FindingModelFull, Dict]:
    """Merge incoming model with existing model.
    
    Args:
        incoming_model: The incoming finding model
        existing_match: The existing model match dict
        index: Database index
        
    Returns:
        Tuple of (Merged FindingModelFull, merge_details dict)
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
    
    # Build merge details for reporting
    merge_details = {
        'attributes_merged': len(merge_recommendations),
        'attributes_added': len(approved_new_attributes),
        'attributes_created': len(attributes_to_add),
        'merge_recommendations': [
            {
                'incoming_name': extract_attr_name(mr.get('incoming_attribute', {})),
                'existing_name': extract_attr_name(mr.get('existing_attribute', {})),
                'relationship': (
                    mr.get('relationship').relationship 
                    if hasattr(mr.get('relationship'), 'relationship') 
                    else (mr.get('relationship', {}).get('relationship', 'unknown') if isinstance(mr.get('relationship'), dict) else 'unknown')
                )
            }
            for mr in merge_recommendations
        ],
        'new_attributes': [
            extract_attr_name(attr)
            for attr in approved_new_attributes
        ],
        'created_attributes': [name for name, _ in attributes_to_add]
    }
    
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
    return (FindingModelFull(**final_finding), merge_details)


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


def create_component_presence_element(component_name: str, main_finding_name: str) -> Dict[str, Any]:
    """Create a presence attribute for a component within a main finding.
    
    Example: "presence of solid component" for ground glass nodule
    This attribute serves as a pointer/reference to the component finding.
    
    Args:
        component_name: Name of the component (e.g., "solid component")
        main_finding_name: Name of the main finding (e.g., "ground glass nodule")
        
    Returns:
        Dictionary representing the presence attribute
    """
    return {
        "name": f"presence of {component_name}",
        "description": f"Whether a {component_name} is present within the {main_finding_name}",
        "type": "choice",
        "required": False,
        "max_selected": 1,
        "values": [
            {"name": "present", "description": f"{component_name.capitalize()} is present"},
            {"name": "absent", "description": f"No {component_name} identified"},
            {"name": "indeterminate", "description": f"Presence of {component_name} cannot be determined"},
            {"name": "unknown", "description": f"Presence of {component_name} is unknown"}
        ]
    }


def has_component_presence_attribute(attributes: List[Dict], component_name: str) -> bool:
    """Check if 'presence of [component]' attribute already exists.
    
    Args:
        attributes: List of attribute dictionaries
        component_name: Name of the component (e.g., "solid component")
        
    Returns:
        True if "presence of [component]" attribute exists
    """
    presence_name = f"presence of {component_name}".lower()
    return any(
        extract_attr_name(attr).lower() == presence_name
        for attr in attributes
    )


async def extract_sub_findings(model: FindingModelFull) -> Tuple[List[FindingModelFull], Dict]:
    """Extract detailed sub-findings as separate models.
    
    Implements component extraction logic:
    - Components with unique attributes → extract to separate finding, keep "presence of [component]" in main
    - Components without unique attributes → keep in main, add "presence of [component]" if missing
    
    Example: "solid component of ground glass nodule" with "solid component size" → extract size to new finding,
    keep "presence of solid component" in main as pointer.
    
    Args:
        model: The finding model to process
        
    Returns:
        Tuple of (list of finding models, tracking_info dict)
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    finding_name = model_dict.get('name', '')
    attributes = model_dict.get('attributes', [])
    
    # Initialize tracking info
    tracking_info = {
        'finding_name': finding_name,
        'extracted': [],
        'kept_with_presence': [],
        'no_components_found': False
    }
    
    try:
        # Use LLM agent to determine if components should be extracted or kept
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
        
        prompt = f"""Analyze this finding model to determine if components should be extracted or kept with presence:

Finding Name: "{finding_name}"
Description: "{model_dict.get('description', '')}"
Attributes: {json.dumps(attributes_summary, indent=2)}

Determine if any components/subcomponents should be extracted as separate findings or kept with presence attributes."""
        
        result = await agent.run(prompt)
        extraction_result = result.output
        
        # If no extraction or kept components, return original model
        if not extraction_result.should_extract or (not extraction_result.extracted_components and not extraction_result.kept_components):
            logger.debug(f"No components to extract or keep for '{finding_name}'")
            tracking_info['no_components_found'] = True
            return ([model], tracking_info)
        
        # Create mapping of attribute names to full attribute objects
        attr_name_to_obj = {}
        for attr in attributes:
            attr_name = extract_attr_name(attr).lower()
            attr_name_to_obj[attr_name] = attr
        
        sub_finding_models = []
        attributes_to_remove = set()  # Track attributes to remove from main
        
        # Process extracted components
        for component_def in extraction_result.extracted_components:
            component_name = component_def.get('name', '').lower()
            component_description = component_def.get('description', '')
            component_attr_names = component_def.get('attributes', [])  # Unique attributes only
            
            # Find presence attribute name for this component
            presence_attr_name = f"presence of {component_name}".lower()
            presence_attr_kept = None
            
            # Collect unique attributes for this component (excluding presence)
            component_attributes = []
            for attr_name in component_attr_names:
                attr_name_lower = attr_name.lower()
                # Skip presence attributes - they stay in main
                if presence_attr_name in attr_name_lower or attr_name_lower == presence_attr_name:
                    continue
                if attr_name_lower in attr_name_to_obj:
                    attr_copy = json.loads(json.dumps(attr_name_to_obj[attr_name_lower]))
                    component_attributes.append(attr_copy)
                    attributes_to_remove.add(attr_name_lower)
                else:
                    logger.warning(f"Attribute '{attr_name}' not found for component '{component_name}'")
            
            # Check if presence attribute exists and should be kept
            if presence_attr_name in attr_name_to_obj:
                presence_attr_kept = presence_attr_name
                logger.debug(f"Keeping '{presence_attr_name}' in main finding as pointer")
            
            # Create sub-finding model
            if component_attributes:
                sub_finding_name = f"{component_name} of {finding_name}".lower()
                sub_finding_dict = {
                    'name': sub_finding_name,
                    'description': component_description or f"{component_name.capitalize()} within {finding_name}",
                    'attributes': component_attributes,
                    'contributors': model_dict.get('contributors', []),
                    'index_codes': model_dict.get('index_codes'),
                    'locations': model_dict.get('locations'),
                    'tags': model_dict.get('tags'),
                    'synonyms': model_dict.get('synonyms')
                }
                
                try:
                    # Preserve metadata fields before conversion
                    preserved_contributors = sub_finding_dict.get('contributors', [])
                    preserved_index_codes = sub_finding_dict.get('index_codes')
                    preserved_locations = sub_finding_dict.get('locations')
                    
                    base_model = FindingModelBase(**sub_finding_dict)
                    model_with_ids = add_ids_to_model(base_model, source="MGB")
                    
                    # Restore preserved metadata fields
                    model_dict = model_with_ids.model_dump(exclude_unset=False, exclude_none=False)
                    if preserved_contributors:
                        model_dict['contributors'] = preserved_contributors
                    if preserved_index_codes:
                        model_dict['index_codes'] = preserved_index_codes
                    if preserved_locations:
                        model_dict['locations'] = preserved_locations
                    
                    sub_finding_model = FindingModelFull(**model_dict)
                    
                    # Ensure required attributes
                    sub_finding_model, _ = await ensure_required_attributes(sub_finding_model)
                    
                    sub_finding_models.append(sub_finding_model)
                    logger.info(f"Created extracted component: '{sub_finding_name}' with {len(component_attributes)} attributes")
                    
                    tracking_info['extracted'].append({
                        'component_name': component_name,
                        'attributes_moved': [attr.get('name', '') for attr in component_attributes],
                        'presence_attribute_kept': presence_attr_kept,
                        'new_finding_name': sub_finding_name
                    })
                except Exception as e:
                    logger.error(f"Error creating extracted component '{component_name}': {e}")
                    continue
        
        # Process kept components (add presence if missing)
        for component_def in extraction_result.kept_components:
            component_name = component_def.get('name', '').lower()
            presence_attr_name = f"presence of {component_name}".lower()
            
            # Check if presence attribute already exists
            if has_component_presence_attribute(attributes, component_name):
                logger.debug(f"Presence attribute '{presence_attr_name}' already exists for '{component_name}'")
                tracking_info['kept_with_presence'].append({
                    'component_name': component_name,
                    'presence_attribute_action': 'already_exists',
                    'presence_attribute_name': presence_attr_name
                })
            else:
                # Add presence attribute
                presence_attr = create_component_presence_element(component_name, finding_name)
                attributes.append(presence_attr)
                logger.info(f"Added presence attribute '{presence_attr_name}' for kept component '{component_name}'")
                tracking_info['kept_with_presence'].append({
                    'component_name': component_name,
                    'presence_attribute_action': 'added',
                    'presence_attribute_name': presence_attr_name
                })
        
        # Modify main model - remove extracted attributes but keep presence attributes
        main_model_attributes = []
        for attr in attributes:
            attr_name_lower = extract_attr_name(attr).lower()
            # Keep attribute if:
            # 1. It's in main_model_attributes list from agent, OR
            # 2. It's a presence attribute (pointer/reference), OR
            # 3. It's not in the attributes_to_remove set
            if (attr_name_lower in {name.lower() for name in extraction_result.main_model_attributes} or
                'presence of' in attr_name_lower or
                attr_name_lower not in attributes_to_remove):
                main_model_attributes.append(attr)
        
        # Update main model dict
        modified_main_dict = model_dict.copy()
        modified_main_dict['attributes'] = main_model_attributes
        
        # Convert back to FindingModelFull
        try:
            # Preserve metadata fields from original model before conversion
            preserved_contributors = modified_main_dict.get('contributors', [])
            preserved_index_codes = modified_main_dict.get('index_codes')
            preserved_locations = modified_main_dict.get('locations')
            
            base_model = FindingModelBase(**modified_main_dict)
            model_with_ids = add_ids_to_model(base_model, source="MGB")
            
            # Restore preserved metadata fields
            model_dict_result = model_with_ids.model_dump(exclude_unset=False, exclude_none=False)
            if preserved_contributors:
                model_dict_result['contributors'] = preserved_contributors
            if preserved_index_codes:
                model_dict_result['index_codes'] = preserved_index_codes
            if preserved_locations:
                model_dict_result['locations'] = preserved_locations
            
            modified_main_model = FindingModelFull(**model_dict_result)
            
            # Ensure required attributes
            modified_main_model, _ = await ensure_required_attributes(modified_main_model)
            
            removed_count = len(attributes) - len(main_model_attributes)
            logger.info(f"Modified main model '{finding_name}': kept {len(main_model_attributes)} attributes, removed {removed_count} component-specific attributes")
        except Exception as e:
            logger.error(f"Error modifying main model: {e}, returning original")
            return ([model], tracking_info)
        
        # Log extracted sub-findings but don't return them (logging only, not creating files)
        if sub_finding_models:
            logger.info(f"Would extract {len(sub_finding_models)} sub-finding(s) from '{finding_name}' (logging only, not creating files)")
            for sub_model in sub_finding_models:
                attr_names = [extract_attr_name(attr) for attr in sub_model.attributes]
                logger.info(f"  - Would create: '{sub_model.name}' with attributes: {', '.join(attr_names)}")
        
        # Return only the main model (sub-findings are logged but not created)
        return ([modified_main_model], tracking_info)
        
    except Exception as e:
        logger.warning(f"Error in sub-finding extraction for '{finding_name}': {e}, returning original model")
        import traceback
        traceback.print_exc()
        # Fallback: return original model
        return ([model], tracking_info)


async def apply_formatting_guidelines(model: FindingModelFull) -> FindingModelFull:
    """Apply formatting guidelines to the model.
    
    Rules:
    1. Lowercase: Convert model name, attribute names, and values to lowercase (except descriptions)
    2. Expand acronyms and add synonyms
    3. Minimize eponyms
    
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
    
    # 2. Expand acronyms and add synonyms - uses LLM agent
    model = await expand_acronyms_and_add_synonyms(model)
    
    # 3. Minimize eponyms - uses LLM agent
    model = await minimize_eponyms(model)
    
    return model

