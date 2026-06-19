"""Triage CDEStaging CT chest sources against the DuckDB finding model index."""

from __future__ import annotations

import argparse
import asyncio
import logging
import os
import sys
from pathlib import Path

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from findingmodels.cdestaging_ct_chest.triage import save_triage_report, triage_chunk

logger = logging.getLogger(__name__)

DEFAULT_INPUT = "../CDEStaging/definitions/hood_CT_chest"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Triage CDEStaging sources against DuckDB index (findingmodel search)"
    )
    parser.add_argument("--input-dir", default=DEFAULT_INPUT)
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Skip first N deduped sources (alphabetical order) before triage",
    )
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--output", required=True, help="Path for triage JSON report")
    parser.add_argument(
        "--db-path",
        default=None,
        help="DuckDB index path (default: DUCKDB_INDEX_PATH from .env)",
    )
    parser.add_argument(
        "--search-limit",
        type=int,
        default=2,
        help="Max results per search target (default: 2)",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s - %(message)s")

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        logger.error("Input directory not found: %s", input_dir)
        sys.exit(1)

    db_path = args.db_path or os.getenv("DUCKDB_INDEX_PATH")
    if not db_path:
        logger.error("Provide --db-path or set DUCKDB_INDEX_PATH in .env")
        sys.exit(1)

    report = asyncio.run(
        triage_chunk(
            input_dir,
            offset=args.offset,
            limit=args.limit,
            db_path=db_path,
            search_limit=args.search_limit,
        )
    )
    output_path = Path(args.output)
    save_triage_report(report, output_path)

    summary = report.to_dict()["summary"]
    logger.info("Wrote %s (%d sources)", output_path, len(report.records))
    logger.info(
        "Triage summary: exact_match=%d no_match=%d ambiguous=%d",
        summary.get("exact_match", 0),
        summary.get("no_match", 0),
        summary.get("ambiguous", 0),
    )
    if report.chunk_duplicate_stems:
        logger.warning("Chunk duplicate stems: %s", ", ".join(report.chunk_duplicate_stems))


if __name__ == "__main__":
    main()
