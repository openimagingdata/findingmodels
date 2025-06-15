# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///

from pathlib import Path

from findingmodel.index import Index

index = Index(Path(__file__).parent.parent)
print(len(index))
index.export_to_jsonl()

