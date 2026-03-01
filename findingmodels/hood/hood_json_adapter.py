import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from dotenv import load_dotenv
from findingmodel import FindingModelFull, FindingModelBase
from findingmodel.common import model_file_name
from findingmodel.tools import add_ids_to_model
from findingmodel_ai.authoring import create_info_from_name

# Load environment variables from .env file
load_dotenv()


class HoodJsonAdapter:

    @staticmethod
    def _truncate_description(description: str, max_length: int = 500) -> str:
        """Truncate description to max_length-4 characters and add '...' if needed."""
        if not description or len(description) <= max_length:
            return description
        
        # Truncate to max_length-4 and add "..."
        return description[:max_length-4] + "..."
    
    @staticmethod
    def _expand_short_name(name: str) -> str:
        """Expand short names to be more descriptive while maintaining medical meaning."""
        # Common medical abbreviations that need expansion
        expansions = {
            "T0": "T0 stage",
            "T1": "T1 stage", 
            "T2": "T2 stage",
            "T3": "T3 stage",
            "T4": "T4 stage",
            "T5": "T5 stage",
            "T6": "T6 stage",
            "T7": "T7 stage",
            "T8": "T8 stage",
            "T9": "T9 stage",
            "C1": "C1 vertebra",
            "C2": "C2 vertebra",
            "C3": "C3 vertebra",
            "C4": "C4 vertebra",
            "C5": "C5 vertebra",
            "C6": "C6 vertebra",
            "C7": "C7 vertebra",
            "L1": "L1 vertebra",
            "L2": "L2 vertebra",
            "L3": "L3 vertebra",
            "L4": "L4 vertebra",
            "L5": "L5 vertebra",
            "S1": "S1 vertebra",
            "S2": "S2 vertebra",
            "S3": "S3 vertebra",
            "S4": "S4 vertebra",
            "S5": "S5 vertebra",
            "A0": "A0 stage",
            "A1": "A1 stage",
            "A2": "A2 stage",
            "A3": "A3 stage",
            "A4": "A4 stage",
            "B1": "B1 stage",
            "B2": "B2 stage",
            "B3": "B3 stage",
            "M1": "M1 stage",
            "M2": "M2 stage",
            "M3": "M3 stage",
            "M4": "M4 stage",
            "F1": "F1 stage",
            "F2": "F2 stage",
            "F3": "F3 stage",
            "F4": "F4 stage",
            "Cabg": "CABG surgery",
            "Ipmn": "IPMN lesion",
            "Picc": "PICC line",
            "CVC": "central venous catheter",
            "ECMO": "ECMO cannula",
            "LVAD": "LVAD device",
            "PFO": "PFO closure",
            "UIP": "UIP pattern"
        }
        
        # Check if name needs expansion
        if name in expansions:
            return expansions[name]
        
        # If name is too short but not in our expansion list, add "Value" suffix
        if len(name) < 3:
            return f"{name} Value"
        
        # If name is still too short for schema requirements (< 5 chars), add "Finding" suffix
        if len(name) < 5:
            return f"{name} Finding"
        
        return name

    @staticmethod
    def _add_value_codes(values: List[Dict], attribute_id: str) -> List[Dict]:
        processed_values = []
        for i, value in enumerate(values):
            processed_value = {
                "value_code": f"{attribute_id}.{i}",
                "name": value["name"]
            }
            
            # Handle value descriptions - use None for short descriptions
            if "description" in value and value["description"] != value["name"]:
                value_description = value["description"]
                # Only include if description is meaningful (≥5 chars)
                if value_description and len(value_description) >= 5:
                    processed_value["description"] = value_description
                
            processed_values.append(processed_value)
        return processed_values

    @staticmethod
    def _create_oidm_organization() -> Dict:
        return {
            "name": "Open Imaging Data Model",
            "code": "OIDM",
            "url": "https://openimagingdata.org"
        }

    @staticmethod
    def _create_mgb_organization() -> Dict:
        return {"name": "Massachusetts General Brigham", "code": "MGB"}

    @staticmethod
    def _create_person() -> Dict:
        return {
            "github_username": "hoodcm",
            "email": "chood@mgh.harvard.edu",
            "name": "C. Michael Hood, MD",
            "organization_code": "MGB"
        }

    @staticmethod
    def _create_default_contributors() -> List[Dict]:
        return [
            HoodJsonAdapter._create_oidm_organization(),
            HoodJsonAdapter._create_mgb_organization(),
            HoodJsonAdapter._create_person()
        ]

    @staticmethod
    async def adapt_hood_json(hood_data: Dict, filename: str) -> FindingModelFull:
        finding_name = hood_data["finding_name"]
        
        # Expand short names using the same method as CDE converter
        expanded_finding_name = HoodJsonAdapter._expand_short_name(finding_name)
        if expanded_finding_name != finding_name:
            print(f"  Fixed: Short name '{finding_name}' -> '{expanded_finding_name}'")
        
        # Handle description - use create_info_from_name if description is too short
        description = hood_data.get("description", "")
        if not description or len(description) < 5:
            try:
                finding_info = await create_info_from_name(expanded_finding_name)
                description = finding_info.description
                print(f"  Generated description for '{expanded_finding_name}': {description[:100]}...")
            except Exception as e:
                print(f"  Warning: Could not generate description for '{expanded_finding_name}': {e}")
                description = f"Description for {expanded_finding_name}"
        else:
            description = HoodJsonAdapter._truncate_description(description)
        
        # Create a basic finding model dict first
        finding_model_dict = {
            "name": expanded_finding_name.replace("_", " ").title(),
            "description": description,
            "attributes": [],
            "contributors": HoodJsonAdapter._create_default_contributors()
        }
        
        # Process attributes and \ them to the dict
        for i, attribute in enumerate(hood_data.get("attributes", [])):
            # Expand short attribute names using the same method as CDE converter
            attr_name = HoodJsonAdapter._expand_short_name(attribute["name"])
            if attr_name != attribute["name"]:
                print(f"  Fixed: Short attribute name '{attribute['name']}' -> '{attr_name}'")
            
            # Handle attribute description like CDE converter - use None for short descriptions
            attr_description = attribute.get("description", "")
            if not attr_description or len(attr_description) < 5:
                attr_description = None  # Let schema handle it like CDE converter
                print(f"  Fixed: Short attribute description -> None (will use schema default)")
            else:
                attr_description = HoodJsonAdapter._truncate_description(attr_description)
            
            # Create base attribute dict
            adapted_attr = {
                "name": attr_name,
                "description": attr_description,
                "type": attribute["type"],
                "required": attribute.get("required", False)
            }
            
            # Handle choice attributes
            if attribute["type"] == "choice":
                adapted_attr["max_selected"] = 1
                # Process values without IDs first
                processed_values = []
                for value in attribute["values"]:
                    processed_value = {
                        "name": value["name"]
                    }
                    if "description" in value and value["description"] != value["name"]:
                        value_description = value["description"]
                        if value_description and len(value_description) >= 5:
                            processed_value["description"] = value_description
                    processed_values.append(processed_value)
                adapted_attr["values"] = processed_values
            
            # Handle numeric attributes
            elif attribute["type"] == "numeric":
                adapted_attr["minimum"] = attribute.get("minimum", 0)
                adapted_attr["maximum"] = attribute.get("maximum", 100)
                adapted_attr["unit"] = attribute.get("unit", "unit")
            
            finding_model_dict["attributes"].append(adapted_attr)

        # Add validation warnings
        if not finding_model_dict["attributes"]:
            print(f"  Warning: No attributes found in {filename}")
        
        # Create FindingModelBase first, then add IDs using the built-in tool
        from findingmodel import FindingModelBase
        base_model = FindingModelBase(**finding_model_dict)
        
        # Use the built-in tool to add IDs
        full_model = add_ids_to_model(base_model, source="MGB")
        
        return full_model

    @staticmethod
    async def process_file(input_file: str, output_dir: str) -> bool:
        try:
            # Try multiple encodings to handle Unicode issues
            try:
                with open(input_file, "r", encoding="utf-8") as f:
                    hood_data = json.load(f)
            except UnicodeDecodeError:
                try:
                    with open(input_file, "r", encoding="latin-1") as f:
                        hood_data = json.load(f)
                except UnicodeDecodeError:
                    with open(input_file, "r", encoding="cp1252") as f:
                        hood_data = json.load(f)
            
            filename = Path(input_file).name
            
            fm = await HoodJsonAdapter.adapt_hood_json(hood_data, filename)
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True), encoding='utf-8')
            
            print(f"Adapted {filename} -> {output_file.name}")
            return True
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            return False

    @staticmethod
    async def process_directory(input_dir: str, output_dir: str):
        """Process all JSON files in a directory."""
        os.makedirs(output_dir, exist_ok=True)
        
        # Track success and failure counts
        successful_count = 0
        failed_count = 0
        total_files = 0
        overwrite_count = 0
        
        print(f"Starting to process files in: {input_dir}")
        print("="*60)
        
        for filename in os.listdir(input_dir):
            if filename.endswith(".json") and not filename.endswith(".cde.json"):
                total_files += 1
                input_file = os.path.join(input_dir, filename)
                
                print(f"Processing {filename}...")
                if await HoodJsonAdapter.process_file(input_file, output_dir):
                    successful_count += 1
                else:
                    failed_count += 1
                    print(f"Failed to process {filename}")
        
        # Count unique output files generated
        unique_output_files = len([f for f in os.listdir(output_dir) if f.endswith('.fm.json')])
        
        # Print summary
        print("\n" + "="*60)
        print("PROCESSING SUMMARY")
        print("="*60)
        print(f"Total hood JSON files found: {total_files}")
        print(f"Successfully adapted: {successful_count}")
        print(f"Failed to adapt: {failed_count}")
        print(f"Success rate: {(successful_count/total_files*100):.1f}%" if total_files > 0 else "Success rate: N/A")
        print(f"Unique finding models generated: {unique_output_files}")
        print(f"Files overwritten: {successful_count - unique_output_files}")
        print("="*60)
        print("Processing complete!")


async def main():
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/hood_findings"
    
    print(f"Adapting hood JSON files from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    await HoodJsonAdapter.process_directory(input_dir, output_dir)


if __name__ == "__main__":
    asyncio.run(main())
