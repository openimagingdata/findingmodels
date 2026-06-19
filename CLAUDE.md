# CLAUDE.md

Guidance for agents working in this repository on the **CDEStaging CT chest** batch branch.

## Repository overview

Open Imaging Finding Models — standardized JSON definitions for radiology findings (`.fm.json` in `defs/`).

This branch (`content/chestcts`) converts CDEStaging chest CT sources into finding models under `defs/from_cdestaging_ct_chest/`.

## Key paths

| Path | Purpose |
|------|---------|
| `../CDEStaging/definitions/hood_CT_chest/` | Source `.json` / `.md` definitions (sibling repo) |
| `defs/from_cdestaging_ct_chest/` | Converted finding models (batch output) |
| `docs/cdestaging_ct_chest_batch_progress.md` | Chunk offsets, limits, status |
| `prompts/fragments/` | Rules and procedures for agents |
| `reviews/` | Triage JSON and review markdown (gitignored) |

## Bulk batch workflow

Use skill **`finding-cdestaging-batch`** (`.claude/skills/finding-cdestaging-batch/SKILL.md`).

- User triggers **one chunk at a time** — never auto-run all 21 chunks.
- Flow per chunk: triage → convert → lint → quality review → apply fixes → review file → TUI handoff → apply feedback.
- Default convert: `--no-enrich-metadata --no-enrich-locations`.
- Triage uses `findingmodel search` (not duplicate analyzers).

## Commands (from repo root)

```bash
uv run --env-file .env python scripts/triage_cdestaging_sources.py --offset N --limit M --output reviews/triage_cdestaging_chunk_<N>.json -v

uv run --env-file .env python scripts/cdestaging_ct_chest_to_finding_model.py -v \
  --no-enrich-metadata --no-enrich-locations \
  --triage-file reviews/triage_cdestaging_chunk_<N>.json --offset N --limit M

uv run scripts/finding_authoring/review_model.py --fix defs/from_cdestaging_ct_chest/<files>

uv run --env-file .env scripts/review_summaries.py reviews/review_cdestaging_chunk_<N>.md
```

## Environment

- `.env` with `DUCKDB_INDEX_PATH` and `OPENAI_API_KEY` (not in git).
- Run `uv run --env-file .env findingmodel config` to verify index access.

## Constraints

- Do not commit without explicit user permission.
- Do not edit auto-generated `text/`, `index.md`, or `ids.json` unless running the validator intentionally.
- JSON convert copies domain attributes from source; agent fills synonyms/description in quality review.
