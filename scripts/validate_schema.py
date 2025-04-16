import os
import json
from jsonschema import validate, ValidationError
import sys


def validate_json(file_path, schema):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        validate(instance=data, schema=schema)
        print(f"Validated {file_path}")
    except ValidationError as e:
        error_path = list(e.path)
        error_field = error_path[-1] if error_path else 'Unknown'
        error_line = None
        error_value = None
        if error_path:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        if f'"{error_field}"' in line:
                            error_line = i + 1
                            break
                error_value = data
                for key in error_path:
                    error_value = error_value.get(key, 'Unknown')
            except Exception:
                pass

        print(f"Validation failed for {file_path}: {e.message}")
        print(
            f"Error details: Path - {error_path}, Field - {error_field}, Line - {error_line}, Value - {error_value}, Schema - {e.schema}")
        raise
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {file_path}: {e}")
        raise


def load_schema():
    schema_path = os.path.join('schema', 'finding_model.schema.json')
    try:
        with open(schema_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading schema: {e}")
        raise


def find_json_files():
    json_files = []
    for root, _, files in os.walk('.'):  # Walk through current directory
        if 'defs' in root:  # Check if 'defs' is in the folder path
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
    return json_files


def main():
    schema = load_schema()
    json_files = find_json_files()
    for file_path in json_files:
        print(f"Processing {file_path}...")
        try:
            validate_json(file_path, schema)
        except Exception:
            print("Stopping due to validation error.")
            return 1

    print("All files validated successfully.")
    return 0


if __name__ == "__main__":
    result = main()
    exit(result)
