import asyncio
import os
from pathlib import Path
import sys

from findingmodel import FindingModelFull
from findingmodel.tools import find_similar_models

async def main() -> None:
    if os.getenv("DUCKDB_INDEX_PATH"):
        db_file = os.getenv("DUCKDB_INDEX_PATH")
        print(f"Using DB file at {db_file}")
        in_dir = sys.argv[1]
    else:
        db_file = sys.argv[1]
        in_dir = sys.argv[2]

    new_files: list[str] = []  
    for fm_file in Path(in_dir).glob("*.fm.json"):
        fm = FindingModelFull.model_validate_json(fm_file.read_text())
        result = await find_similar_models(fm.name, fm.description)
        
        if result.recommendation == 'edit_existing':
            print(f"{fm.name} similar to existing model(s): {', '.join([r['name'] for r in result.similar_models])}")
        elif result.recommendation == 'create_new':
            print(f"{fm.name} appears to be a new model.")
            new_files.append(str(fm_file))

    for nf in new_files:
        print(nf)

asyncio.run(main())