#!/usr/bin/env python3
"""
Test script for the attribute classifier agents.
This script tests the agents with real medical finding attributes.
"""

import asyncio
import json
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from agents.attribute_classifier import (
    AttributeClassifier,
    AttributeComparator, 
    AttributeMerger
)

def load_finding_attributes(finding_path: Path):
    """Load attributes from a finding model file"""
    try:
        with open(finding_path, 'r', encoding='utf-8') as f:
            finding_data = json.load(f)
        return finding_data.get('attributes', [])
    except Exception as e:
        print(f"[ERROR] Failed to load finding: {e}")
        return []

async def test_classification():
    """Test attribute classification with real finding data"""
    print("=" * 60)
    print("TESTING ATTRIBUTE CLASSIFICATION")
    print("=" * 60)
    
    finding_path = Path(__file__).parent.parent.parent / "defs" / "original_defs" / "abnormal_configuration_of_cerebral_ventricles.fm.json"
    attributes = load_finding_attributes(finding_path)
    
    if not attributes:
        print("[ERROR] No attributes found to test")
        return
    
    classifier = AttributeClassifier()
    
    for i, attribute in enumerate(attributes, 1):
        print(f"\n--- Attribute {i}: {attribute['name']} ---")
        print(f"Type: {attribute['type']} | Values: {len(attribute.get('values', []))}")
        
        try:
            result = await classifier.classify_attribute(attribute)
            print(f"✓ Classification: {result.classification} (confidence: {result.confidence:.2f})")
            print(f"  Reasoning: {result.reasoning}")
        except Exception as e:
            print(f"✗ Error: {e}")
        print("-" * 40)


async def test_comparison():
    """Test attribute comparison with real finding data"""
    print("\n" + "=" * 60)
    print("TESTING ATTRIBUTE COMPARISON")
    print("=" * 60)
    
    finding_path = Path(__file__).parent.parent.parent / "defs" / "original_defs" / "abnormal_configuration_of_cerebral_ventricles.fm.json"
    attributes = load_finding_attributes(finding_path)
    
    if len(attributes) < 2:
        print("[ERROR] Need at least 2 attributes for comparison test")
        return
    
    comparator = AttributeComparator()
    
    # Compare first two attributes
    attr1, attr2 = attributes[0], attributes[1]
    print(f"Comparing: '{attr1['name']}' vs '{attr2['name']}'")
    
    try:
        result = await comparator.compare_attributes(
            existing_attribute=attr1,
            new_attribute=attr2,
            finding_name="abnormal configuration of cerebral ventricles",
            attribute_type="choice"
        )
        print(f"✓ Relationship: {result.relationship} (confidence: {result.confidence:.2f})")
        print(f"  Reasoning: {result.reasoning}")
        if result.merge_strategy:
            print(f"  Merge Strategy: {result.merge_strategy}")
    except Exception as e:
        print(f"✗ Error: {e}")


async def test_deterministic_comparisons():
    """Deterministic comparison tests: identical, expanded, different on one choice attribute."""
    print("\n" + "=" * 60)
    print("DETERMINISTIC COMPARISON CASES")
    print("=" * 60)

    finding_path = Path(__file__).parent.parent.parent / "defs" / "original_defs" / "abnormal_configuration_of_cerebral_ventricles.fm.json"
    attributes = load_finding_attributes(finding_path)

    if not attributes:
        print("[ERROR] No attributes found to test")
        return

    # Pick the 'presence' choice attribute as the base
    base = next((a for a in attributes if a.get("type") == "choice" and a.get("name", "").lower() == "presence"), None)
    if base is None:
        print("[ERROR] Could not find 'presence' choice attribute in finding")
        return

    # Build scenarios
    import copy
    identical_attr = copy.deepcopy(base)

    expanded_attr = copy.deepcopy(base)
    # Add a new distinct value while preserving originals
    new_index = len(expanded_attr.get("values", []))
    expanded_attr.setdefault("values", []).append({
        "value_code": f"{expanded_attr['oifma_id']}.{new_index}",
        "name": "equivocal",
        "description": "Equivocal/uncertain presence"
    })

    different_attr = {
        "oifma_id": f"{base['oifma_id']}",
        "name": "change from prior",  # Different concept (temporal)
        "type": "choice",
        "description": "Temporal change",
        "values": [
            {"value_code": f"{base['oifma_id']}.100", "name": "unchanged"},
            {"value_code": f"{base['oifma_id']}.101", "name": "increased"},
            {"value_code": f"{base['oifma_id']}.102", "name": "decreased"}
        ],
        "required": False,
        "max_selected": 1
    }

    comparator = AttributeComparator()

    async def run_case(case_name: str, existing_attr, new_attr, expected: str):
        try:
            result = await comparator.compare_attributes(
                existing_attribute=existing_attr,
                new_attribute=new_attr,
                finding_name="abnormal configuration of cerebral ventricles",
                attribute_type="choice"
            )
            print(f"{case_name}: expected={expected}, got={result.relationship} (conf: {result.confidence:.2f})")
            print(f"  Reasoning: {result.reasoning}")
        except Exception as e:
            print(f"{case_name}: ✗ Error: {e}")

    await run_case("IDENTICAL", base, identical_attr, expected="identical")
    await run_case("EXPANDED", base, expanded_attr, expected="expanded")
    await run_case("DIFFERENT", base, different_attr, expected="different")


async def test_adrenal_nodule_cde_vs_hood():
    """Compare HOOD adrenal nodule attributes against synthesized CDE attributes.

    Scenarios on the 'presence' choice attribute:
      - IDENTICAL: CDE presence mirrors HOOD presence (present/absent)
      - EXPANDED: CDE presence adds an extra value while preserving originals
      - DIFFERENT: CDE stability/temporal change attribute vs HOOD presence
    """
    print("\n" + "=" * 60)
    print("ADRENAL NODULE: CDE vs HOOD COMPARISONS")
    print("=" * 60)

    hood_path = Path(__file__).parent.parent.parent / "defs" / "hood_findings" / "adrenal_nodule.fm.json"
    hood_attrs = load_finding_attributes(hood_path)

    if not hood_attrs:
        print("[ERROR] No HOOD attributes found to test")
        return

    # Base: HOOD 'presence'
    base_presence = next((a for a in hood_attrs if a.get("type") == "choice" and a.get("name", "").lower() == "presence"), None)
    if base_presence is None:
        print("[ERROR] HOOD presence attribute not found")
        return

    # Build CDE variants (synthesized values since CDE listing does not include them here)
    import copy
    cde_identical = {
        "oifma_id": "OIFMA_CDE_001987",
        "name": "Presence",
        "type": "choice",
        "values": [
            {"value_code": "OIFMA_CDE_001987.0", "name": "present"},
            {"value_code": "OIFMA_CDE_001987.1", "name": "absent"}
        ],
        "required": True,
        "max_selected": 1
    }

    cde_expanded = copy.deepcopy(cde_identical)
    cde_expanded["values"].append({"value_code": "OIFMA_CDE_001987.2", "name": "indeterminate"})

    cde_different = {
        "oifma_id": "OIFMA_CDE_001988",
        "name": "Stability, compared to priors",
        "type": "choice",
        "values": [
            {"value_code": "OIFMA_CDE_001988.0", "name": "unchanged"},
            {"value_code": "OIFMA_CDE_001988.1", "name": "increased"},
            {"value_code": "OIFMA_CDE_001988.2", "name": "decreased"}
        ],
        "required": True,
        "max_selected": 1
    }

    comparator = AttributeComparator()

    async def run_case(case_name: str, new_attr, expected: str):
        try:
            result = await comparator.compare_attributes(
                existing_attribute=base_presence,
                new_attribute=new_attr,
                finding_name="Adrenal Nodule",
                attribute_type="choice"
            )
            print(f"{case_name}: expected={expected}, got={result.relationship} (conf: {result.confidence:.2f})")
            print(f"  Reasoning: {result.reasoning}")
            if result.merge_strategy:
                print(f"  Merge Strategy: {result.merge_strategy}")
        except Exception as e:
            print(f"{case_name}: ✗ Error: {e}")

    # Run deterministic cases
    await run_case("IDENTICAL", cde_identical, expected="identical")
    await run_case("EXPANDED", cde_expanded, expected="expanded")
    await run_case("DIFFERENT", cde_different, expected="different")


async def test_error_handling():
    """Test error handling with invalid inputs"""
    print("\n" + "=" * 60)
    print("TESTING ERROR HANDLING")
    print("=" * 60)
    
    classifier = AttributeClassifier()
    
    # Test with invalid JSON
    invalid_attributes = [
        {"name": "test", "type": "invalid_type"},  # Invalid type
        {"name": "test"},  # Missing required fields
        {"invalid": "data"},  # Completely invalid structure
    ]
    
    for i, invalid_attr in enumerate(invalid_attributes, 1):
        print(f"\nTesting invalid attribute {i}: {invalid_attr}")
        try:
            result = await classifier.classify_attribute(invalid_attr)
            print(f"[ERROR] Should have failed but got: {result}")
        except Exception as e:
            print(f"[OK] Correctly caught error: {type(e).__name__}: {e}")

async def main():
    """Run all tests"""
    print("Starting Attribute Classifier Tests")
    print("=" * 60)
    
    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("[WARNING] OPENAI_API_KEY not found in environment variables")
        print("   Some tests may fail. Please set your OpenAI API key.")
        print("   You can create a .env file with: OPENAI_API_KEY=your_key_here")
        print()
    
    try:
        await test_classification()
        await test_comparison()
        await test_adrenal_nodule_cde_vs_hood()
        await test_deterministic_comparisons()
        await test_error_handling()
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[ERROR] Test suite failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
