"""
Attribute Classifier Agent

This module contains the AttributeClassifier AI agent that determines if an attribute
is "presence", "change_from_prior", or "other" based on its name, type, description, and values.
"""

import json
import os
from typing import Literal, Dict, Any, Union
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv
from findingmodel import ChoiceAttributeIded, NumericAttributeIded

# Load environment variables from .env file
load_dotenv()


# Pydantic model returned by the agent
class AttributeClassification(BaseModel):
    """Output from attribute classifier"""
    classification: Literal["presence", "change_from_prior", "other"]
    confidence: float
    reasoning: str


# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")


class AttributeClassifier:
    """Classifies attributes as presence, change_from_prior, or other"""
    
    def __init__(self):
        self.agent = Agent(
            model=model,
            output_type=AttributeClassification,
            system_prompt="""You are a medical imaging expert specializing in finding model attributes.

            Your task is to classify finding model attributes into three categories:

            1. "presence" - Attributes that ask whether something is present or absent
            Value examples: ["present", "absent", "unknown", "indeterminate"]

            2. "change_from_prior" - Attributes that ask about changes over time compared to previous scans
            Examples: "change_from_prior", "progression", "interval_change", "stability", "Status"
            Values examples: ["unchanged", "stable", "increased", "decreased", "new", "resolved", "no prior"]

            3. "other" - All other attributes (size, location, characteristics, etc.)
            Value Examples: "size", "location", "shape", "density", "enhancement" "Morphology", "Type Finding", "Severity"

            Analyze the attribute name and values to determine the most appropriate classification.
            Important:Presence will always have present, absent, unknown, or indeterminate as values.
            Important: Change from prior will always have unchanged, stable, increased, decreased, new, resolved, or no prior as values.
            Consider both the attribute name and the actual values when making your decision.
            Provide a confidence score (0.0 to 1.0) and clear reasoning for your classification."""
        )
    
    
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
