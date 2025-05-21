# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
import json

from findingmodel import FindingModelFull

def main():
    # Get the schema of the FindingModelFull class
    schema = FindingModelFull.model_json_schema()
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()