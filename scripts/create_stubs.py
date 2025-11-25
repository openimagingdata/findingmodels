import asyncio
from pathlib import Path
import sys

from findingmodel import logger
from findingmodel.common import model_file_name
from findingmodel.tools import create_info_from_name, create_model_stub_from_info, add_ids_to_model, add_standard_codes_to_model

def load_finding_names(list_path: Path) -> list[str]:
    with list_path.open("r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return names

async def main(finding_names: list[str], output_dir: Path) -> None:
    names_ids: dict[str, tuple[str, str]] = {}
    for name in finding_names:
        logger.info(f"Processing finding: {name}")
        info = await create_info_from_name(name)
        base_stub = create_model_stub_from_info(info)
        stub = add_ids_to_model(base_stub, source="OIDM")
        add_standard_codes_to_model(stub)

        output_path = output_dir / model_file_name(stub.name)

        logger.info(f"Writing stub to: {output_path}")
        output_path.write_text(stub.model_dump_json(indent=2, exclude_none=True))
        names_ids[name] = (stub.oifm_id, stub.attributes[0].oifma_id)

    for name, ids in names_ids.items():
        print(f"{name} {ids[0]} {ids[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_stubs.py <finding_names_file> <output_dir>")
        sys.exit(1)

    logger.enable("findingmodel")
    
    finding_names = load_finding_names(Path(sys.argv[1]))
    logger.info(f"Loaded {len(finding_names)} finding names ({', '.join(finding_names[:3])})...")
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)
    asyncio.run(main(finding_names, output_dir))