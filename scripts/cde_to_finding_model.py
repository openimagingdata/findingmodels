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
        """Create a RADELEMENT code reference to the original CDE"""
        return {
            "system": "RADELEMENT",
            "code": cde_id,
            "display": name.lower()
        }

    @staticmethod
    def _process_index_codes(index_codes: List[Dict]) -> Optional[List[Dict]]:
        """Process index codes from CDE to FindingModel format."""
        if not index_codes:
            return None
        
        processed_codes = []
        for code in index_codes:
            if isinstance(code, dict):
                processed_code = {
                    "system": code.get("system", ""),
                    "code": code.get("code", ""),
                    "display": code.get("display", "").lower()
                }
                processed_codes.append(processed_code)
        return processed_codes if processed_codes else None

    @staticmethod
    def _process_body_parts(body_parts: List[Dict]) -> List[Dict]:
        """Process body parts from CDE to FindingModel to be placed at the top level of finding model."""
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
        for i, value in enumerate(value_set["values"], 0):
            # Generate value code using the attribute_id (not the CDE value code)
            # This ensures consistency with the attribute ID
            value_code = f"{attribute_id}.{i:02d}"
            
            cde_name = value.get("name", "")
            cde_value = value.get("value", "")
            cde_definition = value.get("definition", "")
            
            # Handle the complex name/description logic
            if cde_value and cde_name:
                # Both value and name are defined: put value in name, name in description
                fm_name = cde_value
                fm_description = cde_name
                if cde_definition and cde_definition != cde_name:
                    fm_description = f"{cde_name}: {cde_definition}"
            elif cde_value:
                # Only value is defined: use value as name
                fm_name = cde_value
                fm_description = cde_definition if cde_definition != cde_value else ""
            else:
                # Only name is defined (or neither): use name as name
                fm_name = cde_name
                fm_description = cde_definition if cde_definition != cde_name else ""

            processed_value = {
                "value_code": value_code,
                "name": fm_name,
                "description": fm_description,
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
            "minimum": numeric_value.get("min"),
            "maximum": numeric_value.get("max"),
            "unit": numeric_value.get("unit", "unit"),
            "required": False,
            "index_codes": CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        }

    @staticmethod
    def _process_choice_attribute(element: Dict, attribute_id: str) -> Dict:
        """Process a choice attribute from CDE to FindingModel format."""
        value_set = element.get("value_set", {})
        
        # Get max_selected from value_set cardinality
        max_selected = 1  # default
        if value_set.get("max_cardinality"):
            max_cardinality = value_set["max_cardinality"]
            if max_cardinality == "all":
                max_selected = "all"
            else:
                try:
                    max_selected = int(max_cardinality)
                except (ValueError, TypeError):
                    max_selected = 1
        
        return {
            "oifma_id": attribute_id,
            "name": element.get("name", ""),
            "description": element.get("definition", ""),
            "type": "choice",
            "required": False,
            "max_selected": max_selected,
            "values": CDEToFindingModel._process_value_set(value_set, attribute_id),
            "index_codes": CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        }

    @staticmethod
    def convert_cde(cde_data: Dict) -> Dict:
        """Convert a CDE to FindingModel."""
        model_id = CDEToFindingModel._generate_model_id(cde_data["id"])
        
        # Get body part index codes - handle both single objects and arrays
        body_part_codes = []
        for part in cde_data.get("body_parts", []):
            if "index_codes" in part:
                index_codes = part["index_codes"]
                if isinstance(index_codes, dict):
                    # Single index code object
                    body_part_codes.append(index_codes)
                elif isinstance(index_codes, list):
                    # Array of index codes
                    body_part_codes.extend(index_codes)
        
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
            
            # Only add body part codes to attributes if the element itself has index codes
            # Body part codes should only be at the top level, not copied to individual attributes
            attributes.append(attribute)

        # Initialize index codes
        model_index_codes = []
        
        # Add RADELEMENT code
        model_index_codes.append(CDEToFindingModel._create_radelement_code(cde_data["id"], cde_data["name"]))
        
        # Add any existing index codes
        if cde_data.get("index_codes"):
            existing_codes = CDEToFindingModel._process_index_codes(cde_data["index_codes"])
            if existing_codes:
                model_index_codes.extend(existing_codes)

        # Create FindingModel - REMOVE body_parts from output
        finding_model = {
            "oifm_id": model_id,
            "name": cde_data["name"],
            "description": cde_data["description"],
            "attributes": attributes,
            "index_codes": model_index_codes
        }

        # Add body part codes to top-level index_codes
        if body_part_codes:
            for code in body_part_codes:
                if isinstance(code, dict):
                    finding_model["index_codes"].append({
                        "system": code["system"],
                        "code": code["code"],
                        "display": code.get("display", "").lower()
                    })

        return finding_model

    @staticmethod
    def process_file(input_file: str, output_file: str) -> bool:
        """Process a single CDE file."""
        try:
            with open(input_file, "r") as f:
                cde_data = json.load(f)
            
            finding_model = CDEToFindingModel.convert_cde(cde_data)
            
            if not finding_model.get("description") or len(finding_model["description"]) < 5:
                print(f"Warning: CDE {cde_data['id']} has a missing or short description.")
            
            # Alert no attributes created 
            if not finding_model.get("attributes"):
                print(f"Warning: No attributes found in {input_file}")

            index_codes = finding_model.get("index_codes")
            if index_codes is None or len(index_codes) < 1:
                print(f"Warning: Finding Model does not meet minimum index code requirement of 1")
            
            # Fix numeric attributes
            for attr in finding_model.get("attributes", []):
                if attr.get("type") == "numeric":
                    if attr.get("minimum") is None:
                        attr["minimum"] = 0
                    if attr.get("maximum") is None:
                        attr["maximum"] = 100
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