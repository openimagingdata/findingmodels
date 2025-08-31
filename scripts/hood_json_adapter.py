import json
import os
from typing import Dict, List
from pathlib import Path

from findingmodel import FindingModelFull
from findingmodel.common import model_file_name


class HoodJsonAdapter:
    @staticmethod
    def _generate_model_id(filename: str) -> str:
        import hashlib
        hash_obj = hashlib.md5(filename.encode())
        number = int(hash_obj.hexdigest()[:6], 16) % 999999
        return f"OIFM_HOOD_{number:06d}"

    @staticmethod
    def _generate_attribute_id(filename: str, attribute_name: str, index: int) -> str:
        import hashlib
        combined = f"{filename}_{attribute_name}_{index}"
        hash_obj = hashlib.md5(combined.encode())
        number = int(hash_obj.hexdigest()[:6], 16) % 999999
        return f"OIFMA_HOOD_{number:06d}"

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
            "T0": "T0 Stage",
            "T1": "T1 Stage", 
            "T2": "T2 Stage",
            "T3": "T3 Stage",
            "T4": "T4 Stage",
            "T5": "T5 Stage",
            "T6": "T6 Stage",
            "T7": "T7 Stage",
            "T8": "T8 Stage",
            "T9": "T9 Stage",
            "C1": "C1 Vertebra",
            "C2": "C2 Vertebra",
            "C3": "C3 Vertebra",
            "C4": "C4 Vertebra",
            "C5": "C5 Vertebra",
            "C6": "C6 Vertebra",
            "C7": "C7 Vertebra",
            "L1": "L1 Vertebra",
            "L2": "L2 Vertebra",
            "L3": "L3 Vertebra",
            "L4": "L4 Vertebra",
            "L5": "L5 Vertebra",
            "S1": "S1 Vertebra",
            "S2": "S2 Vertebra",
            "S3": "S3 Vertebra",
            "S4": "S4 Vertebra",
            "S5": "S5 Vertebra",
            "A0": "A0 Stage",
            "A1": "A1 Stage",
            "A2": "A2 Stage",
            "A3": "A3 Stage",
            "A4": "A4 Stage",
            "B1": "B1 Stage",
            "B2": "B2 Stage",
            "B3": "B3 Stage",
            "M1": "M1 Stage",
            "M2": "M2 Stage",
            "M3": "M3 Stage",
            "M4": "M4 Stage",
            "F1": "F1 Stage",
            "F2": "F2 Stage",
            "F3": "F3 Stage",
            "F4": "F4 Stage",
            # Additional medical abbreviations from hood data
            "Cabg": "CABG Surgery",
            "Ipmn": "IPMN Lesion",
            "Picc": "PICC Line",
            "CVC": "Central Venous Catheter",
            "ECMO": "ECMO Cannula",
            "LVAD": "LVAD Device",
            "PFO": "PFO Closure",
            "UIP": "UIP Pattern"
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
            
            # Handle value descriptions - use None for short descriptions like CDE converter
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
            HoodJsonAdapter._create_person()
        ]

    @staticmethod
    def adapt_hood_json(hood_data: Dict, filename: str) -> Dict:
        """Adapt hood JSON format to FindingModel format."""
        finding_name = hood_data["finding_name"]
        model_id = HoodJsonAdapter._generate_model_id(filename)
        
        # Expand short names using the same method as CDE converter
        expanded_finding_name = HoodJsonAdapter._expand_short_name(finding_name)
        if expanded_finding_name != finding_name:
            print(f"  Fixed: Short name '{finding_name}' -> '{expanded_finding_name}'")
        
        # Handle description - main finding description is required, so provide fallback
        description = hood_data.get("description", "")
        if not description or len(description) < 5:
            description = f"Description for {expanded_finding_name}"  # Required field needs fallback
            print(f"  Fixed: Short description -> '{description}'")
        else:
            description = HoodJsonAdapter._truncate_description(description)
        
        # Process attributes
        attributes = []
        for i, attribute in enumerate(hood_data.get("attributes", [])):
            attribute_id = HoodJsonAdapter._generate_attribute_id(filename, attribute["name"], i)
            
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
            
            # Create base attribute
            adapted_attr = {
                "oifma_id": attribute_id,
                "name": attr_name,
                "description": attr_description,
                "type": attribute["type"],
                "required": attribute.get("required", False)
            }
            
            # Handle choice attributes
            if attribute["type"] == "choice":
                adapted_attr["max_selected"] = 1
                adapted_attr["values"] = HoodJsonAdapter._add_value_codes(attribute["values"], attribute_id)
            
            # Handle numeric attributes
            elif attribute["type"] == "numeric":
                adapted_attr["minimum"] = attribute.get("minimum", 0)
                adapted_attr["maximum"] = attribute.get("maximum", 100)
                adapted_attr["unit"] = attribute.get("unit", "unit")
            
            attributes.append(adapted_attr)

        # Add validation warnings
        if not attributes:
            print(f"  Warning: No attributes found in {filename}")
        
        finding_model = {
            "oifm_id": model_id,
            "name": expanded_finding_name.replace("_", " ").title(),
            "description": description,
            "attributes": attributes,
            "contributors": HoodJsonAdapter._create_default_contributors()
        }

        return finding_model

    @staticmethod
    def process_file(input_file: str, output_dir: str) -> bool:
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
            
            finding_model_dict = HoodJsonAdapter.adapt_hood_json(hood_data, filename)
            
            fm = FindingModelFull(**finding_model_dict)
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True), encoding='utf-8')
            
            print(f"Adapted {filename} -> {output_file.name}")
            return True
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            return False

    @staticmethod
    def process_directory(input_dir: str, output_dir: str):
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
                if HoodJsonAdapter.process_file(input_file, output_dir):
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


def main():
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/hood_findings"
    
    print(f"Adapting hood JSON files from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    HoodJsonAdapter.process_directory(input_dir, output_dir)


if __name__ == "__main__":
    main() 