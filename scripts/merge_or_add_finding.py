"""
CLI tool for merging or adding finding models.

This script processes an INCOMING FM JSON file and either:
- Creates a NEW model with required attributes (presence + change_from_prior) if no match found
- Merges INCOMING model with EXISTING model by adding attributes/values if match found

Output:
- New models → defs/new_findings/{finding_name}.fm.json
- Merged models → defs/merged_findings/{finding_name}.fm.json
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from findingmodel.tools import find_similar_models
from findingmodel.index import Index
from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.common import model_file_name
from findingmodel.tools import add_ids_to_model
from agents.attribute_classifier import AttributeClassifier, AttributeComparator


async def load_incoming_model(file_path: Path) -> FindingModelFull:
    """Load and validate INCOMING model from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            model_data = json.load(f)
        
        model = FindingModelFull(**model_data)
        return model
    except Exception as e:
        raise ValueError(f"Failed to load INCOMING model from {file_path}: {e}")


async def find_existing_model(incoming_model: FindingModelFull, index: Index) -> Optional[Dict[str, Any]]:
    """Find EXISTING model using similarity search. Returns highest confidence match or None."""
    finding_name = incoming_model.name
    description = incoming_model.description
    synonyms = getattr(incoming_model, 'synonyms', []) or []
    
    # Run similarity analysis
# find_similar_models returns a Recommendation (edit_existing, create_new, review_needed)
    analysis = await find_similar_models(
        finding_name=finding_name,
        description=description,
        synonyms=synonyms,
        index=index
    )
    
    # If recommendation is to create new, no match found
    if analysis.recommendation == "create_new":
        return None
    
    # If recommendation is to edit existing, get the highest confidence match
    if analysis.recommendation == "edit_existing" and analysis.similar_models:
        # Check if individual similar_models have confidence scores
        if 'confidence' in analysis.similar_models[0]:
            # Sort by confidence descending and get highest
            sorted_models = sorted(
                analysis.similar_models,
                key=lambda x: x.get('confidence', 0.0),
                reverse=True
            )
            return sorted_models[0] if sorted_models else None
        else:
            # No individual confidence scores - use first match
            return analysis.similar_models[0]
    
    return None


async def get_existing_model_from_db(oifm_id: str, index: Index) -> Optional[Dict[str, Any]]:
    """Load EXISTING model from MongoDB by oifm_id."""
    data = await index.index_collection.find_one({"oifm_id": oifm_id})
    return data


async def has_presence_attribute(attributes: List[Dict[str, Any]], finding_name: str) -> bool:
    """Check if model has a presence attribute with required values using AttributeClassifier."""
    presence_values = {'present', 'absent', 'unknown', 'indeterminate'}
    classifier = AttributeClassifier()
    
    for attr in attributes:
        try:
            # Classify the attribute using AI
            classification = await classifier.classify_attribute(attr, finding_name)
            
            # Check if classified as "presence"
            if classification.classification == "presence":
                # Still validate that it has required values
                if attr.get('type') == 'choice':
                    values = attr.get('values', [])
                    value_names = {v.get('name', '').lower() for v in values}
                    # Check if it has at least the required values
                    if presence_values.issubset(value_names):
                        return True
        except Exception as e:
            # If classification fails, skip this attribute
            print(f"Warning: Could not classify attribute '{attr.get('name', 'unknown')}': {e}")
            continue
    
    return False


async def has_change_from_prior_attribute(attributes: List[Dict[str, Any]], finding_name: str) -> bool:
    """Check if model has a change from prior attribute using AttributeClassifier."""
    classifier = AttributeClassifier()
    
    for attr in attributes:
        try:
            # Classify the attribute using AI
            classification = await classifier.classify_attribute(attr, finding_name)
            
            # Check if classified as "change_from_prior"
            if classification.classification == "change_from_prior":
                return True
        except Exception as e:
            # If classification fails, skip this attribute
            print(f"Warning: Could not classify attribute '{attr.get('name', 'unknown')}': {e}")
            continue
    
    return False




async def ensure_required_attributes(model: FindingModelFull) -> FindingModelFull:
    """Ensure model has presence and change_from_prior attributes. Adds IDs if needed."""
    attributes = [attr.model_dump() for attr in model.attributes] if model.attributes else []
    finding_name = model.name
    
    # Check and add presence attribute if missing
    if not await has_presence_attribute(attributes, finding_name):
        # Create attribute without ID - will be generated by add_ids_to_model
        presence_attr = {
            "name": "presence",
            "description": f"Presence or absence of {finding_name}",
            "type": "choice",
            "values": [
                {"name": "absent", "description": f"{finding_name} is absent"},
                {"name": "present", "description": f"{finding_name} is present"},
                {"name": "indeterminate", "description": f"Presence of {finding_name} cannot be determined"},
                {"name": "unknown", "description": f"Presence of {finding_name} is unknown"}
            ],
            "required": False,
            "max_selected": 1
        }
        attributes.insert(0, presence_attr)  # Add at beginning
    
    # Check and add change_from_prior attribute if missing
    if not await has_change_from_prior_attribute(attributes, finding_name):
        change_attr = {
            "name": "change from prior",
            "description": f"Whether and how {finding_name} has changed over time",
            "type": "choice",
            "values": [
                {"name": "unchanged", "description": f"{finding_name} is unchanged"},
                {"name": "stable", "description": f"{finding_name} is stable"},
                {"name": "new", "description": f"{finding_name} is new"},
                {"name": "resolved", "description": f"{finding_name} seen on prior exam has resolved"},
                {"name": "increased", "description": f"{finding_name} has increased"},
                {"name": "decreased", "description": f"{finding_name} has decreased"}
            ],
            "required": False,
            "max_selected": 1
        }
        attributes.append(change_attr)
    
    # Convert back to model structure
    model_dict = model.model_dump()
    model_dict['attributes'] = attributes
    
    # Use add_ids_to_model to generate IDs for model and all attributes
    # This works even if model already has oifm_id - it will only add IDs where missing
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    return full_model


def get_value_names(attribute: Dict[str, Any]) -> set:
    """Extract value names from an attribute."""
    if attribute.get('type') != 'choice':
        return set()
    values = attribute.get('values', [])
    return {v.get('name', '').lower() for v in values}


async def merge_attributes(
    existing_attributes: List[Dict[str, Any]],
    incoming_attributes: List[Dict[str, Any]],
    finding_name: str
) -> List[Dict[str, Any]]:
    """Merge INCOMING attributes with EXISTING attributes."""
    comparator = AttributeComparator()
    merged_attributes = existing_attributes.copy()  # Start with all EXISTING attributes
    
    for incoming_attr in incoming_attributes:
        incoming_attr_dict = incoming_attr if isinstance(incoming_attr, dict) else incoming_attr.model_dump()
        overlap_found = False
        
        # Check for overlap with each EXISTING attribute
        for i, existing_attr_dict in enumerate(merged_attributes):
            existing_attr_dict = existing_attr_dict if isinstance(existing_attr_dict, dict) else existing_attr_dict.model_dump()
            
            try:
                comparison = await comparator.compare_attributes(
                    existing_attribute=existing_attr_dict,
                    new_attribute=incoming_attr_dict,
                    finding_name=finding_name,
                    attribute_type=incoming_attr_dict.get('type', 'choice')
                )
                
                # If identical or expanded, there's an overlap
                if comparison.relationship in ('identical', 'expanded'):
                    overlap_found = True
                    
                    # Check if INCOMING adds new values
                    existing_value_names = get_value_names(existing_attr_dict)
                    incoming_value_names = get_value_names(incoming_attr_dict)
                    new_value_names = incoming_value_names - existing_value_names
                    
                    if new_value_names:
                        # Add new values to EXISTING attribute
                        existing_values = existing_attr_dict.get('values', []).copy()
                        existing_oifma_id = existing_attr_dict.get('oifma_id')
                        
                        # Get next index for value codes
                        max_index = max(
                            (int(v.get('value_code', '').split('.')[-1]) 
                             for v in existing_values if '.' in v.get('value_code', '')),
                            default=-1
                        )
                        
                        # Add new values from INCOMING
                        incoming_values = incoming_attr_dict.get('values', [])
                        for incoming_value in incoming_values:
                            value_name = incoming_value.get('name', '').lower()
                            if value_name in new_value_names:
                                max_index += 1
                                new_value = incoming_value.copy()
                                # Ensure value_code exists
                                if 'value_code' not in new_value or not new_value.get('value_code'):
                                    new_value['value_code'] = f"{existing_oifma_id}.{max_index}"
                                existing_values.append(new_value)
                        
                        # Update the merged attribute
                        merged_attributes[i] = existing_attr_dict.copy()
                        merged_attributes[i]['values'] = existing_values
                    
                    # If no new values, keep EXISTING as-is (do nothing)
                    break
            
            except Exception as e:
                # If comparison fails, treat as different attribute
                print(f"Warning: Could not compare attributes '{existing_attr_dict.get('name')}' and '{incoming_attr_dict.get('name')}': {e}")
                continue
        
        # If no overlap found, add INCOMING attribute as new
        if not overlap_found:
            merged_attributes.append(incoming_attr_dict)
    
    return merged_attributes


async def create_new_model(incoming_model: FindingModelFull, index: Index) -> FindingModelFull:
    """Create NEW model with required attributes."""
    # Ensure required attributes exist
    new_model = await ensure_required_attributes(incoming_model)
    return new_model


async def merge_models(
    existing_model_data: Dict[str, Any],
    incoming_model: FindingModelFull,
    index: Index
) -> FindingModelFull:
    """Merge INCOMING model with EXISTING model."""
    # Start with EXISTING model as base
    existing_attributes = existing_model_data.get('attributes', [])
    incoming_attributes = incoming_model.attributes or []
    
    # Merge attributes
    merged_attributes = await merge_attributes(
        existing_attributes=existing_attributes,
        incoming_attributes=incoming_attributes,
        finding_name=existing_model_data.get('name', incoming_model.name)
    )
    
    # Build merged model (preserve EXISTING structure)
    merged_model_dict = existing_model_data.copy()
    merged_model_dict['attributes'] = merged_attributes
    
    # For attributes without IDs (newly added), we need to generate IDs
    # Check if any attribute is missing oifma_id
    needs_id_generation = False
    for attr in merged_attributes:
        if not attr.get('oifma_id'):
            needs_id_generation = True
            break
    
    # If any new attributes were added without IDs, use add_ids_to_model
    if needs_id_generation:
        # Convert to FindingModelBase and back to generate IDs
        base_model = FindingModelBase(**merged_model_dict)
        full_model = add_ids_to_model(base_model, source="MGB")
        return full_model
    
    # Validate and return
    merged_model = FindingModelFull(**merged_model_dict)
    return merged_model


async def save_model(model: FindingModelFull, output_dir: Path, is_merged: bool):
    """Save model to appropriate directory."""
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = model_file_name(model.name)
    output_path = output_dir / filename
    
    # Save as JSON
    json_content = model.model_dump_json(indent=2, exclude_none=True)
    output_path.write_text(json_content, encoding='utf-8')
    
    print(f"Saved {'merged' if is_merged else 'new'} model to: {output_path}")


async def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Merge or add finding model from INCOMING FM JSON file"
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to INCOMING FM JSON file'
    )
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    try:
        # Initialize index
        print("Initializing MongoDB index...")
        index = Index()
        
        # Load INCOMING model
        print(f"Loading INCOMING model from {input_path}...")
        incoming_model = await load_incoming_model(input_path)
        print(f"Loaded model: {incoming_model.name} (ID: {incoming_model.oifm_id or 'none'})")
        
        # Search for EXISTING model
        print("Searching for EXISTING model...")
        existing_match = await find_existing_model(incoming_model, index)
        
        if existing_match:
            print(f"Found EXISTING model match: {existing_match.get('name')} (confidence: {existing_match.get('confidence', 0):.2f})")
            oifm_id = existing_match.get('oifm_id')
            
            # Load EXISTING model from database
            print(f"Loading EXISTING model from database (ID: {oifm_id})...")
            existing_model_data = await get_existing_model_from_db(oifm_id, index)
            
            if existing_model_data:
                # Merge models
                print("Merging models...")
                merged_model = await merge_models(existing_model_data, incoming_model, index)
                
                # Save to merged_findings directory
                output_dir = Path("defs/merged_findings")
                await save_model(merged_model, output_dir, is_merged=True)
            else:
                print(f"Warning: EXISTING model {oifm_id} not found in database, creating NEW model instead")
                # Fall through to NEW model creation
                existing_match = None
        
        if not existing_match:
            # Create NEW model
            print("No EXISTING model match found, creating NEW model...")
            new_model = await create_new_model(incoming_model, index)
            
            # Save to new_findings directory
            output_dir = Path("defs/new_findings")
            await save_model(new_model, output_dir, is_merged=False)
        
        print("Done!")
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

