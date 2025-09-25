"""
Attribute Merger Agent

This module contains the AttributeMerger AI agent that merges two attributes by adding
non-duplicative choices from a new attribute to an existing attribute.
"""

import json
import os
from typing import Dict, Any, List, Literal
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv
from findingmodel import ChoiceAttributeIded, NumericAttributeIded

# Load environment variables from .env file
load_dotenv()


# Pydantic model returned by the agent
class AttributeMergeResult(BaseModel):
    """Output from attribute merger"""
    merged_attribute: Dict[str, Any]
    added_values: List[Dict[str, Any]]
    skipped_values: List[Dict[str, Any]]
    reasoning: str


# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")


class AttributeMerger:
    """Merges attributes by adding non-duplicative choices from new to existing"""
    
    def __init__(self):
        self.agent = Agent(
            model=model,
            output_type=AttributeMergeResult,
            system_prompt="""You are a medical imaging expert specializing in finding model attributes.

            Your task is to merge two attributes by adding non-duplicative choices from a new attribute to an existing attribute.

            Rules:
            1. Keep the existing attribute as the base (name, type, description, etc.)
            2. Only add values from the new attribute that don't already exist in the existing attribute
            3. Consider values as duplicates if they have the same name (case-insensitive)
            4. Preserve all existing values and their IDs
            5. Generate new IDs for added values following the pattern: existing_id.{next_number}
            6. Maintain the same attribute structure and required fields

            For each value you add:
            - Generate a new value_code following the existing pattern
            - Include the name and description (if available)
            - Preserve any existing index_codes or other metadata

            Provide clear reasoning for what was added and what was skipped."""
        )
    
    async def merge(self, existing_attribute: Dict[str, Any], new_attribute: Dict[str, Any]) -> AttributeMergeResult:
        """Merge two attributes by adding non-duplicative choices from new to existing"""
        
        # Validate both attributes using Pydantic models
        try:
            existing_validated = ChoiceAttributeIded.model_validate(existing_attribute)
            new_validated = ChoiceAttributeIded.model_validate(new_attribute)
        except Exception as e:
            raise ValueError(f"Attribute validation failed: {e}")
        
        # Extract information for the model
        existing_name = existing_validated.name
        existing_values = []
        for v in existing_validated.values:
            value_info = {
                "value_code": v.value_code,
                "name": v.name,
                "description": getattr(v, 'description', '') or '',
                "index_codes": getattr(v, 'index_codes', []) or []
            }
            existing_values.append(value_info)
        
        new_values = []
        for v in new_validated.values:
            value_info = {
                "value_code": v.value_code,
                "name": v.name,
                "description": getattr(v, 'description', '') or '',
                "index_codes": getattr(v, 'index_codes', []) or []
            }
            new_values.append(value_info)
        
        # Create context for the model
        merge_context = f"""Existing Attribute:
        Name: {existing_name}
        Type: {existing_validated.type}
        Description: {getattr(existing_validated, 'description', '')}
        Existing Values: {existing_values}
        
        New Attribute:
        Name: {new_validated.name}
        Type: {new_validated.type}
        Description: {getattr(new_validated, 'description', '')}
        New Values: {new_values}
        
        Please merge these attributes by adding non-duplicative values from the new attribute to the existing attribute."""
        
        result = await self.agent.run(merge_context)
        return result.output
