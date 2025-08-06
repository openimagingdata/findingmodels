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
    def _add_value_codes(values: List[Dict], attribute_id: str) -> List[Dict]:
        processed_values = []
        for i, value in enumerate(values):
            processed_value = {
                "value_code": f"{attribute_id}.{i}",
                "name": value["name"]
            }
            
            if "description" in value and value["description"] != value["name"]:
                processed_value["description"] = value["description"]
                
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
        
        # Process attributes
        attributes = []
        for i, attribute in enumerate(hood_data.get("attributes", [])):
            attribute_id = HoodJsonAdapter._generate_attribute_id(filename, attribute["name"], i)
            
            # Create base attribute
            adapted_attr = {
                "oifma_id": attribute_id,
                "name": attribute["name"],
                "description": attribute.get("description", ""),
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

        finding_model = {
            "oifm_id": model_id,
            "name": finding_name.replace("_", " ").title(),
            "description": hood_data["description"],
            "attributes": attributes,
            "contributors": HoodJsonAdapter._create_default_contributors()
        }

        return finding_model

    @staticmethod
    def process_file(input_file: str, output_dir: str) -> bool:
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                hood_data = json.load(f)
            
            filename = Path(input_file).name
            
            finding_model_dict = HoodJsonAdapter.adapt_hood_json(hood_data, filename)
            
            fm = FindingModelFull(**finding_model_dict)
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True))
            
            print(f"Adapted {input_file} -> {output_file}")
            return True
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            return False

    @staticmethod
    def process_directory(input_dir: str, output_dir: str):
        """Process all JSON files in a directory."""
        os.makedirs(output_dir, exist_ok=True)
        
        for filename in os.listdir(input_dir):
            if filename.endswith(".json") and not filename.endswith(".cde.json"):
                input_file = os.path.join(input_dir, filename)
                HoodJsonAdapter.process_file(input_file, output_dir)


def main():
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/hood_findings"
    
    print(f"Adapting hood JSON files from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    HoodJsonAdapter.process_directory(input_dir, output_dir)


if __name__ == "__main__":
    main() 