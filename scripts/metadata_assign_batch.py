# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "findingmodel",
#   "findingmodel-ai",
#   "oidm-common",
#   "oidm-maintenance",
#   "anatomic-locations",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "findingmodel-ai" = { path = "../.metadata-runs/wheelhouse/current/findingmodel_ai-0.2.1-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# "oidm-maintenance" = { path = "../.metadata-runs/wheelhouse/current/oidm_maintenance-0.2.5-py3-none-any.whl" }
# "anatomic-locations" = { path = "../.metadata-runs/wheelhouse/current/anatomic_locations-0.2.5-py3-none-any.whl" }
# ///
"""Run metadata assignment over finding model JSON files."""

from __future__ import annotations

import argparse
import asyncio
import json
import traceback
from datetime import UTC, datetime
import findingmodel
import findingmodel_ai
from pathlib import Path
from time import perf_counter
from typing import Any

from findingmodel import FindingModelFull
from findingmodel_ai.metadata import assign_metadata, audit_enrichment
from findingmodel_ai.observability import ensure_logfire_configured
from anatomic_locations import AnatomicLocationIndex

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RUN_DIR = REPO_ROOT / ".metadata-runs" / "enrichment"
DEFAULT_ONTOLOGY_CACHE = REPO_ROOT / ".metadata-runs" / "ontology-cache.duckdb"


def load_paths(args: argparse.Namespace) -> list[Path]:
    paths: list[Path] = []
    if args.manifest:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        paths.extend(REPO_ROOT / item["path"] for item in manifest["files"])
    paths.extend(args.paths)
    if not paths:
        paths = sorted((REPO_ROOT / "defs").glob("*.fm.json"))
    return sorted({path.resolve() for path in paths})


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def artifact_stem(path: Path) -> str:
    return path.name.removesuffix(".fm.json")


def is_transient_error(exc: Exception) -> bool:
    if isinstance(exc, TimeoutError):
        return False
    text = repr(exc).lower()
    transient_terms = (
        "timeout",
        "timed out",
        "rate limit",
        "ratelimit",
        "temporarily",
        "temporary",
        "connection",
        "server error",
        "service unavailable",
        "429",
        "500",
        "502",
        "503",
        "504",
    )
    return any(term in text for term in transient_terms)


async def assign_and_audit(
    model: FindingModelFull,
    *,
    ontology_cache: Path,
    anatomic_index: AnatomicLocationIndex,
    anatomic_index_lock: asyncio.Lock,
    include_llm_audit: bool,
) -> tuple[Any, Any]:
    result = await assign_metadata(
        model,
        ontology_cache=ontology_cache,
        anatomic_index=anatomic_index,
        anatomic_index_lock=anatomic_index_lock,
    )
    audit = await audit_enrichment(
        result.model,
        ontology_cache=ontology_cache,
        anatomic_index=anatomic_index,
        anatomic_index_lock=anatomic_index_lock,
        include_llm=include_llm_audit,
    )
    return result, audit


async def assign_and_audit_with_timeout(
    model: FindingModelFull,
    *,
    ontology_cache: Path,
    anatomic_index: AnatomicLocationIndex,
    anatomic_index_lock: asyncio.Lock,
    include_llm_audit: bool,
    timeout_seconds: float | None,
) -> tuple[Any, Any]:
    if timeout_seconds is None or timeout_seconds <= 0:
        return await assign_and_audit(
            model,
            ontology_cache=ontology_cache,
            anatomic_index=anatomic_index,
            anatomic_index_lock=anatomic_index_lock,
            include_llm_audit=include_llm_audit,
        )
    async with asyncio.timeout(timeout_seconds):
        return await assign_and_audit(
            model,
            ontology_cache=ontology_cache,
            anatomic_index=anatomic_index,
            anatomic_index_lock=anatomic_index_lock,
            include_llm_audit=include_llm_audit,
        )


async def process_file(
    path: Path,
    args: argparse.Namespace,
    semaphore: asyncio.Semaphore,
    anatomic_index: AnatomicLocationIndex,
    anatomic_index_lock: asyncio.Lock,
) -> dict[str, Any]:
    async with semaphore:
        start = perf_counter()
        stem = artifact_stem(path)
        status: dict[str, Any] = {
            "path": relative(path),
            "started_at": datetime.now(tz=UTC).isoformat(),
            "status": "started",
        }
        review_dir = args.run_dir / "reviews"
        before_after_dir = args.run_dir / "before-after"
        audit_dir = args.run_dir / "audits"
        review_dir.mkdir(parents=True, exist_ok=True)
        before_after_dir.mkdir(parents=True, exist_ok=True)
        audit_dir.mkdir(parents=True, exist_ok=True)
        print(f"started: {status['path']}", flush=True)

        try:
            if args.skip_completed and (review_dir / f"{stem}.metadata-review.json").exists():
                status["status"] = "skipped_existing_review"
                return status
            original_text = path.read_text(encoding="utf-8")
            model = FindingModelFull.model_validate_json(original_text)
            retries = 0
            while True:
                try:
                    result, audit = await assign_and_audit_with_timeout(
                        model,
                        ontology_cache=args.ontology_cache,
                        anatomic_index=anatomic_index,
                        anatomic_index_lock=anatomic_index_lock,
                        include_llm_audit=not args.audit_deterministic_only,
                        timeout_seconds=args.record_timeout_seconds,
                    )
                    break
                except Exception as exc:
                    if retries >= args.retries or not is_transient_error(exc):
                        raise
                    retries += 1
                    status["retries"] = retries
                    status["last_retry_error"] = repr(exc)
            updated_text = result.model.model_dump_json(indent=2, exclude_none=True)
            (before_after_dir / f"{stem}.before.json").write_text(original_text, encoding="utf-8")
            (before_after_dir / f"{stem}.after.json").write_text(updated_text + "\n", encoding="utf-8")
            (review_dir / f"{stem}.metadata-review.json").write_text(
                result.review.model_dump_json(indent=2) + "\n",
                encoding="utf-8",
            )
            (audit_dir / f"{stem}.audit.json").write_text(audit.model_dump_json(indent=2) + "\n", encoding="utf-8")
            if not args.dry_run:
                path.write_text(updated_text + "\n", encoding="utf-8")
            status.update(
                {
                    "status": "dry_run_success" if args.dry_run else "success",
                    "logfire_trace_id": result.review.logfire_trace_id,
                    "warnings": result.review.warnings,
                    "audit_flags": len(audit.flags),
                }
            )
        except Exception as exc:
            status.update({"status": "failed", "error": repr(exc), "traceback": traceback.format_exc()})
        finally:
            status["duration_seconds"] = round(perf_counter() - start, 3)
        return status


async def run(args: argparse.Namespace) -> int:
    if args.logfire:
        ensure_logfire_configured(console=False)
    args.run_dir.mkdir(parents=True, exist_ok=True)
    paths = load_paths(args)
    semaphore = asyncio.Semaphore(args.concurrency)
    status_path = args.run_dir / "status.jsonl"
    failures = 0
    anatomic_index_lock = asyncio.Lock()
    async with AnatomicLocationIndex() as anatomic_index:
        with status_path.open("a", encoding="utf-8") as status_file:
            for coro in asyncio.as_completed(
                [process_file(path, args, semaphore, anatomic_index, anatomic_index_lock) for path in paths]
            ):
                status = await coro
                if status["status"] == "failed":
                    failures += 1
                status_file.write(json.dumps(status, sort_keys=True) + "\n")
                status_file.flush()
                print(f"{status['status']}: {status['path']}")
    print(f"Processed {len(paths)} files; failures={failures}; status={relative(status_path)}")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Specific .fm.json files. Defaults to defs/*.fm.json.")
    parser.add_argument("--manifest", type=Path, help="Pilot manifest JSON from metadata_select_pilot.py.")
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--ontology-cache", type=Path, default=DEFAULT_ONTOLOGY_CACHE)
    parser.add_argument("--concurrency", type=int, default=3)
    parser.add_argument("--retries", type=int, default=1, help="Whole-file retries for transient assignment/audit failures.")
    parser.add_argument(
        "--record-timeout-seconds",
        type=float,
        default=90,
        help="Fail an individual record if assignment plus audit exceeds this many seconds. Use 0 to disable.",
    )
    parser.add_argument("--skip-completed", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Write artifacts but do not update source .fm.json files.")
    parser.add_argument("--logfire", action="store_true", help="Opt in to Logfire instrumentation for this run.")
    parser.add_argument(
        "--audit-deterministic-only",
        action="store_true",
        help="Skip the LLM auditor pass and write only deterministic audit flags.",
    )
    parser.add_argument("--debug-runtime", action="store_true", help="Print imported package paths and exit.")
    args = parser.parse_args()
    if args.debug_runtime:
        print(f"findingmodel: {findingmodel.__file__}")
        print(f"findingmodel_ai: {findingmodel_ai.__file__}")
        print("FindingModelFull fields:")
        for field_name in sorted(FindingModelFull.model_fields):
            print(f"- {field_name}")
        return 0
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
