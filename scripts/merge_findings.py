"""
CLI tool for merging finding models.

This script processes an INCOMING FM JSON file and searches the database for matches.
"""

import asyncio
import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple, List, Any
from datetime import datetime

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from findingmodel.tools import find_similar_models
from findingmodel.index import Index
from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.tools import add_ids_to_model
from findingmodel.common import model_file_name
# Note: We'll create attributes as dicts, not ChoiceAttribute objects
from agents.merge_agents import (
    create_classification_agent, 
    AttributeClassification,
    create_attribute_relationship_agent,
    AttributeRelationship
)
from agents.attribute_classifier import AttributeNameSimilarityChecker


# Helper functions for attribute value extraction
def extract_value_names(attr: Dict[str, Any]) -> List[str]:
    """Extract value names from a choice attribute (handles both dict and object types)."""
    values = attr.get('values', [])
    value_names = []
    for val in values:
        if isinstance(val, dict):
            value_names.append(val.get('name', ''))
        else:
            value_names.append(getattr(val, 'name', ''))
    return value_names


def extract_attr_name(attr: Dict[str, Any]) -> str:
    """Extract attribute name (handles both dict and object types)."""
    return attr.get('name', 'unknown') if isinstance(attr, dict) else getattr(attr, 'name', 'unknown')


async def load_incoming_model(file_path: Path) -> FindingModelFull:
    """Load and validate INCOMING model from JSON file.
    Handles models with or without IDs by using FindingModelBase first."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            model_data = json.load(f)
        
        # Try FindingModelFull first (if it has all IDs)
        try:
            model = FindingModelFull(**model_data)
            return model
        except Exception:
            # If that fails, use FindingModelBase (for models without IDs)
            # Then add IDs using the tool
            base_model = FindingModelBase(**model_data)
            full_model = add_ids_to_model(base_model, source="MGB")
            return full_model
    except Exception as e:
        raise ValueError(f"Failed to load INCOMING model from {file_path}: {e}")


async def find_existing_model(incoming_model: FindingModelFull, index: Index) -> Optional[Dict]:
    """Search for existing model in database.
    
    Returns: highest confidence match dict or None"""
    finding_name = incoming_model.name
    description = incoming_model.description
    synonyms = getattr(incoming_model, 'synonyms', []) or []
    
    # Run similarity analysis
    analysis = await find_similar_models(
        finding_name=finding_name,
        description=description,
        synonyms=synonyms,
        index=index
    )
    
    # If recommendation is to create new, no match found
    if analysis.recommendation == "create_new":
        return None
    
    # If recommendation is to edit existing or review needed, get the highest confidence match
    if analysis.recommendation in ["edit_existing", "review_needed"]:
        if analysis.similar_models and len(analysis.similar_models) > 0:
            # Get the highest confidence match
            best_match = analysis.similar_models[0]
            
            # Convert to dict if it's an object
            if isinstance(best_match, dict):
                return best_match
            else:
                # It's an object (IndexEntry) - convert to dict
                return {
                    'oifm_id': best_match.oifm_id,
                    'name': best_match.name,
                    'slug_name': best_match.slug_name,
                    'filename': best_match.filename,
                    'description': best_match.description,
                    'synonyms': best_match.synonyms,
                    'tags': best_match.tags,
                    'contributors': best_match.contributors
                }
    
    return None


async def get_existing_model_from_db(oifm_id: str, index: Index) -> Optional[Dict[str, Any]]:
    """Load EXISTING model from DuckDB index by oifm_id."""
    try:
        model = await index.get_full(oifm_id)
        if model:
            return model.model_dump(exclude_unset=False, exclude_none=False)
        return None
    except Exception as e:
        print(f"Error loading model {oifm_id} from database: {e}")
        return None


async def classify_attribute(attr: Dict[str, Any], finding_name: str) -> AttributeClassification:
    """Classify a single attribute using the classification agent."""
    classification_agent = create_classification_agent()
    
    # Prepare attribute info for classification
    attr_name = extract_attr_name(attr)
    attr_type = attr.get('type', 'unknown')
    
    # Extract value names if it's a choice attribute
    value_names = []
    if attr_type == 'choice':
        value_names = extract_value_names(attr)
    
    # Create prompt for classification
    prompt = f"""Attribute to classify:
- Name: {attr_name}
- Type: {attr_type}
- Finding: {finding_name}
"""
    if value_names:
        prompt += f"- Values: {', '.join(value_names)}\n"
    
    result = await classification_agent.run(prompt)
    return result.output


async def classify_and_group_attributes(
    attributes: List[Dict[str, Any]], 
    finding_name: str
) -> Dict[str, List[Dict[str, Any]]]:
    """Classify all attributes and group them by classification.
    
    Returns: Dict with keys 'presence', 'change_from_prior', 'other', each containing list of attributes with their classification."""
    grouped = {
        'presence': [],
        'change_from_prior': [],
        'other': []
    }
    
    for attr in attributes:
        try:
            classification = await classify_attribute(attr, finding_name)
            
            # Add classification info to attribute
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = classification.classification
            attr_with_classification['_confidence'] = classification.confidence
            attr_with_classification['_reasoning'] = classification.reasoning
            
            # Group by classification
            grouped[classification.classification].append(attr_with_classification)
        except Exception as e:
            # Add to 'other' as fallback
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = 'other'
            attr_with_classification['_confidence'] = 0.0
            attr_with_classification['_reasoning'] = f"Classification failed: {e}"
            grouped['other'].append(attr_with_classification)
    
    return grouped


def normalize_incomplete_attribute(attr: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize attributes by ensuring basic requirements are met.
    
    Returns normalized attribute dict."""
    normalized = attr.copy()
    
    if normalized.get('type') == 'choice':
        # Ensure max_selected is valid
        if normalized.get('max_selected', 1) < 1:
            normalized['max_selected'] = 1
    
    # Ensure oifma_id exists (use attribute_id if available)
    if not normalized.get('oifma_id') and normalized.get('attribute_id'):
        normalized['oifma_id'] = normalized.get('attribute_id')
    
    return normalized


async def compare_attributes_within_group(
    incoming_attrs: List[Dict[str, Any]],
    existing_attrs: List[Dict[str, Any]],
    classification_type: str,
    finding_name: str
) -> List[Dict[str, Any]]:
    """Compare attributes within the same classification group using the relationship agent.
    
    Returns: List of comparison results with relationship information."""
    relationship_agent = create_attribute_relationship_agent()
    comparisons = []
    
    # Normalize all attributes first
    normalized_incoming = [normalize_incomplete_attribute(attr) for attr in incoming_attrs]
    normalized_existing = [normalize_incomplete_attribute(attr) for attr in existing_attrs]
    
    # Compare each incoming attribute with each existing attribute
    for incoming_attr in normalized_incoming:
        incoming_name = incoming_attr.get('name', 'unknown')
        best_match = None
        best_relationship = None
        best_confidence = 0.0
        
        for existing_attr in normalized_existing:
            existing_name = existing_attr.get('name', 'unknown')
            existing_type = existing_attr.get('type', 'unknown')
            incoming_type = incoming_attr.get('type', 'unknown')
            
            # Skip if types don't match (choice vs numeric)
            if existing_type != incoming_type:
                continue
            
            # For "other" attributes only, check semantic name similarity first
            if classification_type == 'other':
                name_checker = AttributeNameSimilarityChecker()
                try:
                    similarity = await name_checker.check_similarity(
                        existing_name,
                        incoming_name,
                        finding_name
                    )
                    if not similarity.is_similar:
                        continue
                except Exception:
                    # Continue with comparison anyway
                    pass
            
            # Extract values for comparison
            incoming_values = extract_value_names(incoming_attr) if incoming_attr.get('type') == 'choice' else []
            existing_values = extract_value_names(existing_attr) if existing_attr.get('type') == 'choice' else []
            
            # Create prompt for relationship agent
            prompt = f"""Compare these two {classification_type} attributes:

EXISTING Attribute:
- Name: {existing_name}
- Type: {existing_attr.get('type', 'unknown')}
- Values: {', '.join(existing_values) if existing_values else 'None'}

INCOMING Attribute:
- Name: {incoming_name}
- Type: {incoming_attr.get('type', 'unknown')}
- Values: {', '.join(incoming_values) if incoming_values else 'None'}

Finding: {finding_name}

Determine the relationship between these attributes. Provide clear reasoning for your classification."""
            
            try:
                result = await relationship_agent.run(prompt)
                relationship = result.output
                
                # Print comparison details
                print(f"\n      Comparing:")
                print(f"        EXISTING: {existing_name} ({existing_attr.get('type', 'unknown')})")
                if existing_values:
                    print(f"          Values: {', '.join(existing_values)}")
                print(f"        INCOMING: {incoming_name} ({incoming_attr.get('type', 'unknown')})")
                if incoming_values:
                    print(f"          Values: {', '.join(incoming_values)}")
                print(f"        RESULT: {relationship.relationship} (confidence: {relationship.confidence:.2f})")
                print(f"        RECOMMENDATION: {relationship.recommendation}")
                print(f"        REASONING: {relationship.reasoning}")
                
                # Show value analysis if available
                if relationship.shared_values or relationship.existing_only_values or relationship.incoming_only_values:
                    print(f"        VALUE ANALYSIS:")
                    if relationship.shared_values:
                        print(f"          Shared: {', '.join(relationship.shared_values)}")
                    if relationship.existing_only_values:
                        print(f"          Existing only: {', '.join(relationship.existing_only_values)}")
                    if relationship.incoming_only_values:
                        print(f"          Incoming only: {', '.join(relationship.incoming_only_values)}")
                
                # Track best match (highest confidence)
                if relationship.confidence > best_confidence:
                    best_confidence = relationship.confidence
                    best_match = existing_attr
                    best_relationship = relationship
            except Exception as e:
                print(f"      ERROR comparing '{existing_name}' vs '{incoming_name}': {e}")
                pass
        
        if best_match and best_relationship:
            print(f"\n    ✓ Best match for '{incoming_name}': '{extract_attr_name(best_match)}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f})")
            print(f"      Recommendation: {best_relationship.recommendation}")
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': best_match,
                'relationship': best_relationship
            })
        else:
            # No match found - new attribute
            print(f"\n    ✗ No match found for '{incoming_name}' - new attribute")
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': None,
                'relationship': None
            })
    
    return comparisons


def create_presence_element(finding_name: str) -> Dict[str, Any]:
    """Create a presence attribute for a finding."""
    return {
        "name": "presence",
        "description": f"Presence or absence of {finding_name}",
        "type": "choice",
        "required": False,
        "max_selected": 1,
        "values": [
            {"name": "absent", "description": f"{finding_name.capitalize()} is absent"},
            {"name": "present", "description": f"{finding_name.capitalize()} is present"},
            {"name": "indeterminate", "description": f"Presence of {finding_name} cannot be determined"},
            {"name": "unknown", "description": f"Presence of {finding_name} is unknown"},
        ],
    }


def build_final_finding(
    existing_model_data: Dict[str, Any],
    incoming_model: FindingModelFull,
    merge_recommendations: List[Dict[str, Any]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]],
    approved_new_attributes: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Build the final finding model based on automatic merge decisions.
    
    Merge strategy: Keep existing attribute, then add incoming values that don't already exist.
    
    Returns: Dictionary representing the final finding model."""
    # Start with existing model structure (if available) or incoming model
    if existing_model_data:
        final_finding = existing_model_data.copy()
        # Remove _id from MongoDB if present
        final_finding.pop('_id', None)
    else:
        # Use incoming model as base
        final_finding = incoming_model.model_dump(exclude_unset=False, exclude_none=False)
    
    # Collect all final attributes
    final_attributes = []
    processed_incoming_attrs = set()
    
    # Process merge recommendations - automatically merge (keep existing + add new values)
    for merge_rec in merge_recommendations:
        incoming_attr = merge_rec['incoming_attribute']
        existing_attr = merge_rec['existing_attribute']
        incoming_name = incoming_attr.get('name', 'unknown')
        existing_name = existing_attr.get('name', 'unknown')
        
        processed_incoming_attrs.add(incoming_name)
        
        # Automatic merge strategy: Keep existing, then add incoming values that don't exist
        combined_attr = existing_attr.copy()
        if existing_attr.get('type') == 'choice' and incoming_attr.get('type') == 'choice':
            existing_value_names = set(extract_value_names(existing_attr))
            incoming_values = incoming_attr.get('values', [])
            # Add incoming values that don't exist in existing
            for val in incoming_values:
                val_name = extract_attr_name(val) if isinstance(val, dict) else getattr(val, 'name', '')
                if val_name not in existing_value_names:
                    combined_attr['values'].append(val)
        final_attributes.append(combined_attr)
    
    # Add all new attributes (automatically approved)
    for new_attr in approved_new_attributes:
        attr_name = new_attr.get('name', 'unknown')
        if attr_name not in processed_incoming_attrs:
            final_attributes.append(new_attr.copy())
            processed_incoming_attrs.add(attr_name)
    
    # Add existing attributes that weren't part of any merge recommendation
    if existing_model_data:
        existing_attrs = existing_model_data.get('attributes', [])
        for existing_attr in existing_attrs:
            existing_name = existing_attr.get('name', 'unknown')
            # Check if this attribute was part of a merge recommendation
            was_merged = any(
                merge_rec['existing_attribute'].get('name', 'unknown') == existing_name
                for merge_rec in merge_recommendations
            )
            if not was_merged:
                final_attributes.append(existing_attr.copy())
    
    # Add new attributes (presence/change_from_prior) - automatically added
    for attr_name, attr_dict in attributes_to_add:
        final_attributes.append(attr_dict.copy())
    
    final_finding['attributes'] = final_attributes
    
    return final_finding


def clean_final_finding(final_finding: Dict[str, Any]) -> Dict[str, Any]:
    """Clean up final finding dict by removing classification metadata, fixing contributors, and normalizing attributes."""
    cleaned = final_finding.copy()
    
    # Remove classification metadata from attributes and normalize them
    attributes = cleaned.get('attributes', [])
    cleaned_attributes = []
    for attr in attributes:
        cleaned_attr = attr.copy()
        # Remove classification metadata
        cleaned_attr.pop('_classification', None)
        cleaned_attr.pop('_confidence', None)
        cleaned_attr.pop('_reasoning', None)
        
        # Normalize attributes using the same logic
        cleaned_attr = normalize_incomplete_attribute(cleaned_attr)
        
        cleaned_attributes.append(cleaned_attr)
    cleaned['attributes'] = cleaned_attributes
    
    # Fix contributors if they're stored as strings instead of Person/Organization objects
    contributors = cleaned.get('contributors', [])
    if contributors:
        fixed_contributors = []
        for contrib in contributors:
            if isinstance(contrib, str):
                # Convert string contributor code to Organization
                if contrib == "CDE":
                    fixed_contributors.append({
                        "name": "ACR/RSNA Common Data Elements Project",
                        "code": "CDE",
                        "url": "https://radelement.org"
                    })
                elif contrib == "MGB":
                    fixed_contributors.append({
                        "name": "Mass General Brigham",
                        "code": "MGB",
                        "url": None
                    })
                else:
                    # Generic organization for unknown codes
                    fixed_contributors.append({
                        "name": contrib,
                        "code": contrib,
                        "url": None
                    })
            else:
                # Already a dict/object, keep as is
                fixed_contributors.append(contrib)
        cleaned['contributors'] = fixed_contributors
    
    return cleaned


def print_merge_summary(
    finding_name: str,
    existing_match: Optional[Dict],
    merge_recommendations: List[Dict[str, Any]],
    new_attributes: List[Dict[str, Any]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]]
) -> None:
    """Print a concise summary of all changes made and AI reasoning."""
    print(f"\n{'='*80}")
    print(f"MERGE SUMMARY: {finding_name}")
    print(f"{'='*80}\n")
    
    if existing_match:
        print(f"Existing Model: {existing_match.get('name', 'Unknown')} (ID: {existing_match.get('oifm_id', 'N/A')})")
        print()
    
    # Merged attributes
    if merge_recommendations:
        print(f"MERGED ATTRIBUTES ({len(merge_recommendations)}):")
        for idx, merge_rec in enumerate(merge_recommendations, 1):
            incoming_attr = merge_rec['incoming_attribute']
            existing_attr = merge_rec['existing_attribute']
            relationship = merge_rec['relationship']
            
            incoming_name = incoming_attr.get('name', 'unknown')
            existing_name = existing_attr.get('name', 'unknown')
            
            print(f"  {idx}. {existing_name} ← {incoming_name}")
            print(f"     Relationship: {relationship.relationship} (confidence: {relationship.confidence:.2f})")
            print(f"     Reasoning: {relationship.reasoning}")
            
            # Show values added
            if existing_attr.get('type') == 'choice' and incoming_attr.get('type') == 'choice':
                existing_value_names = set(extract_value_names(existing_attr))
                incoming_value_names = extract_value_names(incoming_attr)
                added_values = [v for v in incoming_value_names if v not in existing_value_names]
                if added_values:
                    print(f"     Added values: {', '.join(added_values)}")
            print()
    else:
        print("MERGED ATTRIBUTES: None\n")
    
    # New attributes
    if new_attributes:
        print(f"NEW ATTRIBUTES ADDED ({len(new_attributes)}):")
        for idx, new_attr_info in enumerate(new_attributes, 1):
            incoming_attr = new_attr_info['incoming_attribute']
            attr_name = incoming_attr.get('name', 'unknown')
            print(f"  {idx}. {attr_name}")
            if incoming_attr.get('description'):
                print(f"     Description: {incoming_attr.get('description')}")
        print()
    else:
        print("NEW ATTRIBUTES ADDED: None\n")
    
    # Required attributes
    if attributes_to_add:
        print(f"REQUIRED ATTRIBUTES ADDED ({len(attributes_to_add)}):")
        for attr_name, attr_dict in attributes_to_add:
            print(f"  - {attr_dict.get('name', 'unknown')}")
        print()
    else:
        print("REQUIRED ATTRIBUTES ADDED: None\n")
    
    # Summary
    print(f"SUMMARY:")
    print(f"  - Attributes merged: {len(merge_recommendations)}")
    print(f"  - New attributes added: {len(new_attributes)}")
    print(f"  - Required attributes added: {len(attributes_to_add)}")
    print(f"\n{'='*80}\n")


def format_attribute_for_report(attr: Dict[str, Any]) -> List[str]:
    """Format an attribute for report display with all details."""
    lines = []
    attr_name = extract_attr_name(attr)
    attr_type = attr.get('type', 'unknown')
    
    lines.append(f"- **Name:** {attr_name}")
    lines.append(f"- **Type:** {attr_type}")
    
    if attr.get('description'):
        lines.append(f"- **Description:** {attr.get('description')}")
    
    if attr_type == 'choice':
        value_names = extract_value_names(attr)
        if value_names:
            lines.append(f"- **Values:** {', '.join(value_names)}")
        else:
            lines.append("- **Values:** None")
        if attr.get('max_selected'):
            lines.append(f"- **Max selected:** {attr.get('max_selected')}")
    elif attr_type == 'numeric':
        if attr.get('unit'):
            lines.append(f"- **Unit:** {attr.get('unit')}")
        if attr.get('minimum') is not None or attr.get('maximum') is not None:
            lines.append(f"- **Range:** {attr.get('minimum', 'N/A')} - {attr.get('maximum', 'N/A')}")
    
    if attr.get('required') is not None:
        lines.append(f"- **Required:** {attr.get('required')}")
    
    return lines


def generate_merge_report(
    finding_name: str,
    existing_match: Optional[Dict],
    existing_attrs: List[Dict[str, Any]],
    incoming_attrs: List[Dict[str, Any]],
    final_attrs: List[Dict[str, Any]],
    merge_recommendations: List[Dict[str, Any]],
    new_attributes: List[Dict[str, Any]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]],
    report_path: Path
) -> None:
    """Generate individual merge report for this finding.
    
    Creates a markdown report documenting all changes made during the merge process.
    Each merge gets its own file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Build report
    report_lines = []
    report_lines.append(f"# Merge Report: {finding_name}")
    report_lines.append(f"**Timestamp:** {timestamp}")
    report_lines.append("")
    
    if existing_match:
        report_lines.append(f"**Existing Model:** {existing_match.get('name', 'Unknown')} (ID: {existing_match.get('oifm_id', 'N/A')})")
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # All Existing Attributes
    report_lines.append(f"## Existing Attributes ({len(existing_attrs)})")
    report_lines.append("")
    if existing_attrs:
        for idx, attr in enumerate(existing_attrs, 1):
            report_lines.append(f"### {idx}. {extract_attr_name(attr)}")
            report_lines.extend(format_attribute_for_report(attr))
            report_lines.append("")
    else:
        report_lines.append("None")
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # All Incoming Attributes
    report_lines.append(f"## Incoming Attributes ({len(incoming_attrs)})")
    report_lines.append("")
    if incoming_attrs:
        for idx, attr in enumerate(incoming_attrs, 1):
            report_lines.append(f"### {idx}. {extract_attr_name(attr)}")
            report_lines.extend(format_attribute_for_report(attr))
            report_lines.append("")
    else:
        report_lines.append("None")
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # Merge recommendations section
    if merge_recommendations:
        report_lines.append(f"### Merged Attributes ({len(merge_recommendations)})")
        report_lines.append("")
        for idx, merge_rec in enumerate(merge_recommendations, 1):
            incoming_attr = merge_rec['incoming_attribute']
            existing_attr = merge_rec['existing_attribute']
            relationship = merge_rec['relationship']
            
            incoming_name = incoming_attr.get('name', 'unknown')
            existing_name = existing_attr.get('name', 'unknown')
            
            report_lines.append(f"#### {idx}. {existing_name}")
            report_lines.append(f"- **Relationship:** {relationship.relationship} (confidence: {relationship.confidence:.2f})")
            report_lines.append(f"- **Incoming attribute:** {incoming_name}")
            report_lines.append("")
            
            # Show values
            if existing_attr.get('type') == 'choice':
                existing_value_names = extract_value_names(existing_attr)
                incoming_value_names = extract_value_names(incoming_attr)
                
                # Determine which values were added
                existing_set = set(existing_value_names)
                incoming_set = set(incoming_value_names)
                added_values = list(incoming_set - existing_set)
                
                report_lines.append(f"- **Existing values:** {', '.join(existing_value_names) if existing_value_names else 'None'}")
                report_lines.append(f"- **Incoming values:** {', '.join(incoming_value_names) if incoming_value_names else 'None'}")
                if added_values:
                    report_lines.append(f"- **Added values:** {', '.join(added_values)}")
                else:
                    report_lines.append("- **Added values:** None (all values already existed)")
            elif existing_attr.get('type') == 'numeric':
                report_lines.append(f"- **Type:** Numeric")
                if existing_attr.get('unit'):
                    report_lines.append(f"- **Unit:** {existing_attr.get('unit')}")
                if existing_attr.get('minimum') is not None or existing_attr.get('maximum') is not None:
                    report_lines.append(f"- **Range:** {existing_attr.get('minimum', 'N/A')} - {existing_attr.get('maximum', 'N/A')}")
            
            report_lines.append("")
    else:
        report_lines.append("### Merged Attributes")
        report_lines.append("None")
        report_lines.append("")
    
    # New attributes section
    if new_attributes:
        report_lines.append(f"### New Attributes Added ({len(new_attributes)})")
        report_lines.append("")
        for idx, new_attr_info in enumerate(new_attributes, 1):
            incoming_attr = new_attr_info['incoming_attribute']
            attr_name = incoming_attr.get('name', 'unknown')
            attr_type = incoming_attr.get('type', 'unknown')
            
            report_lines.append(f"#### {idx}. {attr_name}")
            report_lines.append(f"- **Type:** {attr_type}")
            
            if attr_type == 'choice':
                value_names = extract_value_names(incoming_attr)
                if value_names:
                    report_lines.append(f"- **Values:** {', '.join(value_names)}")
                else:
                    report_lines.append("- **Values:** None")
            elif attr_type == 'numeric':
                if incoming_attr.get('unit'):
                    report_lines.append(f"- **Unit:** {incoming_attr.get('unit')}")
                if incoming_attr.get('minimum') is not None or incoming_attr.get('maximum') is not None:
                    report_lines.append(f"- **Range:** {incoming_attr.get('minimum', 'N/A')} - {incoming_attr.get('maximum', 'N/A')}")
            
            if incoming_attr.get('description'):
                report_lines.append(f"- **Description:** {incoming_attr.get('description')}")
            
            report_lines.append("")
    else:
        report_lines.append("### New Attributes Added")
        report_lines.append("None")
        report_lines.append("")
    
    # Required attributes section
    if attributes_to_add:
        report_lines.append(f"### Required Attributes Added ({len(attributes_to_add)})")
        report_lines.append("")
        for attr_name, attr_dict in attributes_to_add:
            report_lines.append(f"#### {attr_dict.get('name', 'unknown')}")
            report_lines.append(f"- **Type:** {attr_dict.get('type', 'unknown')}")
            if attr_dict.get('type') == 'choice':
                values = attr_dict.get('values', [])
                if values:
                    value_names = [v.get('name', '') for v in values]
                    report_lines.append(f"- **Values:** {', '.join(value_names)}")
            report_lines.append("")
    else:
        report_lines.append("### Required Attributes Added")
        report_lines.append("None")
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # All Final Attributes
    report_lines.append(f"## Final Attributes ({len(final_attrs)})")
    report_lines.append("")
    if final_attrs:
        for idx, attr in enumerate(final_attrs, 1):
            report_lines.append(f"### {idx}. {extract_attr_name(attr)}")
            report_lines.extend(format_attribute_for_report(attr))
            report_lines.append("")
    else:
        report_lines.append("None")
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # Summary statistics
    report_lines.append("## Summary")
    report_lines.append("")
    report_lines.append(f"- **Attributes merged:** {len(merge_recommendations)}")
    report_lines.append(f"- **New attributes added:** {len(new_attributes)}")
    report_lines.append(f"- **Required attributes added:** {len(attributes_to_add)}")
    report_lines.append(f"- **Total existing attributes:** {len(existing_attrs)}")
    report_lines.append(f"- **Total incoming attributes:** {len(incoming_attrs)}")
    report_lines.append(f"- **Total final attributes:** {len(final_attrs)}")
    report_lines.append("")
    
    # Write report to individual file
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines), encoding='utf-8')


async def save_final_model(final_finding: Dict[str, Any], output_dir: Path):
    """Save final finding model to file after validation."""
    # Clean up the final finding
    cleaned_finding = clean_final_finding(final_finding)
    
    # Validate and convert to FindingModelFull
    try:
        model = FindingModelFull(**cleaned_finding)
    except Exception as e:
        print(f"Error: Failed to validate final model: {e}")
        print("The model may have validation errors. Please review the output above.")
        return False
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = model_file_name(model.name)
    output_path = output_dir / filename
    
    # Save as JSON
    json_content = model.model_dump_json(indent=2, exclude_none=True)
    output_path.write_text(json_content, encoding='utf-8')
    
    return True


def create_change_element(finding_name: str) -> Dict[str, Any]:
    """Create a change from prior attribute for a finding."""
    return {
        "name": "change from prior",
        "description": f"Whether and how a {finding_name} has changed over time",
        "type": "choice",
        "required": False,
        "max_selected": 1,
        "values": [
            {"name": "unchanged", "description": f"{finding_name.capitalize()} is unchanged"},
            {"name": "stable", "description": f"{finding_name.capitalize()} is stable"},
            {"name": "new", "description": f"{finding_name.capitalize()} is new"},
            {"name": "resolved", "description": f"{finding_name.capitalize()} seen on a prior exam has resolved"},
            {"name": "increased", "description": f"{finding_name.capitalize()} has increased"},
            {"name": "decreased", "description": f"{finding_name.capitalize()} has decreased"},
            {"name": "larger", "description": f"{finding_name.capitalize()} is larger"},
            {"name": "smaller", "description": f"{finding_name.capitalize()} is smaller"},
        ],
    }


async def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Search for existing finding model matches in database"
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to INCOMING FM JSON file'
    )
    parser.add_argument(
        '--db-path',
        type=str,
        default=None,
        help='Path to DuckDB index file (or set DUCKDB_INDEX_PATH environment variable)'
    )
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    # Get database path from argument or environment variable
    db_path = args.db_path or os.getenv("DUCKDB_INDEX_PATH")
    if not db_path:
        print("Error: Database path not specified.")
        print("Please provide --db-path argument or set DUCKDB_INDEX_PATH environment variable.")
        print("Example: python merge_findings.py input.json --db-path ../findingmodels_20251111.duckdb")
        sys.exit(1)
    
    if not Path(db_path).exists():
        print(f"Error: Database file not found: {db_path}")
        sys.exit(1)
    
    try:
        # Initialize index with DuckDB file
        try:
            index = Index(db_path=db_path)
        except Exception as e:
            print(f"Error: Failed to connect to DuckDB index: {e}")
            print(f"Please ensure the database file exists and is accessible: {db_path}")
            sys.exit(1)
        
        # Load INCOMING model
        print("Loading incoming model...")
        incoming_model = await load_incoming_model(input_path)
        print(f"  ✓ Loaded: {incoming_model.name}")
        
        # Search for EXISTING model
        print("Searching for existing model in database...")
        existing_match = await find_existing_model(incoming_model, index)
        if existing_match:
            print(f"  ✓ Found match: {existing_match.get('name')} (ID: {existing_match.get('oifm_id')})")
        else:
            print("  ✓ No match found")
        
        if existing_match:
            # Load EXISTING model from database
            print("Loading existing model from database...")
            existing_model_data = await get_existing_model_from_db(existing_match.get('oifm_id'), index)
            
            if existing_model_data:
                finding_name = incoming_model.name
                print(f"  ✓ Loaded existing model data")
                
                # Get attributes from both models
                print("Extracting attributes from models...")
                incoming_attrs = []
                for attr in incoming_model.attributes or []:
                    if isinstance(attr, dict):
                        incoming_attrs.append(attr.copy())
                    else:
                        incoming_attrs.append(attr.model_dump(exclude_unset=False, exclude_none=False))
                
                existing_attrs = existing_model_data.get('attributes', [])
                print(f"  ✓ Incoming: {len(incoming_attrs)} attributes")
                print(f"  ✓ Existing: {len(existing_attrs)} attributes")
                
                # Classify and group incoming attributes
                print("Classifying incoming attributes...")
                incoming_grouped = await classify_and_group_attributes(incoming_attrs, finding_name)
                print(f"  ✓ Classified {len(incoming_attrs)} attributes")
                
                # Classify and group existing attributes
                print("Classifying existing attributes...")
                existing_grouped = await classify_and_group_attributes(existing_attrs, finding_name)
                print(f"  ✓ Classified {len(existing_attrs)} attributes")
                
                # Compare attributes within each classification group
                print("Comparing attributes...")
                all_comparisons = {}
                for classification_type in ['presence', 'change_from_prior', 'other']:
                    incoming_attrs_group = incoming_grouped[classification_type]
                    existing_attrs_group = existing_grouped[classification_type]
                    
                    if incoming_attrs_group or existing_attrs_group:
                        incoming_names = [extract_attr_name(attr) for attr in incoming_attrs_group]
                        existing_names = [extract_attr_name(attr) for attr in existing_attrs_group]
                        print(f"  Comparing {classification_type} attributes:")
                        print(f"    Incoming: {', '.join(incoming_names) if incoming_names else 'None'}")
                        print(f"    Existing: {', '.join(existing_names) if existing_names else 'None'}")
                        comparisons = await compare_attributes_within_group(
                            incoming_attrs_group,
                            existing_attrs_group,
                            classification_type,
                            finding_name
                        )
                        all_comparisons[classification_type] = comparisons
                        print(f"    ✓ Completed {classification_type} comparison ({len(comparisons)} comparisons)")
                
                # Collect all merge recommendations and new attributes
                print("Collecting merge recommendations and new attributes...")
                merge_recommendations = []
                new_attributes = []
                
                for classification_type, comparisons in all_comparisons.items():
                    if comparisons:
                        print(f"\n  {classification_type.upper()} Results:")
                        for comp in comparisons:
                            if comp['relationship']:
                                recommendation = comp['relationship'].recommendation
                                incoming_attr_name = extract_attr_name(comp['incoming_attribute'])
                                existing_attr_name = extract_attr_name(comp['existing_attribute'])
                                relationship = comp['relationship']
                                
                                print(f"    '{incoming_attr_name}' (incoming) ↔ '{existing_attr_name}' (existing)")
                                print(f"      Relationship: {relationship.relationship} (confidence: {relationship.confidence:.2f})")
                                print(f"      Recommendation: {recommendation}")
                                
                                # Collect merge recommendations
                                if recommendation == "merge":
                                    merge_recommendations.append({
                                        'classification_type': classification_type,
                                        'incoming_attribute': comp['incoming_attribute'],
                                        'existing_attribute': comp['existing_attribute'],
                                        'relationship': comp['relationship']
                                    })
                            else:
                                # Collect new attributes
                                incoming_attr_name = extract_attr_name(comp['incoming_attribute'])
                                print(f"    '{incoming_attr_name}' (incoming): NEW (no match found)")
                                new_attributes.append({
                                    'classification_type': classification_type,
                                    'incoming_attribute': comp['incoming_attribute']
                                })
                
                print(f"  ✓ Found {len(merge_recommendations)} merge recommendations")
                print(f"  ✓ Found {len(new_attributes)} new attributes")
                
                # Automatic new attributes process - add all new attributes
                approved_new_attributes = []
                for new_attr_info in new_attributes:
                    approved_new_attributes.append(new_attr_info['incoming_attribute'])
                
                # Automatic check for missing presence/change_from_prior attributes
                print("Checking for required attributes...")
                incoming_has_presence = any(
                    attr.get('_classification') == 'presence' 
                    for attr_list in incoming_grouped.values() 
                    for attr in attr_list
                )
                incoming_has_change_from_prior = any(
                    attr.get('_classification') == 'change_from_prior' 
                    for attr_list in incoming_grouped.values() 
                    for attr in attr_list
                )
                
                attributes_to_add = []
                
                if not incoming_has_presence:
                    print("  ✓ Adding presence attribute")
                    presence_attr = create_presence_element(finding_name)
                    attributes_to_add.append(('presence', presence_attr))
                
                if not incoming_has_change_from_prior:
                    print("  ✓ Adding change_from_prior attribute")
                    change_attr = create_change_element(finding_name)
                    attributes_to_add.append(('change_from_prior', change_attr))
                
                if not attributes_to_add:
                    print("  ✓ All required attributes present")
                
                # Build the final finding
                print("Building final finding model...")
                final_finding = build_final_finding(
                    existing_model_data=existing_model_data,
                    incoming_model=incoming_model,
                    merge_recommendations=merge_recommendations,
                    attributes_to_add=attributes_to_add,
                    approved_new_attributes=approved_new_attributes
                )
                final_attrs = final_finding.get('attributes', [])
                print(f"  ✓ Final model has {len(final_attrs)} attributes")
                
                # Automatically save the final model
                print("Saving final model...")
                output_dir = Path("defs/merged_findings")
                success = await save_final_model(final_finding, output_dir)
                if not success:
                    print("  ✗ Error: Failed to save model.")
                    return
                print("  ✓ Model saved successfully")
                
                # Generate merge report (individual file per merge)
                print("Generating merge report...")
                # Create filename from finding name
                safe_name = finding_name.lower().replace(' ', '_').replace('/', '_')
                report_filename = f"merge_report_{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                report_path = Path("merge_reports") / report_filename
                generate_merge_report(
                    finding_name=finding_name,
                    existing_match=existing_match,
                    existing_attrs=existing_attrs,
                    incoming_attrs=incoming_attrs,
                    final_attrs=final_attrs,
                    merge_recommendations=merge_recommendations,
                    new_attributes=new_attributes,
                    attributes_to_add=attributes_to_add,
                    report_path=report_path
                )
                print(f"  ✓ Report saved to: {report_path}")
                
                # Print summary
                print_merge_summary(
                    finding_name=finding_name,
                    existing_match=existing_match,
                    merge_recommendations=merge_recommendations,
                    new_attributes=new_attributes,
                    attributes_to_add=attributes_to_add
                )
            else:
                print("Warning: Could not load existing model data from database.")
        else:
            print("No existing model match found in database.")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

