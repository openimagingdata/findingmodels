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
def validate_oifm_id_collisions():
    id_map = defaultdict(list)
    json_files = find_json_files_in_defs()

    for file_path in json_files:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                oifm_id = data.get('OIFM_ID')
                if oifm_id:
                    id_map[oifm_id].append(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    collisions = {key: value for key, value in id_map.items() if len(value) > 1}

    if collisions:
        print("OIFM ID collisions detected:")
        for oifm_id, files in collisions.items():
            print(f"OIFM_ID: {oifm_id} found in files: {', '.join(files)}")
        raise ValueError("OIFM ID collisions found.")
    else:
        print("No OIFM ID collisions detected.")

if __name__ == "__main__":
    validate_oifm_id_collisions()