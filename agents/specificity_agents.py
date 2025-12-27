"""
Specificity checking agents for finding model matching.

This module contains AI agents used to determine if one finding model name
is too general (a hypernym) compared to another finding model name.
"""

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")


class SpecificityCheck(BaseModel):
    """Output from specificity checker"""
    is_too_general: bool = Field(description="True if TERM 2 is too general (hypernym) compared to TERM 1")
    confidence: float = Field(description="Confidence score (0.0 to 1.0)")
    reasoning: str = Field(description="Clear explanation of why TERM 2 is or isn't too general compared to TERM 1")


def create_specificity_check_agent() -> Agent[str, SpecificityCheck]:
    """Create agent for checking if one term is too general compared to another."""
    return Agent(
        model=model,
        output_type=SpecificityCheck,
        system_prompt="""You are a medical imaging expert specializing in radiology finding terminology.

Your task is to determine if TERM 2 is too general (a hypernym) compared to TERM 1.

CRITICAL RULE: TERM 2 is "too general" if it represents a broader category that encompasses TERM 1, but TERM 1 is more specific.

Examples of "too general" (should return is_too_general=True):
- TERM 1: "tunneled catheter" vs TERM 2: "detectable hardware on chest X-ray" → TOO GENERAL
  (tunneled catheter is a specific type of hardware, but "detectable hardware" is too broad)
  
- TERM 1: "pulmonary nodule" vs TERM 2: "pulmonary finding" → TOO GENERAL
  (pulmonary nodule is a specific type of pulmonary finding)

- TERM 1: "pneumothorax" vs TERM 2: "chest abnormality" → TOO GENERAL
  (pneumothorax is a specific chest abnormality)

- TERM 1: "tunneled catheter" vs TERM 2: "detectable hardware" → TOO GENERAL
  (works in either direction - if TERM 2 is the general one, it's too general)

Examples of NOT "too general" (should return is_too_general=False):
- TERM 1: "pulmonary nodule" vs TERM 2: "pulmonary nodule" → NOT TOO GENERAL (same)
- TERM 1: "tension pneumothorax" vs TERM 2: "pneumothorax" → NOT TOO GENERAL (TERM 1 is more specific, but TERM 2 is still appropriate)
- TERM 1: "anterior mediastinal mass" vs TERM 2: "mediastinal mass" → NOT TOO GENERAL (TERM 1 is a subtype, but TERM 2 is still specific enough)

KEY PRINCIPLES:
1. If TERM 2 contains very general terms like "detectable", "hardware", "device", "finding", "abnormality" without specificity, it's likely too general
2. If TERM 2 is a broad category and TERM 1 is a specific instance, TERM 2 is too general
3. If both are similarly specific (even if one is slightly more specific), it's NOT too general
4. Consider medical terminology: specific anatomical structures or conditions are preferred over generic terms
5. This check works bidirectionally - determine which term is more general and return True if TERM 2 is the general one

Provide a confidence score (0.0 to 1.0) and clear reasoning for your decision."""
    )

