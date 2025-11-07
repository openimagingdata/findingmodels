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
import difflib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from findingmodel.tools import find_similar_models
from findingmodel.index import Index
from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.common import model_file_name
from findingmodel.tools import add_ids_to_model
from agents.attribute_classifier import AttributeClassifier, AttributeComparator, AttributeNameSimilarityChecker


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


async def find_existing_model(incoming_model: FindingModelFull, index: Index) -> Tuple[Optional[Dict[str, Any]], Optional[str], Optional[float]]:
    """Find EXISTING model using similarity search. 
    Returns: (highest confidence match or None, recommendation string or None, confidence float or None)"""
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
        return None, None, None
    
    # If recommendation is to edit existing or review needed, get the highest confidence match
    if analysis.recommendation in ("edit_existing", "review_needed") and analysis.similar_models:
        # Get the overall confidence from analysis (this is the confidence for the match)
        confidence = getattr(analysis, 'confidence', None)
        
        # Check if individual similar_models have confidence scores
        if 'confidence' in analysis.similar_models[0]:
            # Sort by confidence descending and get highest
            sorted_models = sorted(
                analysis.similar_models,
                key=lambda x: x.get('confidence', 0.0),
                reverse=True
            )
            match = sorted_models[0] if sorted_models else None
            # Use individual model confidence if available, otherwise use analysis confidence
            if match and 'confidence' in match:
                confidence = match.get('confidence', confidence)
            return match, analysis.recommendation, confidence
        else:
            # No individual confidence scores - use first match and analysis confidence
            return analysis.similar_models[0], analysis.recommendation, confidence
    
    return None, None, None


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




async def ensure_required_attributes(model: FindingModelFull) -> Tuple[FindingModelFull, List[Dict[str, Any]]]:
    """Ensure model has presence and change_from_prior attributes. Adds IDs if needed.
    Returns: (enhanced_model, added_attributes)"""
    attributes = [attr.model_dump() for attr in model.attributes] if model.attributes else []
    finding_name = model.name
    added_attributes = []
    
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
        added_attributes.append(presence_attr)
    
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
        added_attributes.append(change_attr)
    
    # Convert back to model structure
    model_dict = model.model_dump()
    model_dict['attributes'] = attributes
    
    # Use add_ids_to_model to generate IDs for model and all attributes
    # This works even if model already has oifm_id - it will only add IDs where missing
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="MGB")
    return full_model, added_attributes


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
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Merge INCOMING attributes with EXISTING attributes.
    Returns: (merged_attributes, change_summary)"""
    comparator = AttributeComparator()
    merged_attributes = existing_attributes.copy()  # Start with all EXISTING attributes
    
    # Track changes
    change_summary = {
        'new_attributes': [],
        'expanded_attributes': [],
        'identical_attributes': [],
        'new_values': {}  # attribute_name -> [list of new value names]
    }
    
    total_incoming = len(incoming_attributes)
    print(f"  Comparing {total_incoming} incoming attributes against {len(existing_attributes)} existing attributes...")
    
    for attr_idx, incoming_attr in enumerate(incoming_attributes, 1):
        # Convert to dict, ensuring all fields are included (especially for choice attributes)
        if isinstance(incoming_attr, dict):
            incoming_attr_dict = incoming_attr.copy()
        else:
            # Pydantic model - use model_dump with all fields included
            incoming_attr_dict = incoming_attr.model_dump(exclude_unset=False, exclude_none=False)
        incoming_attr_name = incoming_attr_dict.get('name', 'unknown')
        print(f"  [{attr_idx}/{total_incoming}] Processing attribute: '{incoming_attr_name}'...")
        overlap_found = False
        
        # Check for overlap with each EXISTING attribute
        for i, existing_attr_dict in enumerate(merged_attributes):
            # Convert to dict if needed, ensuring all fields are included
            if not isinstance(existing_attr_dict, dict):
                existing_attr_dict = existing_attr_dict.model_dump(exclude_unset=False, exclude_none=False)
                # Store the converted dict back
                merged_attributes[i] = existing_attr_dict
            else:
                # Already a dict, but make a copy to avoid modifying the original
                existing_attr_dict = existing_attr_dict.copy()
            
            try:
                existing_attr_name = existing_attr_dict.get('name', 'unknown')
                existing_attr_type = existing_attr_dict.get('type', 'unknown')
                # Handle enum types (convert to string)
                if hasattr(existing_attr_type, 'value'):
                    existing_attr_type = existing_attr_type.value
                elif not isinstance(existing_attr_type, str):
                    existing_attr_type = str(existing_attr_type)
                
                incoming_attr_type = incoming_attr_dict.get('type', 'unknown')
                # Handle enum types (convert to string)
                if hasattr(incoming_attr_type, 'value'):
                    incoming_attr_type = incoming_attr_type.value
                elif not isinstance(incoming_attr_type, str):
                    incoming_attr_type = str(incoming_attr_type)
                
                # Quick pre-filter: Skip if types don't match (choice vs numeric)
                if existing_attr_type != incoming_attr_type:
                    print(f"      Skipping '{existing_attr_name}' (type mismatch: {existing_attr_type} vs {incoming_attr_type})")
                    continue
                
                # Quick pre-filter: Check if names are similar (case-insensitive)
                existing_name_lower = existing_attr_name.lower()
                incoming_name_lower = incoming_attr_name.lower()
                
                # If names are exactly the same (case-insensitive), likely a match - do AI comparison
                # If names are very different, check semantic classification
                name_similarity = existing_name_lower == incoming_name_lower
                if not name_similarity:
                    # Use semantic classification to check if they're the same type
                    # (e.g., "status" and "change from prior" are both "change_from_prior")
                    try:
                        classifier = AttributeClassifier()
                        existing_classification = await classifier.classify_attribute(existing_attr_dict, finding_name)
                        incoming_classification = await classifier.classify_attribute(incoming_attr_dict, finding_name)
                        
                        # If both are classified as presence or change_from_prior, they're likely the same
                        # No need for additional semantic similarity check - proceed directly to comparison
                        if existing_classification.classification in ("presence", "change_from_prior") and \
                           existing_classification.classification == incoming_classification.classification:
                            # Same semantic type (presence or change_from_prior) - proceed to comparison
                            pass  # Continue to comparison below
                        elif existing_classification.classification == "other" and \
                             incoming_classification.classification == "other":
                            # Both are "other" - use AI to check if names are semantically similar
                            similarity_checker = AttributeNameSimilarityChecker()
                            similarity = await similarity_checker.check_similarity(
                                existing_attr_name, 
                                incoming_attr_name, 
                                finding_name
                            )
                            if similarity.is_similar:
                                # Semantically similar - proceed to comparison
                                pass  # Continue to comparison below
                            else:
                                # Not semantically similar - skip
                                print(f"      Skipping '{existing_attr_name}' (not semantically similar: '{existing_attr_name}' vs '{incoming_attr_name}')")
                                continue
                        else:
                            # Different semantic types - definitely different attributes
                            print(f"      Skipping '{existing_attr_name}' (different semantic types: '{existing_classification.classification}' vs '{incoming_classification.classification}')")
                            continue
                    except Exception as e:
                        # If classification fails (e.g., due to missing values), try semantic similarity check
                        # This can still work because it only needs the attribute names
                        try:
                            similarity_checker = AttributeNameSimilarityChecker()
                            similarity = await similarity_checker.check_similarity(
                                existing_attr_name, 
                                incoming_attr_name, 
                                finding_name
                            )
                            if similarity.is_similar:
                                # Semantically similar - proceed to comparison
                                print(f"      Classification failed, but semantic similarity check: SIMILAR (confidence: {similarity.confidence:.2f}, reasoning: {similarity.reasoning[:100]}...)")
                                pass  # Continue to comparison below
                            else:
                                # Not semantically similar - skip
                                print(f"      Skipping '{existing_attr_name}' (not semantically similar: '{existing_attr_name}' vs '{incoming_attr_name}', confidence: {similarity.confidence:.2f}, reasoning: {similarity.reasoning[:100]}...)")
                                continue
                        except Exception as e2:
                            # If semantic similarity check also fails, fall back to word-overlap check
                            words_existing = set(existing_name_lower.split())
                            words_incoming = set(incoming_name_lower.split())
                            # If no words overlap, skip (very different attributes)
                            if not words_existing.intersection(words_incoming):
                                print(f"      Skipping '{existing_attr_name}' (name too different: '{existing_attr_name}' vs '{incoming_attr_name}')")
                                continue
                
                # Show attribute details
                print(f"\n      INCOMING: '{incoming_attr_name}' ({incoming_attr_type})")
                if incoming_attr_type == 'choice':
                    # Handle both dict and object values
                    incoming_values_list = incoming_attr_dict.get('values', [])
                    incoming_values = []
                    for v in incoming_values_list:
                        if isinstance(v, dict):
                            incoming_values.append(v.get('name', ''))
                        else:
                            incoming_values.append(getattr(v, 'name', ''))
                    if incoming_values:
                        print(f"        Values: {', '.join(incoming_values[:5])}{'...' if len(incoming_values) > 5 else ''}")
                    else:
                        print(f"        Values: (none)")
                
                print(f"      EXISTING: '{existing_attr_name}' ({existing_attr_type})")
                if existing_attr_type == 'choice':
                    # Handle both dict and object values
                    existing_values_list = existing_attr_dict.get('values', [])
                    existing_values = []
                    for v in existing_values_list:
                        if isinstance(v, dict):
                            existing_values.append(v.get('name', ''))
                        else:
                            existing_values.append(getattr(v, 'name', ''))
                    if existing_values:
                        print(f"        Values: {', '.join(existing_values[:5])}{'...' if len(existing_values) > 5 else ''}")
                    else:
                        print(f"        Values: (none)")
                
                print(f"      Comparing...", end=' ', flush=True)
                comparison = await comparator.compare_attributes(
                    existing_attribute=existing_attr_dict,
                    new_attribute=incoming_attr_dict,
                    finding_name=finding_name,
                    attribute_type=incoming_attr_dict.get('type', 'choice')
                )
                print(f"✓ Result: {comparison.relationship} (confidence: {comparison.confidence:.2f})")
                
                # If identical or expanded, there's an overlap
                if comparison.relationship in ('identical', 'expanded'):
                    overlap_found = True
                    attr_name = existing_attr_dict.get('name', 'unknown')
                    
                    if comparison.relationship == 'identical':
                        change_summary['identical_attributes'].append({
                            'name': attr_name,
                            'relationship': 'identical'
                        })
                    else:  # expanded
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
                                
                            # Track new values
                            added_values = []
                            
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
                                    added_values.append(incoming_value.get('name', ''))
                            
                            # Update the merged attribute
                            merged_attributes[i] = existing_attr_dict.copy()
                            merged_attributes[i]['values'] = existing_values
                                
                            # Track the expansion
                            change_summary['expanded_attributes'].append({
                                'name': attr_name,
                                'relationship': 'expanded',
                                'new_values': added_values
                            })
                            change_summary['new_values'][attr_name] = added_values
                        else:
                            # Expanded but no new values
                            change_summary['expanded_attributes'].append({
                                'name': attr_name,
                                'relationship': 'expanded',
                                'new_values': []
                            })
                    
                    # If no new values, keep EXISTING as-is (do nothing)
                    break
            
            except Exception as e:
                # If comparison fails, treat as different attribute
                print(f"Warning: Could not compare attributes '{existing_attr_dict.get('name')}' and '{incoming_attr_dict.get('name')}': {e}")
                continue
        
        # If no overlap found, add INCOMING attribute as new
        if not overlap_found:
            # Ensure required fields are present for choice attributes
            attr_type = incoming_attr_dict.get('type', 'choice')
            if attr_type == 'choice':
                # Ensure 'values' field exists (required for choice attributes)
                # The schema requires 'values' to be present and have at least 2 items
                if 'values' not in incoming_attr_dict or incoming_attr_dict.get('values') is None:
                    incoming_attr_dict['values'] = []
                # Ensure 'max_selected' has a default
                if 'max_selected' not in incoming_attr_dict:
                    incoming_attr_dict['max_selected'] = 1
            
            merged_attributes.append(incoming_attr_dict)
            change_summary['new_attributes'].append({
                'name': incoming_attr_dict.get('name', 'unknown'),
                'type': attr_type
            })
    
    return merged_attributes, change_summary


async def create_new_model(incoming_model: FindingModelFull, index: Index) -> Tuple[FindingModelFull, List[Dict[str, Any]]]:
    """Create NEW model with required attributes.
    Returns: (new_model, added_attributes)"""
    # Ensure required attributes exist
    new_model, added_attributes = await ensure_required_attributes(incoming_model)
    return new_model, added_attributes


async def merge_models(
    existing_model_data: Dict[str, Any],
    incoming_model: FindingModelFull,
    index: Index
) -> Tuple[FindingModelFull, Dict[str, Any]]:
    """Merge INCOMING model with EXISTING model.
    Returns: (merged_model, change_summary)"""
    # Start with EXISTING model as base
    existing_attributes = existing_model_data.get('attributes', [])
    incoming_attributes = incoming_model.attributes or []
    
    # Merge attributes
    merged_attributes, change_summary = await merge_attributes(
        existing_attributes=existing_attributes,
        incoming_attributes=incoming_attributes,
        finding_name=existing_model_data.get('name', incoming_model.name)
    )
    
    # Build merged model (preserve EXISTING structure)
    merged_model_dict = existing_model_data.copy()
    
    # Ensure ALL attributes have required fields before validation
    # This is critical because the validator checks all attributes
    # Show warnings but don't skip - let validation fail if needed
    for attr in merged_attributes:
        attr_type = attr.get('type', 'choice')
        if attr_type == 'choice':
            # Ensure 'values' field exists (required for choice attributes)
            values = attr.get('values', [])
            if values is None:
                values = []
                print(f"  WARNING: Choice attribute '{attr.get('name', 'unknown')}' has None values - setting to empty list")
            
            # Schema requires at least 2 values for choice attributes
            # Show warning if invalid, but don't skip - let validation fail
            if len(values) < 2:
                print(f"  WARNING: Choice attribute '{attr.get('name', 'unknown')}' has {len(values)} values (requires at least 2) - validation will fail")
            
            attr['values'] = values
            
            # Ensure 'max_selected' is valid (>= 1)
            max_selected = attr.get('max_selected', 1)
            if max_selected is None or max_selected < 1:
                print(f"  WARNING: Choice attribute '{attr.get('name', 'unknown')}' has invalid max_selected={max_selected} - fixing to 1")
                attr['max_selected'] = 1
    
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
        return full_model, change_summary
    
    # Validate and return
    merged_model = FindingModelFull(**merged_model_dict)
    return merged_model, change_summary


def convert_to_json_serializable(obj: Any) -> Any:
    """Recursively convert MongoDB ObjectId and other non-serializable objects to strings."""
    from bson import ObjectId
    
    if isinstance(obj, ObjectId):
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
        except:
            return obj


def display_model_summary(model_data: Union[Dict[str, Any], FindingModelFull], title: str = "MODEL"):
    """Display a finding model in readable JSON format (not as a single block)."""
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)
    
    # Convert to dict if needed
    if isinstance(model_data, FindingModelFull):
        model_dict = model_data.model_dump(exclude_none=True)
    else:
        model_dict = model_data
    
    # Convert MongoDB ObjectIds and other non-serializable objects
    model_dict = convert_to_json_serializable(model_dict)
    
    # Display as formatted JSON with proper indentation
    # Print it line by line so it's not one big block
    json_str = json.dumps(model_dict, indent=2, ensure_ascii=False)
    for line in json_str.split('\n'):
        print(line)
    
    print("=" * 70 + "\n")


def get_user_confirmation(prompt: str) -> bool:
    """Get user confirmation (y/n). Returns True if yes, False if no."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def display_comparison_summary(
    existing: Dict[str, Any],
    incoming: FindingModelFull,
    confidence: float = None
) -> None:
    """Display high-level comparison summary."""
    print("\n" + "=" * 70)
    print("COMPARISON SUMMARY")
    print("=" * 70)
    print(f"Existing Finding: \"{existing.get('name', 'Unknown')}\" ({existing.get('oifm_id', 'none')})")
    print(f"Incoming Finding: \"{incoming.name}\" ({incoming.oifm_id or 'none'})")
    if confidence is not None:
        print(f"Confidence: {confidence:.2f}")
    
    existing_attr_count = len(existing.get('attributes', []))
    incoming_attr_count = len(incoming.attributes or [])
    print(f"Attribute Count: Existing={existing_attr_count}, Incoming={incoming_attr_count}")
    print("=" * 70 + "\n")


def display_attribute_comparison(
    existing_attrs: List[Dict[str, Any]],
    incoming_attrs: List[Dict[str, Any]],
    change_summary: Dict[str, Any],
    finding_name: str
) -> None:
    """Display detailed attribute-by-attribute comparison."""
    print("\n" + "=" * 70)
    print("ATTRIBUTE-BY-ATTRIBUTE COMPARISON")
    print("=" * 70)
    
    attr_num = 1
    
    # Show identical attributes
    for identical in change_summary.get('identical_attributes', []):
        attr_name = identical['name']
        print(f"{attr_num}. \"{attr_name}\" - IDENTICAL (no changes)")
        attr_num += 1
    
    # Show expanded attributes
    for expanded in change_summary.get('expanded_attributes', []):
        attr_name = expanded['name']
        new_values = expanded.get('new_values', [])
        if new_values:
            print(f"{attr_num}. \"{attr_name}\" - EXPANDED (adding values: {', '.join(new_values)})")
        else:
            print(f"{attr_num}. \"{attr_name}\" - EXPANDED (no new values to add)")
        attr_num += 1
    
    # Show new attributes
    for new_attr in change_summary.get('new_attributes', []):
        attr_name = new_attr['name']
        attr_type = new_attr.get('type', 'choice')
        print(f"{attr_num}. \"{attr_name}\" - NEW (new attribute, type: {attr_type}, will be added)")
        attr_num += 1
    
    if attr_num == 1:
        print("No attribute changes detected.")
    
    print("=" * 70 + "\n")


def display_json_diff(existing_dict: Dict[str, Any], merged_dict: Dict[str, Any]) -> None:
    """Display JSON diff showing changes."""
    print("\n" + "=" * 70)
    print("JSON DIFF")
    print("=" * 70)
    
    # Convert to JSON strings for diffing
    existing_json = json.dumps(existing_dict, indent=2, sort_keys=True, ensure_ascii=False)
    merged_json = json.dumps(merged_dict, indent=2, sort_keys=True, ensure_ascii=False)
    
    # Use difflib to show differences
    existing_lines = existing_json.splitlines(keepends=True)
    merged_lines = merged_json.splitlines(keepends=True)
    
    diff = difflib.unified_diff(
        existing_lines,
        merged_lines,
        fromfile='Existing',
        tofile='Merged',
        lineterm='',
        n=3
    )
    
    diff_output = ''.join(diff)
    if diff_output:
        print(diff_output)
    else:
        print("No differences found.")
    
    print("=" * 70 + "\n")


def display_console_comparison(
    existing: Dict[str, Any],
    incoming: FindingModelFull,
    merged: FindingModelFull
) -> None:
    """Display side-by-side console comparison."""
    print("\n" + "=" * 70)
    print("CONSOLE COMPARISON")
    print("=" * 70)
    
    print("\n--- EXISTING MODEL ---")
    print(f"Name: {existing.get('name', 'Unknown')}")
    print(f"ID: {existing.get('oifm_id', 'none')}")
    print(f"Description: {existing.get('description', '')[:100]}..." if len(existing.get('description', '')) > 100 else f"Description: {existing.get('description', '')}")
    print(f"Attributes: {len(existing.get('attributes', []))}")
    
    print("\n--- INCOMING MODEL ---")
    print(f"Name: {incoming.name}")
    print(f"ID: {incoming.oifm_id or 'none'}")
    desc = incoming.description
    print(f"Description: {desc[:100]}..." if len(desc) > 100 else f"Description: {desc}")
    print(f"Attributes: {len(incoming.attributes or [])}")
    
    print("\n--- MERGED MODEL (RESULT) ---")
    print(f"Name: {merged.name}")
    print(f"ID: {merged.oifm_id or 'none'}")
    merged_desc = merged.description
    print(f"Description: {merged_desc[:100]}..." if len(merged_desc) > 100 else f"Description: {merged_desc}")
    print(f"Attributes: {len(merged.attributes or [])}")
    
    print("=" * 70 + "\n")


def display_merge_proposal(
    existing: Dict[str, Any],
    incoming: FindingModelFull,
    merged: FindingModelFull,
    change_summary: Dict[str, Any],
    confidence: float = None
) -> None:
    """Display comprehensive merge proposal with all formats."""
    print("\n" + "=" * 70)
    print("MERGE PROPOSAL")
    print("=" * 70)
    
    # Display comparison summary
    display_comparison_summary(existing, incoming, confidence)
    
    # Display attribute comparison
    existing_attrs = existing.get('attributes', [])
    incoming_attrs = [attr.model_dump() if hasattr(attr, 'model_dump') else attr for attr in (incoming.attributes or [])]
    display_attribute_comparison(existing_attrs, incoming_attrs, change_summary, existing.get('name', ''))
    
    # Display JSON diff
    existing_dict = existing.copy()
    merged_dict = merged.model_dump()
    display_json_diff(existing_dict, merged_dict)
    
    # Display console comparison
    display_console_comparison(existing, incoming, merged)
    
    # Display full merged model preview
    print("\n" + "=" * 70)
    print("FULL MERGED MODEL PREVIEW")
    print("=" * 70)
    merged_json = merged.model_dump_json(indent=2, exclude_none=True)
    print(merged_json)
    print("=" * 70 + "\n")


def display_new_finding_proposal(
    incoming: FindingModelFull,
    enhanced: FindingModelFull,
    added_attributes: List[Dict[str, Any]]
) -> None:
    """Display new finding proposal with required attributes."""
    print("\n" + "=" * 70)
    print("NEW FINDING PROPOSAL")
    print("=" * 70)
    
    print("\n--- INCOMING FINDING ---")
    print(f"Name: {incoming.name}")
    print(f"ID: {incoming.oifm_id or 'none'}")
    desc = incoming.description
    print(f"Description: {desc[:200]}..." if len(desc) > 200 else f"Description: {desc}")
    print(f"Attributes: {len(incoming.attributes or [])}")
    
    if added_attributes:
        print("\n--- REQUIRED ATTRIBUTES TO ADD ---")
        for attr in added_attributes:
            attr_name = attr.get('name', 'unknown')
            attr_type = attr.get('type', 'choice')
            value_count = len(attr.get('values', []))
            print(f"- \"{attr_name}\" (type: {attr_type}, {value_count} values) - will be added")
    else:
        print("\n--- REQUIRED ATTRIBUTES ---")
        print("All required attributes (presence, change from prior) are already present.")
    
    print("\n--- ENHANCED MODEL PREVIEW ---")
    enhanced_json = enhanced.model_dump_json(indent=2, exclude_none=True)
    print(enhanced_json)
    print("=" * 70 + "\n")


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
        try:
            index = Index()
        except Exception as e:
            print(f"Error: Failed to connect to MongoDB: {e}")
            print("Please ensure MongoDB is running and accessible.")
            sys.exit(1)
        
        # Load INCOMING model
        print(f"Loading INCOMING model from {input_path}...")
        incoming_model = await load_incoming_model(input_path)
        print(f"Loaded model: {incoming_model.name} (ID: {incoming_model.oifm_id or 'none'})")
        
        # Search for EXISTING model
        print("Searching for EXISTING model...")
        existing_match, recommendation, confidence = await find_existing_model(incoming_model, index)
        
        if existing_match:
            # Check if this was a "review_needed" recommendation
            confidence_display = confidence if confidence is not None else 0.0
            if recommendation == "review_needed":
                print(f"⚠️  REVIEW NEEDED: Found similar model match: {existing_match.get('name')} (confidence: {confidence_display:.2f})")
                print("   This match requires manual review. Please verify it's the correct match before proceeding.")
            else:
                print(f"Found EXISTING model match: {existing_match.get('name')} (confidence: {confidence_display:.2f})")
            oifm_id = existing_match.get('oifm_id')
            confidence = confidence if confidence is not None else 0.0
            
            # Load EXISTING model from database
            print(f"Loading EXISTING model from database (ID: {oifm_id})...")
            existing_model_data = await get_existing_model_from_db(oifm_id, index)
            
            if existing_model_data:
                # Debug: Show attribute counts and which ones have 0 values
                existing_attrs = existing_model_data.get('attributes', [])
                print(f"  Database model has {len(existing_attrs)} attributes")
                for attr in existing_attrs:
                    attr_name = attr.get('name', 'unknown')
                    attr_type = attr.get('type', 'unknown')
                    if attr_type == 'choice':
                        values = attr.get('values', [])
                        value_count = len(values) if values else 0
                        if value_count == 0:
                            print(f"    WARNING: '{attr_name}' (choice) has 0 values in database")
                        elif value_count < 2:
                            print(f"    WARNING: '{attr_name}' (choice) has only {value_count} value(s) in database (needs ≥2)")
                # Display both models before processing
                print("\n" + "=" * 70)
                print("BEFORE MERGE PROCESSING")
                print("=" * 70)
                display_model_summary(existing_model_data, "EXISTING MODEL (from database)")
                display_model_summary(incoming_model, "INCOMING MODEL (from file)")
                
                # Merge models (preview mode)
                print("Analyzing merge...")
                merged_model, change_summary = await merge_models(existing_model_data, incoming_model, index)
                
                # Display merge proposal
                display_merge_proposal(
                    existing=existing_model_data,
                    incoming=incoming_model,
                    merged=merged_model,
                    change_summary=change_summary,
                    confidence=confidence
                )
                
                # Get user confirmation
                if get_user_confirmation("Proceed with merge?"):
                    # Save to merged_findings directory
                    output_dir = Path("defs/merged_findings")
                    await save_model(merged_model, output_dir, is_merged=True)
                    print("Merge completed!")
                else:
                    print("Merge cancelled by user.")
            else:
                print(f"Warning: EXISTING model {oifm_id} not found in database, creating NEW model instead")
                # Fall through to NEW model creation
                existing_match = None
        
        if not existing_match:
            # Create NEW model (preview mode)
            print("No EXISTING model match found, analyzing new finding...")
            
            # Display incoming model before processing
            print("\n" + "=" * 70)
            print("BEFORE NEW FINDING PROCESSING")
            print("=" * 70)
            display_model_summary(incoming_model, "INCOMING MODEL (from file)")
            
            new_model, added_attributes = await create_new_model(incoming_model, index)
            
            # Display new finding proposal
            display_new_finding_proposal(
                incoming=incoming_model,
                enhanced=new_model,
                added_attributes=added_attributes
            )
            
            # Get user confirmation
            if get_user_confirmation("Proceed with creating new finding?"):
                # Save to new_findings directory
                output_dir = Path("defs/new_findings")
                await save_model(new_model, output_dir, is_merged=False)
                print("New finding created!")
            else:
                print("Creation cancelled by user.")
        
        print("Done!")
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

