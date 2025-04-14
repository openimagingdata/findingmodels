import os
import json
from jsonschema import validate, ValidationError

# Function to format JSON files
def format_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Formatted {file_path}")
    except Exception as e:
        print(f"Error formatting {file_path}: {e}")

# Function to validate JSON files against a schema
def validate_json(file_path, schema):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        validate(instance=data, schema=schema)
        print(f"Validated {file_path}")
    except ValidationError as e:
        print(f"Validation failed for {file_path}: {e.message}")
        raise
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {file_path}: {e}")
        raise

# Load schema from schema folder
def load_schema():
    schema_path = os.path.join('schema', 'finding_model.schema.json')
    try:
        with open(schema_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading schema: {e}")
        raise

# Find all JSON files in defs folders
def find_json_files():
    json_files = []
    for root, _, files in os.walk('.'):  # Walk through current directory
        if 'defs' in root:  # Check if 'defs' is in the folder path
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
    return json_files

# Main function
def main():
    schema = load_schema()
    json_files = find_json_files()
    for file_path in json_files:
        print(f"Processing {file_path}...")        
        try:
            format_json(file_path)
            validate_json(file_path, schema)
        except Exception:
            print("Stopping due to validation error.")
            return

    print("All files processed successfully.")

if __name__ == "__main__":
    main()