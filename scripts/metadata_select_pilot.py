# /// script
# requires-python = ">=3.11"
# ///
"""Select a deterministic representative pilot set for metadata enrichment."""

from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DEFS_DIR = REPO_ROOT / "defs"
DEFAULT_OUTPUT_DIR = REPO_ROOT / ".metadata-runs" / "pilot"

BUCKET_KEYWORDS: dict[str, tuple[str, ...]] = {
    "neuro": ("brain", "cerebral", "intracranial", "ventric", "skull", "calvar", "spine", "cord"),
    "chest": ("lung", "pulmonary", "pleur", "mediastin", "hilar", "airway", "rib"),
    "cardiovascular": ("aortic", "arter", "venous", "vascular", "aneurysm", "dissection", "thrombus", "embol"),
    "abdomen_gi": ("abdom", "bowel", "colon", "append", "pancre", "liver", "splenic", "gastric", "esoph"),
    "gu": ("renal", "kidney", "ureter", "bladder", "prostate", "testis", "adrenal"),
    "msk": ("bone", "fracture", "joint", "femur", "tibia", "fibula", "clavicle", "vertebr", "meniscus"),
    "breast": ("breast", "mamm", "axillary"),
    "pediatric": ("infant", "child", "newborn", "pediatric", "fetal"),
    "oncology": ("tumor", "mass", "neoplasm", "cancer", "metasta", "lesion", "lymphadenopathy"),
    "trauma": ("fracture", "injury", "trauma", "contusion", "rupture", "laceration"),
    "measurement_classification": ("measurement", "classification", "score", "index", "bi_rads", "li_rads"),
    "artifact_technique": ("artifact", "marker", "hardware", "stent", "clip", "catheter", "device"),
    "broad_abnormality": ("abnormal", "abnormality", "disease", "opacity", "enlargement", "dilatation"),
}


@dataclass
class Candidate:
    path: Path
    name: str
    tags: list[str] = field(default_factory=list)
    buckets: set[str] = field(default_factory=set)


def load_candidates(defs_dir: Path) -> list[Candidate]:
    candidates: list[Candidate] = []
    for path in sorted(defs_dir.resolve().glob("*.fm.json")):
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        name = str(data.get("name") or path.stem)
        tags = [str(tag) for tag in data.get("tags") or []]
        haystack = " ".join([path.stem, name, *tags]).lower()
        buckets = {bucket for bucket, terms in BUCKET_KEYWORDS.items() if any(term in haystack for term in terms)}
        if not buckets:
            buckets.add("general")
        candidates.append(Candidate(path=path.resolve(), name=name, tags=tags, buckets=buckets))
    return candidates


def select_pilot(candidates: list[Candidate], *, target_count: int, seed: int) -> list[Candidate]:
    if target_count >= len(candidates):
        return candidates

    rng = random.Random(seed)
    by_bucket: dict[str, list[Candidate]] = defaultdict(list)
    for candidate in candidates:
        for bucket in candidate.buckets:
            by_bucket[bucket].append(candidate)
    for bucket_candidates in by_bucket.values():
        rng.shuffle(bucket_candidates)

    selected: dict[Path, Candidate] = {}
    bucket_names = sorted(by_bucket)
    cursor = 0
    max_bucket_size = max((len(items) for items in by_bucket.values()), default=0)
    while len(selected) < target_count and cursor < max_bucket_size:
        for bucket in bucket_names:
            if len(selected) >= target_count:
                break
            items = by_bucket[bucket]
            if cursor < len(items):
                selected.setdefault(items[cursor].path, items[cursor])
        cursor += 1

    remaining = [candidate for candidate in candidates if candidate.path not in selected]
    rng.shuffle(remaining)
    for candidate in remaining:
        if len(selected) >= target_count:
            break
        selected[candidate.path] = candidate
    return sorted(selected.values(), key=lambda candidate: candidate.path.name)


def write_manifest(selected: list[Candidate], *, output_dir: Path, seed: int, target_count: int) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "created_at": datetime.now(tz=UTC).isoformat(),
        "seed": seed,
        "target_count": target_count,
        "selected_count": len(selected),
        "files": [
            {
                "path": str(candidate.path.relative_to(REPO_ROOT)),
                "name": candidate.name,
                "tags": candidate.tags,
                "buckets": sorted(candidate.buckets),
            }
            for candidate in selected
        ],
    }
    manifest_path = output_dir / "pilot_manifest.json"
    manifest_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "pilot_files.txt").write_text(
        "\n".join(item["path"] for item in payload["files"]) + "\n",
        encoding="utf-8",
    )
    return manifest_path


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--defs-dir", type=Path, default=DEFAULT_DEFS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--target-count", type=int, default=150)
    parser.add_argument("--seed", type=int, default=20260426)
    args = parser.parse_args()

    candidates = load_candidates(args.defs_dir)
    selected = select_pilot(candidates, target_count=args.target_count, seed=args.seed)
    manifest_path = write_manifest(selected, output_dir=args.output_dir, seed=args.seed, target_count=args.target_count)
    print(f"Selected {len(selected)} files into {display_path(manifest_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
