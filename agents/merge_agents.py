"""
Merge Agents

This module contains AI agents for merging finding model attributes.
"""

import json
import os
from typing import Literal, Dict, Any, Union, Optional, List
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")

system_medial_expert_prompt = """
You are a medical imaging expert specializing in the attributes of findings that radiologist describe in medical imaging exams.

We are working with a system for defining data models for these imaging findings. Each finding model consists of basic descriptive data and a set of attributes
that represent the different descriptors used in clinical practice. In this system, there are two kinds of attributes: Numeric and Choice. 
Choice represents a categorical descriptor with defined allowed values.

 """


# Pydantic models for agent outputs
class AttributeClassification(BaseModel):
    """Output from attribute classifier"""
    classification: Literal["presence", "change_from_prior", "other"]
    confidence: float
    reasoning: str


class AttributeRelationship(BaseModel):
    """Output from attribute relationship classifier"""
    relationship: Literal["identical", "enhanced", "subset", "needs_review", "no_similarities"]
    confidence: float
    reasoning: str
    recommendation: Literal["merge", "no_merge"] = Field(description="Recommendation: merge if incoming is enhanced or if semantically same but with different values")
    existing_values: List[str] = Field(default_factory=list, description="List of existing attribute values")
    incoming_values: List[str] = Field(default_factory=list, description="List of incoming attribute values")
    shared_values: List[str] = Field(default_factory=list, description="Values present in both attributes")
    existing_only_values: List[str] = Field(default_factory=list, description="Values only in existing attribute")
    incoming_only_values: List[str] = Field(default_factory=list, description="Values only in incoming attribute")


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


def create_attribute_relationship_agent() -> Agent[str, AttributeRelationship]:
    """Create agent for classifying the relationship between two attributes."""
    return Agent(
        model=model,
        output_type=AttributeRelationship,
        system_prompt=f"""{system_medial_expert_prompt}

Your task is to classify the relationship between two attributes (EXISTING and INCOMING) that refer to the same concept.

The attributes will be provided with their names, types, and values. You need to determine how the INCOMING attribute relates to the EXISTING attribute.

DECISION TREE - Follow this order when classifying:

1. Check if ALL values from one attribute are contained in the other:
   - If ALL incoming values are in existing AND existing has more → "subset"
   - If ALL existing values are in incoming AND incoming has more → "enhanced"
   - If ALL values match exactly → "identical"
   
2. If not all values are contained, check for overlap:
   - If there are shared values AND each has unique values → "needs_review"
   - If there are NO shared values → "no_similarities"

RELATIONSHIP TYPES:

1. "identical" - Both attributes have exactly the same values (order doesn't matter)
   - Example: Existing: ["present", "absent"], Incoming: ["present", "absent"] → identical
   - Example: Existing: ["solid", "subsolid"], Incoming: ["solid", "subsolid"] → identical
   - CRITICAL: Every value in existing must be in incoming, AND every value in incoming must be in existing

2. "enhanced" - INCOMING has ALL the values from EXISTING plus additional values
   - Example: Existing: ["present", "absent"], Incoming: ["present", "absent", "unknown", "indeterminate"] → enhanced
   - Example: Existing: ["smooth", "lobulated"], Incoming: ["smooth", "lobulated", "spiculated", "ill-defined"] → enhanced
   - CRITICAL: ALL existing values must be present in incoming, AND incoming must have at least one additional value
   - If even one existing value is missing from incoming, this is NOT "enhanced"

3. "subset" - EXISTING has ALL the values from INCOMING plus additional values
   - Example: Existing: ["present", "absent", "unknown", "indeterminate"], Incoming: ["present", "absent"] → subset
   - Example: Existing: ["left", "right", "unknown"], Incoming: ["left", "right"] → subset
   - CRITICAL: ALL incoming values must be present in existing, AND existing must have at least one additional value
   - If even one incoming value is missing from existing, this is NOT "subset"
   - IMPORTANT: If incoming has NO unique values (all its values are in existing), this MUST be "subset", NOT "different"

4. "needs_review" - There are some shared values, but each attribute has unique values not in the other
   - Example: Existing: ["present", "absent", "unknown"], Incoming: ["present", "absent", "indeterminate"] → needs_review
   - Example: Existing: ["smooth", "lobulated", "spiculated"], Incoming: ["smooth", "lobulated", "ill-defined"] → needs_review
   - CRITICAL: Must have at least one shared value AND at least one value unique to EACH attribute
   - If incoming has NO unique values (all incoming values are in existing), this is "subset", NOT "needs_review"
   - If existing has NO unique values (all existing values are in incoming), this is "enhanced", NOT "needs_review"

5. "no_similarities" - No shared values at all (completely different value sets)
   - Example: Existing: ["present", "absent"], Incoming: ["solid", "subsolid"] → no_similarities
   - Example: Existing: ["smooth", "lobulated"], Incoming: ["right upper lobe", "left lower lobe"] → no_similarities
   - CRITICAL: Zero overlap in values

IMPORTANT RULES:
- For numeric attributes, compare the ranges (min/max) and units
- For choice attributes, compare the actual value names (case-insensitive)
- Order of values does NOT matter
- Case differences in value names should be normalized (treat as same)
- Be precise: "enhanced" and "subset" require ALL values from one to be in the other
- ALWAYS check for "subset" or "enhanced" FIRST before considering "needs_review"
- If one attribute has no unique values (all its values are in the other), it cannot be "needs_review"

OUTPUT REQUIREMENTS:
- relationship: One of the five relationship types above
- confidence: How certain you are (0.0 to 1.0)
- reasoning: **CRITICAL** - Provide a clear, detailed explanation of:
  * Why you chose this specific relationship type
  * How the values compare (which values are shared, which are unique)
  * Explicitly state: "All incoming values are in existing" or "Some incoming values are not in existing"
  * Explicitly state: "Incoming has unique values: [list]" or "Incoming has no unique values"
  * What makes this relationship "identical", "enhanced", "subset", "needs_review", or "no_similarities"
- recommendation: **CRITICAL** - Must be "merge" or "no_merge":
  * "merge" if relationship is "enhanced" (incoming has all existing values plus more)
  * "no_merge" if relationship is "identical" (same values)
  * "no_merge" for "subset" (existing has more values, so no need to merge incoming)
  * "no_merge" for "needs_review" or "no_similarities" (requires human review or different attributes)
- existing_values: List of all values from the existing attribute
- incoming_values: List of all values from the incoming attribute
- shared_values: List of values present in both attributes
- existing_only_values: List of values only in existing attribute
- incoming_only_values: List of values only in incoming attribute

**IMPORTANT**: Your reasoning must clearly explain your classification decision. Be specific about value comparisons and why the relationship is what you say it is. Your recommendation must be consistent with the relationship type.

Analyze the provided attributes carefully and determine the most accurate relationship."""
    )

