"""Model generation and validation for Hood definitions."""

import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from findingmodel import FindingModelFull, FindingModelBase, FindingInfo
from findingmodel.tools import (
    create_model_from_markdown,
    add_ids_to_model,
    add_standard_codes_to_model
)

from findingmodels.hood.hood_json_adapter import HoodJsonAdapter
from findingmodels.hood.markdown_to_finding_model_adapter import MarkdownToFindingModelAdapter
from scripts.merge_findings import classify_attribute
from scripts.merge_findings_helpers import (
    create_presence_element,
    create_change_element,
    ensure_standard_presence_values,
    ensure_standard_change_values,
    extract_attr_name,
    extract_value_names
)

logger = logging.getLogger(__name__)


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
    sub_feature_patterns = [
        r'presence of (calcification|enhancement|thickening|mass|nodule|lesion)',
        r'change in (enhancement|pattern|characteristic)',
        r'within the (finding|nodule|mass)',
        r'component of',
        r'feature of',
    ]
    
    for pattern in sub_feature_patterns:
        if re.search(pattern, desc_lower) and name_lower not in desc_lower:
            return False
    
    sub_feature_indicators = [
        'calcification', 'enhancement', 'associated', 'within', 
        'component', 'feature', 'characteristic', 'pattern',
    ]
    
    has_sub_feature_indicator = any(
        indicator in desc_lower and finding_name not in desc_lower
        for indicator in sub_feature_indicators
    )
    
    if has_sub_feature_indicator:
        return False
    
    return True


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
        filename = file_path.name
        model = await HoodJsonAdapter.adapt_hood_json(data, filename)
        return model, missing_attributes
    
    elif file_type == "md":
        expected_attrs = extract_expected_attributes_from_markdown(markdown_content)
        
        filename = file_path.stem
        finding_name = filename.replace('-', ' ').replace('_', ' ').title()
        
        finding_info = FindingInfo(
            name=finding_name.lower(),
            description=""
        )
        
        model = await create_model_from_markdown(
            finding_info,
            markdown_text=markdown_content
        )
        
        actual_attrs = {extract_attr_name(attr).lower() for attr in model.attributes}
        
        expected_normalized = set()
        for exp_attr in expected_attrs:
            normalized = exp_attr
            for prefix in ['presence of ', 'signs of ', 'other ']:
                if normalized.startswith(prefix):
                    normalized = normalized[len(prefix):].strip()
            expected_normalized.add(normalized)
        
        for exp_attr in expected_attrs:
            if exp_attr not in actual_attrs:
                normalized = exp_attr
                for prefix in ['presence of ', 'signs of ', 'other ']:
                    if normalized.startswith(prefix):
                        normalized = normalized[len(prefix):].strip()
                
                found = False
                for actual_attr in actual_attrs:
                    if normalized in actual_attr or actual_attr in normalized:
                        found = True
                        break
                
                if not found:
                    missing_attributes.append(exp_attr)
        
        full_model = add_ids_to_model(model, source="MGB")
        add_standard_codes_to_model(full_model)
        
        full_model.contributors = MarkdownToFindingModelAdapter._create_default_contributors()
        
        full_model_dict = full_model.model_dump(exclude_unset=False, exclude_none=False)
        preserved_index_codes = full_model_dict.get('index_codes')
        preserved_locations = full_model_dict.get('locations')
        
        result_model = FindingModelFull(**full_model_dict)
        
        if preserved_index_codes:
            result_model.index_codes = preserved_index_codes
        if preserved_locations:
            result_model.locations = preserved_locations
        
        return result_model, missing_attributes
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


async def ensure_required_attributes(model: FindingModelFull) -> Tuple[FindingModelFull, Dict]:
    """Ensure presence and change_from_prior attributes exist.
    
    Uses hybrid detection: exact match → heuristic → classification agent.
    Verifies attributes are about the main finding, not sub-features.
    
    Args:
        model: The finding model
        
    Returns:
        Tuple of (model with required attributes, tracking_info dict)
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    attributes = model_dict.get('attributes', [])
    finding_name = model.name
    
    tracking_info = {
        'presence': {'action': None, 'original_name': None, 'finding_name': finding_name},
        'change_from_prior': {'action': None, 'original_name': None, 'finding_name': finding_name}
    }
    
    standard_presence_values = {"present", "absent", "indeterminate", "unknown"}
    standard_change_values = {"unchanged", "stable", "increased", "decreased", "new", "resolved", "no prior"}
    
    sub_feature_indicators = [
        'calcification', 'enhancement', 'associated', 'within', 
        'component', 'feature', 'characteristic', 'pattern',
        'subcutaneous', 'pleural', 'pulmonary'
    ]
    
    # PRESENCE ATTRIBUTE DETECTION
    found_presence = False
    presence_attr_index = None
    
    for i, attr in enumerate(attributes):
        if extract_attr_name(attr).lower() == 'presence':
            found_presence = True
            presence_attr_index = i
            attributes[i] = ensure_standard_presence_values(attr, finding_name)
            tracking_info['presence'] = {
                'action': 'exact_match',
                'original_name': 'presence',
                'finding_name': finding_name
            }
            logger.debug("Found exact match for presence attribute")
            break
    
    if not found_presence:
        for i, attr in enumerate(attributes):
            attr_name = extract_attr_name(attr)
            attr_name_lower = attr_name.lower()
            
            if 'presence' in attr_name_lower:
                attr_values = set(extract_value_names(attr))
                matching_values = standard_presence_values.intersection(attr_values)
                if len(matching_values) >= 2:
                    description = attr.get('description', '')
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        original_name = attr_name
                        attr['name'] = 'presence'
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
    
    if not found_presence:
        for i, attr in enumerate(attributes):
            try:
                classification = await classify_attribute(attr, finding_name)
                
                if classification.classification == 'presence':
                    description = attr.get('description', '')
                    attr_name = extract_attr_name(attr)
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        original_name = attr_name
                        attr['name'] = 'presence'
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
    
    if not found_presence:
        presence_attr = create_presence_element(finding_name)
        attributes.insert(0, presence_attr)
        tracking_info['presence'] = {
            'action': 'added',
            'original_name': None,
            'finding_name': finding_name
        }
        logger.info("Added presence attribute")
    
    # CHANGE FROM PRIOR ATTRIBUTE DETECTION
    found_change = False
    change_attr_index = None
    
    for i, attr in enumerate(attributes):
        if extract_attr_name(attr).lower() == 'change from prior':
            found_change = True
            change_attr_index = i
            attributes[i] = ensure_standard_change_values(attr, finding_name)
            tracking_info['change_from_prior'] = {
                'action': 'exact_match',
                'original_name': 'change from prior',
                'finding_name': finding_name
            }
            logger.debug("Found exact match for change from prior attribute")
            break
    
    if not found_change:
        for i, attr in enumerate(attributes):
            attr_name = extract_attr_name(attr)
            attr_name_lower = attr_name.lower()
            
            change_keywords = ['change', 'prior', 'interval', 'progression', 'stability', 'status']
            if any(keyword in attr_name_lower for keyword in change_keywords):
                attr_values = set(extract_value_names(attr))
                matching_values = standard_change_values.intersection(attr_values)
                if len(matching_values) >= 2:
                    description = attr.get('description', '')
                    finding_name_lower = finding_name.lower()
                    is_about_main_finding_check = (
                        finding_name_lower in description.lower() or
                        'finding' in description.lower() or
                        'changed over time' in description.lower() or
                        'compared to prior' in description.lower() or
                        'interval change' in description.lower()
                    )
                    
                    if is_about_main_finding_check:
                        desc_lower = description.lower()
                        is_sub_feature = any(
                            indicator in desc_lower and finding_name_lower not in desc_lower
                            for indicator in sub_feature_indicators
                        )
                        
                        if not is_sub_feature:
                            original_name = attr_name
                            attr['name'] = 'change from prior'
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
    
    if not found_change:
        for i, attr in enumerate(attributes):
            try:
                classification = await classify_attribute(attr, finding_name)
                
                if classification.classification == 'change_from_prior':
                    description = attr.get('description', '')
                    attr_name = extract_attr_name(attr)
                    
                    if is_about_main_finding(description, finding_name, attr_name):
                        original_name = attr_name
                        attr['name'] = 'change from prior'
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
    
    if not found_change:
        change_attr = create_change_element(finding_name)
        insert_pos = 1 if found_presence else 0
        attributes.insert(insert_pos, change_attr)
        tracking_info['change_from_prior'] = {
            'action': 'added',
            'original_name': None,
            'finding_name': finding_name
        }
        logger.info("Added change_from_prior attribute")
    
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
    
    preserved_contributors = model_dict.get('contributors', [])
    preserved_index_codes = model_dict.get('index_codes')
    preserved_locations = model_dict.get('locations')
    
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    
    full_model_dict = full_model.model_dump(exclude_unset=False, exclude_none=False)
    if preserved_contributors:
        full_model_dict['contributors'] = preserved_contributors
    if preserved_index_codes:
        full_model_dict['index_codes'] = preserved_index_codes
    if preserved_locations:
        full_model_dict['locations'] = preserved_locations
    
    return (FindingModelFull(**full_model_dict), tracking_info)
