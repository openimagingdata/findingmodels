"""
Formatting agents for Hood definition processing.

This module contains AI agents used for formatting and transforming finding models,
including acronym expansion, eponym minimization, and sub-finding extraction.
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")

system_medical_expert_prompt = """
You are a medical imaging expert specializing in radiology finding terminology and nomenclature.

We are working with a system for defining data models for radiology findings. Each finding model has:
- A name (should be descriptive, lowercase, with acronyms spelled out)
- Synonyms (alternative terms, including compact acronym forms)
- Attributes (characteristics of the finding)

Your task is to help format and transform finding model names according to medical terminology best practices.
"""


class AcronymExpansion(BaseModel):
    """Output from acronym expansion agent"""
    expanded_name: str = Field(description="The name with all acronyms expanded to full terms")
    compact_forms: List[str] = Field(default_factory=list, description="List of compact acronym forms to add as synonyms (e.g., ['ACL tear', 'IVC filter'])")
    confidence: float = Field(description="Confidence score (0.0 to 1.0)")
    reasoning: str = Field(description="Explanation of acronyms detected and how they were expanded")


class EponymMinimization(BaseModel):
    """Output from eponym minimization agent"""
    descriptive_name: str = Field(description="The name with eponym replaced by descriptive term, or original name if no eponym found")
    has_eponym: bool = Field(description="True if an eponym was detected in the name")
    eponym_synonym: Optional[str] = Field(default=None, description="The original eponym form to add as synonym (e.g., 'Bochdalek hernia')")
    confidence: float = Field(description="Confidence score (0.0 to 1.0)")
    reasoning: str = Field(description="Explanation of eponym detection and replacement, or why no change was made")


class SubFindingExtraction(BaseModel):
    """Output from sub-finding extraction agent"""
    should_extract: bool = Field(description="True if any components should be extracted or kept with presence")
    extracted_components: List[dict] = Field(default_factory=list, description="Components to extract as separate findings (have unique attributes). Each dict has 'name', 'description', and 'attributes' (list of attribute names)")
    kept_components: List[dict] = Field(default_factory=list, description="Components to keep in main finding but add presence attribute (no unique attributes). Each dict has 'name' and 'description'")
    main_model_attributes: List[str] = Field(default_factory=list, description="List of attribute names to keep in main model")
    confidence: float = Field(description="Confidence score (0.0 to 1.0)")
    reasoning: str = Field(description="Explanation of why components should or shouldn't be extracted, and which attributes belong where")


def create_acronym_expansion_agent() -> Agent[str, AcronymExpansion]:
    """Create agent for expanding acronyms in finding model names."""
    return Agent(
        model=model,
        output_type=AcronymExpansion,
        system_prompt=f"""{system_medical_expert_prompt}

Your task is to expand acronyms in radiology finding model names and identify compact forms for synonyms.

RULES:
1. Detect all medical acronyms in the finding name (e.g., IVC, PICC, CVC, ECMO, AICD, ACL, SVC)
2. Expand each acronym to its full medical term
3. Preserve the rest of the name structure
4. Identify compact forms (original name with acronyms) to add as synonyms

EXAMPLES:
- Input: "Ivc Filter" → expanded_name: "inferior vena cava filter", compact_forms: ["ivc filter"]
- Input: "Tunneled Cvc" → expanded_name: "tunneled central venous catheter", compact_forms: ["tunneled cvc"]
- Input: "Picc Finding" → expanded_name: "peripherally inserted central catheter finding", compact_forms: ["picc finding"]
- Input: "Ecmo Cannula" → expanded_name: "extracorporeal membrane oxygenation cannula", compact_forms: ["ecmo cannula"]
- Input: "Pacemaker Aicd" → expanded_name: "pacemaker automatic implantable cardioverter defibrillator", compact_forms: ["pacemaker aicd"]
- Input: "pulmonary nodule" → expanded_name: "pulmonary nodule", compact_forms: [] (no acronyms)

COMMON MEDICAL ACRONYMS:
- IVC: inferior vena cava
- PICC: peripherally inserted central catheter
- CVC: central venous catheter
- ECMO: extracorporeal membrane oxygenation
- AICD: automatic implantable cardioverter defibrillator
- ACL: anterior cruciate ligament
- SVC: superior vena cava

IMPORTANT:
- All output should be lowercase (per formatting rules)
- If no acronyms are found, return the original name (lowercased) with empty compact_forms
- Handle multiple acronyms in a single name
- Be context-aware: some acronyms may have different expansions in different contexts

Provide the expanded name, list of compact forms to add as synonyms, confidence, and reasoning."""
    )


def create_eponym_minimization_agent() -> Agent[str, EponymMinimization]:
    """Create agent for minimizing eponyms in finding model names."""
    return Agent(
        model=model,
        output_type=EponymMinimization,
        system_prompt=f"""{system_medical_expert_prompt}

Your task is to minimize eponyms in radiology finding model names by replacing them with descriptive terms.

RULES:
1. Detect eponyms (proper nouns used as medical terms, often capitalized)
2. If an eponym is the preferred term, replace it with a descriptive alternative
3. Keep the original eponym form as a synonym
4. Eponyms can be uppercase but should NOT be the preferred term if a descriptive alternative exists

EXAMPLES:
- Input: "Bochdalek Hernia" → descriptive_name: "congenital diaphragmatic hernia", eponym_synonym: "bochdalek hernia", has_eponym: True
- Input: "Morgagni Hernia" → descriptive_name: "anterior diaphragmatic hernia", eponym_synonym: "morgagni hernia", has_eponym: True
- Input: "pulmonary nodule" → descriptive_name: "pulmonary nodule", eponym_synonym: None, has_eponym: False

COMMON MEDICAL EPONYMS:
- Bochdalek: congenital diaphragmatic (hernia)
- Morgagni: anterior diaphragmatic (hernia)
- Chiari: (various, context-dependent)
- Valsalva: (sinus of Valsalva - may keep as is if no good alternative)

IMPORTANT:
- All output should be lowercase (per formatting rules)
- If no eponym is found, return the original name (lowercased) with has_eponym=False
- If an eponym is found but no good descriptive alternative exists, keep the eponym but set has_eponym=True
- Be conservative: only replace eponyms when a clear, widely-accepted descriptive alternative exists
- Consider medical context and standard terminology

Provide the descriptive name, whether an eponym was found, the eponym synonym (if applicable), confidence, and reasoning."""
    )


def create_sub_finding_extraction_agent() -> Agent[str, SubFindingExtraction]:
    """Create agent for identifying and extracting sub-findings."""
    return Agent(
        model=model,
        output_type=SubFindingExtraction,
        system_prompt=f"""{system_medical_expert_prompt}

Your task is to identify components/subcomponents within a finding model and determine whether they should be extracted as separate findings or kept in the main finding with a presence attribute.

DECISION CRITERIA:

FOR EACH potential component/subcomponent:
  1. Identify component-specific attributes (e.g., "[component] size", "[component] density", "[component] morphology")
  2. Check if attributes ONLY apply to that component (not to main finding)
  3. Identify if "presence of [component]" attribute already exists
  
  IF component has unique attributes (size, density, morphology, etc.):
    → EXTRACT unique attributes to separate finding
    → KEEP "presence of [component]" in main finding (it's a pointer/reference)
    → Remove only component-specific attributes, NOT the presence attribute
  ELSE (component has no unique attributes):
    → KEEP everything as-is
    → Check if "presence of [component]" exists
      - If exists → leave it (no duplicate)
      - If doesn't exist → add "presence of [component]" attribute

CRITICAL RULE: "presence of [component]" is NOT a unique attribute - it's a pointer/reference that should always be kept in the main finding, even when extracting component-specific attributes.

EXAMPLES:

Ground Glass Nodule Example:
- Main finding: "ground glass nodule"
- Attributes: "presence" (of nodule), "size" (overall), "presence of solid component", "solid component size"
- Decision:
  - "solid component size" → Extract (unique attribute) → Create "solid component of ground glass nodule" finding
  - "presence of solid component" → Keep in main (pointer/reference)
  - Result: Main keeps: presence, size, "presence of solid component"
  - Result: New finding created: "solid component of ground glass nodule" with: presence, "solid component size"

KEY RULES:
- Look for attribute names containing component names (e.g., "solid component size")
- Check attribute descriptions to see if they mention "only applies to [component]"
- "presence of [component]" is NOT a unique attribute - it's a pointer/reference
- If component has unique attributes (size, density, etc.) → extract those, but keep presence attribute
- If component has no unique attributes → keep everything, add presence if missing

OUTPUT FORMAT:
- extracted_components: List of components with unique attributes to extract. Each should have 'name', 'description', and 'attributes' (list of unique attribute names, NOT including "presence of [component]")
- kept_components: List of components without unique attributes. Each should have 'name' and 'description'
- main_model_attributes: List of all attribute names to keep in main model (including "presence of [component]" attributes)

Provide whether extraction should occur, list of extracted/kept components, which attributes to keep in main model, confidence, and reasoning."""
    )

