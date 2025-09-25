"""
AAS Test Script

This script demonstrates attribute merging between a MongoDB stub and a full JSON file
using the Acute Aortic Syndrome example.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add the project root to the path
sys.path.append(str(Path(__file__).parent.parent))

from findingmodel.index import Index
from findingmodel import FindingModelFull
from agents.attribute_data_merger import AttributeDataMerger


async def get_stub_from_db(oifm_id: str):
    """Get stub data from MongoDB"""
    index = Index()
    data = await index.index_collection.find_one({"oifm_id": oifm_id})
    return data


def load_full_from_json(file_path: str):
    """Load full data from JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)


async def analyze_and_merge_attributes():
    """Main function to analyze and merge attributes"""
    print("AAS Attribute Merge Test")
    print("=" * 50)
    
    # Step 1: Get stub data from MongoDB
    print("Step 1: Loading stub data from MongoDB...")
    try:
        stub_data = await get_stub_from_db("OIFM_CDE_000126")
        if not stub_data:
            print("ERROR: No stub data found in MongoDB for OIFM_CDE_000126")
            return
        
        print(f"SUCCESS: Loaded stub data for '{stub_data.get('name', 'Unknown')}'")
        print(f"  OIFM ID: {stub_data.get('oifm_id')}")
        print(f"  Stub Attributes: {len(stub_data.get('attributes', []))}")
    except Exception as e:
        print(f"ERROR: Failed to load stub data from MongoDB: {e}")
        return
    
    # Step 2: Load full data from JSON file
    print("\nStep 2: Loading full data from JSON file...")
    try:
        full_data = load_full_from_json("defs/findings_from_cdes/acute_aortic_syndrome.fm.json")
        print(f"SUCCESS: Loaded full data for '{full_data.get('name', 'Unknown')}'")
        print(f"  OIFM ID: {full_data.get('oifm_id')}")
        print(f"  Full Attributes: {len(full_data.get('attributes', []))}")
    except Exception as e:
        print(f"ERROR: Failed to load full data from JSON file: {e}")
        return
    
    # Step 3: Display the findings being compared
    print("\nStep 3: Displaying findings to be compared...")
    
    # Check stub attributes for values
    print("\n" + "=" * 60)
    print("STUB ATTRIBUTES ANALYSIS")
    print("=" * 60)
    stub_attrs = stub_data.get('attributes', [])
    print(f"Total stub attributes: {len(stub_attrs)}")
    
    for i, attr in enumerate(stub_attrs, 1):
        print(f"\n{i}. {attr.get('name', 'Unknown')} ({attr.get('type', 'unknown')})")
        print(f"   ID: {attr.get('attribute_id', 'N/A')}")
        print(f"   Has 'values' field: {'values' in attr}")
        if 'values' in attr:
            print(f"   Values count: {len(attr['values'])}")
            print(f"   Values: {attr['values']}")
        else:
            print("   Values: NOT PRESENT")
        print(f"   All fields: {list(attr.keys())}")
    
    print("\n" + "=" * 60)
    print("STUB FINDING (from MongoDB)")
    print("=" * 60)
    print(json.dumps(stub_data, indent=2, default=str))
    
    print("\n" + "=" * 60)
    print("FULL FINDING (from JSON file)")
    print("=" * 60)
    print(json.dumps(full_data, indent=2, default=str))
    
    # Step 4: Initialize the attribute merger
    print("\nStep 4: Initializing attribute merger...")
    try:
        merger = AttributeDataMerger()
        print("SUCCESS: Attribute merger initialized")
    except Exception as e:
        print(f"ERROR: Failed to initialize attribute merger: {e}")
        return
    
    # Step 5: Run the merge analysis
    print("\nStep 5: Running attribute merge analysis...")
    try:
        merge_result = await merger.merge_attribute_data(stub_data, full_data)
        print("SUCCESS: Merge analysis completed")
        print(f"  Exact Matches Found: {len(merge_result.exact_matches)}")
        print(f"  Unmatched Stub Attributes: {len(merge_result.unmatched_stub_attributes)}")
        print(f"  Unmatched Full Attributes: {len(merge_result.unmatched_full_attributes)}")
    except Exception as e:
        print(f"ERROR: Failed to run merge analysis: {e}")
        return
    
    # Step 6: Create merged attributes
    print("\nStep 6: Creating merged attributes...")
    try:
        merged_attributes = merger.create_merged_attributes(merge_result)
        print(f"SUCCESS: Created {len(merged_attributes)} merged attributes")
    except Exception as e:
        print(f"ERROR: Failed to create merged attributes: {e}")
        return
    
    # Step 7: Display the results
    print("\n" + "=" * 60)
    print("MERGE ANALYSIS RESULTS")
    print("=" * 60)
    
    print(f"\nFinding: {merge_result.finding_name}")
    print(f"Stub Attributes: {merge_result.total_stub_attributes}")
    print(f"Full Attributes: {merge_result.total_full_attributes}")
    print(f"Exact Matches: {len(merge_result.exact_matches)}")
    
    # Display exact matches
    if merge_result.exact_matches:
        print(f"\nEXACT MATCHES:")
        print("-" * 30)
        for i, match in enumerate(merge_result.exact_matches, 1):
            print(f"\n{i}. {match.stub_attribute['name']} ↔ {match.full_attribute['name']}")
            print(f"   Confidence: {match.confidence:.2f}")
            print(f"   Type: {match.stub_attribute.get('type', 'unknown')}")
            print(f"   Stub ID: {match.stub_attribute.get('attribute_id', 'N/A')}")
            print(f"   Full ID: {match.full_attribute.get('oifma_id', 'N/A')}")
            print(f"   Reasoning: {match.reasoning}")
    
    # Display unmatched attributes
    if merge_result.unmatched_stub_attributes:
        print(f"\nUNMATCHED STUB ATTRIBUTES:")
        print("-" * 40)
        for attr in merge_result.unmatched_stub_attributes:
            print(f"  - {attr.get('name', 'Unknown')} ({attr.get('type', 'unknown')})")
    
    if merge_result.unmatched_full_attributes:
        print(f"\nUNMATCHED FULL ATTRIBUTES:")
        print("-" * 40)
        for attr in merge_result.unmatched_full_attributes:
            print(f"  - {attr.get('name', 'Unknown')} ({attr.get('type', 'unknown')})")
    
    # Display the final merged finding
    print(f"\n" + "=" * 60)
    print("FINAL MERGED FINDING")
    print("=" * 60)
    
    print(f"\nFinding Name: {stub_data.get('name')}")
    print(f"OIFM ID: {stub_data.get('oifm_id')}")
    print(f"Description: {stub_data.get('description', 'No description')}")
    print(f"Total Attributes: {len(merged_attributes)}")
    
    print(f"\nMERGED ATTRIBUTES:")
    print("-" * 50)
    
    for i, attr in enumerate(merged_attributes, 1):
        print(f"\n{i}. {attr.get('name', 'Unknown')} ({attr.get('type', 'unknown')})")
        print(f"   ID: {attr.get('attribute_id') or attr.get('oifma_id', 'N/A')}")
        if attr.get('description'):
            print(f"   Description: {attr['description']}")
        print(f"   Required: {attr.get('required', False)}")
        print(f"   Max Selected: {attr.get('max_selected', 1)}")
        
        # Show values for choice attributes
        if attr.get('type') == 'choice' and 'values' in attr:
            print(f"   Values ({len(attr['values'])}):")
            for value in attr['values']:
                value_desc = f" - {value.get('description')}" if value.get('description') else ""
                print(f"     - {value.get('name', 'Unknown')}{value_desc}")
        
        # Show numeric range for numeric attributes
        elif attr.get('type') == 'numeric':
            if 'min_value' in attr or 'max_value' in attr:
                min_val = attr.get('min_value', 'N/A')
                max_val = attr.get('max_value', 'N/A')
                unit = attr.get('unit', '')
                print(f"   Range: {min_val} - {max_val} {unit}")
    
    # Step 8: Validate the merged finding against FindingModelFull schema
    print(f"\n" + "=" * 60)
    print("VALIDATION AGAINST FINDING MODEL SCHEMA")
    print("=" * 60)
    
    try:
        # Create the complete merged finding model
        merged_finding = {
            "oifm_id": stub_data.get('oifm_id'),
            "name": stub_data.get('name'),
            "description": stub_data.get('description'),
            "contributors": full_data.get('contributors', []),  # Use full data contributors (proper format)
            "attributes": merged_attributes
        }
        
        # Add any additional fields from the full data that might be missing. This may overwrite - want to fix?
        if 'synonyms' in full_data and full_data['synonyms']:
            merged_finding['synonyms'] = full_data['synonyms']
        if 'tags' in full_data and full_data['tags']:
            merged_finding['tags'] = full_data['tags']
        if 'index_codes' in full_data and full_data['index_codes']:
            merged_finding['index_codes'] = full_data['index_codes']
        
        print("Attempting to validate merged finding against FindingModelFull schema...")
        
        # Validate against FindingModelFull
        validated_model = FindingModelFull(**merged_finding)
        
        print("✅ SUCCESS: Merged finding validates against FindingModelFull schema!")
        print(f"Validated model name: {validated_model.name}")
        print(f"Validated model OIFM ID: {validated_model.oifm_id}")
        print(f"Validated attributes count: {len(validated_model.attributes)}")
        
        # Print the validated JSON
        print(f"\n" + "=" * 60)
        print("VALIDATED MERGED FINDING (JSON)")
        print("=" * 60)
        
        # Convert to dict and print as JSON
        validated_dict = validated_model.model_dump()
        print(json.dumps(validated_dict, indent=2, default=str))
        
        print(f"\n✅ VALIDATION SUCCESSFUL - Merged finding is valid!")
        
    except Exception as validation_error:
        print(f"❌ VALIDATION FAILED: {validation_error}")
        print(f"Error type: {type(validation_error).__name__}")
        
        # Print the problematic merged finding for debugging
        print(f"\n" + "=" * 60)
        print("PROBLEMATIC MERGED FINDING (for debugging)")
        print("=" * 60)
        print(json.dumps(merged_finding, indent=2, default=str))
        
        # Print detailed validation error
        if hasattr(validation_error, 'errors'):
            print(f"\nDetailed validation errors:")
            for error in validation_error.errors():
                print(f"  - Field: {error.get('loc', 'Unknown')}")
                print(f"    Error: {error.get('msg', 'Unknown error')}")
                print(f"    Input: {error.get('input', 'N/A')}")
                print()
        
        raise ValueError(f"Validation failed: {validation_error}")
    
    # Display summary
    print(f"\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(merge_result.summary)
    
    print(f"\nTest completed successfully!")


async def main():
    """Main execution function"""
    try:
        await analyze_and_merge_attributes()
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
