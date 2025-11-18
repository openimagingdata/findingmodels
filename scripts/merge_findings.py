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


async def find_existing_model(incoming_model: FindingModelFull, index: Index) -> Tuple[Optional[Dict], Optional[str], Optional[float]]:
    """Search for existing model in database.
    
    Returns: (highest confidence match or None, recommendation string or None, confidence float or None)"""
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
        return None, None, None
    
    # If recommendation is to edit existing or review needed, get the highest confidence match
    if analysis.recommendation in ["edit_existing", "review_needed"]:
        if analysis.similar_models and len(analysis.similar_models) > 0:
            # Get the highest confidence match
            best_match = analysis.similar_models[0]
            
            # Handle both dict and object types
            if isinstance(best_match, dict):
                match_data = {
                    'oifm_id': best_match.get('oifm_id'),
                    'name': best_match.get('name'),
                    'slug_name': best_match.get('slug_name'),
                    'filename': best_match.get('filename'),
                    'description': best_match.get('description'),
                    'synonyms': best_match.get('synonyms'),
                    'tags': best_match.get('tags'),
                    'contributors': best_match.get('contributors')
                }
            else:
                # It's an object (IndexEntry)
                match_data = {
                    'oifm_id': best_match.oifm_id,
                    'name': best_match.name,
                    'slug_name': best_match.slug_name,
                    'filename': best_match.filename,
                    'description': best_match.description,
                    'synonyms': best_match.synonyms,
                    'tags': best_match.tags,
                    'contributors': best_match.contributors
                }
            return match_data, analysis.recommendation, analysis.confidence
    
    return None, None, None


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
    attr_name = attr.get('name', 'unknown')
    attr_type = attr.get('type', 'unknown')
    values = attr.get('values', [])
    
    # Extract value names if it's a choice attribute
    value_names = []
    if attr_type == 'choice' and values:
        for val in values:
            if isinstance(val, dict):
                value_names.append(val.get('name', ''))
            else:
                value_names.append(getattr(val, 'name', ''))
    
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
    finding_name: str,
    source: str
) -> Dict[str, List[Dict[str, Any]]]:
    """Classify all attributes and group them by classification.
    
    Returns: Dict with keys 'presence', 'change_from_prior', 'other', each containing list of attributes with their classification."""
    grouped = {
        'presence': [],
        'change_from_prior': [],
        'other': []
    }
    
    print(f"\n  Classifying {len(attributes)} attributes from {source}...")
    
    for attr in attributes:
        attr_name = attr.get('name', 'unknown')
        try:
            classification = await classify_attribute(attr, finding_name)
            
            # Add classification info to attribute
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = classification.classification
            attr_with_classification['_confidence'] = classification.confidence
            attr_with_classification['_reasoning'] = classification.reasoning
            
            # Group by classification
            grouped[classification.classification].append(attr_with_classification)
            print(f"    - '{attr_name}': {classification.classification} (confidence: {classification.confidence:.2f})")
        except Exception as e:
            print(f"    - '{attr_name}': ERROR - {e}")
            # Add to 'other' as fallback
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = 'other'
            attr_with_classification['_confidence'] = 0.0
            attr_with_classification['_reasoning'] = f"Classification failed: {e}"
            grouped['other'].append(attr_with_classification)
    
    return grouped


def normalize_incomplete_attribute(attr: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize incomplete attributes by adding placeholder values if needed.
    
    For choice attributes with 0 values, adds 2 placeholder values to meet schema requirements.
    Returns normalized attribute dict."""
    normalized = attr.copy()
    attr_type = normalized.get('type', 'unknown')
    attr_name = normalized.get('name', 'unknown')
    
    if attr_type == 'choice':
        values = normalized.get('values', [])
        if not values or len(values) == 0:
            # Add placeholder values
            normalized['values'] = [
                {'name': 'placeholder_value_1', 'description': 'Placeholder value - actual values missing from database'},
                {'name': 'placeholder_value_2', 'description': 'Placeholder value - actual values missing from database'}
            ]
            print(f"    WARNING: Attribute '{attr_name}' has 0 values - adding placeholder values for comparison")
        
        # Ensure max_selected is valid
        if normalized.get('max_selected', 1) < 1:
            normalized['max_selected'] = 1
    
    # Ensure oifma_id exists (use attribute_id if available)
    if not normalized.get('oifma_id') and normalized.get('attribute_id'):
        normalized['oifma_id'] = normalized.get('attribute_id')
        print(f"    WARNING: Attribute '{attr_name}' has attribute_id but missing oifma_id - using attribute_id")
    
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
    
    print(f"\n  Comparing {len(incoming_attrs)} incoming {classification_type} attributes against {len(existing_attrs)} existing {classification_type} attributes...")
    
    # Normalize all attributes first
    normalized_incoming = [normalize_incomplete_attribute(attr) for attr in incoming_attrs]
    normalized_existing = [normalize_incomplete_attribute(attr) for attr in existing_attrs]
    
    # Compare each incoming attribute with each existing attribute
    for incoming_attr in normalized_incoming:
        incoming_name = incoming_attr.get('name', 'unknown')
        best_match = None
        best_relationship = None
        best_confidence = 0.0
        
        print(f"    Comparing incoming '{incoming_name}'...")
        
        for existing_attr in normalized_existing:
            existing_name = existing_attr.get('name', 'unknown')
            existing_type = existing_attr.get('type', 'unknown')
            incoming_type = incoming_attr.get('type', 'unknown')
            
            # Skip if types don't match (choice vs numeric)
            if existing_type != incoming_type:
                print(f"      SKIPPING '{existing_name}': Type mismatch (existing: {existing_type}, incoming: {incoming_type})")
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
                        print(f"      SKIPPING '{existing_name}': Names not semantically similar (confidence: {similarity.confidence:.2f}, reasoning: {similarity.reasoning[:80]}...)")
                        continue
                    else:
                        print(f"      Names semantically similar: '{existing_name}' ↔ '{incoming_name}' (confidence: {similarity.confidence:.2f})")
                except Exception as e:
                    print(f"      WARNING: Semantic similarity check failed for '{existing_name}': {e}")
                    # Continue with comparison anyway
            
            # Extract values for comparison
            incoming_values = []
            if incoming_attr.get('type') == 'choice':
                for val in incoming_attr.get('values', []):
                    if isinstance(val, dict):
                        incoming_values.append(val.get('name', ''))
                    else:
                        incoming_values.append(getattr(val, 'name', ''))
            
            existing_values = []
            if existing_attr.get('type') == 'choice':
                for val in existing_attr.get('values', []):
                    if isinstance(val, dict):
                        existing_values.append(val.get('name', ''))
                    else:
                        existing_values.append(getattr(val, 'name', ''))
            
            # Check if one has values and other doesn't (for semantic match case)
            existing_has_values = len(existing_values) > 0 and not all('placeholder' in v.lower() for v in existing_values)
            incoming_has_values = len(incoming_values) > 0 and not all('placeholder' in v.lower() for v in incoming_values)
            one_has_values_other_not = (existing_has_values and not incoming_has_values) or (incoming_has_values and not existing_has_values)
            
            # Create prompt for relationship agent
            prompt = f"""Compare these two {classification_type} attributes:

EXISTING Attribute:
- Name: {existing_name}
- Type: {existing_attr.get('type', 'unknown')}
- Values: {', '.join(existing_values) if existing_values else 'None (incomplete)'}

INCOMING Attribute:
- Name: {incoming_name}
- Type: {incoming_attr.get('type', 'unknown')}
- Values: {', '.join(incoming_values) if incoming_values else 'None (incomplete)'}

Finding: {finding_name}

Determine the relationship between these attributes. Provide clear reasoning for your classification.

IMPORTANT: If these attributes are semantically the same (refer to the same concept) but one has actual values and the other doesn't (or only has placeholders), recommend "merge" as the incoming can provide the missing values."""
            
            try:
                result = await relationship_agent.run(prompt)
                relationship = result.output
                
                # Print attribute details for debugging
                print(f"\n      COMPARING:")
                print(f"        EXISTING: {existing_name} ({existing_attr.get('type', 'unknown')})")
                print(f"          Values: {', '.join(existing_values) if existing_values else 'None (incomplete)'}")
                print(f"        INCOMING: {incoming_name} ({incoming_attr.get('type', 'unknown')})")
                print(f"          Values: {', '.join(incoming_values) if incoming_values else 'None (incomplete)'}")
                
                # Track best match (highest confidence)
                if relationship.confidence > best_confidence:
                    best_confidence = relationship.confidence
                    best_match = existing_attr
                    best_relationship = relationship
                
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
                print()
            except Exception as e:
                print(f"      vs '{existing_name}': ERROR - {e}")
        
        if best_match and best_relationship:
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': best_match,
                'relationship': best_relationship
            })
            print(f"    ✓ Best match: '{best_match.get('name')}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f})")
            print(f"      Recommendation: {best_relationship.recommendation}")
            print(f"      Reasoning: {best_relationship.reasoning}")
        else:
            # No match found - new attribute
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': None,
                'relationship': None
            })
            print(f"    ✗ No match found - new attribute")
    
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
    all_comparisons: Dict[str, List[Dict[str, Any]]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]],
    approved_new_attributes: List[Dict[str, Any]],
    finding_name: str
) -> Dict[str, Any]:
    """Build the final finding model based on merge decisions and user choices.
    
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
    
    # Process merge recommendations
    for merge_rec in merge_recommendations:
        incoming_attr = merge_rec['incoming_attribute']
        existing_attr = merge_rec['existing_attribute']
        user_choice = merge_rec.get('user_choice', '2')  # Default to 'keep existing'
        incoming_name = incoming_attr.get('name', 'unknown')
        existing_name = existing_attr.get('name', 'unknown')
        
        processed_incoming_attrs.add(incoming_name)
        
        if user_choice == '1':  # Replace existing with enhanced
            # Use incoming attribute (it's enhanced)
            final_attributes.append(incoming_attr.copy())
        elif user_choice == '2':  # Keep existing
            # Use existing attribute
            final_attributes.append(existing_attr.copy())
        elif user_choice == '3':  # Combine
            # Merge both attributes - combine values
            combined_attr = existing_attr.copy()
            if existing_attr.get('type') == 'choice' and incoming_attr.get('type') == 'choice':
                existing_values = {v.get('name', '') if isinstance(v, dict) else getattr(v, 'name', '') 
                                 for v in existing_attr.get('values', [])}
                incoming_values = incoming_attr.get('values', [])
                # Add incoming values that don't exist in existing
                for val in incoming_values:
                    val_name = val.get('name', '') if isinstance(val, dict) else getattr(val, 'name', '')
                    if val_name not in existing_values and 'placeholder' not in val_name.lower():
                        combined_attr['values'].append(val)
            final_attributes.append(combined_attr)
    
    # Add approved new attributes (only those the user chose to include)
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
    
    # Add new attributes (presence/change_from_prior) if user chose to add them
    for attr_name, attr_dict in attributes_to_add:
        # Generate ID for the attribute if needed
        if not attr_dict.get('oifma_id'):
            # Will be generated later by add_ids_to_model
            pass
        final_attributes.append(attr_dict.copy())
    
    final_finding['attributes'] = final_attributes
    
    return final_finding


def convert_to_json_serializable(obj: Any) -> Any:
    """Recursively convert Pydantic HttpUrl and other non-serializable objects to strings."""
    from pydantic import HttpUrl
    
    if isinstance(obj, HttpUrl):
        return str(obj)
    elif isinstance(obj, dict):
        return {key: convert_to_json_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json_serializable(item) for item in obj]
    elif isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    else:
        # For other types, try to convert to string
        try:
            return str(obj)
        except Exception:
            return obj


def print_final_finding(final_finding: Dict[str, Any]):
    """Print the final finding model in a readable format."""
    print(f"\nFinding Name: {final_finding.get('name', 'Unknown')}")
    if final_finding.get('oifm_id'):
        print(f"ID: {final_finding.get('oifm_id')}")
    if final_finding.get('description'):
        print(f"Description: {final_finding.get('description')}")
    
    attributes = final_finding.get('attributes', [])
    print(f"\nAttributes ({len(attributes)} total):")
    
    for idx, attr in enumerate(attributes, 1):
        attr_name = attr.get('name', 'unknown')
        attr_type = attr.get('type', 'unknown')
        print(f"\n  [{idx}] {attr_name} ({attr_type})")
        
        if attr_type == 'choice':
            values = attr.get('values', [])
            if values:
                print(f"      Values ({len(values)}):")
                for val in values:
                    val_name = val.get('name', '') if isinstance(val, dict) else getattr(val, 'name', '')
                    val_desc = val.get('description', '') if isinstance(val, dict) else getattr(val, 'description', '')
                    if val_desc:
                        print(f"        - {val_name}: {val_desc}")
                    else:
                        print(f"        - {val_name}")
            else:
                print(f"      Values: (none)")
            if attr.get('max_selected'):
                print(f"      Max selected: {attr.get('max_selected')}")
        
        elif attr_type == 'numeric':
            if attr.get('unit'):
                print(f"      Unit: {attr.get('unit')}")
            if attr.get('minimum') is not None or attr.get('maximum') is not None:
                print(f"      Range: {attr.get('minimum', 'N/A')} - {attr.get('maximum', 'N/A')}")
        
        if attr.get('required') is not None:
            print(f"      Required: {attr.get('required')}")
        if attr.get('description'):
            print(f"      Description: {attr.get('description')}")
    
    # Also print as JSON for easy copy/paste
    print(f"\n{'='*60}")
    print("FINAL FINDING MODEL (JSON)")
    print(f"{'='*60}")
    # Convert HttpUrl objects to strings before JSON serialization
    serializable_finding = convert_to_json_serializable(final_finding)
    print(json.dumps(serializable_finding, indent=2, ensure_ascii=False))


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
        
        # Normalize incomplete attributes (same logic as normalize_incomplete_attribute)
        attr_type = cleaned_attr.get('type', 'unknown')
        attr_name = cleaned_attr.get('name', 'unknown')
        
        if attr_type == 'choice':
            values = cleaned_attr.get('values', [])
            if not values or len(values) < 2:
                if len(values) == 0:
                    # Add placeholder values to meet schema requirements
                    cleaned_attr['values'] = [
                        {'name': 'placeholder_value_1', 'description': 'Placeholder value - actual values missing from database'},
                        {'name': 'placeholder_value_2', 'description': 'Placeholder value - actual values missing from database'}
                    ]
                else:
                    # Has 1 value but needs at least 2
                    values.append({'name': 'placeholder_value_1', 'description': 'Placeholder value - actual values missing from database'})
                    cleaned_attr['values'] = values
            
            # Ensure max_selected is valid
            if cleaned_attr.get('max_selected', 1) < 1:
                cleaned_attr['max_selected'] = 1
        
        # Ensure oifma_id exists (use attribute_id if available)
        if not cleaned_attr.get('oifma_id') and cleaned_attr.get('attribute_id'):
            cleaned_attr['oifma_id'] = cleaned_attr.get('attribute_id')
        
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
    
    print(f"\nSaved merged model to: {output_path}")
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
        print(f"Initializing DuckDB index from {db_path}...")
        try:
            index = Index(db_path=db_path)
        except Exception as e:
            print(f"Error: Failed to connect to DuckDB index: {e}")
            print(f"Please ensure the database file exists and is accessible: {db_path}")
            sys.exit(1)
        
        # Load INCOMING model
        print(f"Loading INCOMING model from {input_path}...")
        incoming_model = await load_incoming_model(input_path)
        print(f"Loaded model: {incoming_model.name} (ID: {incoming_model.oifm_id or 'none'})")
        
        # Search for EXISTING model
        print("Searching for EXISTING model...")
        existing_match, recommendation, confidence = await find_existing_model(incoming_model, index)
        
        if existing_match:
            confidence_display = confidence if confidence is not None else 0.0
            if recommendation == "review_needed":
                print(f"REVIEW NEEDED: Found similar model match: {existing_match.get('name')} (confidence: {confidence_display:.2f})")
                print("   This match requires manual review. Please verify it's the correct match before proceeding.")
            else:
                print(f"Found EXISTING model match: {existing_match.get('name')} (confidence: {confidence_display:.2f})")
            print(f"   Match ID: {existing_match.get('oifm_id')}")
            
            # Load EXISTING model from database
            print(f"\nLoading EXISTING model from database...")
            existing_model_data = await get_existing_model_from_db(existing_match.get('oifm_id'), index)
            
            if existing_model_data:
                finding_name = incoming_model.name
                
                # Get attributes from both models
                incoming_attrs = []
                for attr in incoming_model.attributes or []:
                    if isinstance(attr, dict):
                        incoming_attrs.append(attr.copy())
                    else:
                        incoming_attrs.append(attr.model_dump(exclude_unset=False, exclude_none=False))
                
                existing_attrs = existing_model_data.get('attributes', [])
                
                # Classify and group incoming attributes
                print(f"\n{'='*60}")
                print("CLASSIFYING INCOMING ATTRIBUTES")
                print(f"{'='*60}")
                incoming_grouped = await classify_and_group_attributes(
                    incoming_attrs, 
                    finding_name,
                    "INCOMING"
                )
                
                # Classify and group existing attributes
                print(f"\n{'='*60}")
                print("CLASSIFYING EXISTING ATTRIBUTES")
                print(f"{'='*60}")
                existing_grouped = await classify_and_group_attributes(
                    existing_attrs,
                    finding_name,
                    "EXISTING"
                )
                
                # Display grouped results
                print(f"\n{'='*60}")
                print("ATTRIBUTE CLASSIFICATION SUMMARY")
                print(f"{'='*60}")
                
                for classification_type in ['presence', 'change_from_prior', 'other']:
                    print(f"\n{classification_type.upper()}:")
                    print(f"  INCOMING: {len(incoming_grouped[classification_type])} attributes")
                    for attr in incoming_grouped[classification_type]:
                        print(f"    - {attr.get('name', 'unknown')}")
                    
                    print(f"  EXISTING: {len(existing_grouped[classification_type])} attributes")
                    for attr in existing_grouped[classification_type]:
                        print(f"    - {attr.get('name', 'unknown')}")
                
                # Compare attributes within each classification group
                print(f"\n{'='*60}")
                print("ATTRIBUTE RELATIONSHIP COMPARISON")
                print(f"{'='*60}")
                
                all_comparisons = {}
                for classification_type in ['presence', 'change_from_prior', 'other']:
                    incoming_attrs = incoming_grouped[classification_type]
                    existing_attrs = existing_grouped[classification_type]
                    
                    if incoming_attrs or existing_attrs:
                        print(f"\n{classification_type.upper()} ATTRIBUTES:")
                        comparisons = await compare_attributes_within_group(
                            incoming_attrs,
                            existing_attrs,
                            classification_type,
                            finding_name
                        )
                        all_comparisons[classification_type] = comparisons
                
                # Display final summary
                print(f"\n{'='*60}")
                print("COMPARISON SUMMARY")
                print(f"{'='*60}")
                
                # Collect all merge recommendations and new attributes
                merge_recommendations = []
                new_attributes = []
                
                for classification_type, comparisons in all_comparisons.items():
                    if comparisons:
                        print(f"\n{classification_type.upper()}:")
                        for comp in comparisons:
                            incoming_name = comp['incoming_attribute'].get('name', 'unknown')
                            if comp['relationship']:
                                existing_name = comp['existing_attribute'].get('name', 'unknown')
                                rel_type = comp['relationship'].relationship
                                confidence = comp['relationship'].confidence
                                recommendation = comp['relationship'].recommendation
                                print(f"  '{incoming_name}' (incoming) ↔ '{existing_name}' (existing): {rel_type} (confidence: {confidence:.2f}, recommendation: {recommendation})")
                                
                                # Collect merge recommendations
                                if recommendation == "merge":
                                    merge_recommendations.append({
                                        'classification_type': classification_type,
                                        'incoming_attribute': comp['incoming_attribute'],
                                        'existing_attribute': comp['existing_attribute'],
                                        'relationship': comp['relationship']
                                    })
                            else:
                                print(f"  '{incoming_name}' (incoming): NEW (no match found)")
                                # Collect new attributes
                                new_attributes.append({
                                    'classification_type': classification_type,
                                    'incoming_attribute': comp['incoming_attribute']
                                })
                
                # Interactive merge process
                if merge_recommendations:
                    print(f"\n{'='*60}")
                    print(f"MERGE RECOMMENDATIONS FOUND: {len(merge_recommendations)}")
                    print(f"{'='*60}")
                    
                    response = input("\nContinue to merge recommendations? (y/n): ").strip().lower()
                    
                    if response == 'y':
                        print(f"\n{'='*60}")
                        print("MERGE PROCESS")
                        print(f"{'='*60}")
                        
                        for idx, merge_rec in enumerate(merge_recommendations, 1):
                            incoming_attr = merge_rec['incoming_attribute']
                            existing_attr = merge_rec['existing_attribute']
                            relationship = merge_rec['relationship']
                            
                            incoming_name = incoming_attr.get('name', 'unknown')
                            existing_name = existing_attr.get('name', 'unknown')
                            
                            print(f"\n[{idx}/{len(merge_recommendations)}] MERGE RECOMMENDATION:")
                            print(f"  Relationship: {relationship.relationship} (confidence: {relationship.confidence:.2f})")
                            print(f"  Reasoning: {relationship.reasoning}")
                            
                            # Print existing attribute
                            print(f"\n  EXISTING ATTRIBUTE: '{existing_name}'")
                            print(f"    Type: {existing_attr.get('type', 'unknown')}")
                            if existing_attr.get('type') == 'choice':
                                values = existing_attr.get('values', [])
                                if values:
                                    value_names = [v.get('name', '') if isinstance(v, dict) else getattr(v, 'name', '') for v in values]
                                    print(f"    Values: {', '.join(value_names)}")
                                else:
                                    print(f"    Values: (none)")
                            elif existing_attr.get('type') == 'numeric':
                                print(f"    Unit: {existing_attr.get('unit', 'N/A')}")
                                print(f"    Range: {existing_attr.get('minimum', 'N/A')} - {existing_attr.get('maximum', 'N/A')}")
                            
                            # Print incoming attribute
                            print(f"\n  INCOMING ATTRIBUTE: '{incoming_name}'")
                            print(f"    Type: {incoming_attr.get('type', 'unknown')}")
                            if incoming_attr.get('type') == 'choice':
                                values = incoming_attr.get('values', [])
                                if values:
                                    value_names = [v.get('name', '') if isinstance(v, dict) else getattr(v, 'name', '') for v in values]
                                    print(f"    Values: {', '.join(value_names)}")
                                else:
                                    print(f"    Values: (none)")
                            elif incoming_attr.get('type') == 'numeric':
                                print(f"    Unit: {incoming_attr.get('unit', 'N/A')}")
                                print(f"    Range: {incoming_attr.get('minimum', 'N/A')} - {incoming_attr.get('maximum', 'N/A')}")
                            
                            # Get user choice
                            print(f"\n  OPTIONS:")
                            print(f"    1. Replace existing with enhanced (use incoming to replace existing)")
                            print(f"    2. Keep existing (don't merge, keep existing as is)")
                            print(f"    3. Combine (Keeps all existing values. Adds incoming values that aren't already present. Skips placeholder values.)")
                            
                            while True:
                                choice = input(f"\n  Your choice (1/2/3): ").strip()
                                if choice in ['1', '2', '3']:
                                    merge_rec['user_choice'] = choice
                                    if choice == '1':
                                        print(f"    ✓ Selected: Replace existing with enhanced")
                                    elif choice == '2':
                                        print(f"    ✓ Selected: Keep existing")
                                    elif choice == '3':
                                        print(f"    ✓ Selected: Combine")
                                    break
                                else:
                                    print(f"    Invalid choice. Please enter 1, 2, or 3.")
                        
                        print(f"\n{'='*60}")
                        print("MERGE PROCESS COMPLETE")
                        print(f"{'='*60}")
                        print(f"\nProcessed {len(merge_recommendations)} merge recommendations.")
                    else:
                        print("\nMerge process skipped by user.")
                
                # Interactive new attributes process
                approved_new_attributes = []
                if new_attributes:
                    print(f"\n{'='*60}")
                    print(f"NEW ATTRIBUTES FOUND: {len(new_attributes)}")
                    print(f"{'='*60}")
                    
                    response = input("\nReview new attributes? (y/n): ").strip().lower()
                    
                    if response == 'y':
                        print(f"\n{'='*60}")
                        print("NEW ATTRIBUTES REVIEW")
                        print(f"{'='*60}")
                        
                        for idx, new_attr_info in enumerate(new_attributes, 1):
                            incoming_attr = new_attr_info['incoming_attribute']
                            incoming_name = incoming_attr.get('name', 'unknown')
                            attr_type = incoming_attr.get('type', 'unknown')
                            
                            print(f"\n[{idx}/{len(new_attributes)}] NEW ATTRIBUTE: '{incoming_name}'")
                            print(f"  Type: {attr_type}")
                            
                            if attr_type == 'choice':
                                values = incoming_attr.get('values', [])
                                if values:
                                    value_names = [v.get('name', '') if isinstance(v, dict) else getattr(v, 'name', '') for v in values]
                                    print(f"  Values: {', '.join(value_names)}")
                                else:
                                    print(f"  Values: (none)")
                            elif attr_type == 'numeric':
                                print(f"  Unit: {incoming_attr.get('unit', 'N/A')}")
                                print(f"  Range: {incoming_attr.get('minimum', 'N/A')} - {incoming_attr.get('maximum', 'N/A')}")
                            
                            if incoming_attr.get('description'):
                                print(f"  Description: {incoming_attr.get('description')}")
                            
                            # Get user choice
                            while True:
                                choice = input(f"\n  Add this attribute to final model? (y/n): ").strip().lower()
                                if choice in ['y', 'n']:
                                    if choice == 'y':
                                        approved_new_attributes.append(incoming_attr)
                                        print(f"    ✓ Selected: Add attribute")
                                    else:
                                        print(f"    ✗ Selected: Skip attribute")
                                    break
                                else:
                                    print(f"    Invalid choice. Please enter y or n.")
                        
                        print(f"\n{'='*60}")
                        print("NEW ATTRIBUTES REVIEW COMPLETE")
                        print(f"{'='*60}")
                        print(f"\nApproved {len(approved_new_attributes)} of {len(new_attributes)} new attributes.")
                    else:
                        print("\nNew attributes review skipped by user.")
                
                # Check for missing presence/change_from_prior attributes in incoming model
                print(f"\n{'='*60}")
                print("REQUIRED ATTRIBUTES CHECK")
                print(f"{'='*60}")
                
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
                add_attributes_to_final = False
                
                if not incoming_has_presence:
                    print(f"\n  Missing 'presence' attribute in incoming model.")
                    response = input("  Add 'presence' attribute? (y/n): ").strip().lower()
                    if response == 'y':
                        presence_attr = create_presence_element(finding_name)
                        print(f"    ✓ Created presence attribute")
                        attributes_to_add.append(('presence', presence_attr))
                
                if not incoming_has_change_from_prior:
                    print(f"\n  Missing 'change from prior' attribute in incoming model.")
                    response = input("  Add 'change from prior' attribute? (y/n): ").strip().lower()
                    if response == 'y':
                        change_attr = create_change_element(finding_name)
                        print(f"    ✓ Created change from prior attribute")
                        attributes_to_add.append(('change_from_prior', change_attr))
                
                # Ask if user wants to add these to the final finding
                if attributes_to_add:
                    print(f"\n  Created {len(attributes_to_add)} attribute(s) to add:")
                    for attr_name, attr in attributes_to_add:
                        print(f"    - {attr_name}: {attr.get('name', 'unknown')}")
                        if attr.get('type') == 'choice':
                            values = attr.get('values', [])
                            value_names = [v.get('name', '') for v in values]
                            print(f"      Values: {', '.join(value_names)}")
                    
                    response = input(f"\n  Add these attributes to the final finding? (y/n): ").strip().lower()
                    if response == 'y':
                        add_attributes_to_final = True
                        print(f"    ✓ Attributes will be added to final finding")
                    else:
                        print(f"    ✗ Attributes will NOT be added to final finding")
                else:
                    print(f"\n  All required attributes (presence, change_from_prior) are present.")
                
                # Build and display the final finding
                print(f"\n{'='*60}")
                print("FINAL FINDING MODEL")
                print(f"{'='*60}")
                
                final_finding = build_final_finding(
                    existing_model_data=existing_model_data,
                    incoming_model=incoming_model,
                    merge_recommendations=merge_recommendations,
                    all_comparisons=all_comparisons,
                    attributes_to_add=attributes_to_add if add_attributes_to_final else [],
                    approved_new_attributes=approved_new_attributes,
                    finding_name=finding_name
                )
                
                print_final_finding(final_finding)
                
                # Ask if user wants to save
                print(f"\n{'='*60}")
                response = input("Save final model? (y/n): ").strip().lower()
                if response == 'y':
                    output_dir = Path("defs/merged_findings")
                    success = await save_final_model(final_finding, output_dir)
                    if success:
                        print("Model saved successfully!")
                    else:
                        print("Failed to save model. Please check the errors above.")
                else:
                    print("Save cancelled by user.")
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

