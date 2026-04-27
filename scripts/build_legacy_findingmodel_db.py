# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "findingmodel @ git+https://github.com/openimagingdata/findingmodel.git@75afd39a400419dcfaf7c8d4a34f065b4d804e0d#subdirectory=packages/findingmodel",
#   "oidm-common @ git+https://github.com/openimagingdata/findingmodel.git@75afd39a400419dcfaf7c8d4a34f065b4d804e0d#subdirectory=packages/oidm-common",
#   "oidm-maintenance @ git+https://github.com/openimagingdata/findingmodel.git@75afd39a400419dcfaf7c8d4a34f065b4d804e0d#subdirectory=packages/oidm-maintenance",
#   "anatomic-locations @ git+https://github.com/openimagingdata/findingmodel.git@75afd39a400419dcfaf7c8d4a34f065b4d804e0d#subdirectory=packages/anatomic-locations",
# ]
# ///
"""Build or publish the current-compatible findingmodel DuckDB artifact with pinned current-main tooling."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from oidm_maintenance.findingmodel.build import build_findingmodel_database
from oidm_maintenance.findingmodel.publish import publish_findingmodel_database

REPO_ROOT = Path(__file__).resolve().parent.parent


async def run(args: argparse.Namespace) -> int:
    if args.build:
        args.database.parent.mkdir(parents=True, exist_ok=True)
        await build_findingmodel_database(
            source_dir=args.defs_dir,
            output_path=args.database,
            generate_embeddings=not args.no_embeddings,
        )
    if args.publish:
        publish_findingmodel_database(
            args.database,
            version=args.version,
            dry_run=args.dry_run,
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--defs-dir", type=Path, default=REPO_ROOT / "defs")
    parser.add_argument("--database", type=Path, default=REPO_ROOT / ".metadata-runs" / "db" / "findingmodels.duckdb")
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
