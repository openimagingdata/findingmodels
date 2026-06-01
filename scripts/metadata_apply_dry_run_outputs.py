# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "findingmodel",
#   "oidm-common",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# ///
"""Promote reviewed metadata dry-run artifacts into source finding-model JSON files."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from findingmodel import FindingModelFull

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DEFS_DIR = REPO_ROOT / "defs"


@dataclass(frozen=True)
class ApplyDecision:
    path: str
    status: str
    reason: str | None = None


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def artifact_stem(path: Path) -> str:
    return path.name.removesuffix(".fm.json")


def normalize_item(value: str) -> str:
    item = value.strip()
    if not item:
        return ""
    path = Path(item)
    if path.suffix == ".json" and path.name.endswith(".fm.json"):
        return path.name.removesuffix(".fm.json")
    return path.name.removesuffix(".fm.json")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_item_set(path: Path | None) -> set[str]:
    if path is None:
        return set()
    if path.suffix == ".json":
        payload = read_json(path)
        if isinstance(payload, dict) and isinstance(payload.get("files"), list):
            values = [str(item.get("path") or item.get("file") or item.get("stem") or "") for item in payload["files"]]
        elif isinstance(payload, list):
            values = [str(item.get("path") if isinstance(item, dict) else item) for item in payload]
        else:
            raise ValueError(f"Unsupported JSON list/manifest shape: {path}")
    else:
        values = [line.split("#", 1)[0] for line in path.read_text(encoding="utf-8").splitlines()]
    return {item for value in values if (item := normalize_item(value))}


def latest_status_by_stem(run_dir: Path) -> dict[str, dict[str, Any]]:
    status_path = run_dir / "status.jsonl"
    if not status_path.exists():
        raise FileNotFoundError(f"Missing status file: {status_path}")
    latest: dict[str, dict[str, Any]] = {}
    for line in status_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        path_value = str(row.get("path") or "")
        if not path_value:
            continue
        latest[artifact_stem(Path(path_value))] = row
    return latest


def successful_stems(run_dir: Path) -> set[str]:
    return {
        stem
        for stem, row in latest_status_by_stem(run_dir).items()
        if row.get("status") == "dry_run_success" and int(row.get("audit_flags") or 0) == 0
    }


def selected_stems(args: argparse.Namespace) -> set[str]:
    selectors = [args.approved_manifest, args.approved_list, args.approved_run_dir, args.all_successful]
    if sum(value is not None and value is not False for value in selectors) != 1:
        raise SystemExit(
            "Choose exactly one selector: --approved-manifest, --approved-list, --approved-run-dir, or --all-successful."
        )
    if args.approved_manifest is not None:
        return load_item_set(args.approved_manifest)
    if args.approved_list is not None:
        return load_item_set(args.approved_list)
    if args.approved_run_dir is not None:
        return successful_stems(args.approved_run_dir)
    return successful_stems(args.run_dir)


def audit_is_clean(run_dir: Path, stem: str) -> bool:
    audit_path = run_dir / "audits" / f"{stem}.audit.json"
    if not audit_path.exists():
        return False
    payload = read_json(audit_path)
    return len(payload.get("flags") or []) == 0


def validate_model_json(path: Path) -> str | None:
    try:
        FindingModelFull.model_validate_json(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report validation failures without aborting the batch.
        return repr(exc)
    return None


def decide_one(stem: str, *, args: argparse.Namespace, latest: dict[str, dict[str, Any]]) -> ApplyDecision:
    source_path = (args.defs_dir / f"{stem}.fm.json").resolve()
    before_path = args.run_dir / "before-after" / f"{stem}.before.json"
    after_path = args.run_dir / "before-after" / f"{stem}.after.json"
    audit_path = args.run_dir / "audits" / f"{stem}.audit.json"
    row = latest.get(stem)
    path_label = rel(source_path)

    if row is None:
        return ApplyDecision(path_label, "refused", "missing status row")
    if row.get("status") != "dry_run_success":
        return ApplyDecision(path_label, "refused", f"status is {row.get('status')!r}")
    if int(row.get("audit_flags") or 0) != 0:
        return ApplyDecision(path_label, "refused", "status row has audit flags")
    for artifact in (before_path, after_path, audit_path):
        if not artifact.exists():
            return ApplyDecision(path_label, "refused", f"missing artifact {rel(artifact)}")
    if not audit_is_clean(args.run_dir, stem):
        return ApplyDecision(path_label, "refused", "audit artifact has flags")
    validation_error = validate_model_json(after_path)
    if validation_error is not None:
        return ApplyDecision(path_label, "refused", f"invalid after.json: {validation_error}")
    if not source_path.exists():
        return ApplyDecision(path_label, "refused", "source file missing")

    source_text = source_path.read_text(encoding="utf-8")
    before_text = before_path.read_text(encoding="utf-8")
    after_text = after_path.read_text(encoding="utf-8")
    if source_text == after_text:
        return ApplyDecision(path_label, "already_applied")
    if source_text != before_text:
        return ApplyDecision(path_label, "refused", "source no longer matches dry-run before.json")
    if args.write:
        source_path.write_text(after_text, encoding="utf-8")
        return ApplyDecision(path_label, "applied")
    return ApplyDecision(path_label, "would_apply")


def write_report(decisions: list[ApplyDecision], *, args: argparse.Namespace) -> None:
    if args.report is None:
        return
    payload = {
        "created_at": datetime.now(tz=UTC).isoformat(),
        "run_dir": rel(args.run_dir),
        "write": args.write,
        "counts": {
            status: sum(1 for decision in decisions if decision.status == status)
            for status in sorted({decision.status for decision in decisions})
        },
        "records": [decision.__dict__ for decision in decisions],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    args.run_dir = args.run_dir.resolve()
    args.defs_dir = args.defs_dir.resolve()
    latest = latest_status_by_stem(args.run_dir)
    approved = selected_stems(args)
    excluded = load_item_set(args.exclude_list)
    requested = sorted(approved - excluded)
    decisions = [decide_one(stem, args=args, latest=latest) for stem in requested]
    write_report(decisions, args=args)

    counts = {
        status: sum(1 for decision in decisions if decision.status == status)
        for status in sorted({decision.status for decision in decisions})
    }
    print(json.dumps({"write": args.write, "selected": len(requested), "counts": counts}, sort_keys=True))
    for decision in decisions:
        if decision.status == "refused":
            print(f"refused: {decision.path}: {decision.reason}")
    return 1 if any(decision.status == "refused" for decision in decisions) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True, help="Dry-run directory containing status/artifacts.")
    parser.add_argument("--defs-dir", type=Path, default=DEFAULT_DEFS_DIR)
    parser.add_argument("--approved-manifest", type=Path, help="JSON manifest with files to promote.")
    parser.add_argument("--approved-list", type=Path, help="Text or JSON list of files/stems to promote.")
    parser.add_argument("--approved-run-dir", type=Path, help="Promote successful records from another reviewed run.")
    parser.add_argument("--all-successful", action="store_true", help="Promote every clean success in --run-dir.")
    parser.add_argument("--exclude-list", type=Path, help="Text or JSON list of files/stems to skip.")
    parser.add_argument("--report", type=Path, help="Write a JSON apply report.")
    parser.add_argument("--write", action="store_true", help="Actually update defs/*.fm.json. Default only reports.")
    args = parser.parse_args()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
