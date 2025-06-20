#!/usr/bin/env python3

import json
import os
from pathlib import Path
from typing import List, Dict, Any
from jsonschema import validate, ValidationError

class FindingModelValidator:
    def __init__(self, schema_file: str = "schema/finding_model.schema.json"):
        """Initialize the validator with the FindingModel schema."""
        self.schema_file = schema_file
        self.schema = self._load_schema()
        
    def _load_schema(self) -> Dict[str, Any]:
        """Load the JSON schema from file."""
        try:
            with open(self.schema_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Schema file not found: {self.schema_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in schema file: {e}")
    
    def validate_file(self, file_path: str) -> List[str]:
        """Validate a single FindingModel JSON file against the schema."""
        errors = []
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Validate against schema
            validate(instance=data, schema=self.schema)
            
        except FileNotFoundError:
            errors.append(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in {file_path}: {e}")
        except ValidationError as e:
            errors.append(f"Schema validation error in {file_path}: {e.message}")
            # Add path information for better debugging
            if e.path:
                errors.append(f"  Path: {' -> '.join(str(p) for p in e.path)}")
        except Exception as e:
            errors.append(f"Unexpected error validating {file_path}: {e}")
            
        return errors
    
    def validate_directory(self, directory: str) -> Dict[str, List[str]]:
        """Validate all FindingModel JSON files in a directory."""
        results = {}
        directory_path = Path(directory)
        
        if not directory_path.exists():
            return {"error": [f"Directory not found: {directory}"]}
        
        # Find all .finding_model.json files
        json_files = list(directory_path.glob("*.finding_model.json"))
        
        if not json_files:
            return {"warning": [f"No .finding_model.json files found in {directory}"]}
        
        print(f"Validating {len(json_files)} FindingModel files...")
        
        for json_file in json_files:
            errors = self.validate_file(str(json_file))
            if errors:
                results[json_file.name] = errors
            else:
                print(f"✓ {json_file.name} - Valid")
        
        return results
    
    def print_validation_summary(self, results: Dict[str, List[str]]) -> None:
        """Print a summary of validation results."""
        if not results:
            print("✓ All files passed validation!")
            return
        
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)
        
        total_files = len(results)
        total_errors = sum(len(errors) for errors in results.values())
        
        print(f"Files with errors: {total_files}")
        print(f"Total errors: {total_errors}")
        print()
        
        for filename, errors in results.items():
            print(f"❌ {filename}:")
            for error in errors:
                print(f"  - {error}")
            print()

def main():
    """Main function to validate FindingModel outputs."""
    # Configuration
    output_dir = "defs/new_findings"
    schema_file = "schema/finding_model.schema.json"
    
    print("FindingModel Schema Validator")
    print("="*40)
    
    # Initialize validator
    try:
        validator = FindingModelValidator(schema_file)
    except Exception as e:
        print(f"❌ Failed to initialize validator: {e}")
        return 1
    
    # Validate all files
    results = validator.validate_directory(output_dir)
    
    # Print summary
    validator.print_validation_summary(results)
    
    # Return exit code
    if results:
        print("❌ Validation failed!")
        return 1
    else:
        print("✓ All files passed validation!")
        return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 