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
    relationship: Literal["identical", "enhanced", "subset", "different", "no_similarities"]
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

RELATIONSHIP TYPES:

1. "identical" - Both attributes have exactly the same values (order doesn't matter)
   - Example: Existing: ["present", "absent"], Incoming: ["present", "absent"] → identical
   - Example: Existing: ["solid", "subsolid"], Incoming: ["solid", "subsolid"] → identical

2. "enhanced" - INCOMING has ALL the values from EXISTING plus additional values
   - Example: Existing: ["present", "absent"], Incoming: ["present", "absent", "unknown", "indeterminate"] → enhanced
   - Example: Existing: ["smooth", "lobulated"], Incoming: ["smooth", "lobulated", "spiculated", "ill-defined"] → enhanced
   - CRITICAL: All existing values must be present in incoming, AND incoming must have at least one additional value

3. "subset" - EXISTING has ALL the values from INCOMING plus additional values
   - Example: Existing: ["present", "absent", "unknown", "indeterminate"], Incoming: ["present", "absent"] → subset
   - Example: Existing: ["smooth", "lobulated", "spiculated", "ill-defined"], Incoming: ["smooth", "lobulated"] → subset
   - CRITICAL: All incoming values must be present in existing, AND existing must have at least one additional value

4. "different" - There are some shared values, but each attribute has unique values not in the other
   - Example: Existing: ["present", "absent", "unknown"], Incoming: ["present", "absent", "indeterminate"] → different
   - Example: Existing: ["smooth", "lobulated", "spiculated"], Incoming: ["smooth", "lobulated", "ill-defined"] → different
   - CRITICAL: Must have at least one shared value AND at least one value unique to each attribute

5. "no_similarities" - No shared values at all (completely different value sets)
   - Example: Existing: ["present", "absent"], Incoming: ["solid", "subsolid"] → no_similarities
   - Example: Existing: ["smooth", "lobulated"], Incoming: ["right upper lobe", "left lower lobe"] → no_similarities
   - CRITICAL: Zero overlap in values

IMPORTANT RULES:
- **PLACEHOLDER VALUES**: If an attribute has placeholder values (e.g., "placeholder_value_1", "placeholder_value_2"), these indicate that the attribute definition exists but actual values are missing from the database. **CRITICAL**: Placeholder values are NOT real values and should be ignored when determining relationships.
  
  **SPECIAL CASE - Semantically Similar Attributes with Placeholders**:
  - If attributes are semantically the same (refer to the same concept) AND:
    - Existing has ONLY placeholders (no real values) AND incoming has real values → **"enhanced"** (incoming provides the missing real values)
    - Existing has real values AND incoming has ONLY placeholders → **"subset"** (existing already has the real values)
    - Both have ONLY placeholders → **"identical"** (both incomplete, but same structure)
  
  **CRITICAL RULE**: When one attribute has placeholders and the other has real values, and they are semantically the same:
  - DO NOT classify as "no_similarities" just because placeholders don't match real values
  - Classify as "enhanced" if incoming has real values and existing has placeholders
  - Classify as "subset" if existing has real values and incoming has placeholders
  - Placeholder values should be clearly identified in the shared_values, existing_only_values, and incoming_only_values lists, but they should NOT prevent "enhanced" classification when semantically similar
- For numeric attributes, compare the ranges (min/max) and units
- For choice attributes, compare the actual value names (case-insensitive)
- Order of values does NOT matter
- Case differences in value names should be normalized (treat as same)
- Be precise: "enhanced" and "subset" require ALL values from one to be in the other

OUTPUT REQUIREMENTS:
- relationship: One of the five relationship types above
- confidence: How certain you are (0.0 to 1.0)
- reasoning: **CRITICAL** - Provide a clear, detailed explanation of:
  * Why you chose this specific relationship type
  * How the values compare (which values are shared, which are unique)
  * What makes this relationship "identical", "enhanced", "subset", "different", or "no_similarities"
  * Any special considerations (e.g., placeholder values, incomplete data)
- recommendation: **CRITICAL** - Must be "merge" or "no_merge":
  * "merge" if relationship is "enhanced" (incoming has all existing values plus more, OR incoming has real values and existing has only placeholders)
  * "no_merge" if relationship is "identical" (same values)
  * "merge" if semantically same attributes but one has real values and other has only placeholders (incomplete data case - incoming provides missing values)
  * "no_merge" for "subset" (existing has more real values, so no need to merge incoming)
  * "no_merge" for "different" or "no_similarities" (different attributes, UNLESS they are semantically similar and one has placeholders while other has real values - then use "enhanced" + "merge")
- existing_values: List of all values from the existing attribute
- incoming_values: List of all values from the incoming attribute
- shared_values: List of values present in both attributes
- existing_only_values: List of values only in existing attribute
- incoming_only_values: List of values only in incoming attribute

**IMPORTANT**: Your reasoning must clearly explain your classification decision. Be specific about value comparisons and why the relationship is what you say it is. Your recommendation must be consistent with the relationship type.

Analyze the provided attributes carefully and determine the most accurate relationship."""
    )

