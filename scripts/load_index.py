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
    index = Index(db_path=db_file)
    print(await index.count())

    adrenal_node = await index.get_full("OIFM_CDE_000003")
    print(adrenal_node.model_dump_json(indent=2,exclude_none=True))

asyncio.run(main())