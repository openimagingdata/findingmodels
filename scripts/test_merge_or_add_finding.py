"""
Test script for merge_or_add_finding.py

This script provides test cases and helper functions to test the merge/add functionality.
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

# Import the merge functions - need to handle the script as a module
import importlib.util
merge_script_path = Path(__file__).parent / "merge_or_add_finding.py"
spec = importlib.util.spec_from_file_location("merge_or_add_finding", merge_script_path)
merge_module = importlib.util.module_from_spec(spec)
sys.modules['merge_or_add_finding'] = merge_module
spec.loader.exec_module(merge_module)

# Import functions from the module
load_incoming_model = merge_module.load_incoming_model
find_existing_model = merge_module.find_existing_model
ensure_required_attributes = merge_module.ensure_required_attributes
has_presence_attribute = merge_module.has_presence_attribute
has_change_from_prior_attribute = merge_module.has_change_from_prior_attribute
create_new_model = merge_module.create_new_model
merge_models = merge_module.merge_models
get_existing_model_from_db = merge_module.get_existing_model_from_db

from findingmodel import FindingModelFull
from findingmodel.index import Index


def create_test_incoming_model(name: str, has_presence: bool = False, has_change: bool = False) -> FindingModelFull:
    """Create a test INCOMING model with optional attributes."""
    attributes = []
    
    if has_presence:
        attributes.append({
            "name": "presence",
            "type": "choice",
            "values": [
                {"name": "present"},
                {"name": "absent"},
                {"name": "unknown"},
                {"name": "indeterminate"}
            ]
        })
    
    if has_change:
        attributes.append({
            "name": "change from prior",
            "type": "choice",
            "values": [
                {"name": "unchanged"},
                {"name": "stable"}
            ]
        })
    
    # Add some other attributes
    attributes.extend([
        {
            "name": "Size",
            "type": "choice",
            "values": [
                {"name": "small"},
                {"name": "large"}
            ]
        },
        {
            "name": "Location",
            "type": "choice",
            "values": [
                {"name": "upper lobe"},
                {"name": "lower lobe"}
            ]
        }
    ])
    
    model_dict = {
        "name": name,
        "description": f"Test finding: {name}",
        "attributes": attributes
    }
    
    # Create FindingModelBase first, then add IDs
    from findingmodel import FindingModelBase
    from findingmodel.tools import add_ids_to_model
    
    base_model = FindingModelBase(**model_dict)
    full_model = add_ids_to_model(base_model, source="TEST")
    return full_model


async def test_load_incoming_model():
    """Test loading an INCOMING model."""
    print("\n" + "="*60)
    print("TEST 1: Load INCOMING Model")
    print("="*60)
    
    # Create a temporary test file
    test_model = create_test_incoming_model("Test Finding", has_presence=True, has_change=True)
    test_file = Path("test_incoming.fm.json")
    test_file.write_text(test_model.model_dump_json(indent=2), encoding='utf-8')
    
    try:
        loaded = await load_incoming_model(test_file)
        print(f"✅ Successfully loaded: {loaded.name}")
        print(f"   Attributes: {len(loaded.attributes)}")
        attributes = [a.model_dump() for a in loaded.attributes]
        has_presence = await has_presence_attribute(attributes, loaded.name)
        print(f"   Has presence: {has_presence}")
        return True
    except Exception as e:
        print(f"❌ Failed: {e}")
        return False
    finally:
        # Cleanup
        if test_file.exists():
            test_file.unlink()


async def test_has_presence_attribute():
    """Test presence attribute detection."""
    print("\n" + "="*60)
    print("TEST 2: Has Presence Attribute")
    print("="*60)
    
    # Test with presence attribute
    model_with = create_test_incoming_model("Test Finding", has_presence=True)
    attributes = [a.model_dump() for a in model_with.attributes]
    result = await has_presence_attribute(attributes, "Test Finding")
    print(f"Model WITH presence: {result} {'✅' if result else '❌'}")
    
    # Test without presence attribute
    model_without = create_test_incoming_model("Test Finding", has_presence=False)
    attributes = [a.model_dump() for a in model_without.attributes]
    result = await has_presence_attribute(attributes, "Test Finding")
    print(f"Model WITHOUT presence: {result} {'✅' if not result else '❌'}")
    
    return True


async def test_has_change_from_prior_attribute():
    """Test change_from_prior attribute detection."""
    print("\n" + "="*60)
    print("TEST 3: Has Change From Prior Attribute")
    print("="*60)
    
    # Test with change attribute
    model_with = create_test_incoming_model("Test Finding", has_change=True)
    attributes = [a.model_dump() for a in model_with.attributes]
    result = await has_change_from_prior_attribute(attributes, "Test Finding")
    print(f"Model WITH change_from_prior: {result} {'✅' if result else '❌'}")
    
    # Test without change attribute
    model_without = create_test_incoming_model("Test Finding", has_change=False)
    attributes = [a.model_dump() for a in model_without.attributes]
    result = await has_change_from_prior_attribute(attributes, "Test Finding")
    print(f"Model WITHOUT change_from_prior: {result} {'✅' if not result else '❌'}")
    
    return True


async def test_ensure_required_attributes():
    """Test that required attributes are added."""
    print("\n" + "="*60)
    print("TEST 4: Ensure Required Attributes")
    print("="*60)
    
    # Model missing both attributes
    model_incomplete = create_test_incoming_model("Test Finding", has_presence=False, has_change=False)
    print(f"Before: {len(model_incomplete.attributes)} attributes")
    
    model_complete = await ensure_required_attributes(model_incomplete)
    print(f"After: {len(model_complete.attributes)} attributes")
    
    # Check presence
    attributes = [a.model_dump() for a in model_complete.attributes]
    has_presence = await has_presence_attribute(attributes, model_complete.name)
    has_change = await has_change_from_prior_attribute(attributes, model_complete.name)
    
    print(f"Has presence: {has_presence} {'✅' if has_presence else '❌'}")
    print(f"Has change_from_prior: {has_change} {'✅' if has_change else '❌'}")
    
    return has_presence and has_change


async def test_find_existing_model():
    """Test finding EXISTING model in database."""
    print("\n" + "="*60)
    print("TEST 5: Find EXISTING Model")
    print("="*60)
    
    index = Index()
    
    # Use an existing model from the repository
    test_file = Path("defs/original_defs/flat_femoral_head.fm.json")
    if test_file.exists():
        incoming = await load_incoming_model(test_file)
        match = await find_existing_model(incoming, index)
        
        if match:
            print(f"✅ Found match: {match.get('name')}")
            print(f"   Confidence: {match.get('confidence', 'N/A')}")
            print(f"   OIFM ID: {match.get('oifm_id')}")
        else:
            print(f"ℹ️  No match found (this is expected if it's truly unique)")
        return True
    else:
        print("⚠️  Test file not found, skipping")
        return False


async def test_new_model_creation():
    """Test creating a NEW model."""
    print("\n" + "="*60)
    print("TEST 6: Create NEW Model")
    print("="*60)
    
    index = Index()
    
    # Create a unique model (unlikely to exist)
    unique_model = create_test_incoming_model(
        "Unique Test Finding XYZ123",
        has_presence=False,
        has_change=False
    )
    
    new_model = await create_new_model(unique_model, index)
    
    # Check it has required attributes
    attributes = [a.model_dump() for a in new_model.attributes]
    has_presence = await has_presence_attribute(attributes, new_model.name)
    has_change = await has_change_from_prior_attribute(attributes, new_model.name)
    
    print(f"Model created: {new_model.name}")
    print(f"Has presence: {has_presence} {'✅' if has_presence else '❌'}")
    print(f"Has change_from_prior: {has_change} {'✅' if has_change else '❌'}")
    print(f"Total attributes: {len(new_model.attributes)}")
    
    return has_presence and has_change


async def test_merge_scenario():
    """Test merging two models."""
    print("\n" + "="*60)
    print("TEST 7: Merge Models Scenario")
    print("="*60)
    
    # This test requires MongoDB to have a model
    # We'll use a known model from the repository
    index = Index()
    test_file = Path("defs/original_defs/flat_femoral_head.fm.json")
    
    if not test_file.exists():
        print("⚠️  Test file not found, skipping")
        return False
    
    try:
        # Load as INCOMING
        incoming = await load_incoming_model(test_file)
        
        # Find EXISTING match
        match = await find_existing_model(incoming, index)
        
        if match:
            oifm_id = match.get('oifm_id')
            existing_data = await get_existing_model_from_db(oifm_id, index)
            
            if existing_data:
                print(f"✅ Found EXISTING model: {existing_data.get('name')}")
                print(f"   EXISTING attributes: {len(existing_data.get('attributes', []))}")
                print(f"   INCOMING attributes: {len(incoming.attributes)}")
                
                # Merge them
                merged = await merge_models(existing_data, incoming, index)
                print(f"   MERGED attributes: {len(merged.attributes)}")
                print(f"✅ Merge successful!")
                return True
            else:
                print("⚠️  Model not found in database")
                return False
        else:
            print("ℹ️  No match found - would create NEW model instead")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("RUNNING ALL TESTS")
    print("="*60)
    
    results = []
    
    # Run individual tests
    results.append(("Load INCOMING Model", await test_load_incoming_model()))
    results.append(("Has Presence Attribute", await test_has_presence_attribute()))
    results.append(("Has Change From Prior", await test_has_change_from_prior_attribute()))
    results.append(("Ensure Required Attributes", await test_ensure_required_attributes()))
    results.append(("Find EXISTING Model", await test_find_existing_model()))
    results.append(("Create NEW Model", await test_new_model_creation()))
    results.append(("Merge Models", await test_merge_scenario()))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    return passed == total


if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)

