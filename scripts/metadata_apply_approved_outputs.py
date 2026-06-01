# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "findingmodel",
#     "oidm-common",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# ///
"""Apply human-approved metadata outputs to source finding-model JSON files."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from findingmodel import FindingModelFull

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DEFS_DIR = REPO_ROOT / "defs"
DEFAULT_APPROVED_OUTPUTS = (
    REPO_ROOT
    / ".."
    / "findingmodel-metadata"
    / "packages"
    / "findingmodel-ai"
    / "evals"
    / "fixtures"
    / "metadata_review_approved_outputs.json"
).resolve()
DEFAULT_REPORT_DIR = REPO_ROOT / ".metadata-runs" / "approved-output-apply"
DEFAULT_EXPECTED_COUNT = 67


@dataclass(frozen=True)
class ApplyDecision:
    item_id: str
    path: str
    review_id: str
    status: str
    reason: str | None = None
    before_sha256: str | None = None
    after_sha256: str | None = None
    approved_source_sha256: str | None = None
    before_matches_approved_source: bool | None = None
    after_matches_approved_source: bool | None = None
    reviewed_payload_sha256: str | None = None
    review_package_sha256: str | None = None
    source_hash_policy: str | None = None


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalized_text_sha256(value: str) -> str:
    return text_sha256(value.rstrip())


def artifact_sha256(path: Path) -> str:
    if path.is_file():
        return file_sha256(path)
    digest = hashlib.sha256()
    for file_path in sorted(child for child in path.rglob("*") if child.is_file()):
        digest.update(str(file_path.relative_to(path)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def reviewed_item_for_record(record: dict[str, Any]) -> dict[str, Any] | None:
    package_path_value = record.get("review_package_path")
    item_id = record.get("item_id")
    if not isinstance(package_path_value, str) or not isinstance(item_id, str):
        return None
    package_path = Path(package_path_value)
    if record.get("snapshot_source") == "pilot_after_payload":
        item_path = package_path / f"{item_id}.after.json"
        return read_json(item_path) if item_path.exists() else None
    if record.get("snapshot_source") == "review_package_payload" and package_path.exists():
        package = read_json(package_path)
        for item in package.get("items") or []:
            if item.get("id") == item_id:
                return item
    return None


def reviewed_payload_sha256(record: dict[str, Any]) -> str | None:
    reviewed_item = reviewed_item_for_record(record)
    if reviewed_item is None:
        return None
    return hashlib.sha256(json.dumps(reviewed_item, sort_keys=True).encode("utf-8")).hexdigest()


def normalize_item(value: str) -> str:
    item = value.strip()
    if not item:
        return ""
    path = Path(item)
    if path.name.endswith(".fm.json"):
        return path.name.removesuffix(".fm.json")
    return path.name


def load_item_filter(path: Path | None) -> set[str] | None:
    if path is None:
        return None
    if path.suffix == ".json":
        payload = read_json(path)
        if isinstance(payload, dict) and isinstance(payload.get("items"), list):
            raw_values = payload["items"]
        elif isinstance(payload, dict) and isinstance(payload.get("records"), list):
            raw_values = [record.get("item_id") or record.get("path") for record in payload["records"]]
        elif isinstance(payload, list):
            raw_values = payload
        else:
            raise ValueError(f"Unsupported item filter JSON shape: {path}")
    else:
        raw_values = [line.split("#", 1)[0] for line in path.read_text(encoding="utf-8").splitlines()]
    return {item for value in raw_values if value is not None and (item := normalize_item(str(value)))}


def load_approved_records(path: Path) -> list[dict[str, Any]]:
    payload = read_json(path)
    records = payload.get("records") if isinstance(payload, dict) else None
    if not isinstance(records, list):
        raise ValueError(f"Approved outputs file must contain a records list: {path}")
    return records


def validate_approved_record(record: dict[str, Any]) -> str | None:
    item_id = record.get("item_id")
    metadata = record.get("metadata")
    path = record.get("path")
    review_id = record.get("review_id")
    snapshot_source = record.get("snapshot_source")
    review_package_path = record.get("review_package_path")
    review_package_sha256 = record.get("review_package_sha256")
    expected_reviewed_payload_sha256 = record.get("reviewed_payload_sha256")
    approved_source_sha256 = record.get("source_sha256")
    if not isinstance(item_id, str) or not item_id:
        return "missing item_id"
    if not isinstance(path, str) or not path.startswith("defs/") or not path.endswith(".fm.json"):
        return "path is not a defs/*.fm.json source file"
    if Path(path).name.removesuffix(".fm.json") != item_id:
        return "item_id does not match source filename"
    if not isinstance(review_id, str) or not review_id:
        return "missing review_id"
    if snapshot_source == "current_data_repo_def":
        return "approved output was sourced from current dirty source definition"
    if not isinstance(snapshot_source, str) or snapshot_source not in {"pilot_after_payload", "review_package_payload"}:
        return "unsupported snapshot_source"
    if not isinstance(review_package_path, str) or not Path(review_package_path).exists():
        return "review package path missing"
    if not isinstance(review_package_sha256, str) or artifact_sha256(Path(review_package_path)) != review_package_sha256:
        return "review package hash mismatch"
    actual_reviewed_payload_sha256 = reviewed_payload_sha256(record)
    if (
        not isinstance(expected_reviewed_payload_sha256, str)
        or actual_reviewed_payload_sha256 != expected_reviewed_payload_sha256
    ):
        return "reviewed payload hash mismatch"
    if not isinstance(approved_source_sha256, str) or len(approved_source_sha256) != 64:
        return "missing approved source hash"
    if not isinstance(metadata, dict):
        return "missing metadata object"
    return None


def apply_metadata(source: dict[str, Any], metadata: dict[str, Any], fields: list[str]) -> dict[str, Any]:
    updated = dict(source)
    for field in fields:
        if field not in metadata:
            continue
        value = metadata[field]
        if value is None or value == []:
            updated.pop(field, None)
        else:
            updated[field] = value
    return updated


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def decide_one(
    record: dict[str, Any],
    *,
    defs_dir: Path,
    metadata_fields: list[str],
    report_dir: Path,
    write: bool,
) -> ApplyDecision:
    item_id = str(record.get("item_id") or "")
    review_id = str(record.get("review_id") or "")
    source_rel = str(record.get("path") or "")
    source_path = (REPO_ROOT / source_rel).resolve()
    if not source_path.exists():
        return ApplyDecision(item_id, source_rel, review_id, "refused", "source file missing")
    try:
        source_path.relative_to(defs_dir.resolve())
    except ValueError:
        return ApplyDecision(item_id, source_rel, review_id, "refused", "source path outside defs dir")

    before_text = source_path.read_text(encoding="utf-8")
    before_sha256 = text_sha256(before_text)
    before_normalized_sha256 = normalized_text_sha256(before_text)
    source_payload = json.loads(before_text)
    after_payload = apply_metadata(source_payload, record["metadata"], metadata_fields)
    try:
        model = FindingModelFull.model_validate(after_payload)
    except Exception as exc:  # noqa: BLE001 - report validation failures without aborting the batch.
        return ApplyDecision(item_id, source_rel, review_id, "refused", f"updated model validation failed: {exc!r}")

    after_text = model.model_dump_json(indent=2, exclude_none=True) + "\n"
    after_sha256 = text_sha256(after_text)
    after_normalized_sha256 = normalized_text_sha256(after_text)
    approved_source_sha256 = str(record.get("source_sha256") or "")
    hash_context = {
        "before_sha256": before_sha256,
        "after_sha256": after_sha256,
        "approved_source_sha256": approved_source_sha256,
        "before_matches_approved_source": before_sha256 == approved_source_sha256
        or before_normalized_sha256 == approved_source_sha256,
        "after_matches_approved_source": after_sha256 == approved_source_sha256
        or after_normalized_sha256 == approved_source_sha256,
        "reviewed_payload_sha256": str(record.get("reviewed_payload_sha256") or ""),
        "review_package_sha256": str(record.get("review_package_sha256") or ""),
        "source_hash_policy": (
            "Approved metadata is overlaid onto the current source file after verifying review "
            "package and reviewed-payload hashes. approved_source_sha256 is recorded for audit; "
            "it may differ from the current source after generated diffs are cleared."
        ),
    }
    if before_text.rstrip() == after_text.rstrip():
        status = "already_applied"
    else:
        status = "applied" if write else "would_apply"

    before_after_dir = report_dir / "before-after"
    before_after_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(source_rel).name.removesuffix(".fm.json")
    (before_after_dir / f"{stem}.before.json").write_text(before_text, encoding="utf-8")
    (before_after_dir / f"{stem}.after.json").write_text(after_text, encoding="utf-8")
    if write and status == "applied":
        source_path.write_text(after_text, encoding="utf-8")
    return ApplyDecision(item_id, source_rel, review_id, status, **hash_context)


def run(args: argparse.Namespace) -> int:
    approved_outputs = args.approved_outputs.resolve()
    report_dir = args.report_dir.resolve()
    records = load_approved_records(approved_outputs)
    fields = read_json(approved_outputs).get("metadata_fields") or []
    if not isinstance(fields, list) or not all(isinstance(field, str) for field in fields):
        raise SystemExit("approved outputs file must contain a metadata_fields string list")
    if args.expected_count and len(records) != args.expected_count:
        raise SystemExit(f"approved output count mismatch: expected {args.expected_count}, found {len(records)}")

    item_filter = load_item_filter(args.items)
    records_by_item: dict[str, dict[str, Any]] = {}
    refused: list[ApplyDecision] = []
    for record in records:
        reason = validate_approved_record(record)
        item_id = str(record.get("item_id") or "")
        if reason is not None:
            refused.append(ApplyDecision(item_id, str(record.get("path") or ""), str(record.get("review_id") or ""), "refused", reason))
            continue
        records_by_item[item_id] = record

    requested = sorted(item_filter if item_filter is not None else records_by_item)
    decisions = list(refused)
    for item_id in requested:
        record = records_by_item.get(item_id)
        if record is None:
            decisions.append(ApplyDecision(item_id, f"defs/{item_id}.fm.json", "", "refused", "item is not in approved outputs"))
            continue
        decisions.append(
            decide_one(
                record,
                defs_dir=args.defs_dir,
                metadata_fields=fields,
                report_dir=report_dir,
                write=args.write,
            )
        )

    report = {
        "approved_outputs": rel(approved_outputs),
        "created_at": datetime.now(tz=UTC).isoformat(),
        "metadata_fields": fields,
        "write": args.write,
        "counts": {
            status: sum(1 for decision in decisions if decision.status == status)
            for status in sorted({decision.status for decision in decisions})
        },
        "records": [asdict(decision) for decision in decisions],
    }
    write_json(report_dir / "apply-report.json", report)
    print(json.dumps({"write": args.write, "selected": len(requested), "counts": report["counts"]}, sort_keys=True))
    for decision in decisions:
        if decision.status == "refused":
            print(f"refused: {decision.path}: {decision.reason}")
    return 1 if any(decision.status == "refused" for decision in decisions) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approved-outputs", type=Path, default=DEFAULT_APPROVED_OUTPUTS)
    parser.add_argument("--defs-dir", type=Path, default=DEFAULT_DEFS_DIR)
    parser.add_argument("--items", type=Path, help="Optional text/JSON item list. Items not in approved outputs are refused.")
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    parser.add_argument("--expected-count", type=int, default=DEFAULT_EXPECTED_COUNT)
    parser.add_argument("--write", action="store_true", help="Write source defs. Default is dry-run only.")
    args = parser.parse_args()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
