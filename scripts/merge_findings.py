"""
CLI tool for merging finding models.

This script processes an INCOMING FM JSON file and searches the database for matches.
Helper functions and reporting utilities are in merge_findings_helpers.py.
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

from findingmodel.tools import find_similar_models, add_ids_to_model
from findingmodel.index import Index
from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.common import model_file_name
from agents.merge_agents import (
    create_classification_agent, 
    AttributeClassification,
    create_attribute_relationship_agent,
    AttributeRelationship
)
from merge_findings_helpers import (
    extract_value_names,
    extract_attr_name,
    create_presence_element,
    create_change_element,
    clean_final_finding,
    print_merge_summary,
    format_attribute_for_report,
    generate_merge_report,
    interactive_review_needs_review,
    build_final_finding,
    ensure_hood_contributor,
    reorder_attributes,
    preserve_existing_ids
)


def has_standard_presence_values(attr: Dict[str, Any]) -> bool:
    """Check if an attribute has the standard presence values."""
    standard_values = {"absent", "present", "indeterminate", "unknown"}
    attr_values = set(extract_value_names(attr))
    return standard_values.issubset(attr_values)


def has_standard_change_from_prior_values(attr: Dict[str, Any]) -> bool:
    """Check if an attribute has the standard change_from_prior values."""
    standard_values = {"unchanged", "stable", "new", "resolved", "increased", "decreased", "larger", "smaller"}
    attr_values = set(extract_value_names(attr))
    # Check if it has at least the core values (not necessarily all)
    core_values = {"unchanged", "stable", "new", "resolved", "increased", "decreased"}
    return core_values.issubset(attr_values) or standard_values.issubset(attr_values)


async def load_incoming_model(file_path: Path) -> FindingModelFull:
    """Load and validate INCOMING model from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            model_data = json.load(f)
        
        model = FindingModelFull(**model_data)
        return model
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
            # Get the highest confidence match (should already be a dict)
            best_match = analysis.similar_models[0]
            return best_match
    
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
    
    total_attrs = len(attributes)
    for idx, attr in enumerate(attributes, 1):
        attr_name = extract_attr_name(attr)
        if total_attrs > 1:
            print(f"    Classifying attribute {idx}/{total_attrs}: {attr_name}...", end='\r', flush=True)
        try:
            classification = await classify_attribute(attr, finding_name)
            
            # Add classification info to attribute
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = classification.classification
            attr_with_classification['_confidence'] = classification.confidence
            attr_with_classification['_reasoning'] = classification.reasoning
            
            # Group by classification
            grouped[classification.classification].append(attr_with_classification)
            if total_attrs > 1:
                print(f"    Classifying attribute {idx}/{total_attrs}: {attr_name}... [OK]")
        except Exception as e:
            # Add to 'other' as fallback
            attr_with_classification = attr.copy()
            attr_with_classification['_classification'] = 'other'
            attr_with_classification['_confidence'] = 0.0
            attr_with_classification['_reasoning'] = f"Classification failed: {e}"
            grouped['other'].append(attr_with_classification)
            if total_attrs > 1:
                print(f"    Classifying attribute {idx}/{total_attrs}: {attr_name}... [ERROR]")
    
    if total_attrs > 1:
        print()  # New line after progress indicators
    return grouped


async def compare_attributes_within_group(
    incoming_attrs: List[Dict[str, Any]],
    existing_attrs: List[Dict[str, Any]],
    classification_type: str,
    finding_name: str
) -> List[Dict[str, Any]]:
    """Compare attributes within the same classification group using the relationship agent.
    
    Uses relationship type prioritization:
    1. enhanced (with confidence >= 0.7) > subset/identical > needs_review > no_similarities
    2. Only add as new if ALL comparisons are no_similarities
    
    Returns: List of comparison results with relationship information."""
    relationship_agent = create_attribute_relationship_agent()
    ENHANCED_CONFIDENCE_THRESHOLD = 0.7
    comparisons = []
    
    # EARLY EXIT: For presence/change_from_prior, if existing has standard values, skip comparison
    if classification_type in ['presence', 'change_from_prior'] and existing_attrs:
        # Check if any existing attribute has standard values
        has_standard = False
        standard_existing_attr = None
        
        for existing_attr in existing_attrs:
            if classification_type == 'presence':
                if has_standard_presence_values(existing_attr):
                    has_standard = True
                    standard_existing_attr = existing_attr
                    break
            elif classification_type == 'change_from_prior':
                if has_standard_change_from_prior_values(existing_attr):
                    has_standard = True
                    standard_existing_attr = existing_attr
                    break
        
        if has_standard and standard_existing_attr:
            # Skip all comparisons - keep existing, discard all incoming
            standard_attr_name = extract_attr_name(standard_existing_attr)
            print(f"\n    [INFO] Existing '{standard_attr_name}' has standard {classification_type} values - KEEP EXISTING, DISCARD ALL INCOMING")
            
            for incoming_attr in incoming_attrs:
                incoming_name = extract_attr_name(incoming_attr)
                # Create a "subset" relationship to indicate keep existing
                best_relationship = AttributeRelationship(
                    relationship="subset",
                    confidence=1.0,
                    reasoning=f"Existing attribute has standard {classification_type} values. Incoming attribute '{incoming_name}' will be discarded.",
                    recommendation="no_merge",
                    existing_values=extract_value_names(standard_existing_attr),
                    incoming_values=extract_value_names(incoming_attr),
                    shared_values=[],
                    existing_only_values=extract_value_names(standard_existing_attr),
                    incoming_only_values=extract_value_names(incoming_attr)
                )
                comparisons.append({
                    'incoming_attribute': incoming_attr,
                    'existing_attribute': standard_existing_attr,
                    'relationship': best_relationship
                })
                print(f"      Discarding incoming '{incoming_name}' (standard structure preferred)")
            
            return comparisons  # Early return - no API calls needed!
    
    # Compare each incoming attribute with each existing attribute
    total_incoming = len(incoming_attrs)
    total_existing = len(existing_attrs)
    
    for incoming_idx, incoming_attr in enumerate(incoming_attrs, 1):
        incoming_name = incoming_attr.get('name', 'unknown')
        all_relationships = []  # Store all comparisons for this incoming attribute
        
        for existing_idx, existing_attr in enumerate(existing_attrs, 1):
            existing_name = existing_attr.get('name', 'unknown')
            existing_type = existing_attr.get('type', 'unknown')
            incoming_type = incoming_attr.get('type', 'unknown')
            
            # Show progress for each comparison
            print(f"    Comparing: '{incoming_name}' (incoming {incoming_idx}/{total_incoming}) <-> '{existing_name}' (existing {existing_idx}/{total_existing})...", end='\r', flush=True)
            
            # Skip if types don't match (choice vs numeric)
            if existing_type != incoming_type:
                continue
            
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
                
                # Clear the progress line and print comparison details with separator
                print()  # New line after progress indicator
                print(f"\n      {'-' * 60}")
                print(f"      Comparing:")
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
                print(f"      {'-' * 60}")
                
                # Store all relationships for prioritization
                all_relationships.append({
                    'existing_attribute': existing_attr,
                    'relationship': relationship
                })
            except Exception as e:
                print(f"      ERROR comparing '{existing_name}' vs '{incoming_name}': {e}")
                pass
        
        # Prioritize relationship types (not just confidence)
        best_match = None
        best_relationship = None
        
        if all_relationships:
            # Priority order: enhanced (with threshold) > subset/identical > needs_review > no_similarities
            # Within each type, use highest confidence
            
            # 1. Check for "enhanced" with confidence >= threshold
            enhanced_matches = [
                r for r in all_relationships 
                if r['relationship'].relationship == 'enhanced' 
                and r['relationship'].confidence >= ENHANCED_CONFIDENCE_THRESHOLD
            ]
            if enhanced_matches:
                best_match = max(enhanced_matches, key=lambda x: x['relationship'].confidence)
                best_relationship = best_match['relationship']
                print(f"\n    [OK] Best match for '{incoming_name}': '{extract_attr_name(best_match['existing_attribute'])}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f}) - MERGE")
            
            # 2. Check for "subset" or "identical"
            elif any(r['relationship'].relationship in ['subset', 'identical'] for r in all_relationships):
                subset_identical_matches = [
                    r for r in all_relationships 
                    if r['relationship'].relationship in ['subset', 'identical']
                ]
                best_match = max(subset_identical_matches, key=lambda x: x['relationship'].confidence)
                best_relationship = best_match['relationship']
                print(f"\n    [OK] Best match for '{incoming_name}': '{extract_attr_name(best_match['existing_attribute'])}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f}) - KEEP EXISTING")
            
            # 3. Check for "needs_review"
            elif any(r['relationship'].relationship == 'needs_review' for r in all_relationships):
                needs_review_matches = [
                    r for r in all_relationships 
                    if r['relationship'].relationship == 'needs_review'
                ]
                best_match = max(needs_review_matches, key=lambda x: x['relationship'].confidence)
                best_relationship = best_match['relationship']
                print(f"\n    [WARN] Best match for '{incoming_name}': '{extract_attr_name(best_match['existing_attribute'])}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f}) - NEEDS REVIEW")
            
            # 4. Check for "enhanced" below threshold (treat as needs_review)
            elif any(r['relationship'].relationship == 'enhanced' for r in all_relationships):
                enhanced_low_conf = [
                    r for r in all_relationships 
                    if r['relationship'].relationship == 'enhanced'
                ]
                best_match = max(enhanced_low_conf, key=lambda x: x['relationship'].confidence)
                # Override relationship type to needs_review for low confidence enhanced
                best_relationship = best_match['relationship']
                print(f"\n    [WARN] Best match for '{incoming_name}': '{extract_attr_name(best_match['existing_attribute'])}' - enhanced (confidence: {best_relationship.confidence:.2f} < {ENHANCED_CONFIDENCE_THRESHOLD}) - NEEDS REVIEW (low confidence)")
            
            # 5. All are "no_similarities"
            elif all(r['relationship'].relationship == 'no_similarities' for r in all_relationships):
                # For presence/change_from_prior: if we get here, existing doesn't have standard values (caught earlier)
                # Flag for review so human can decide
                if classification_type in ['presence', 'change_from_prior'] and existing_attrs:
                    print(f"\n    [WARN] All comparisons for '{incoming_name}' are 'no_similarities', and existing {classification_type} attribute does not have standard values - NEEDS REVIEW")
                    # Use the first existing attribute for review
                    best_match = {'existing_attribute': existing_attrs[0]}
                    best_relationship = AttributeRelationship(
                        relationship="needs_review",
                        confidence=0.5,
                        reasoning=f"Both attributes are {classification_type} but have no_similarities. Existing does not have standard values. Requires human review.",
                        recommendation="no_merge",
                        existing_values=extract_value_names(existing_attrs[0]),
                        incoming_values=extract_value_names(incoming_attr),
                        shared_values=[],
                        existing_only_values=extract_value_names(existing_attrs[0]),
                        incoming_only_values=extract_value_names(incoming_attr)
                    )
                else:
                    # Not presence/change_from_prior, or no existing attributes - add as new
                    print(f"\n    [ERROR] All comparisons for '{incoming_name}' are 'no_similarities' - NEW ATTRIBUTE")
                    best_match = None
                    best_relationship = None
            else:
                # Fallback: use highest confidence
                best_match = max(all_relationships, key=lambda x: x['relationship'].confidence)
                best_relationship = best_match['relationship']
                print(f"\n    [OK] Best match for '{incoming_name}': '{extract_attr_name(best_match['existing_attribute'])}' - {best_relationship.relationship} (confidence: {best_relationship.confidence:.2f})")
        
        if total_incoming > 1:
            print(f"    Comparing incoming attribute {incoming_idx}/{total_incoming}: {incoming_name}... [OK]")
        
        print()  # Extra blank line for separation
        
        if best_match and best_relationship:
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': best_match['existing_attribute'],
                'relationship': best_relationship
            })
        else:
            # No match found or all no_similarities - new attribute
            comparisons.append({
                'incoming_attribute': incoming_attr,
                'existing_attribute': None,
                'relationship': None
            })
    
    return comparisons


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
        '--auto-keep-existing',
        action='store_true',
        help='Automatically choose "keep existing" for all review decisions (non-interactive mode)'
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
        print(f"  [OK] Loaded: {incoming_model.name}")
        
        # Search for EXISTING model
        print("Searching for existing model in database...")
        existing_match = await find_existing_model(incoming_model, index)
        if existing_match:
            print(f"  [OK] Found match: {existing_match.get('name')} (ID: {existing_match.get('oifm_id')})")
        else:
            print("  [OK] No match found")
        
        if existing_match:
            # Load EXISTING model from database
            print("Loading existing model from database...")
            existing_model_data = await get_existing_model_from_db(existing_match.get('oifm_id'), index)
            
            if existing_model_data:
                finding_name = incoming_model.name
                print(f"  [OK] Loaded existing model data")
                
                # Get attributes from both models
                print("Extracting attributes from models...")
                incoming_attrs = []
                for attr in incoming_model.attributes or []:
                    if isinstance(attr, dict):
                        incoming_attrs.append(attr.copy())
                    else:
                        incoming_attrs.append(attr.model_dump(exclude_unset=False, exclude_none=False))
                
                existing_attrs = existing_model_data.get('attributes', [])
                print(f"  [OK] Incoming: {len(incoming_attrs)} attributes")
                print(f"  [OK] Existing: {len(existing_attrs)} attributes")
                
                # Classify and group incoming attributes
                print("Classifying incoming attributes...")
                incoming_grouped = await classify_and_group_attributes(incoming_attrs, finding_name)
                print(f"  [OK] Classified {len(incoming_attrs)} attributes")
                
                # Classify and group existing attributes
                print("Classifying existing attributes...")
                existing_grouped = await classify_and_group_attributes(existing_attrs, finding_name)
                print(f"  [OK] Classified {len(existing_attrs)} attributes")
                
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
                        print(f"    [OK] Completed {classification_type} comparison ({len(comparisons)} comparisons)")
                
                # Collect all merge recommendations, no_merge comparisons, needs_review, and new attributes
                print("Collecting merge recommendations and new attributes...")
                merge_recommendations = []
                no_merge_comparisons = []
                needs_review_comparisons = []
                new_attributes = []
                ENHANCED_CONFIDENCE_THRESHOLD = 0.7
                
                for classification_type, comparisons in all_comparisons.items():
                    if comparisons:
                        print(f"\n  {'=' * 70}")
                        print(f"  {classification_type.upper()} Results:")
                        print(f"  {'=' * 70}")
                        for comp in comparisons:
                            if comp['relationship']:
                                relationship = comp['relationship']
                                relationship_type = relationship.relationship
                                incoming_attr_name = extract_attr_name(comp['incoming_attribute'])
                                existing_attr_name = extract_attr_name(comp['existing_attribute'])
                                
                                print(f"    '{incoming_attr_name}' (incoming) <-> '{existing_attr_name}' (existing)")
                                print(f"      Relationship: {relationship_type} (confidence: {relationship.confidence:.2f})")
                                print(f"      Recommendation: {relationship.recommendation}")
                                
                                # Categorize based on relationship type
                                if relationship_type == 'enhanced':
                                    # Enhanced with confidence >= threshold -> merge
                                    if relationship.confidence >= ENHANCED_CONFIDENCE_THRESHOLD:
                                        merge_recommendations.append({
                                            'incoming_attribute': comp['incoming_attribute'],
                                            'existing_attribute': comp['existing_attribute'],
                                            'relationship': comp['relationship']
                                        })
                                    else:
                                        # Enhanced below threshold -> needs review
                                        needs_review_comparisons.append({
                                            'incoming_attribute': comp['incoming_attribute'],
                                            'existing_attribute': comp['existing_attribute'],
                                            'relationship': comp['relationship'],
                                            'reason': f'Enhanced relationship but confidence ({relationship.confidence:.2f}) below threshold ({ENHANCED_CONFIDENCE_THRESHOLD})'
                                        })
                                elif relationship_type in ['subset', 'identical']:
                                    # Keep existing - no merge needed
                                    no_merge_comparisons.append({
                                        'incoming_attribute': comp['incoming_attribute'],
                                        'existing_attribute': comp['existing_attribute'],
                                        'relationship': comp['relationship']
                                    })
                                elif relationship_type == 'needs_review':
                                    # Flag for human review
                                    needs_review_comparisons.append({
                                        'incoming_attribute': comp['incoming_attribute'],
                                        'existing_attribute': comp['existing_attribute'],
                                        'relationship': comp['relationship'],
                                        'reason': 'Attributes have shared values but each has unique values'
                                    })
                                elif relationship_type == 'no_similarities':
                                    # This shouldn't happen here since no_similarities should result in relationship=None
                                    # But handle it just in case
                                    new_attributes.append({
                                        'incoming_attribute': comp['incoming_attribute']
                                    })
                            else:
                                # No relationship found - all comparisons were no_similarities -> new attribute
                                incoming_attr_name = extract_attr_name(comp['incoming_attribute'])
                                print(f"    '{incoming_attr_name}' (incoming): NEW (all comparisons were no_similarities)")
                                new_attributes.append({
                                    'incoming_attribute': comp['incoming_attribute']
                                })
                
                print(f"  [OK] Found {len(merge_recommendations)} merge recommendations")
                print(f"  [OK] Found {len(needs_review_comparisons)} attributes needing review")
                print(f"  [OK] Found {len(new_attributes)} new attributes")
                
                # Automatic new attributes process - add all new attributes
                approved_new_attributes = []
                for new_attr_info in new_attributes:
                    approved_new_attributes.append(new_attr_info['incoming_attribute'])
                
                # Automatic check for missing presence/change_from_prior attributes
                # Check both incoming AND existing to avoid duplicates
                # Use the classification metadata from the classification agent
                print("Checking for required attributes...")
                
                # Check incoming attributes using classification metadata
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
                
                # Check if existing model has these required attributes
                existing_has_presence = any(
                    attr.get('_classification') == 'presence'
                    for attr_list in existing_grouped.values() 
                    for attr in attr_list
                )
                existing_has_change_from_prior = any(
                    attr.get('_classification') == 'change_from_prior'
                    for attr_list in existing_grouped.values() 
                    for attr in attr_list
                )
                
                attributes_to_add = []
                
                # Check final attributes list to ensure we don't add duplicates
                # Use the classified attributes which have _classification metadata from the agent
                # Collect all attributes that will be in the final model (from classified groups)
                final_attrs_to_check = []
                # Add all existing classified attributes
                for attr_list in existing_grouped.values():
                    final_attrs_to_check.extend(attr_list)
                # Add all incoming classified attributes that will be added
                for attr_list in incoming_grouped.values():
                    final_attrs_to_check.extend(attr_list)
                
                # Check if presence/change_from_prior already exists in final attributes
                # Use classification metadata from the classification agent
                has_presence_in_final = any(
                    attr.get('_classification') == 'presence'
                    for attr in final_attrs_to_check
                )
                has_change_in_final = any(
                    attr.get('_classification') == 'change_from_prior'
                    for attr in final_attrs_to_check
                )
                
                # Only add if neither incoming nor existing has it, AND it's not already in final attributes
                if not incoming_has_presence and not existing_has_presence and not has_presence_in_final:
                    print("  [OK] Adding presence attribute")
                    presence_attr = create_presence_element(finding_name)
                    attributes_to_add.append(('presence', presence_attr))
                elif (incoming_has_presence or existing_has_presence or has_presence_in_final):
                    print("  [OK] Presence attribute already exists, skipping")
                
                if not incoming_has_change_from_prior and not existing_has_change_from_prior and not has_change_in_final:
                    print("  [OK] Adding change_from_prior attribute")
                    change_attr = create_change_element(finding_name)
                    attributes_to_add.append(('change_from_prior', change_attr))
                elif (incoming_has_change_from_prior or existing_has_change_from_prior or has_change_in_final):
                    print("  [OK] Change from prior attribute already exists, skipping")
                
                if not attributes_to_add:
                    print("  [OK] All required attributes present")
                
                # Interactive review of needs_review attributes
                review_decisions = []
                if needs_review_comparisons:
                    auto_decision = 'keep_existing' if args.auto_keep_existing else None
                    review_decisions = interactive_review_needs_review(needs_review_comparisons, auto_decision=auto_decision)
                
                # Build the final finding
                print("Building final finding model...")
                final_finding = build_final_finding(
                    existing_model_data=existing_model_data,
                    incoming_model=incoming_model,
                    merge_recommendations=merge_recommendations,
                    attributes_to_add=attributes_to_add,
                    approved_new_attributes=approved_new_attributes,
                    review_decisions=review_decisions
                )
                final_attrs = final_finding.get('attributes', [])
                print(f"  [OK] Final model has {len(final_attrs)} attributes")
                
                # Ensure Michael Hood is included as a contributor
                print("Ensuring Michael Hood is included as contributor...")
                final_finding = ensure_hood_contributor(final_finding)
                print("  [OK] Contributor added")
                
                # Reorder attributes: presence and change from prior at the top
                print("Reordering attributes (presence and change from prior first)...")
                final_finding = reorder_attributes(final_finding)
                print("  [OK] Attributes reordered")
                
                # Extract source from existing model's oifm_id (e.g., OIFM_CDE_000003 -> CDE)
                # Pattern: OIFM_{SOURCE}_{NUMBER}
                source = "MGB"  # Default fallback
                if existing_model_data and 'oifm_id' in existing_model_data:
                    oifm_id = existing_model_data['oifm_id']
                    # Extract source from pattern OIFM_{SOURCE}_{NUMBER}
                    parts = oifm_id.split('_')
                    if len(parts) >= 3:
                        source = parts[1]  # Get the SOURCE part
                
                # Add IDs to any attributes missing them using the existing model's source
                # Preserve existing IDs from both existing and incoming models
                print("Adding IDs to attributes missing them...")
                final_finding = preserve_existing_ids(final_finding, source=source)
                print(f"  [OK] Preserved existing IDs and added missing ones using source: {source}")
                
                # Automatically save the final model
                print("Saving final model...")
                output_dir = Path("defs/merged_findings")
                success = await save_final_model(final_finding, output_dir)
                if not success:
                    print("  [ERROR] Error: Failed to save model.")
                    return
                print("  [OK] Model saved successfully")
                
                # Generate merge report (individual file per merge)
                print("Generating merge report...")
                # Reconstruct full classified attribute lists from grouped dictionaries
                # This preserves the _classification metadata added by the agent
                existing_attrs_classified = []
                for classification_type in ['presence', 'change_from_prior', 'other']:
                    existing_attrs_classified.extend(existing_grouped[classification_type])
                
                incoming_attrs_classified = []
                for classification_type in ['presence', 'change_from_prior', 'other']:
                    incoming_attrs_classified.extend(incoming_grouped[classification_type])
                
                # Create filename from finding name
                safe_name = finding_name.lower().replace(' ', '_').replace('/', '_')
                report_filename = f"merge_report_{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                report_path = Path("merge_reports") / report_filename
                generate_merge_report(
                    finding_name=finding_name,
                    existing_match=existing_match,
                    existing_attrs=existing_attrs_classified,
                    incoming_attrs=incoming_attrs_classified,
                    final_attrs=final_attrs,
                    merge_recommendations=merge_recommendations,
                    no_merge_comparisons=no_merge_comparisons,
                    needs_review_comparisons=needs_review_comparisons,
                    review_decisions=review_decisions,
                    new_attributes=new_attributes,
                    attributes_to_add=attributes_to_add,
                    report_path=report_path
                )
                print(f"  [OK] Report saved to: {report_path}")
                
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

