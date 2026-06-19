"""Batch report generation for CDEStaging CT chest conversion."""

import json
from datetime import datetime
from pathlib import Path

from findingmodels.cdestaging_ct_chest.convert import ConversionResult


def write_batch_report(
    results: list[ConversionResult],
    *,
    input_dir: Path,
    output_dir: Path,
) -> tuple[Path, Path]:
    """Write markdown and JSON batch reports to the output directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    md_path = output_dir / f"batch_report_{timestamp}.md"
    json_path = output_dir / f"batch_report_{timestamp}.json"

    succeeded = [r for r in results if r.status == "success"]
    failed = [r for r in results if r.status == "error"]
    skipped_triage = [r for r in results if r.status == "skipped_triage_match"]
    json_count = sum(1 for r in results if r.source_type == "json")
    md_count = sum(1 for r in results if r.source_type == "md")

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "total": len(results),
        "succeeded": len(succeeded),
        "failed": len(failed),
        "skipped_triage_match": len(skipped_triage),
        "json_count": json_count,
        "md_count": md_count,
        "entries": [
            {
                "source": r.source_path.name,
                "source_type": r.source_type,
                "status": r.status,
                "output": r.output_path.name if r.output_path else None,
                "oifm_id": r.oifm_id,
                "finding_name": r.finding_name,
                "error": r.error,
            }
            for r in results
        ],
    }

    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# CDEStaging CT Chest Conversion Batch Report",
        "",
        f"**Generated:** {summary['generated_at']}",
        f"**Input Directory:** {input_dir}",
        f"**Output Directory:** {output_dir}",
        "",
        "## Summary",
        "",
        f"- **Total processed:** {len(results)}",
        f"- **Succeeded:** {len(succeeded)}",
        f"- **Failed:** {len(failed)}",
        f"- **Skipped (triage match):** {len(skipped_triage)}",
        f"- **JSON sources:** {json_count}",
        f"- **Markdown sources:** {md_count}",
        "",
        "## Results",
        "",
        "| Source | Type | Status | Output | OIFM ID | Finding | Error |",
        "|--------|------|--------|--------|---------|---------|-------|",
    ]

    for entry in summary["entries"]:
        lines.append(
            "| {source} | {source_type} | {status} | {output} | {oifm_id} | {finding_name} | {error} |".format(
                source=entry["source"],
                source_type=entry["source_type"],
                status=entry["status"],
                output=entry["output"] or "",
                oifm_id=entry["oifm_id"] or "",
                finding_name=(entry["finding_name"] or "").replace("|", "\\|"),
                error=(entry["error"] or "").replace("|", "\\|").replace("\n", " "),
            )
        )

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path, json_path
