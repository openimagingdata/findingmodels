import os
import json

# Function to find all finding model definitions
def find_model_definitions():
    model_definitions = []
    for root, _, files in os.walk('.'):  # Walk through current directory
        if 'defs' in root:  # Check if 'defs' is in the folder path
            for file in files:
                if file.endswith('.json'):
                    model_definitions.append(os.path.join(root, file))
    return model_definitions

# Function to create an index.json file
def create_index_json():
    try:
        model_definitions = find_model_definitions()
        with open('index.json', 'w') as file:
            json.dump({"model_definitions": model_definitions}, file, indent=4)
        print("index.json file created successfully.")
    except Exception as e:
        print(f"Error creating index.json file: {e}")
        raise

if __name__ == "__main__":
    create_index_json()