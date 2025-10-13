#!/usr/bin/env python3
"""
Debug test for attribute comparison - focuses only on presence attribute comparison
"""

import asyncio
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from agents.attribute_classifier import AttributeComparator

async def test_presence_comparison():
    """Test just the presence attribute comparison"""
    print("=" * 60)
    print("DEBUG: PRESENCE ATTRIBUTE COMPARISON")
    print("=" * 60)
    
    # HOOD presence attribute (simplified)
    hood_presence = {
        "oifma_id": "OIFMA_MGB_981246",
        "name": "presence",
        "type": "choice",
        "values": [
            {"value_code": "OIFMA_MGB_981246.0", "name": "present"},
            {"value_code": "OIFMA_MGB_981246.1", "name": "absent"}
        ],
        "required": True,
        "max_selected": 1
    }
    
    # CDE presence attribute (simplified)
    cde_presence = {
        "oifma_id": "OIFMA_CDE_001987",
        "name": "Presence",
        "type": "choice",
        "values": [
            {"value_code": "OIFMA_CDE_001987.0", "name": "absent"},
            {"value_code": "OIFMA_CDE_001987.1", "name": "present"},
            {"value_code": "OIFMA_CDE_001987.2", "name": "indeterminate"},
            {"value_code": "OIFMA_CDE_001987.3", "name": "unknown"}
        ],
        "required": False,
        "max_selected": 1
    }
    
    print("HOOD presence values:")
    for v in hood_presence["values"]:
        print(f"  - {v['name']}")
    
    print("\nCDE presence values:")
    for v in cde_presence["values"]:
        print(f"  - {v['name']}")
    
    print(f"\nHOOD has {len(hood_presence['values'])} values")
    print(f"CDE has {len(cde_presence['values'])} values")
    
    # Check if CDE is a superset
    hood_values = {v['name'] for v in hood_presence['values']}
    cde_values = {v['name'] for v in cde_presence['values']}
    
    print(f"\nHOOD value set: {hood_values}")
    print(f"CDE value set: {cde_values}")
    print(f"CDE contains all HOOD values: {hood_values.issubset(cde_values)}")
    print(f"CDE has extra values: {cde_values - hood_values}")
    
    print("\n" + "=" * 60)
    print("RUNNING COMPARISON AGENT")
    print("=" * 60)
    
    comparator = AttributeComparator()
    
    try:
        result = await comparator.compare_attributes(
            existing_attribute=hood_presence,
            new_attribute=cde_presence,
            finding_name="Adrenal Nodule",
            attribute_type="choice"
        )
        
        print(f"\n🤖 AI RESULT:")
        print(f"Relationship: {result.relationship}")
        print(f"Confidence: {result.confidence:.2f}")
        print(f"Reasoning: {result.reasoning}")
        
        if result.merge_strategy:
            print(f"Merge Strategy: {result.merge_strategy}")
            
        print(f"\n✅ EXPECTED: 'expanded' (CDE has all HOOD values + extras)")
        print(f"❌ ACTUAL: '{result.relationship}'")
        
        if result.relationship == "expanded":
            print("🎉 SUCCESS: AI correctly identified as expanded!")
        else:
            print("🚨 FAILURE: AI did not identify as expanded")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_presence_comparison())
