import os
import json
import subprocess

# Function to find all finding model definitions
def find_model_definitions():
    model_definitions = []
    for root, _, files in os.walk('.'):  # Walk through current directory
        if 'defs' in root:  # Check if 'defs' is in the folder path
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                            oifm_id = data.get('oifm_id')
                            name = data.get('name')
                            model_definitions.append({
                                'oifm_id': oifm_id,
                                'name': name,
                                'file_path': file_path
                            })
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
    return model_definitions

# Function to create an index.json file
def create_index_json():
    try:
        model_definitions = find_model_definitions()
        with open('index.json', 'w') as file:
            json.dump({"model_definitions": model_definitions}, file, indent=4)
        print("index.json file created successfully.")
        try:
            subprocess.run(['git', 'add', 'index.json'], check=True)
            print("index.json file added to Git successfully.")
        except Exception as git_error:
            print(f"Error adding index.json to Git: {git_error}")
        return 0
    except Exception as e:
        print(f"Error creating index.json file: {e}")
        return 1

if __name__ == "__main__":
    exit(create_index_json())