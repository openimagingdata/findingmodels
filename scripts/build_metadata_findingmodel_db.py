# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "findingmodel",
#   "oidm-common",
#   "oidm-maintenance",
#   "anatomic-locations",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# "oidm-maintenance" = { path = "../.metadata-runs/wheelhouse/current/oidm_maintenance-0.2.5-py3-none-any.whl" }
# "anatomic-locations" = { path = "../.metadata-runs/wheelhouse/current/anatomic_locations-0.2.5-py3-none-any.whl" }
# ///
"""Build or publish the metadata-aware findingmodel DuckDB artifact."""

from __future__ import annotations

import argparse
import asyncio
import subprocess
from pathlib import Path

from oidm_maintenance.findingmodel.build import build_findingmodel_database
from oidm_maintenance.findingmodel.publish import publish_findingmodel_database

REPO_ROOT = Path(__file__).resolve().parent.parent


def source_commit() -> str | None:
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        return None
    commit = result.stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    if dirty.returncode == 0 and dirty.stdout.strip():
        return f"{commit}-dirty"
    return commit


async def run(args: argparse.Namespace) -> int:
    if args.build:
        args.database.parent.mkdir(parents=True, exist_ok=True)
        await build_findingmodel_database(
            source_dir=args.defs_dir,
            output_path=args.database,
            generate_embeddings=not args.no_embeddings,
            schema_name="finding_models_metadata",
            schema_version=args.schema_version,
            source_commit=args.source_commit or source_commit(),
        )
    if args.publish:
        publish_findingmodel_database(
            args.database,
            version=args.version,
            dry_run=args.dry_run,
            manifest_key="finding_models_metadata",
            s3_prefix="findingmodel-metadata",
            artifact_name="findingmodels_metadata.duckdb",
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--defs-dir", type=Path, default=REPO_ROOT / "defs")
    parser.add_argument("--database", type=Path, default=REPO_ROOT / ".metadata-runs" / "db" / "findingmodels_metadata.duckdb")
    parser.add_argument("--source-commit")
    parser.add_argument("--schema-version", default="2.0.0-dev")
    parser.add_argument("--version")
    parser.add_argument("--no-embeddings", action="store_true")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not args.build and not args.publish:
        args.build = True
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
