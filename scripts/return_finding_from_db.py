import asyncio
import sys
from pathlib import Path

"dd the project root to the path so scripts can import modules from the main package."
sys.path.append(str(Path(__file__).parent.parent))
from findingmodel.index import Index

async def get_finding(oifm_id):
    index = Index()
    data = await index.index_collection.find_one({"oifm_id": oifm_id})
    return data

if __name__ == "__main__":
    result = asyncio.run(get_finding("OIFM_CDE_000126"))
    print(result)
