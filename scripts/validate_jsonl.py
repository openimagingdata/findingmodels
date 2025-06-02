import os
import json
from collections import defaultdict

# Function to find all JSON files in the 'defs' directory
def find_json_files_in_defs():
    json_files = []
    for root, _, files in os.walk('./defs'):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

# Function to validate OIFM ID collisions
# Ensure oifm_id is unique across all models
def validate_oifm_id_collisions():
    id_map = defaultdict(list)
    json_files = find_json_files_in_defs()

    for file_path in json_files:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                oifm_id = data.get('oifm_id')
                if oifm_id:
                    id_map[oifm_id].append(os.path.basename(file_path))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    collisions = {key: value for key, value in id_map.items() if len(value) > 1}

    if collisions:
        print("Validation failed: Duplicate oifm_id values found.")
        for oifm_id, files in collisions.items():
            print(f"oifm_id: {oifm_id} found in models: [{', '.join(files)}]")
        return 1
    else:
        print("Validation passed: All oifm_id values are unique.")
        return 0

# Function to validate OIFMA ID collisions within attributes -> oifma_id field
def validate_oifma_id_within_attributes():
    json_files = find_json_files_in_defs()
    oifma_ids = defaultdict(list)
    duplicates = defaultdict(list)

    for file_path in json_files:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                attributes = data.get('attributes', [])

                for attribute in attributes:
                    oifma_id = attribute.get('oifma_id')
                    if oifma_id in oifma_ids:
                        duplicates[oifma_id].append(os.path.basename(file_path))
                    else:
                        oifma_ids[oifma_id].append(os.path.basename(file_path))

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if duplicates:
        print("Validation failed: Duplicate oifma_id values found.")
        for oifma_id, files in duplicates.items():
            print(f"Duplicate oifma_id: {oifma_id} found in files: [{', '.join(files)}]")
        return 1
    else:
        print("Validation passed: All oifma_id values are unique.")
        return 0

# Main function to call validation functions and return overall status
def main():
    oifm_status = validate_oifm_id_collisions()
    oifma_status = validate_oifma_id_within_attributes()

    if oifm_status == 0 and oifma_status == 0:
        print("All validations passed successfully.")
        return 0
    else:
        print("Validation errors detected.")
        return 1

# Example usage:
if __name__ == "__main__":
    exit(main())