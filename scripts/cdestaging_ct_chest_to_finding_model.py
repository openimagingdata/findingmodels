"""Convert CDEStaging CT chest definitions to validated finding model JSON files."""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from dotenv import load_dotenv

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from findingmodels.cdestaging_ct_chest.batch_report import write_batch_report
from findingmodels.cdestaging_ct_chest.convert import convert_definition
from findingmodels.cdestaging_ct_chest.loaders import dedupe_input_files, should_process_file

logger = logging.getLogger(__name__)

DEFAULT_INPUT = "../CDEStaging/definitions/hood_CT_chest"
DEFAULT_OUTPUT = "defs/from_cdestaging_ct_chest"


async def run_batch(
    input_dir: Path,
    output_dir: Path,
    limit: int | None,
    *,
    enrich_metadata: bool = True,
    enrich_locations: bool = True,
) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)

    all_files = [f for f in input_dir.glob("*") if f.is_file()]
    eligible = [f for f in all_files if should_process_file(f, all_files)]
    files_to_process = dedupe_input_files(eligible)
    if limit is not None:
        files_to_process = files_to_process[:limit]

    results = []
    output_claims: dict[str, Path] = {}
    for file_path in files_to_process:
        result = await convert_definition(
            file_path,
            output_dir=output_dir,
            output_claims=output_claims,
            enrich_metadata=enrich_metadata,
            enrich_locations=enrich_locations,
        )
        results.append(result)
        if result.status == "success":
            logger.info("Converted %s -> %s", file_path.name, result.output_path.name)
        else:
            logger.error("Failed %s: %s", file_path.name, result.error)

    md_path, json_path = write_batch_report(
        results,
        input_dir=input_dir,
        output_dir=output_dir,
    )
    logger.info("Batch report: %s", md_path)
    logger.info("Batch report: %s", json_path)

    failed = sum(1 for r in results if r.status == "error")
    return 1 if failed else 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert CDEStaging CT chest definitions to validated .fm.json files"
    )
    parser.add_argument("--input-dir", default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="WARNING",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    enrich_group = parser.add_mutually_exclusive_group()
    enrich_group.add_argument(
        "--enrich-metadata",
        action="store_true",
        default=True,
        help="Enrich JSON models with create_info_from_name (default: on)",
    )
    enrich_group.add_argument(
        "--no-enrich-metadata",
        action="store_false",
        dest="enrich_metadata",
        help="Skip synonym/tag metadata enrichment",
    )
    location_group = parser.add_mutually_exclusive_group()
    location_group.add_argument(
        "--enrich-locations",
        action="store_true",
        default=True,
        help="Populate anatomic_locations via find_anatomic_locations (default: on)",
    )
    location_group.add_argument(
        "--no-enrich-locations",
        action="store_false",
        dest="enrich_locations",
        help="Skip anatomic location search",
    )
    args = parser.parse_args()

    load_dotenv()

    log_level = logging.DEBUG if args.verbose else getattr(logging, args.log_level)
    logging.basicConfig(
        level=log_level,
        format="%(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        logger.error("Input directory not found: %s", input_dir)
        sys.exit(1)

    exit_code = asyncio.run(
        run_batch(
            input_dir,
            Path(args.output_dir),
            args.limit,
            enrich_metadata=args.enrich_metadata,
            enrich_locations=args.enrich_locations,
        )
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
