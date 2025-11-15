# /// script
# requires-python = "==3.12"
# dependencies = [
#     "findingmodel",
# ]
# ///
import asyncio
import sys

from findingmodel import Index

async def main() -> None:
    db_file = sys.argv[1]
    query = sys.argv[2]

    index = Index(db_path=db_file)
    results = await index.search(query)
    for result in results:
        print(f"{result.oifm_id}: {result.name}")


asyncio.run(main())