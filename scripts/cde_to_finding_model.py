#!/usr/bin/env python3

import json
import os
from typing import Dict, List, Optional, Union
from pathlib import Path

class CDEToFindingModel:
    @staticmethod
    def _generate_model_id(cde_id: str) -> str:
        """Generate a FindingModel ID from a CDE ID."""
        number = int(cde_id.replace("RDES", ""))
        return f"OIFM_CDE_{number:06d}"

    @staticmethod
    def _generate_attribute_id(cde_id: str, element_id: str) -> str:
        """Generate an attribute ID from a CDE element ID."""
        number = int(element_id.replace("RDE", ""))
        return f"OIFMA_CDE_{number:06d}"

    @staticmethod
    def _create_radelement_code(cde_id: str, name: str) -> Dict:
        """Create a RADELEMENT code for the model."""
        return {
            "system": "RADELEMENT",
            "code": cde_id,
            "display": name.lower()
        }

    @staticmethod
    def _process_index_codes(index_codes: List[Dict]) -> List[Dict]:
        """Process index codes from CDE to FindingModel format."""
        if not index_codes:
            return []
        
        processed_codes = []
        for code in index_codes:
            if isinstance(code, dict):
                processed_code = {
                    "system": code.get("system", ""),
                    "code": code.get("code", ""),
                    "display": code.get("display", "").lower()
                }
                processed_codes.append(processed_code)
        return processed_codes

    @staticmethod
    def _process_body_parts(body_parts: List[Dict]) -> List[Dict]:
        """Process body parts from CDE to FindingModel format."""
        if not body_parts:
            return []
        
        processed_parts = []
        for part in body_parts:
            if isinstance(part, dict):
                processed_part = {
                    "name": part.get("name", ""),
                    "index_codes": CDEToFindingModel._process_index_codes(part.get("index_codes", []))
                }
                processed_parts.append(processed_part)
        return processed_parts

    @staticmethod
    def _is_numeric_value_set(value_set: Dict) -> bool:
        """Check if a value set contains only numeric values."""
        if not value_set.get("values"):
            return False
        return all(str(v.get("value", "")).isdigit() for v in value_set["values"])

    @staticmethod
    def _process_value_set(value_set: Dict, attribute_id: str) -> List[Dict]:
        """Process a value set from CDE to FindingModel format."""
        if not value_set.get("values"):
            return []

        # Skip if it's a numeric-only value set
        if CDEToFindingModel._is_numeric_value_set(value_set):
            return []

        values = []
        for i, value in enumerate(value_set["values"], 1):
            value_code = f"{attribute_id}.{i}"
            name = value.get("name", "")
            definition = value.get("definition", "")
            
            # Skip if definition is same as name
            if definition == name:
                definition = ""

            processed_value = {
                "value_code": value_code,
                "name": name,
                "description": definition,
                "index_codes": CDEToFindingModel._process_index_codes(value.get("index_codes", []))
            }
            values.append(processed_value)
        return values

    @staticmethod
    def _process_numeric_attribute(element: Dict, attribute_id: str) -> Dict:
        """Process a numeric attribute from CDE to FindingModel format."""
        numeric_value = element.get("float_value", {}) or element.get("integer_value", {})
        return {
            "oifma_id": attribute_id,
            "name": element.get("name", ""),
            "description": element.get("definition", ""),
            "type": "numeric",
            "min": numeric_value.get("min"),
            "max": numeric_value.get("max"),
            "step": numeric_value.get("step", 1),
            "unit": numeric_value.get("unit", "unit"),
            "required": False,
            "index_codes": CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        }

    @staticmethod
    def _process_choice_attribute(element: Dict, attribute_id: str) -> Dict:
        """Process a choice attribute from CDE to FindingModel format."""
        value_set = element.get("value_set", {})
        return {
            "oifma_id": attribute_id,
            "name": element.get("name", ""),
            "description": element.get("definition", ""),
            "type": "choice",
            "required": False,
            "values": CDEToFindingModel._process_value_set(value_set, attribute_id),
            "index_codes": CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        }

    @staticmethod
    def convert_cde(cde_data: Dict) -> Dict:
        """Convert a CDE to FindingModel format."""
        model_id = CDEToFindingModel._generate_model_id(cde_data["id"])
        
        # Get body part index codes
        body_part_codes = []
        for part in cde_data.get("body_parts", []):
            if "index_codes" in part:
                body_part_codes.append(part["index_codes"])
        
        # Process attributes
        attributes = []
        for element in cde_data.get("elements", []):
            element_id = element["id"]
            attribute_id = CDEToFindingModel._generate_attribute_id(cde_data["id"], element_id)
            
            if "value_set" in element:
                attribute = CDEToFindingModel._process_choice_attribute(element, attribute_id)
            elif "integer_value" in element or "float_value" in element:
                attribute = CDEToFindingModel._process_numeric_attribute(element, attribute_id)
            else:
                continue
            
            # If attribute has no index codes but we have body part codes, use those
            if not attribute.get("index_codes") and body_part_codes:
                attribute["index_codes"] = CDEToFindingModel._process_index_codes(body_part_codes)
                
            attributes.append(attribute)

        # Create base index codes for the model
        model_index_codes = []
        
        # Add RADELEMENT code
        model_index_codes.append(CDEToFindingModel._create_radelement_code(cde_data["id"], cde_data["name"]))
        
        # Add any existing index codes
        if cde_data.get("index_codes"):
            model_index_codes.extend(CDEToFindingModel._process_index_codes(cde_data["index_codes"]) or [])

        # Create FindingModel
        finding_model = {
            "oifm_id": model_id,
            "name": cde_data["name"],
            "description": cde_data["description"],
            "attributes": attributes,
            "index_codes": model_index_codes,
            "body_parts": CDEToFindingModel._process_body_parts(cde_data.get("body_parts", []))
        }

        # Add body part codes to top-level index_codes
        if body_part_codes:
            for code in body_part_codes:
                if isinstance(code, dict):  # Handle single code object
                    finding_model["index_codes"].append({
                        "system": code["system"],
                        "code": code["code"],
                        "display": code.get("display")
                    })

        return finding_model

    @staticmethod
    def process_file(input_file: str, output_file: str) -> bool:
        """Process a single CDE file."""
        try:
            with open(input_file, "r") as f:
                cde_data = json.load(f)
            
            finding_model = CDEToFindingModel.convert_cde(cde_data)
            
            # Ensure minimum length for string values
            if finding_model.get("description") and len(finding_model["description"]) < 3:
                finding_model["description"] = "No description provided"
            
            # Ensure attributes array is not empty
            if not finding_model.get("attributes"):
                finding_model["attributes"] = [{
                    "oifma_id": f"OIFMA_CDE_{cde_data['id'].replace('RDES', '')}",
                    "name": "Presence",
                    "description": "Whether the finding is present",
                    "type": "choice",
                    "required": True,
                    "values": [
                        {
                            "value_code": f"OIFMA_CDE_{cde_data['id'].replace('RDES', '')}.1",
                            "name": "Present",
                            "description": "The finding is present"
                        },
                        {
                            "value_code": f"OIFMA_CDE_{cde_data['id'].replace('RDES', '')}.2",
                            "name": "Absent",
                            "description": "The finding is absent"
                        }
                    ]
                }]
            
            # Fix numeric attributes
            for attr in finding_model.get("attributes", []):
                if attr.get("type") == "numeric":
                    if attr.get("min") is None:
                        attr["min"] = 0
                    if attr.get("max") is None:
                        attr["max"] = 100
                    if attr.get("step") is None:
                        attr["step"] = 1
                    if not attr.get("unit"):
                        attr["unit"] = "unit"
            
            with open(output_file, "w") as f:
                json.dump(finding_model, f, indent=2)
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            return False
        return True

def main():
    """Main function to process CDE files."""
    # Hardcoded paths
    input_dir = "cdes/definitions"
    output_dir = "defs/new_findings"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process all CDE files
    for filename in os.listdir(input_dir):
        if filename.endswith(".cde.json"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace(".cde.json", ".finding_model.json"))
            if CDEToFindingModel.process_file(input_file, output_file):
                print(f"Processed {filename}")

if __name__ == "__main__":
    main() 