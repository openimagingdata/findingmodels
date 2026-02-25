"""Formatting and transformation for Hood models."""

import logging
from typing import Any, Dict, List

from findingmodel import FindingModelFull

from agents.formatting_agents import (
    create_acronym_expansion_agent,
    create_eponym_minimization_agent
)

logger = logging.getLogger(__name__)


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
        agent = create_acronym_expansion_agent()
        prompt = f"""Expand acronyms in this finding model name: "{original_name}"

Detect all medical acronyms, expand them to full terms, and identify compact forms for synonyms."""
        
        result = await agent.run(prompt)
        expansion_result = result.output
        
        if expansion_result.expanded_name and expansion_result.expanded_name.lower() != original_name.lower():
            model_dict['name'] = expansion_result.expanded_name.lower()
            
            if model_dict.get('synonyms') is None:
                model_dict['synonyms'] = []
            
            synonyms = model_dict.get('synonyms', []) or []
            for compact_form in expansion_result.compact_forms:
                compact_lower = compact_form.lower()
                if compact_lower not in [s.lower() for s in synonyms]:
                    synonyms.append(compact_lower)
            
            model_dict['synonyms'] = synonyms
            
            logger.debug(f"Expanded acronyms in '{original_name}' → '{expansion_result.expanded_name}' (confidence: {expansion_result.confidence:.2f})")
        
    except Exception as e:
        logger.warning(f"Error in acronym expansion for '{original_name}': {e}, keeping original name")
    
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
        agent = create_eponym_minimization_agent()
        prompt = f"""Minimize eponyms in this finding model name: "{original_name}"

Detect any eponyms, replace with descriptive terms if appropriate, and keep original as synonym."""
        
        result = await agent.run(prompt)
        eponym_result = result.output
        
        if eponym_result.has_eponym and eponym_result.descriptive_name.lower() != original_name.lower():
            model_dict['name'] = eponym_result.descriptive_name.lower()
            
            if model_dict.get('synonyms') is None:
                model_dict['synonyms'] = []
            
            if eponym_result.eponym_synonym:
                synonyms = model_dict.get('synonyms', []) or []
                eponym_lower = eponym_result.eponym_synonym.lower()
                if eponym_lower not in [s.lower() for s in synonyms]:
                    synonyms.append(eponym_lower)
                model_dict['synonyms'] = synonyms
            
            logger.debug(f"Minimized eponym in '{original_name}' → '{eponym_result.descriptive_name}' (confidence: {eponym_result.confidence:.2f})")
        
    except Exception as e:
        logger.warning(f"Error in eponym minimization for '{original_name}': {e}, keeping original name")
    
    return FindingModelFull(**model_dict)


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
    
    if model_dict.get('name'):
        model_dict['name'] = model_dict['name'].lower()
    
    attributes = model_dict.get('attributes', [])
    for attr in attributes:
        if attr.get('name'):
            attr['name'] = attr['name'].lower()
        
        if attr.get('type') == 'choice' and attr.get('values'):
            for value in attr['values']:
                if value.get('name'):
                    value['name'] = value['name'].lower()
    
    model = FindingModelFull(**model_dict)
    
    model = await expand_acronyms_and_add_synonyms(model)
    model = await minimize_eponyms(model)
    
    return model
