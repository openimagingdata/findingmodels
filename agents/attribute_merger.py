"""
Attribute Merger Agent

This module contains the AttributeMerger AI agent that merges two attributes,
combining their values while preserving all existing values and generating proper IDs.
"""

import json
import os
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Pydantic models for the agent
class AttributeMergeInput(BaseModel):
    """Input for attribute merging"""
    existing_attribute: Dict[str, Any]
    new_attribute: Dict[str, Any]


class AttributeMergeOutput(BaseModel):
    """Output from attribute merger"""
    merged_attribute: Dict[str, Any] = Field(default={}, description="The complete merged attribute object with all values")
    added_values: List[str] = Field(default=[], description="List of new value names that were added")
    skipped_values: List[str] = Field(default=[], description="List of value names that were skipped as duplicates")
    reasoning: str = Field(default="", description="Explanation of what was done and why")


# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")


class AttributeMerger:
    """Merges two attributes, combining their values while preserving existing ones"""
    
    def __init__(self):
        self.agent = Agent(
            model=model,
            output_type=AttributeMergeOutput,
            system_prompt="""You are a medical imaging expert specializing in finding model attribute merging.

Your task is to merge two attributes of the same type, combining their values while preserving all existing values.

CRITICAL RULES:
1. NEVER delete any existing values from the existing attribute
2. Add new unique values from the new attribute
3. If values have the same meaning but different wording, keep both (e.g., "Present" and "Yes")
4. Maintain the existing attribute's name and structure
5. Generate appropriate IDs for new values
6. Preserve the existing attribute's metadata (required, description, etc.)

For each new value:
- Check if it's semantically equivalent to an existing value
- If equivalent, skip it and note in skipped_values
- If unique, add it to the merged attribute
- Generate a new ID for truly new values

The merged attribute should contain all unique values from both attributes, with the existing attribute's structure preserved.

You must return a JSON object with these exact fields:
- merged_attribute: The complete merged attribute object
- added_values: List of new value names that were added
- skipped_values: List of value names that were skipped as duplicates
- reasoning: Explanation of what was done and why"""
        )
    
    async def merge(self, existing: Dict[str, Any], new: Dict[str, Any]) -> AttributeMergeOutput:
        """Merge two attributes, combining their values"""
        # Convert to string for the agent
        merge_str = f"""Existing Attribute:
{json.dumps(existing, indent=2)}

New Attribute:
{json.dumps(new, indent=2)}"""
        
        result = await self.agent.run(merge_str)
        
        # Pydantic AI returns the structured output in the .output attribute
        return result.output
