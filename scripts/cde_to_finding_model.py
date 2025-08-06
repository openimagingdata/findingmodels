import json
import os
from typing import Dict, List, Optional, Union
from pathlib import Path

from findingmodel import FindingModelFull
from findingmodel.common import model_file_name

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
    def _create_oidm_organization() -> Dict:
        """Create the OIDM organization contributor."""
        return {
            "name": "Open Imaging Data Model",
            "code": "OIDM",
            "url": "https://openimagingdata.org"
        }

    @staticmethod
    def _create_cde_contributors(cde_data: Dict) -> List[Dict]:
        """Create contributors for CDE finding models."""
        return [
            {
                "name": "Open Imaging Data Model",
                "code": "OIDM",
                "url": "https://openimagingdata.org"
            }
        ]

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
    def _process_value_set(value_set: Dict, attribute_id: str) -> List[Dict]:
        """Process a value set from CDE to FindingModel format."""
        if not value_set.get("values"):
            return []

        values = []
        for i, value in enumerate(value_set["values"], 0):
            # Generate value code using the attribute_id with zero-based index
            value_code = f"{attribute_id}.{i}"
            
            cde_name = value.get("name", "")
            cde_definition = value.get("definition", "")
            
            fm_name = cde_name
            fm_description = None
            
            # Only include description if definition exists and is different from name (casefolded)
            if cde_definition and cde_definition.lower() != cde_name.lower():
                fm_description = cde_definition

            processed_value = {
                "value_code": value_code,
                "name": fm_name
            }
            
            # Only add description if it exists and is different from name
            if fm_description:
                processed_value["description"] = fm_description
                
            # Add index codes if they exist
            index_codes = CDEToFindingModel._process_index_codes(value.get("index_codes", []))
            if index_codes:
                processed_value["index_codes"] = index_codes
                
            values.append(processed_value)
        return values

    @staticmethod
    def _process_numeric_attribute(element: Dict, attribute_id: str) -> Dict:
        """Process a numeric attribute from CDE to FindingModel format."""
        numeric_value = element.get("float_value", {}) or element.get("integer_value", {})
        
        index_codes = CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        
        description = element.get("definition", "")
        if not description or len(description) < 5:
            description = None  # Use None instead of empty string
        else:
            description = description
        
        return {
            "oifma_id": attribute_id,
            "name": element.get("name", ""),
            "description": description,
            "type": "numeric",
            "minimum": numeric_value.get("min"),
            "maximum": numeric_value.get("max"),
            "unit": numeric_value.get("unit", "unit"),
            "required": False,
            "index_codes": index_codes
        }

    @staticmethod
    def _process_choice_attribute(element: Dict, attribute_id: str) -> Dict:
        """Process a choice attribute from CDE to FindingModel format."""
        value_set = element.get("value_set", {})
        
        max_selected = 1  
        if value_set.get("max_cardinality"):
            max_cardinality = value_set["max_cardinality"]
            if max_cardinality == "all":
                max_selected = "all"
            else:
                try:
                    max_selected = int(max_cardinality)
                except (ValueError, TypeError):
                    max_selected = 1
        
        index_codes = CDEToFindingModel._process_index_codes(element.get("index_codes", []))
        
        description = element.get("definition", "")
        if not description or len(description) < 5:
            description = None  # Use None instead of empty string
        else:
            description = description
        
        return {
            "oifma_id": attribute_id,
            "name": element.get("name", ""),
            "description": description,
            "type": "choice",
            "required": False,
            "max_selected": max_selected,
            "values": CDEToFindingModel._process_value_set(value_set, attribute_id),
            "index_codes": index_codes
        }

    @staticmethod
    def convert_cde(cde_data: Dict) -> Dict:
        """Convert a CDE to FindingModel."""
        model_id = CDEToFindingModel._generate_model_id(cde_data["id"])
        
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
                # Process choice attribute but only add it if it has values
                attribute = CDEToFindingModel._process_choice_attribute(element, attribute_id)
                if attribute.get("values"):  # Only add if it has values
                    attributes.append(attribute)
            elif "integer_value" in element or "float_value" in element:
                attribute = CDEToFindingModel._process_numeric_attribute(element, attribute_id)
                attributes.append(attribute)
            else:
                continue
        
        # If no attributes were created, create a default "Presence" attribute
        if not attributes:
            default_attribute_id = CDEToFindingModel._generate_attribute_id(cde_data["id"], "RDE999")
            attributes = [{
                "oifma_id": default_attribute_id,
                "name": "Presence",
                "description": "Whether the finding is present or absent",
                "type": "choice",
                "required": True,
                "max_selected": 1,
                "values": [
                    {
                        "value_code": f"{default_attribute_id}.0",
                        "name": "Present",
                        "description": "The finding is present"
                    },
                    {
                        "value_code": f"{default_attribute_id}.1", 
                        "name": "Absent",
                        "description": "The finding is absent"
                    }
                ]
            }]

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
            "index_codes": model_index_codes,
            "contributors": CDEToFindingModel._create_cde_contributors(cde_data)
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
    def process_file(input_file: str, output_dir: str) -> bool:
        """Process a single CDE file."""
        try:
            try:
                with open(input_file, "r", encoding="utf-8") as f:
                    cde_data = json.load(f)
            except UnicodeDecodeError:
                try:
                    with open(input_file, "r", encoding="latin-1") as f:
                        cde_data = json.load(f)
                except UnicodeDecodeError:
                    with open(input_file, "r", encoding="cp1252") as f:
                        cde_data = json.load(f)
            
            finding_model_dict = CDEToFindingModel.convert_cde(cde_data)
            
            if not finding_model_dict.get("description") or len(finding_model_dict["description"]) < 5:
                # For the main FindingModel, we need a description of at least 5 characters
                finding_model_dict["description"] = f"Description for {cde_data.get('name', 'finding model')}"
                print(f"Warning: CDE {cde_data['id']} had a missing or short description, using default.")
            
            if not finding_model_dict.get("attributes"):
                print(f"Warning: No attributes found in {input_file}")

            index_codes = finding_model_dict.get("index_codes")
            if index_codes is None or len(index_codes) < 1:
                print(f"Warning: Finding Model does not meet minimum index code requirement of 1")
            
            # Fix numeric attributes
            for attr in finding_model_dict.get("attributes", []):
                if attr.get("type") == "numeric":
                    if attr.get("minimum") is None:
                        attr["minimum"] = 0
                    if attr.get("maximum") is None:
                        attr["maximum"] = 100
                    if not attr.get("unit"):
                        attr["unit"] = "unit"
            
            # Create FindingModelFull object and write using the package
            fm = FindingModelFull(**finding_model_dict)
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            # Ensure output directory exists
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write using the package's method
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True))
                
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
            if CDEToFindingModel.process_file(input_file, output_dir):
                print(f"Processed {filename}")

if __name__ == "__main__":
    main() 