---

name: finding-cdestaging-batch

description: >

  Use when converting CDEStaging CT chest definitions to finding models in bulk

  with chunk-by-chunk review. Includes DuckDB triage, alphabetical chunk conversion,

  mechanical lint, quality review, human TUI sign-off, and progress tracking. User must

  trigger each chunk — never auto-run the full batch.

allowed-tools: Bash, Read, Grep, Glob, Write, Edit, Agent

---



# finding-cdestaging-batch



Bulk conversion from CDEStaging `hood_CT_chest` to validated `.fm.json` files in `defs/from_cdestaging_ct_chest/`. Cross-finding context isolation is mandatory during quality review.



All rules live in `prompts/fragments/` and `docs/cdestaging_ct_chest_batch_progress.md`. This file is pure orchestration.



## Hard rules



- **Never auto-run the full batch** or loop over all chunks without explicit user instruction.

- **Never run convert** unless the user asks for a specific chunk or "next incomplete chunk".

- **Always hand off TUI to the user** — do not launch `review_summaries.py` yourself.

- **Exact DuckDB match** = no new `.fm.json` in `defs/from_cdestaging_ct_chest/`.



## Orientation (read once per session)



- `prompts/fragments/core_concept.md` — what a finding model is.

- `prompts/fragments/session_defaults.md` — source `MGB`, default tags, JSON vs MD metadata ownership.

- `prompts/fragments/search_and_triage.md` — DuckDB triage before convert.

- `docs/cdestaging_ct_chest_batch_progress.md` — chunk offsets, limits, status.

- Default bulk runs: `--no-enrich-metadata --no-enrich-locations` (agent fills synonyms/description; locations pilot later).

- Before first triage: `uv run --env-file .env findingmodel config` and a test search.



## Step 1 — Determine which chunk



Read the progress doc.



- **"Which chunks are complete?"** — report status; verify review files have all entries `ok` or blank.

- **"Run the next incomplete chunk"** — lowest chunk ID not fully done.

- **"Run chunk N"** — use that chunk's offset and limit.



## Step 2 — Triage (only when user asks to run a chunk)



Load `prompts/fragments/search_and_triage.md` and `prompts/fragments/synonym_rules.md`.



Run triage for the chunk:



```powershell

uv run --env-file .env python scripts/triage_cdestaging_sources.py --offset N --limit M --output reviews/triage_cdestaging_chunk_<N>.json -v

```



For each source: review heuristic `decision` in the JSON; apply semantic judgment per `search_and_triage.md`; override ambiguous rows as needed.



- Present a triage table to the user.

- Get decisions on **ambiguous** rows; update triage JSON (`exact_match`, `convert`, or `user_skip`).

- Flag **chunk_duplicate_stems** from the report.



Update progress doc triage column and tallies.



## Step 3 — Convert (only when user asks)



```powershell

uv run --env-file .env python scripts/cdestaging_ct_chest_to_finding_model.py -v --no-enrich-metadata --no-enrich-locations --skip-existing --triage-file reviews/triage_cdestaging_chunk_<N>.json --offset N --limit M

```



Convert only sources not skipped by triage (`exact_match`, `user_skip`). Source-first: JSON attrs from source; MD via `create_model_from_markdown`; agent fills synonyms/description in Steps 5–6.



Update progress doc. Do not re-convert TUI-approved chunks (`--skip-existing`).



## Step 4 — Mechanical lint



Load `prompts/fragments/mechanical_lint.md`. Run:



```powershell

uv run scripts/finding_authoring/review_model.py --fix defs/from_cdestaging_ct_chest/<chunk files>

```



## Step 5 — Quality review (sub-agents, groups of 5)



For each **converted** file in the chunk (not existing-match rows), resolve the CDEStaging source path (`../CDEStaging/definitions/hood_CT_chest/`; prefer `.json` over `.md`; match hyphen/underscore stems — see `scripts/generate_cdestaging_review.py` `source_type_for_stem`).



Spawn one sub-agent via the Agent tool with:



- **Instructions:** "Quality-review the finding model at `<model_path>`. Read the CDEStaging source at `<source_path>`. Read `prompts/fragments/core_concept.md`, `prompts/fragments/metadata_fill.md`, `prompts/fragments/quality_checklist.md`, `prompts/fragments/naming.md`, `prompts/fragments/synonym_rules.md`, and `prompts/fragments/presence_and_change.md`. Return metadata_proposals, issues, suggested fixes (concrete edits), extraction candidates (use exact attribute names), and warnings."

- **Context:** model path + source path only. No neighbors, no batch context.



Fan out in parallel groups of 5.



## Step 6 — Apply fixes



Apply Step 5 **metadata_proposals** and other suggested fixes to `.fm.json` files with Edit. Use `modify_change_from_prior.py` for CFP winnow when appropriate. Re-run `review_model.py --fix` on edited files.



## Step 7 — Review file



Load `prompts/fragments/review_file_generation.md`. Write `reviews/review_cdestaging_chunk_<N>.md` (~8-10 entries).



Include **new models**, **existing-match** entries, and **skipped** entries from triage JSON.



```powershell

uv run python scripts/generate_cdestaging_review.py --label "CDEStaging chunk <N>" --output reviews/review_cdestaging_chunk_<N>.md --triage-file reviews/triage_cdestaging_chunk_<N>.json defs/from_cdestaging_ct_chest/<converted files...>

```



Summarize applied metadata and flag only remaining judgment calls in each new-model entry's Assessment.



## Step 8 — TUI handoff



Load `prompts/fragments/tui_handoff.md`. Tell user to run:



```powershell

uv run --env-file .env scripts/review_summaries.py reviews/review_cdestaging_chunk_<N>.md

```



Wait for user to return.



## Step 9 — Read responses and fix



- `ok` or blank → no action

- Feedback → apply requested changes to models; use `modify_change_from_prior.py` for CFP winnow when appropriate; re-lint

- Questions → answer, iterate

- If substantive changes were made, regenerate the review file for affected entries and re-surface to the user



Chunk TUI = `done` only when all entries signed off.



## Stop conditions



- User says stop, or chunk is fully signed off.

- Do not commit without explicit permission.



## Known edge case



`cabg.json` may fail validation (name `cabg` < 5 chars) — fix or skip when that chunk runs.

