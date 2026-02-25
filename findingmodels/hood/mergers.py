"""Merge processing for Hood definitions."""

import logging
from typing import Dict, List, Tuple

from findingmodel import FindingModelFull
from findingmodel.index import Index

from scripts.merge_findings import (
    get_existing_model_from_db,
    classify_and_group_attributes,
    compare_attributes_within_group
)
from scripts.merge_findings_helpers import (
    create_presence_element,
    create_change_element,
    build_final_finding,
    ensure_hood_contributor,
    reorder_attributes,
    preserve_existing_ids,
    extract_attr_name
)

logger = logging.getLogger(__name__)

ENHANCED_CONFIDENCE_THRESHOLD = 0.7
CLASSIFICATION_TYPES = ['presence', 'change_from_prior', 'other']


def _collect_merge_recommendations(all_comparisons: Dict) -> Dict:
    """Process comparisons and categorize merge recommendations.
    
    Args:
        all_comparisons: Dict of comparisons by classification type
        
    Returns:
        Dict with keys: merge_recommendations, no_merge_comparisons, 
        needs_review_comparisons, new_attributes
    """
    merge_recommendations = []
    no_merge_comparisons = []
    needs_review_comparisons = []
    new_attributes = []
    
    for classification_type, comparisons in all_comparisons.items():
        for comparison in comparisons:
            relationship = comparison.get('relationship')
            
            if not relationship:
                new_attributes.append({
                    'incoming_attribute': comparison.get('incoming_attribute')
                })
                continue
            
            relationship_type = relationship.relationship if hasattr(relationship, 'relationship') else relationship.get('relationship')
            confidence = relationship.confidence if hasattr(relationship, 'confidence') else relationship.get('confidence', 0.0)
            
            if relationship_type == 'enhanced':
                if confidence >= ENHANCED_CONFIDENCE_THRESHOLD:
                    merge_recommendations.append({
                        'incoming_attribute': comparison.get('incoming_attribute'),
                        'existing_attribute': comparison.get('existing_attribute'),
                        'relationship': relationship
                    })
                else:
                    needs_review_comparisons.append({
                        'incoming_attribute': comparison.get('incoming_attribute'),
                        'existing_attribute': comparison.get('existing_attribute'),
                        'relationship': relationship,
                        'reason': f'Enhanced relationship but confidence ({confidence:.2f}) below threshold ({ENHANCED_CONFIDENCE_THRESHOLD})'
                    })
            elif relationship_type in ['identical', 'subset']:
                no_merge_comparisons.append({
                    'incoming_attribute': comparison.get('incoming_attribute'),
                    'existing_attribute': comparison.get('existing_attribute'),
                    'relationship': relationship
                })
            elif relationship_type == 'needs_review':
                needs_review_comparisons.append({
                    'incoming_attribute': comparison.get('incoming_attribute'),
                    'existing_attribute': comparison.get('existing_attribute'),
                    'relationship': relationship,
                    'reason': 'Attributes have shared values but each has unique values'
                })
            elif relationship_type == 'no_similarities':
                new_attributes.append({
                    'incoming_attribute': comparison.get('incoming_attribute')
                })
    
    return {
        'merge_recommendations': merge_recommendations,
        'no_merge_comparisons': no_merge_comparisons,
        'needs_review_comparisons': needs_review_comparisons,
        'new_attributes': new_attributes
    }


def _check_required_attributes(incoming_grouped: Dict, existing_grouped: Dict) -> Dict:
    """Check for presence and change_from_prior in both models."""
    incoming_has_presence = any(
        attr.get('_classification') == 'presence'
        for attr_list in incoming_grouped.values()
        for attr in attr_list
    )
    existing_has_presence = any(
        attr.get('_classification') == 'presence'
        for attr_list in existing_grouped.values()
        for attr in attr_list
    )
    
    incoming_has_change = any(
        attr.get('_classification') == 'change_from_prior'
        for attr_list in incoming_grouped.values()
        for attr in attr_list
    )
    existing_has_change = any(
        attr.get('_classification') == 'change_from_prior'
        for attr_list in existing_grouped.values()
        for attr in attr_list
    )
    
    return {
        'incoming_has_presence': incoming_has_presence,
        'existing_has_presence': existing_has_presence,
        'incoming_has_change': incoming_has_change,
        'existing_has_change': existing_has_change
    }


def _prepare_merge_data(
    new_attributes: List[Dict],
    needs_review_comparisons: List[Dict],
    incoming_has_presence: bool,
    existing_has_presence: bool,
    incoming_has_change: bool,
    existing_has_change: bool,
    finding_name: str
) -> Dict:
    """Prepare data structures for merge."""
    approved_new_attributes = []
    for new_attr_info in new_attributes:
        approved_new_attributes.append(new_attr_info.get('incoming_attribute'))
    
    attributes_to_add = []
    if not incoming_has_presence and not existing_has_presence:
        presence_attr = create_presence_element(finding_name)
        attributes_to_add.append(('presence', presence_attr))
    
    if not incoming_has_change and not existing_has_change:
        change_attr = create_change_element(finding_name)
        attributes_to_add.append(('change_from_prior', change_attr))
    
    review_decisions = []
    for review_comp in needs_review_comparisons:
        review_decisions.append({
            'incoming_attribute': review_comp.get('incoming_attribute'),
            'existing_attribute': review_comp.get('existing_attribute'),
            'decision': 'merge_values'
        })
    
    return {
        'approved_new_attributes': approved_new_attributes,
        'attributes_to_add': attributes_to_add,
        'review_decisions': review_decisions
    }


async def merge_with_existing(
    incoming_model: FindingModelFull,
    existing_match: Dict,
    index: Index
) -> Tuple[FindingModelFull, Dict]:
    """Merge incoming model with existing model.
    
    Args:
        incoming_model: The incoming finding model
        existing_match: The existing model match dict
        index: Database index
        
    Returns:
        Tuple of (Merged FindingModelFull, merge_details dict)
    """
    existing_model_data = await get_existing_model_from_db(
        existing_match.get('oifm_id'),
        index
    )
    
    if not existing_model_data:
        raise ValueError(f"Failed to load existing model {existing_match.get('oifm_id')}")
    
    finding_name = incoming_model.name
    
    incoming_attrs = []
    for attr in incoming_model.attributes or []:
        if isinstance(attr, dict):
            incoming_attrs.append(attr.copy())
        else:
            incoming_attrs.append(attr.model_dump(exclude_unset=False, exclude_none=False))
    
    existing_attrs = existing_model_data.get('attributes', [])
    
    incoming_grouped = await classify_and_group_attributes(incoming_attrs, finding_name)
    existing_grouped = await classify_and_group_attributes(existing_attrs, finding_name)
    
    all_comparisons = {}
    for classification_type in CLASSIFICATION_TYPES:
        incoming_attrs_group = incoming_grouped.get(classification_type, [])
        existing_attrs_group = existing_grouped.get(classification_type, [])
        
        if incoming_attrs_group or existing_attrs_group:
            comparisons = await compare_attributes_within_group(
                incoming_attrs_group,
                existing_attrs_group,
                classification_type,
                finding_name
            )
            all_comparisons[classification_type] = comparisons
    
    merge_data = _collect_merge_recommendations(all_comparisons)
    merge_recommendations = merge_data['merge_recommendations']
    no_merge_comparisons = merge_data['no_merge_comparisons']
    needs_review_comparisons = merge_data['needs_review_comparisons']
    new_attributes = merge_data['new_attributes']
    
    required_attrs = _check_required_attributes(incoming_grouped, existing_grouped)
    incoming_has_presence = required_attrs['incoming_has_presence']
    existing_has_presence = required_attrs['existing_has_presence']
    incoming_has_change = required_attrs['incoming_has_change']
    existing_has_change = required_attrs['existing_has_change']
    
    merge_prep = _prepare_merge_data(
        new_attributes,
        needs_review_comparisons,
        incoming_has_presence,
        existing_has_presence,
        incoming_has_change,
        existing_has_change,
        finding_name
    )
    approved_new_attributes = merge_prep['approved_new_attributes']
    attributes_to_add = merge_prep['attributes_to_add']
    review_decisions = merge_prep['review_decisions']
    
    merge_details = {
        'attributes_merged': len(merge_recommendations),
        'attributes_added': len(approved_new_attributes),
        'attributes_created': len(attributes_to_add),
        'merge_recommendations': [
            {
                'incoming_name': extract_attr_name(mr.get('incoming_attribute', {})),
                'existing_name': extract_attr_name(mr.get('existing_attribute', {})),
                'relationship': (
                    mr.get('relationship').relationship 
                    if hasattr(mr.get('relationship'), 'relationship') 
                    else (mr.get('relationship', {}).get('relationship', 'unknown') if isinstance(mr.get('relationship'), dict) else 'unknown')
                )
            }
            for mr in merge_recommendations
        ],
        'new_attributes': [
            extract_attr_name(attr)
            for attr in approved_new_attributes
        ],
        'created_attributes': [name for name, _ in attributes_to_add]
    }
    
    final_finding = build_final_finding(
        existing_model_data=existing_model_data,
        incoming_model=incoming_model,
        merge_recommendations=merge_recommendations,
        attributes_to_add=attributes_to_add,
        approved_new_attributes=approved_new_attributes,
        review_decisions=review_decisions
    )
    
    final_finding = ensure_hood_contributor(final_finding)
    final_finding = reorder_attributes(final_finding)
    final_finding = preserve_existing_ids(final_finding, source="MGB")
    
    return (FindingModelFull(**final_finding), merge_details)
