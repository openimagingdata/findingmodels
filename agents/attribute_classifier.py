"""
Attribute Processing Agents

This module contains AI agents for attribute classification, comparison, and merging.
"""

import json
import os
from typing import Literal, Dict, Any, Union, Optional
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv
from findingmodel import ChoiceAttributeIded, NumericAttributeIded

# Load environment variables from .env file
load_dotenv()


# Pydantic models for agent outputs
class AttributeClassification(BaseModel):
    """Output from attribute classifier"""
    classification: Literal["presence", "change_from_prior", "other"]
    confidence: float
    reasoning: str


class AttributeComparison(BaseModel):
    """Output from attribute comparison agent"""
    relationship: Literal["identical", "expanded", "different"]
    confidence: float
    reasoning: str
    merge_strategy: Optional[str] = Field(None, description="Strategy for merging if enhanced")


class MergedAttribute(BaseModel):
    """Output from attribute merger agent"""
    merged_attribute: Dict[str, Any]
    merge_notes: str


# Context for comparison agent
@dataclass
class ComparisonContext:
    existing_attribute: Dict[str, Any]
    new_attribute: Dict[str, Any]
    finding_name: str
    attribute_type: str


# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")

system_medial_expert_prompt = """
You are a medical imaging expert specializing in the attributes of findings that radiologist describe in medical imaging exams.

We are working with a system for defining data models for these imaging findings. Each finding model consists of basic descriptive data and a set of attributes
that represent the different descriptors used in clinical practice. In this system, there are two kinds of attributes: Numeric and Choice. 
Choice represents a categorical descriptor with defined allowed values.

 """


def create_classification_agent() -> Agent[str, AttributeClassification]:
    """Create agent for classifying attributes as presence, change_from_prior, or other"""
    return Agent(
        model=model,
        output_type=AttributeClassification,
        system_prompt=f"""{system_medial_expert_prompt}

Your task is to classify potential attribute definitions into three categories:

1. "presence" - Attributes that ask whether something is present or absent
Value examples: ["present", "absent", "unknown", "indeterminate"]

2. "change_from_prior" - Attributes that ask about changes over time compared to previous scans
Examples: "change_from_prior", "progression", "interval_change", "stability", "Status"
Values examples: ["unchanged", "stable", "increased", "decreased", "new", "resolved", "no prior"]

3. "other" - All other attributes (size, location, characteristics, etc.)
Value Examples: "size", "location", "shape", "density", "enhancement" "Morphology", "Type Finding", "Severity"

Analyze the attribute name and values to determine the most appropriate classification.
Important:Presence will always have present and absent. Although not always using those words. 
Important: Change from prior will usually have choices like "unchanged", "stable", "increased", "decreased", "new", "resolved", or "no prior" as values.
Consider both the attribute name and the actual values when making your decision.
Provide a confidence score (0.0 to 1.0) and clear and concise reasoning for your classification."""
    )


def create_comparison_agent() -> Agent[ComparisonContext, AttributeComparison]:
    """Create agent for comparing two attributes of the same type"""
    return Agent(
        model=model,
        output_type=AttributeComparison,
        deps_type=ComparisonContext,
        system_prompt=f"""{system_medial_expert_prompt}

Your task is to determine the relationship between the existing attribute definitions and proposed new attributes for the same finding:

1. "identical" - Same attribute, no action needed (same name, same values, same meaning)
2. "expanded" - Same concept but new one is that has more values, better descriptions and/oradditional metadata.
3. "different" - Completely different attribute that should be added separately

Consider:
- Attribute names (exact match vs semantic similarity)
- Values (identical, subset, superset, or different)
- Descriptions and metadata
- Medical meaning and context

For "expanded" relationships, provide a merge strategy explaining how to combine them.
Provide confidence score (0.0 to 1.0) and clear reasoning."""
    )


def create_merger_agent() -> Agent[str, MergedAttribute]:
    """Create agent for merging enhanced attributes"""
    return Agent(
        model=model,
        output_type=MergedAttribute,
        system_prompt="""You are a medical imaging expert merging two enhanced attributes.

Given two attributes that represent the same concept but one is expanded, create a merged attribute that:
- Preserves the best name and description
- Combines all unique values from both attributes
- Maintains proper value descriptions
- Keeps the most comprehensive metadata
- Ensures no information is lost
- All of the values from the existing attribute must be presurved and must mantain their original code and meaning. 
- New attributes added to existing attributes must get their own codes that follow the existing attribute code structure: based on the attribute ID with a decimal and unique index integer.
(e.g. OIFMA_MGB_786842.0.1, OIFMA_MGB_786842.0.2, etc.)

Return the complete merged attribute JSON and notes about what was combined."""
    )


class AttributeClassifier:
    """Classifies attributes as presence, change_from_prior, or other"""
    
    def __init__(self):
        self.agent = create_classification_agent()
    
    async def classify_attribute(self, attribute_json: Dict[str, Any]) -> AttributeClassification:
        """Classify an attribute JSON as presence, change_from_prior, or other"""
        # Validate the JSON using Pydantic models
        try:
            # Try to parse as ChoiceAttributeIded first
            validated_attribute = ChoiceAttributeIded.model_validate(attribute_json)
        except Exception:
            try:
                # If that fails, try NumericAttributeIded
                validated_attribute = NumericAttributeIded.model_validate(attribute_json)
            except Exception:
                # If both fail, print and raise error
                print("Failed validation")
                raise ValueError("Attribute JSON failed Pydantic validation")
        
        # Extract validated information
        name = validated_attribute.name
        attr_type = validated_attribute.type
        description = getattr(validated_attribute, 'description', '')
        
        # Extract values (only choice attributes have values)
        values = [{"name": v.name, "description": getattr(v, 'description', '')} for v in validated_attribute.values] if attr_type == "choice" else []
        
        # Create comprehensive context for the AI
        attribute_str = f"""Attribute Name: {name}
        Type: {attr_type}
        Description: {description}
        Values: {values}"""
        
        result = await self.agent.run(attribute_str)
        return result.output


class AttributeComparator:
    """Compares two attributes to determine their relationship"""
    
    def __init__(self):
        self.agent = create_comparison_agent()
    
    async def compare_attributes(
        self, 
        existing_attribute: Dict[str, Any], 
        new_attribute: Dict[str, Any], 
        finding_name: str, 
        attribute_type: str
    ) -> AttributeComparison:
        """Compare two attributes and determine their relationship"""
        context = ComparisonContext(
            existing_attribute=existing_attribute,
            new_attribute=new_attribute,
            finding_name=finding_name,
            attribute_type=attribute_type
        )
        
        result = await self.agent.run(
            f"Compare the existing and new {attribute_type} attributes for finding '{finding_name}'",
            deps=context
        )
        return result.output


class AttributeMerger:
    """Merges enhanced attributes intelligently"""
    
    def __init__(self):
        self.agent = create_merger_agent()
    
    async def merge_attributes(
        self, 
        existing_attribute: Dict[str, Any], 
        new_attribute: Dict[str, Any], 
        merge_strategy: str
    ) -> MergedAttribute:
        """Merge two enhanced attributes based on strategy"""
        merge_instructions = f"""
        Merge these attributes using strategy: {merge_strategy}
        
        Existing attribute:
        {json.dumps(existing_attribute, indent=2)}
        
        New attribute:
        {json.dumps(new_attribute, indent=2)}
        """
        
        result = await self.agent.run(merge_instructions)
        return result.output
