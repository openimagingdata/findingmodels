"""
Attribute Processing Agents

This module contains AI agents for attribute classification, comparison, and merging.
"""

import json
import os
from typing import Literal, Dict, Any, Union, Optional
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry
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


class AttributeNameSimilarity(BaseModel):
    """Output from attribute name similarity agent"""
    is_similar: bool
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


def create_name_similarity_agent() -> Agent[str, AttributeNameSimilarity]:
    """Create agent for checking if two attribute names are semantically similar"""
    return Agent(
        model=model,
        output_type=AttributeNameSimilarity,
        system_prompt=f"""{system_medial_expert_prompt}

Your task is to determine if two attribute names are semantically similar (referring to the same concept).

Examples of semantically similar attribute names:
- "Plurality" and "number" (both refer to count/quantity: single vs multiple)
- "Size" and "size Finding" (both refer to dimensions)
- "Location" and "location" (same word, different case)
- "Morphology" and "morphology" (same word, different case)
- "Status" and "change from prior" (both refer to temporal changes)

Examples of NOT semantically similar:
- "Size" and "Location" (different concepts)
- "Composition" and "Calcification" (different concepts)
- "Presence" and "Size" (different concepts)

Consider:
- Medical terminology and synonyms
- Case variations (should be considered similar)
- Abbreviations and full forms
- Related concepts (e.g., "number" and "plurality" both refer to count)

Return True if the names refer to the same or very similar concepts, False otherwise.
Provide a confidence score (0.0 to 1.0) and clear reasoning."""
    )


def create_classification_agent() -> Agent[str, AttributeClassification]:
    """Create agent for classifying attributes as presence, change_from_prior, or other"""
    return Agent(
        model=model,
        output_type=AttributeClassification,
        system_prompt=f"""{system_medial_expert_prompt}

Your task is to classify potential attribute definitions into three categories:

1. "presence" - Attributes that ask whether the FINDING ITSELF is present or absent
Value examples: ["present", "absent", "unknown", "indeterminate"]
CRITICAL: Only classify as "presence" if asking about the finding itself being present/absent.
DO NOT classify as "presence" if asking about features/characteristics of the finding.

CORRECT "presence" examples:
- "Presence" (with finding name in context)
- "Presence of breast mass" (when asking if breast mass exists)
- "adrenal nodule present" = presence

INCORRECT - These should be "other", NOT "presence":
- "Enhancement" (with present/absent values) = other (asking about feature of finding)
- "Breast calcifications" (with present/absent values) = other (asking about feature, not finding itself)
- "Skin thickening" (with present/absent values) = other (feature of finding)
- "Nipple retraction" (with present/absent values) = other (feature of finding)
- "Axillary lymphadenopathy" (with present/absent values) = other (separate finding/feature)
- "Microscopic fat" (with present/absent values) = other (feature of finding)
- "Enhancement pattern" = other (characteristic, not presence)

KEY RULE: If the attribute name describes a FEATURE, CHARACTERISTIC, or RELATED FINDING (even if it has "present"/"absent" values), it is "other", NOT "presence".

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

You have access to a ComparisonContext with:
- existing_attribute: The existing attribute to compare
- new_attribute: The new attribute to compare  
- finding_name: The name of the finding
- attribute_type: The type of attributes

CRITICAL: You must examine existing_attribute.values and new_attribute.values to compare the actual value sets.

Your task is to determine the relationship between the existing attribute definitions and proposed new attributes for the same finding:

1. "identical" - EXACTLY the same attribute (same name, same values, same meaning). All values must match exactly.
2. "expanded" - Same concept but new one has more values. The new attribute contains ALL the existing values PLUS additional ones. This is the most common case when comparing similar attributes.
3. "different" - Completely different attribute that should be added separately

CRITICAL RULES FOR CLASSIFICATION:
- If the new attribute has ALL the existing values PLUS additional values → "expanded"
- **SPECIAL CASE: If existing attribute has NO values (empty list) and new attribute has values, and names match (case-insensitive) → "expanded"** (new attribute adds values to empty existing)
- If the value sets are exactly identical → "identical" 
- If the value sets are completely different → "different"
- Your reasoning MUST match your classification choice

MANDATORY ANALYSIS STEPS:
1. List all values from existing_attribute.values by name (may be empty!)
2. List all values from new_attribute.values by name
3. **If existing has no values and new has values and names match → "expanded"**
4. Check if new values contain ALL existing values plus extras → "expanded"
5. Check if value sets are identical → "identical"
6. Otherwise → "different"

Consider:
- Attribute names (exact match vs semantic similarity)
- Value sets (must be explicitly compared by name)
- Descriptions and metadata
- Medical meaning and context

For "expanded" relationships, provide a merge strategy explaining how to combine them.
Provide confidence score (0.0 to 1.0) and clear reasoning that includes the value comparison.

IMPORTANT: Your classification must be consistent with your reasoning. If you say the new attribute has more values, classify as "expanded", not "identical"."""
    )


def create_merger_agent() -> Agent[str, MergedAttribute]:
    """Create agent for merging enhanced attributes"""
    return Agent(
        model=model,
        output_type=MergedAttribute,
        system_prompt=f"""{system_medial_expert_prompt}
        
Given two attributes that represent the same concept but one is expanded, create a merged attribute that:
- Preserves the best name and description
- Combines all unique values from both attributes
- Maintains proper value descriptions
- Keeps the most comprehensive metadata
- Ensures no information is lost
- All of the values from the existing attribute must be preserved and must maintain their original code and meaning. 
- New attributes added to existing attributes must get their own codes that follow the existing attribute code structure: based on the attribute ID with a decimal and unique index integer.
(e.g. OIFMA_MGB_786842.0.1, OIFMA_MGB_786842.0.2, etc.)

Return the complete merged attribute JSON and notes about what was combined."""
    )


class AttributeNameSimilarityChecker:
    """Checks if two attribute names are semantically similar"""
    
    def __init__(self):
        self.agent = create_name_similarity_agent()
    
    async def check_similarity(self, name1: str, name2: str, finding_name: str = None) -> AttributeNameSimilarity:
        """Check if two attribute names are semantically similar"""
        context = f"Finding: {finding_name}\n" if finding_name else ""
        prompt = f"""{context}Attribute Name 1: {name1}
Attribute Name 2: {name2}

Are these two attribute names semantically similar (referring to the same concept)?"""
        
        result = await self.agent.run(prompt)
        return result.output


class AttributeClassifier:
    """Classifies attributes as presence, change_from_prior, or other"""
    
    def __init__(self):
        self.agent = create_classification_agent()
    
    async def classify_attribute(self, attribute_json: Dict[str, Any], finding_name: str = None) -> AttributeClassification:
        """Classify an attribute JSON as presence, change_from_prior, or other"""
        # Validate the JSON using Pydantic models
        attr_name = attribute_json.get('name', 'unknown')
        attr_type = attribute_json.get('type', 'unknown')
        
        try:
            # Try to parse as ChoiceAttributeIded first
            validated_attribute = ChoiceAttributeIded.model_validate(attribute_json)
        except Exception as e1:
            try:
                # If that fails, try NumericAttributeIded
                validated_attribute = NumericAttributeIded.model_validate(attribute_json)
            except Exception as e2:
                # If both fail, print detailed error and raise
                error_details = []
                if attr_type == 'choice':
                    values = attribute_json.get('values', [])
                    if not values or len(values) < 2:
                        error_details.append(f"choice attribute requires at least 2 values (has {len(values) if values else 0})")
                    # Check for missing IDs - need oifma_id specifically for value code generation
                    has_oifma_id = 'oifma_id' in attribute_json
                    has_attribute_id = 'attribute_id' in attribute_json
                    if not has_oifma_id and not has_attribute_id:
                        error_details.append("missing oifma_id/attribute_id")
                    elif has_attribute_id and not has_oifma_id:
                        error_details.append("has attribute_id but missing oifma_id (needed for value code generation)")
                    max_selected = attribute_json.get('max_selected', 1)
                    if max_selected is not None and max_selected < 1:
                        error_details.append(f"max_selected must be >= 1 (is {max_selected})")
                
                reason = "; ".join(error_details) if error_details else str(e1) or str(e2)
                print(f"Failed validation at classification step for '{attr_name}': {reason}")
                raise ValueError(f"Attribute JSON failed Pydantic validation: {reason}")
        
        # Extract validated information
        name = validated_attribute.name
        attr_type = validated_attribute.type
        description = getattr(validated_attribute, 'description', '')
        
        # Extract values (only choice attributes have values)
        values = [{"name": v.name, "description": getattr(v, 'description', '')} for v in validated_attribute.values] if attr_type == "choice" else []
        
        # Create comprehensive context for the AI
        finding_context = f"Finding: {finding_name}\n" if finding_name else ""
        attribute_str = f"""{finding_context}Attribute Name: {name}
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
        
        # Get the existing and new values for comparison
        existing_values = [v.get('name') for v in existing_attribute.get('values', [])]
        new_values = [v.get('name') for v in new_attribute.get('values', [])]
        
        # Check for special case: existing has no values
        existing_empty = len(existing_values) == 0
        new_has_values = len(new_values) > 0
        names_match = existing_attribute.get('name', '').lower() == new_attribute.get('name', '').lower()
        
        special_case_note = ""
        if existing_empty and new_has_values and names_match:
            special_case_note = "\n\n⚠️ SPECIAL CASE: Existing attribute has NO values (empty), but new attribute has values and names match. This should be classified as 'expanded' (new attribute adds values to empty existing)."
        
        result = await self.agent.run(
            f"""Compare attributes for '{finding_name}':

EXISTING:
- Name: {existing_attribute.get('name')}
- Values: {existing_values if existing_values else '[EMPTY - no values]'}

NEW:
- Name: {new_attribute.get('name')}
- Values: {new_values}

{special_case_note}

Decide: identical, expanded, or different. Ground your reasoning in the listed values.

CRITICAL: 
- **If existing has NO values and new has values and names match → "expanded"**
- If new values contain ALL existing values plus additional ones → "expanded"
- If value sets are exactly the same → "identical"
- If value sets are different → "different"
- Your classification must match your reasoning!""",
            deps=context
        )
        
        # Validate the result and provide feedback if inconsistent
        output = result.output
        if output.relationship == "identical" and len(new_values) > len(existing_values):
            raise ModelRetry(f"Classification error: You classified as 'identical' but new attribute has {len(new_values)} values while existing has {len(existing_values)}. If new attribute contains all existing values plus additional ones, it should be classified as 'expanded'.")
        elif output.relationship == "expanded" and not all(val in new_values for val in existing_values):
            raise ModelRetry(f"Classification error: You classified as 'expanded' but not all existing values are present in new values. Existing: {existing_values}, New: {new_values}")
        
        return output


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
