import os
import json
import glob
from pathlib import Path
import sys
from jsonschema import validate, ValidationError


def load_schema(schema_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_jsonl_file(jsonl_path, schema):
    errors = []
    with open(jsonl_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            errors.append((jsonl_path.name, str(e)))
    return errors


def main():
    print("Validating JSONL files against schema...")
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    schema_path = project_root / "schema" / "finding_model.schema.json"
    defs_dir = project_root / "defs"

    if not schema_path.exists():
        print(f"schema file not found: {schema_path}")
        sys.exit(1)
    schema = load_schema(schema_path)
    json_files = glob.glob(os.path.join(defs_dir, "*.json"))
    if not json_files:
        print("no json files found in defs directory.")
        sys.exit(1)

    any_errors = False
    for json_file in json_files:
        errors = validate_jsonl_file(json_file, schema)
        if errors:
            any_errors = True
            print(f"\nerrors in {os.path.basename(json_file)}:")
            for line_num, err in errors:
                print(f"  line {line_num}: {err}")
        else:
            print(f"{os.path.basename(json_file)}: ok")

    if any_errors:
        sys.exit(2)
    else:
        print("\nall files validated successfully.")


if __name__ == "__main__":
    main()
