"""Model matching and specificity checking for Hood definitions."""

import logging
from typing import Dict, Optional

from findingmodel import FindingModelFull
from findingmodel.index import Index

from scripts.merge_findings import find_existing_model
from agents.specificity_agents import create_specificity_check_agent

logger = logging.getLogger(__name__)


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
    
    match = await find_existing_model(incoming_model, index)
    
    if match is None:
        return None
    
    existing_name = match.get('name', '')
    logger.info(f"Found potential match: '{existing_name}' (ID: {match.get('oifm_id', 'N/A')}), checking specificity...")
    
    if await is_match_too_general(incoming_name, existing_name):
        logger.info(f"Rejected match '{existing_name}' as too general for '{incoming_name}'")
        return None
    
    if await is_match_too_general(existing_name, incoming_name):
        logger.info(f"Rejected match: incoming '{incoming_name}' is too general for existing '{existing_name}'")
        return None
    
    logger.info(f"Match accepted: '{existing_name}' is appropriate for '{incoming_name}'")
    return match
