"""
Helper functions for merge_findings.py.

This module contains utility functions, reporting functions, and formatting functions
used by the merge_findings CLI tool.
"""

from typing import Dict, Optional, Tuple, List, Any
from pathlib import Path
from datetime import datetime

# Import FindingModelFull for type hints and runtime use
try:
    from findingmodel import FindingModelFull
except ImportError:
    # Fallback for type checking only
    FindingModelFull = Any


# Utility functions for attribute value extraction
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


def clean_final_finding(final_finding: Dict[str, Any]) -> Dict[str, Any]:
    """Clean up final finding dict by removing classification metadata."""
    cleaned = final_finding.copy()
    
    # Remove classification metadata from attributes
    attributes = cleaned.get('attributes', [])
    cleaned_attributes = []
    for attr in attributes:
        cleaned_attr = attr.copy()
        # Remove classification metadata
        cleaned_attr.pop('_classification', None)
        cleaned_attr.pop('_confidence', None)
        cleaned_attr.pop('_reasoning', None)
        
        cleaned_attributes.append(cleaned_attr)
    cleaned['attributes'] = cleaned_attributes
    
    return cleaned


def interactive_review_needs_review(
    needs_review_comparisons: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Interactive review of attributes needing review.
    
    Returns: List of review decisions with 'decision' field: 'keep_existing', 'add_new', or 'merge_values'
    """
    if not needs_review_comparisons:
        return []
    
    print("\n" + "=" * 80)
    print("ATTRIBUTES NEEDING REVIEW")
    print("=" * 80)
    print(f"\nFound {len(needs_review_comparisons)} attribute(s) requiring review.\n")
    
    review_decisions = []
    
    for idx, comp in enumerate(needs_review_comparisons, 1):
        incoming_attr = comp['incoming_attribute']
        existing_attr = comp['existing_attribute']
        relationship = comp['relationship']
        reason = comp.get('reason', '')
        
        incoming_name = extract_attr_name(incoming_attr)
        existing_name = extract_attr_name(existing_attr)
        
        print(f"\n{'─' * 80}")
        print(f"Review {idx}/{len(needs_review_comparisons)}")
        print(f"{'─' * 80}")
        print(f"\nEXISTING: {existing_name}")
        if existing_attr.get('type') == 'choice':
            existing_values = extract_value_names(existing_attr)
            print(f"  Values: {', '.join(existing_values) if existing_values else 'None'}")
        else:
            print(f"  Type: {existing_attr.get('type', 'unknown')}")
        
        print(f"\nINCOMING: {incoming_name}")
        if incoming_attr.get('type') == 'choice':
            incoming_values = extract_value_names(incoming_attr)
            print(f"  Values: {', '.join(incoming_values) if incoming_values else 'None'}")
        else:
            print(f"  Type: {incoming_attr.get('type', 'unknown')}")
        
        print(f"\nRelationship: {relationship.relationship} (confidence: {relationship.confidence:.2f})")
        if reason:
            print(f"Reason: {reason}")
        
        # Show value analysis
        if relationship.shared_values or relationship.existing_only_values or relationship.incoming_only_values:
            print("\nValue Analysis:")
            if relationship.shared_values:
                print(f"  Shared: {', '.join(relationship.shared_values)}")
            if relationship.existing_only_values:
                print(f"  Existing only: {', '.join(relationship.existing_only_values)}")
            if relationship.incoming_only_values:
                print(f"  Incoming only: {', '.join(relationship.incoming_only_values)}")
        
        print(f"\nAI Reasoning: {relationship.reasoning}")
        
        # Get user decision
        while True:
            print("\nDecision:")
            print("  [k] Keep existing (don't add incoming)")
            print("  [n] Add incoming as new attribute")
            print("  [m] Merge values (add incoming values to existing)")
            choice = input("  Enter choice (k/n/m): ").strip().lower()
            
            if choice == 'k':
                decision = 'keep_existing'
                print("  ✓ Decision: Keep existing")
                break
            elif choice == 'n':
                decision = 'add_new'
                print("  ✓ Decision: Add incoming as new attribute")
                break
            elif choice == 'm':
                decision = 'merge_values'
                print("  ✓ Decision: Merge values")
                break
            else:
                print("  ✗ Invalid choice. Please enter 'k', 'n', or 'm'.")
        
        review_decisions.append({
            'incoming_attribute': incoming_attr,
            'existing_attribute': existing_attr,
            'relationship': relationship,
            'reason': reason,
            'decision': decision
        })
    
    print(f"\n{'─' * 80}")
    print("Review complete!")
    print(f"{'─' * 80}\n")
    
    return review_decisions


def build_final_finding(
    existing_model_data: Dict[str, Any],
    incoming_model: FindingModelFull,
    merge_recommendations: List[Dict[str, Any]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]],
    approved_new_attributes: List[Dict[str, Any]],
    review_decisions: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Build the final finding model based on automatic merge decisions and review decisions.
    
    Merge strategy: Keep existing attribute, then add incoming values that don't already exist.
    
    Returns: Dictionary representing the final finding model."""
    if review_decisions is None:
        review_decisions = []
    
    # Start with existing model structure (if available) or incoming model
    if existing_model_data:
        final_finding = existing_model_data.copy()
    else:
        # Use incoming model as base
        final_finding = incoming_model.model_dump(exclude_unset=False, exclude_none=False)
    
    # Collect all final attributes
    final_attributes = []
    processed_incoming_attrs = set()
    processed_existing_attrs = set()
    
    # Process merge recommendations - automatically merge (keep existing + add new values)
    for merge_rec in merge_recommendations:
        incoming_attr = merge_rec['incoming_attribute']
        existing_attr = merge_rec['existing_attribute']
        incoming_name = incoming_attr.get('name', 'unknown')
        existing_name = existing_attr.get('name', 'unknown')
        
        processed_incoming_attrs.add(incoming_name)
        processed_existing_attrs.add(existing_name)
        
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
    
    # Process review decisions
    for review in review_decisions:
        incoming_attr = review['incoming_attribute']
        existing_attr = review['existing_attribute']
        decision = review['decision']
        incoming_name = incoming_attr.get('name', 'unknown')
        existing_name = existing_attr.get('name', 'unknown')
        
        if decision == 'keep_existing':
            # Keep existing, don't add incoming
            processed_incoming_attrs.add(incoming_name)
            processed_existing_attrs.add(existing_name)
            # Existing will be added later if not already processed
        elif decision == 'add_new':
            # Add incoming as new attribute
            processed_incoming_attrs.add(incoming_name)
            final_attributes.append(incoming_attr.copy())
        elif decision == 'merge_values':
            # Merge values: keep existing, add incoming values
            processed_incoming_attrs.add(incoming_name)
            processed_existing_attrs.add(existing_name)
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
    
    # Add existing attributes that weren't part of any merge recommendation or review decision
    if existing_model_data:
        existing_attrs = existing_model_data.get('attributes', [])
        for existing_attr in existing_attrs:
            existing_name = existing_attr.get('name', 'unknown')
            # Check if this attribute was part of a merge recommendation
            was_merged = any(
                merge_rec['existing_attribute'].get('name', 'unknown') == existing_name
                for merge_rec in merge_recommendations
            )
            # Check if this attribute was part of a review decision
            was_reviewed = any(
                review['existing_attribute'].get('name', 'unknown') == existing_name
                for review in review_decisions
            )
            if not was_merged and not was_reviewed:
                final_attributes.append(existing_attr.copy())
            elif was_reviewed:
                # Check if it was kept (keep_existing) or merged (merge_values)
                for review in review_decisions:
                    if review['existing_attribute'].get('name', 'unknown') == existing_name:
                        if review['decision'] == 'keep_existing':
                            # Add existing attribute as-is
                            if existing_name not in processed_existing_attrs:
                                final_attributes.append(existing_attr.copy())
                                processed_existing_attrs.add(existing_name)
                        # If merge_values, it was already added above
                        break
    
    # Add new attributes (presence/change_from_prior) - automatically added
    for attr_name, attr_dict in attributes_to_add:
        final_attributes.append(attr_dict.copy())
    
    final_finding['attributes'] = final_attributes
    
    return final_finding


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
    no_merge_comparisons: List[Dict[str, Any]],
    needs_review_comparisons: List[Dict[str, Any]],
    review_decisions: List[Dict[str, Any]] = None,
    new_attributes: List[Dict[str, Any]],
    attributes_to_add: List[Tuple[str, Dict[str, Any]]],
    report_path: Path
) -> None:
    """Generate individual merge report for this finding.
    
    Creates a markdown report documenting all changes made during the merge process.
    Each merge gets its own file.
    """
    if review_decisions is None:
        review_decisions = []
    
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
    
    # Summary statistics (moved to top)
    report_lines.append("## Summary")
    report_lines.append("")
    report_lines.append(f"- **Attributes merged:** {len(merge_recommendations)}")
    report_lines.append(f"- **Attributes needing review:** {len(needs_review_comparisons)}")
    if review_decisions:
        report_lines.append(f"- **Review decisions made:** {len(review_decisions)}")
        # Count decisions by type
        keep_count = sum(1 for r in review_decisions if r.get('decision') == 'keep_existing')
        add_count = sum(1 for r in review_decisions if r.get('decision') == 'add_new')
        merge_count = sum(1 for r in review_decisions if r.get('decision') == 'merge_values')
        if keep_count > 0:
            report_lines.append(f"  - Keep existing: {keep_count}")
        if add_count > 0:
            report_lines.append(f"  - Add as new: {add_count}")
        if merge_count > 0:
            report_lines.append(f"  - Merge values: {merge_count}")
    report_lines.append(f"- **New attributes added:** {len(new_attributes)}")
    report_lines.append(f"- **Required attributes added:** {len(attributes_to_add)}")
    report_lines.append(f"- **Total existing attributes:** {len(existing_attrs)}")
    report_lines.append(f"- **Total incoming attributes:** {len(incoming_attrs)}")
    report_lines.append(f"- **Total final attributes:** {len(final_attrs)}")
    report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    
    # Needs Review section (at the top, right after summary)
    if needs_review_comparisons:
        report_lines.append(f"## ⚠️ Attributes Needing Review ({len(needs_review_comparisons)})")
        report_lines.append("")
        if review_decisions:
            report_lines.append("*These attributes were reviewed and decisions were made.*")
        else:
            report_lines.append("*These attributes were compared but require human review to determine if they should be merged or kept separate.*")
        report_lines.append("")
        
        # Create a mapping of review decisions by incoming attribute name
        decision_map = {}
        for review in review_decisions:
            incoming_name = extract_attr_name(review['incoming_attribute'])
            decision_map[incoming_name] = review['decision']
        
        for idx, comp in enumerate(needs_review_comparisons, 1):
            incoming_attr = comp['incoming_attribute']
            existing_attr = comp['existing_attribute']
            relationship = comp['relationship']
            reason = comp.get('reason', '')
            
            incoming_name = incoming_attr.get('name', 'unknown')
            existing_name = existing_attr.get('name', 'unknown')
            
            report_lines.append(f"### {idx}. {existing_name} vs {incoming_name}")
            report_lines.append(f"- **Relationship:** {relationship.relationship} (confidence: {relationship.confidence:.2f})")
            report_lines.append(f"- **Recommendation:** {relationship.recommendation}")
            if reason:
                report_lines.append(f"- **Reason for review:** {reason}")
            
            # Show decision if made
            if incoming_name in decision_map:
                decision = decision_map[incoming_name]
                decision_text = {
                    'keep_existing': '✅ **Decision: Keep existing** (incoming attribute not added)',
                    'add_new': '✅ **Decision: Add incoming as new attribute**',
                    'merge_values': '✅ **Decision: Merge values** (incoming values added to existing)'
                }.get(decision, f'Decision: {decision}')
                report_lines.append(f"- {decision_text}")
            else:
                report_lines.append("- **Decision:** ⚠️ Not reviewed")
            
            report_lines.append(f"- **AI Reasoning:** {relationship.reasoning}")
            report_lines.append("")
            
            # Show value analysis if available
            if relationship.shared_values or relationship.existing_only_values or relationship.incoming_only_values:
                if relationship.shared_values:
                    report_lines.append(f"- **Shared values:** {', '.join(relationship.shared_values)}")
                if relationship.existing_only_values:
                    report_lines.append(f"- **Existing only values:** {', '.join(relationship.existing_only_values)}")
                if relationship.incoming_only_values:
                    report_lines.append(f"- **Incoming only values:** {', '.join(relationship.incoming_only_values)}")
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
            report_lines.append(f"- **AI Reasoning:** {relationship.reasoning}")
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
    
    # Comparisons made but not merged (for verification)
    if no_merge_comparisons:
        report_lines.append(f"### Comparisons Made (Not Merged) ({len(no_merge_comparisons)})")
        report_lines.append("")
        report_lines.append("*These attributes were compared but not merged. Review to verify they should remain separate.*")
        report_lines.append("")
        for idx, comp in enumerate(no_merge_comparisons, 1):
            incoming_attr = comp['incoming_attribute']
            existing_attr = comp['existing_attribute']
            relationship = comp['relationship']
            
            incoming_name = incoming_attr.get('name', 'unknown')
            existing_name = existing_attr.get('name', 'unknown')
            
            report_lines.append(f"#### {idx}. {existing_name} vs {incoming_name}")
            report_lines.append(f"- **Relationship:** {relationship.relationship} (confidence: {relationship.confidence:.2f})")
            report_lines.append(f"- **Recommendation:** {relationship.recommendation}")
            report_lines.append(f"- **AI Reasoning:** {relationship.reasoning}")
            report_lines.append("")
            
            # Show value analysis if available
            if relationship.shared_values or relationship.existing_only_values or relationship.incoming_only_values:
                if relationship.shared_values:
                    report_lines.append(f"- **Shared values:** {', '.join(relationship.shared_values)}")
                if relationship.existing_only_values:
                    report_lines.append(f"- **Existing only values:** {', '.join(relationship.existing_only_values)}")
                if relationship.incoming_only_values:
                    report_lines.append(f"- **Incoming only values:** {', '.join(relationship.incoming_only_values)}")
                report_lines.append("")
    else:
        report_lines.append("### Comparisons Made (Not Merged)")
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
    
    # Write report to individual file
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines), encoding='utf-8')

