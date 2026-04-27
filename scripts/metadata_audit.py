# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "findingmodel",
#   "findingmodel-ai",
#   "oidm-common",
#   "anatomic-locations",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "findingmodel-ai" = { path = "../.metadata-runs/wheelhouse/current/findingmodel_ai-0.2.1-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# "anatomic-locations" = { path = "../.metadata-runs/wheelhouse/current/anatomic_locations-0.2.5-py3-none-any.whl" }
# ///
"""Re-run the enrichment auditor without re-running metadata assignment."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from findingmodel import FindingModelFull
from findingmodel_ai.metadata import audit_enrichment

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / ".metadata-runs" / "audits"
DEFAULT_ONTOLOGY_CACHE = REPO_ROOT / ".metadata-runs" / "ontology-cache.duckdb"


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def artifact_stem(path: Path) -> str:
    return path.name.removesuffix(".fm.json")


async def audit_file(path: Path, *, ontology_cache: Path, output_dir: Path, semaphore: asyncio.Semaphore) -> dict[str, object]:
    async with semaphore:
        model = FindingModelFull.model_validate_json(path.read_text(encoding="utf-8"))
        result = await audit_enrichment(model, ontology_cache=ontology_cache)
        output_dir.mkdir(parents=True, exist_ok=True)
        out_path = output_dir / f"{artifact_stem(path)}.audit.json"
        out_path.write_text(result.model_dump_json(indent=2) + "\n", encoding="utf-8")
        return {"path": relative(path), "audit_path": relative(out_path), "flags": len(result.flags)}


async def run(args: argparse.Namespace) -> int:
    if args.all:
        paths = sorted((REPO_ROOT / "defs").glob("*.fm.json"))
    else:
        paths = args.paths
    if not paths:
        raise SystemExit("Pass one or more .fm.json paths, or use --all to audit every definition.")
    semaphore = asyncio.Semaphore(args.concurrency)
    summaries = await asyncio.gather(
        *[
            audit_file(path.resolve(), ontology_cache=args.ontology_cache, output_dir=args.output_dir, semaphore=semaphore)
            for path in paths
        ]
    )
    summary_path = args.output_dir / "audit_summary.json"
    summary_path.write_text(json.dumps({"files": summaries}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Audited {len(summaries)} files; summary={relative(summary_path)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--ontology-cache", type=Path, default=DEFAULT_ONTOLOGY_CACHE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--concurrency", type=int, default=3)
    parser.add_argument("--all", action="store_true", help="Audit every defs/*.fm.json file.")
    return asyncio.run(run(parser.parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
