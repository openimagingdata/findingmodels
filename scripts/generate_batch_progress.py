"""Generate docs/cdestaging_ct_chest_batch_progress.md from CDEStaging sources."""

from pathlib import Path

from findingmodels.cdestaging_ct_chest.loaders import (
    dedupe_input_files,
    normalized_stem,
    should_process_file,
)

CHUNK_SIZE = 10
INPUT_DIR = Path("../CDEStaging/definitions/hood_CT_chest")
OUTPUT_PATH = Path("docs/cdestaging_ct_chest_batch_progress.md")


def main() -> None:
    all_files = [f for f in INPUT_DIR.glob("*") if f.is_file()]
    eligible = [f for f in all_files if should_process_file(f, all_files)]
    deduped = dedupe_input_files(eligible)
    chunks = [deduped[i : i + CHUNK_SIZE] for i in range(0, len(deduped), CHUNK_SIZE)]

    lines = [
        "# CDEStaging CT Chest Batch Progress",
        "",
        "Alphabetical deduped sources from `../CDEStaging/definitions/hood_CT_chest`.",
        f"Total sources: **{len(deduped)}**. Chunk size: **{CHUNK_SIZE}**. Chunks: **{len(chunks)}**.",
        "",
        "## Chunk status",
        "",
        "| Chunk | Offset | Limit | Sources | Convert | Lint | Review file | TUI |",
        "|-------|--------|-------|---------|---------|------|-------------|-----|",
    ]
    for i, chunk in enumerate(chunks):
        offset = i * CHUNK_SIZE
        lines.append(
            f"| {i + 1} | {offset} | {len(chunk)} | {chunk[0].name} … {chunk[-1].name} | pending | pending | pending | pending |"
        )

    lines.extend(
        [
            "",
            "## TUI outcome rules",
            "",
            "- Chunk **done** when every entry has `**Response:**` = `ok` or blank, after fix rounds, and lint is clean.",
            "- Specific feedback → `needs_fix`; questions → `in_progress`; never opened → `pending_tui`.",
            "",
            "## Source index (alphabetical)",
            "",
        ]
    )
    for idx, file_path in enumerate(deduped):
        chunk_id = idx // CHUNK_SIZE + 1
        lines.append(f"- [{chunk_id}] `{normalized_stem(file_path)}` ← `{file_path.name}`")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} ({len(deduped)} sources, {len(chunks)} chunks)")


if __name__ == "__main__":
    main()
