"""Sub-finding extraction for Hood models."""

import json
import logging
from typing import Any, Dict, List, Tuple

from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.tools import add_ids_to_model

from scripts.merge_findings_helpers import extract_attr_name
from agents.formatting_agents import create_sub_finding_extraction_agent

from findingmodels.hood.generators import ensure_required_attributes

logger = logging.getLogger(__name__)


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
    """Check if 'presence of [component]' attribute already exists."""
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
    
    Args:
        model: The finding model to process
        
    Returns:
        Tuple of (list of finding models, tracking_info dict)
    """
    model_dict = model.model_dump(exclude_unset=False, exclude_none=False)
    finding_name = model_dict.get('name', '')
    attributes = model_dict.get('attributes', [])
    
    tracking_info = {
        'finding_name': finding_name,
        'extracted': [],
        'kept_with_presence': [],
        'no_components_found': False
    }
    
    try:
        agent = create_sub_finding_extraction_agent()
        
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
        
        if not extraction_result.should_extract or (not extraction_result.extracted_components and not extraction_result.kept_components):
            logger.debug(f"No components to extract or keep for '{finding_name}'")
            tracking_info['no_components_found'] = True
            return ([model], tracking_info)
        
        attr_name_to_obj = {}
        for attr in attributes:
            attr_name = extract_attr_name(attr).lower()
            attr_name_to_obj[attr_name] = attr
        
        sub_finding_models = []
        attributes_to_remove = set()
        
        for component_def in extraction_result.extracted_components:
            component_name = component_def.get('name', '').lower()
            component_description = component_def.get('description', '')
            component_attr_names = component_def.get('attributes', [])
            
            presence_attr_name = f"presence of {component_name}".lower()
            presence_attr_kept = None
            
            component_attributes = []
            for attr_name in component_attr_names:
                attr_name_lower = attr_name.lower()
                if presence_attr_name in attr_name_lower or attr_name_lower == presence_attr_name:
                    continue
                if attr_name_lower in attr_name_to_obj:
                    attr_copy = json.loads(json.dumps(attr_name_to_obj[attr_name_lower]))
                    component_attributes.append(attr_copy)
                    attributes_to_remove.add(attr_name_lower)
                else:
                    logger.warning(f"Attribute '{attr_name}' not found for component '{component_name}'")
            
            if presence_attr_name in attr_name_to_obj:
                presence_attr_kept = presence_attr_name
                logger.debug(f"Keeping '{presence_attr_name}' in main finding as pointer")
            
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
                    preserved_contributors = sub_finding_dict.get('contributors', [])
                    preserved_index_codes = sub_finding_dict.get('index_codes')
                    preserved_locations = sub_finding_dict.get('locations')
                    
                    base_model = FindingModelBase(**sub_finding_dict)
                    model_with_ids = add_ids_to_model(base_model, source="MGB")
                    
                    model_dict_result = model_with_ids.model_dump(exclude_unset=False, exclude_none=False)
                    if preserved_contributors:
                        model_dict_result['contributors'] = preserved_contributors
                    if preserved_index_codes:
                        model_dict_result['index_codes'] = preserved_index_codes
                    if preserved_locations:
                        model_dict_result['locations'] = preserved_locations
                    
                    sub_finding_model = FindingModelFull(**model_dict_result)
                    
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
        
        for component_def in extraction_result.kept_components:
            component_name = component_def.get('name', '').lower()
            presence_attr_name = f"presence of {component_name}".lower()
            
            if has_component_presence_attribute(attributes, component_name):
                logger.debug(f"Presence attribute '{presence_attr_name}' already exists for '{component_name}'")
                tracking_info['kept_with_presence'].append({
                    'component_name': component_name,
                    'presence_attribute_action': 'already_exists',
                    'presence_attribute_name': presence_attr_name
                })
            else:
                presence_attr = create_component_presence_element(component_name, finding_name)
                attributes.append(presence_attr)
                logger.info(f"Added presence attribute '{presence_attr_name}' for kept component '{component_name}'")
                tracking_info['kept_with_presence'].append({
                    'component_name': component_name,
                    'presence_attribute_action': 'added',
                    'presence_attribute_name': presence_attr_name
                })
        
        main_model_attributes = []
        for attr in attributes:
            attr_name_lower = extract_attr_name(attr).lower()
            if (attr_name_lower in {name.lower() for name in extraction_result.main_model_attributes} or
                'presence of' in attr_name_lower or
                attr_name_lower not in attributes_to_remove):
                main_model_attributes.append(attr)
        
        modified_main_dict = model_dict.copy()
        modified_main_dict['attributes'] = main_model_attributes
        
        try:
            preserved_contributors = modified_main_dict.get('contributors', [])
            preserved_index_codes = modified_main_dict.get('index_codes')
            preserved_locations = modified_main_dict.get('locations')
            
            base_model = FindingModelBase(**modified_main_dict)
            model_with_ids = add_ids_to_model(base_model, source="MGB")
            
            model_dict_result = model_with_ids.model_dump(exclude_unset=False, exclude_none=False)
            if preserved_contributors:
                model_dict_result['contributors'] = preserved_contributors
            if preserved_index_codes:
                model_dict_result['index_codes'] = preserved_index_codes
            if preserved_locations:
                model_dict_result['locations'] = preserved_locations
            
            modified_main_model = FindingModelFull(**model_dict_result)
            
            modified_main_model, _ = await ensure_required_attributes(modified_main_model)
            
            removed_count = len(attributes) - len(main_model_attributes)
            logger.info(f"Modified main model '{finding_name}': kept {len(main_model_attributes)} attributes, removed {removed_count} component-specific attributes")
        except Exception as e:
            logger.error(f"Error modifying main model: {e}, returning original")
            return ([model], tracking_info)
        
        if sub_finding_models:
            logger.info(f"Would extract {len(sub_finding_models)} sub-finding(s) from '{finding_name}' (logging only, not creating files)")
            for sub_model in sub_finding_models:
                attr_names = [extract_attr_name(attr) for attr in sub_model.attributes]
                logger.info(f"  - Would create: '{sub_model.name}' with attributes: {', '.join(attr_names)}")
        
        return ([modified_main_model], tracking_info)
        
    except Exception as e:
        logger.warning(f"Error in sub-finding extraction for '{finding_name}': {e}, returning original model")
        import traceback
        traceback.print_exc()
        return ([model], tracking_info)
