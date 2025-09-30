#!/usr/bin/env python3
"""
Test script for the attribute classifier agents.
This script tests all three agents with realistic medical attribute examples.
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

# Test data - real medical attributes from hood_findings
TEST_ATTRIBUTES = {
    "presence_attr": {
        "oifma_id": "OIFMA_HOOD_354795",
        "name": "Presence",
        "type": "choice",
        "description": "Presence of pneumothorax.",
        "values": [
            {"value_code": "OIFMA_HOOD_354795.0", "name": "Present"},
            {"value_code": "OIFMA_HOOD_354795.1", "name": "Absent"}
        ],
        "required": True,
        "max_selected": 1
    },
    "status_attr": {
        "oifma_id": "OIFMA_HOOD_268428",
        "name": "Status",
        "type": "choice", 
        "description": "Status of pneumothorax.",
        "values": [
            {"value_code": "OIFMA_HOOD_268428.0", "name": "Acute"},
            {"value_code": "OIFMA_HOOD_268428.1", "name": "Chronic"},
            {"value_code": "OIFMA_HOOD_268428.2", "name": "Resolving"},
            {"value_code": "OIFMA_HOOD_268428.3", "name": "Newly identified"},
            {"value_code": "OIFMA_HOOD_268428.4", "name": "Increased"},
            {"value_code": "OIFMA_HOOD_268428.5", "name": "Decreased"},
            {"value_code": "OIFMA_HOOD_268428.6", "name": "Resolved"},
            {"value_code": "OIFMA_HOOD_268428.7", "name": "Persisting"}
        ],
        "required": True,
        "max_selected": 1
    },
    "size_attr": {
        "oifma_id": "OIFMA_HOOD_219837",
        "name": "Size Finding",
        "type": "choice",
        "description": "Size of pneumothorax.",
        "values": [
            {"value_code": "OIFMA_HOOD_219837.0", "name": "Small (<20% lung volume)"},
            {"value_code": "OIFMA_HOOD_219837.1", "name": "Medium (20-50% lung volume)"},
            {"value_code": "OIFMA_HOOD_219837.2", "name": "Large (>50% lung volume)"},
            {"value_code": "OIFMA_HOOD_219837.3", "name": "Tension"}
        ],
        "required": True,
        "max_selected": 1
    },
    "numeric_attr": {
        "oifma_id": "OIFMA_HOOD_621593",
        "name": "size Finding",
        "type": "numeric",
        "description": "Size of the pulmonary nodule.",
        "minimum": 0,
        "maximum": 100,
        "unit": "mm",
        "required": True
    },
    "morphology_attr": {
        "oifma_id": "OIFMA_HOOD_014138",
        "name": "morphology",
        "type": "choice",
        "description": "Morphology of the pulmonary nodule.",
        "values": [
            {"value_code": "OIFMA_HOOD_014138.0", "name": "solid", "description": "The pulmonary nodule is solid."},
            {"value_code": "OIFMA_HOOD_014138.1", "name": "subsolid", "description": "The pulmonary nodule is subsolid."}
        ],
        "required": True,
        "max_selected": 1
    },
    "location_attr": {
        "oifma_id": "OIFMA_HOOD_408638",
        "name": "Location",
        "type": "choice",
        "description": "Location of pneumothorax.",
        "values": [
            {"value_code": "OIFMA_HOOD_408638.0", "name": "Right"},
            {"value_code": "OIFMA_HOOD_408638.1", "name": "Left"},
            {"value_code": "OIFMA_HOOD_408638.2", "name": "Bilateral"}
        ],
        "required": True,
        "max_selected": 1
    }
}

# Test cases for comparison
COMPARISON_TEST_CASES = [
    {
        "name": "Identical presence attributes",
        "existing": TEST_ATTRIBUTES["presence_attr"],
        "new": TEST_ATTRIBUTES["presence_attr"],
        "finding_name": "pneumothorax",
        "attribute_type": "presence"
    },
    {
        "name": "Enhanced presence attribute (more values)",
        "existing": {
            "oifma_id": "OIFMA_HOOD_786842",
            "name": "presence",
            "type": "choice",
            "description": "Presence of the pulmonary nodule.",
            "values": [
                {"value_code": "OIFMA_HOOD_786842.0", "name": "present", "description": "The pulmonary nodule is present."},
                {"value_code": "OIFMA_HOOD_786842.1", "name": "absent", "description": "The pulmonary nodule is absent."}
            ],
            "required": True,
            "max_selected": 1
        },
        "new": TEST_ATTRIBUTES["presence_attr"],
        "finding_name": "pneumothorax", 
        "attribute_type": "presence"
    },
    {
        "name": "Different attribute types",
        "existing": TEST_ATTRIBUTES["presence_attr"],
        "new": TEST_ATTRIBUTES["size_attr"],
        "finding_name": "pneumothorax",
        "attribute_type": "presence"
    },
    {
        "name": "Status vs Presence comparison",
        "existing": TEST_ATTRIBUTES["presence_attr"],
        "new": TEST_ATTRIBUTES["status_attr"],
        "finding_name": "pneumothorax",
        "attribute_type": "presence"
    }
]

async def test_classification_agent():
    """Test the attribute classification agent"""
    print("=" * 60)
    print("TESTING CLASSIFICATION AGENT")
    print("=" * 60)
    
    classifier = AttributeClassifier()
    
    for attr_name, attribute in TEST_ATTRIBUTES.items():
        print(f"\nTesting {attr_name}:")
        print(f"Attribute: {attribute['name']} ({attribute['type']})")
        
        try:
            result = await classifier.classify_attribute(attribute)
            print(f"[OK] Classification: {result.classification}")
            print(f"[OK] Confidence: {result.confidence:.2f}")
            print(f"[OK] Reasoning: {result.reasoning}")
        except Exception as e:
            print(f"[ERROR] Error: {e}")
        
        print("-" * 40)

async def test_comparison_agent():
    """Test the attribute comparison agent"""
    print("\n" + "=" * 60)
    print("TESTING COMPARISON AGENT")
    print("=" * 60)
    
    comparator = AttributeComparator()
    
    for test_case in COMPARISON_TEST_CASES:
        print(f"\nTesting: {test_case['name']}")
        print(f"Finding: {test_case['finding_name']}")
        print(f"Attribute Type: {test_case['attribute_type']}")
        
        try:
            result = await comparator.compare_attributes(
                existing_attribute=test_case['existing'],
                new_attribute=test_case['new'],
                finding_name=test_case['finding_name'],
                attribute_type=test_case['attribute_type']
            )
            print(f"[OK] Relationship: {result.relationship}")
            print(f"[OK] Confidence: {result.confidence:.2f}")
            print(f"[OK] Reasoning: {result.reasoning}")
            if result.merge_strategy:
                print(f"[OK] Merge Strategy: {result.merge_strategy}")
        except Exception as e:
            print(f"[ERROR] Error: {e}")
        
        print("-" * 40)

async def test_merger_agent():
    """Test the attribute merger agent"""
    print("\n" + "=" * 60)
    print("TESTING MERGER AGENT")
    print("=" * 60)
    
    merger = AttributeMerger()
    
    # Test merging enhanced attributes
    existing = {
        "oifma_id": "OIFMA_HOOD_786842",
        "name": "presence",
        "type": "choice",
        "description": "Presence of the pulmonary nodule.",
        "values": [
            {"value_code": "OIFMA_HOOD_786842.0", "name": "present", "description": "The pulmonary nodule is present."},
            {"value_code": "OIFMA_HOOD_786842.1", "name": "absent", "description": "The pulmonary nodule is absent."}
        ],
        "required": True,
        "max_selected": 1
    }
    
    new = TEST_ATTRIBUTES["presence_attr"]
    merge_strategy = "Combine all unique values from both attributes, keeping the most comprehensive description"
    
    print(f"\nMerging enhanced presence attributes:")
    print(f"Existing: {len(existing['values'])} values")
    print(f"New: {len(new['values'])} values")
    print(f"Strategy: {merge_strategy}")
    
    try:
        result = await merger.merge_attributes(existing, new, merge_strategy)
        print(f"[OK] Merge completed successfully")
        print(f"[OK] Merge notes: {result.merge_notes}")
        print(f"[OK] Merged attribute keys: {list(result.merged_attribute.keys())}")
        
        # Pretty print the merged attribute
        print("\nMerged attribute:")
        print(json.dumps(result.merged_attribute, indent=2))
        
    except Exception as e:
        print(f"[ERROR] Error: {e}")

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
        await test_classification_agent()
        await test_comparison_agent() 
        await test_merger_agent()
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
