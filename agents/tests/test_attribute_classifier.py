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

async def test_adrenal_nodule_classification():
    """Test attribute classification for both HOOD and CDE adrenal nodule findings"""
    print("=" * 60)
    print("ADRENAL NODULE CLASSIFICATION TEST (HOOD vs CDE)")
    print("=" * 60)

    hood_path = Path(__file__).parent.parent.parent / "defs" / "hood_findings" / "adrenal_nodule.fm.json"
    cde_path = Path(__file__).parent.parent.parent / "defs" / "findings_from_cdes" / "adrenal_nodule.fm.json"

    hood_attrs = load_finding_attributes(hood_path)
    cde_attrs = load_finding_attributes(cde_path)

    classifier = AttributeClassifier()

    # HOOD section
    print("\n--- HOOD FINDING: adrenal_nodule.fm.json ---")
    if not hood_attrs:
        print("[ERROR] No HOOD attributes found to test")
    else:
        for i, attribute in enumerate(hood_attrs, 1):
            print(f"\n[HOOD] Attribute {i}: {attribute['name']}")
            print(f"Type: {attribute['type']} | Values: {len(attribute.get('values', []))}")
            try:
                result = await classifier.classify_attribute(attribute, "Adrenal Nodule")
                print(f"✓ Classification: {result.classification} (confidence: {result.confidence:.2f})")
                print(f"  Reasoning: {result.reasoning}")
            except Exception as e:
                print(f"✗ Error: {e}")
            print("-" * 40)

    # CDE section
    print("\n--- CDE FINDING: adrenal_nodule.fm.json ---")
    if not cde_attrs:
        print("[ERROR] No CDE attributes found to test")
    else:
        for i, attribute in enumerate(cde_attrs, 1):
            print(f"\n[CDE] Attribute {i}: {attribute['name']}")
            print(f"Type: {attribute['type']} | Values: {len(attribute.get('values', []))}")
            try:
                result = await classifier.classify_attribute(attribute, "Adrenal Nodule")
                print(f"✓ Classification: {result.classification} (confidence: {result.confidence:.2f})")
                print(f"  Reasoning: {result.reasoning}")
            except Exception as e:
                print(f"✗ Error: {e}")
            print("-" * 40)


async def test_adrenal_nodule_cde_vs_hood():
    """Compare presence attributes between CDE and HOOD adrenal nodule findings."""
    print("\n" + "=" * 60)
    print("ADRENAL NODULE: PRESENCE ATTRIBUTE COMPARISON")
    print("=" * 60)

    # Load both finding files
    hood_path = Path(__file__).parent.parent.parent / "defs" / "hood_findings" / "adrenal_nodule.fm.json"
    cde_path = Path(__file__).parent.parent.parent / "defs" / "findings_from_cdes" / "adrenal_nodule.fm.json"
    
    hood_attrs = load_finding_attributes(hood_path)
    cde_attrs = load_finding_attributes(cde_path)

    if not hood_attrs or not cde_attrs:
        print("[ERROR] Could not load one or both finding files")
        return

    comparator = AttributeComparator()

    # Find presence attributes
    hood_presence = next((attr for attr in hood_attrs if attr.get("name", "").lower() == "presence"), None)
    cde_presence = next((attr for attr in cde_attrs if attr.get("name", "").lower() == "presence"), None)
    
    if not hood_presence or not cde_presence:
        print("[ERROR] Could not find presence attributes in one or both findings")
        return

    print("--- PRESENCE ATTRIBUTE COMPARISON ---")
    print(f"HOOD values: {[v['name'] for v in hood_presence.get('values', [])]}")
    print(f"CDE values: {[v['name'] for v in cde_presence.get('values', [])]}")
    print()
    
    # Debug: Show full attribute structures
    print("DEBUG - Full HOOD attribute:")
    print(f"  Name: {hood_presence.get('name')}")
    print(f"  Type: {hood_presence.get('type')}")
    print(f"  Description: {hood_presence.get('description', 'None')}")
    print(f"  Required: {hood_presence.get('required')}")
    print(f"  Max selected: {hood_presence.get('max_selected')}")
    print(f"  Values: {[v.get('name') for v in hood_presence.get('values', [])]}")
    print()
    
    print("DEBUG - Full CDE attribute:")
    print(f"  Name: {cde_presence.get('name')}")
    print(f"  Type: {cde_presence.get('type')}")
    print(f"  Description: {cde_presence.get('description', 'None')}")
    print(f"  Required: {cde_presence.get('required')}")
    print(f"  Max selected: {cde_presence.get('max_selected')}")
    print(f"  Values: {[v.get('name') for v in cde_presence.get('values', [])]}")
    print()
    
    try:
        result = await comparator.compare_attributes(
            existing_attribute=hood_presence,
            new_attribute=cde_presence,
            finding_name="Adrenal Nodule",
            attribute_type="choice"
        )
        print(f"✓ Relationship: {result.relationship} (confidence: {result.confidence:.2f})")
        print(f"  Reasoning: {result.reasoning}")
        if result.merge_strategy:
            print(f"  Merge Strategy: {result.merge_strategy}")
    except Exception as e:
        print(f"✗ Error: {e}")


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
        await test_adrenal_nodule_classification()
        await test_adrenal_nodule_cde_vs_hood()
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[ERROR] Test suite failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())