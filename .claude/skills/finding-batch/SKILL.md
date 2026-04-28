---
name: finding-batch
description: >
  Use when the user hands over a list, CSV, or directory of source content
  describing many findings at once and asks to create models for them in bulk.
  Includes triage, per-finding drafting, mechanical + quality review, human
  TUI sign-off, and (when applicable) CSV writeback. For one-at-a-time
  interactive work, use finding-author. For walking through existing model
  files to propose improvements, use finding-review.
allowed-tools: Bash, Read, Grep, Glob, Write, Edit, Agent
---

# finding-batch

Bulk authoring from a list, CSV, or directory. Cross-finding context isolation is mandatory: each finding is drafted and reviewed by a fresh sub-agent with no exposure to its neighbors. The main skill orchestrates; sub-agents do the per-finding work.

All rules, CLI cheatsheets, and procedures live in `prompts/fragments/` and `prompts/defaults.yml`. This file is pure orchestration.

## Accepted input shapes

- **CSV** with finding names (+ optional description / synonym columns). Structure varies — inspect before parsing.
- **Directory of markdown stubs**, one finding per file.
- **Plain pasted list** of finding names in the chat.

Hood JSON and other legacy inputs are not supported.

## Orientation (read first, once per session)

- `prompts/fragments/core_concept.md` — what a finding model is.
- `prompts/fragments/session_defaults.md` + `prompts/defaults.yml` — confirm source / contributors / tags with the user at session start.

## Step 1 — Parse the input

- **CSV**: `head -1 <csv>`, `head -3 <csv>`. Confirm column layout with the user (see `prompts/fragments/csv_writeback.md` for column inspection). Identify the row-ID column and whether an OIFM column exists.
- **Directory**: list the files, confirm they're the ones to process.
- **Pasted list**: confirm the names back to the user, one per line.

Produce an in-memory list of incoming findings, each tagged with its source row ID (for CSVs) or source file path. For CSV input, preserve the actual source row fields needed for review — at minimum the row ID, incoming name, category/type columns if present, parent ID if present, synonyms if present, description if present, and any existing OIFM/status columns. This original-source information must be carried through to the review file for both newly created models and existing-model matches.

## Step 2 — Triage pass (main skill, whole batch visible)

Load `prompts/fragments/search_and_triage.md`. For each incoming finding, generate 2-3 search targets and run them with small `--limit`. Pool results per finding and classify:

- **Direct match** — finding already exists (record the OIFM ID for CSV writeback).
- **True ambiguity** — needs user triage.
- **No match** — needs a new model.

Look for cross-row duplicates in the incoming list and surface them to the user before drafting.

Present a triage table and get user decisions on ambiguous rows. Keep the direct-match decisions in the batch state; they are not done until the user has reviewed them in the TUI alongside any new models.

## Step 3 — Draft pass (fan-out, sub-agents, parallel groups of 5)

For each row that will become a new model, spawn one sub-agent via the Agent tool with:

- Instructions: "Draft the finding model inputs for this one finding. Read `prompts/fragments/core_concept.md`, `prompts/fragments/naming.md`, `prompts/fragments/synonym_rules.md`, `prompts/fragments/scope_and_specificity.md`, and `prompts/fragments/session_defaults.md`. Return a JSON object with `{name, description, synonyms}` only — the script will generate attributes."
- Context: the row or source content for this one finding only. Do **not** include other findings, prior conversation, or drafts.

Fan out in parallel groups of 5. Collect returned JSON snippets.

## Step 4 — Create

Load `prompts/fragments/create_invocation.md`. Assemble a batch config (session source / contributors / tags + the collected snippets) and run `scripts/finding_authoring/create_model.py --batch` via heredoc.

Parse the `filepath|name|oifm_id` stdout into a `{rowID → oifm_id}` mapping for later CSV writeback.

## Step 5 — Mechanical lint

Load `prompts/fragments/mechanical_lint.md`. Run `review_model.py` over the created files.

## Step 6 — Quality review pass (fan-out, sub-agents, parallel groups of 5)

For each created file, spawn one sub-agent via the Agent tool with:

- Instructions: "Quality-review the finding model at `<path>`. Read `prompts/fragments/core_concept.md` and `prompts/fragments/quality_checklist.md`. Return issues, suggested fixes (concrete edits), extraction candidates (use exact attribute names), and warnings."
- Context: one file path. No neighbors, no batch context.

Fan out in parallel groups of 5.

## Step 7 — Apply fixes and write review files

Apply the sub-agents' suggested fixes with Edit. Then, inline in the main skill (no sub-agent), load `prompts/fragments/review_file_generation.md` and write `reviews/review_<label>_<n>.md` files, splitting into groups of ~8-10 entries.

The review files MUST include every incoming finding decision, not only newly created models:

- **New model entries** — show the created model path, OIFM ID, description, synonyms, change-from-prior values, and the exact source input that produced it.
- **Existing-match entries** — show the matched model path, OIFM ID, description, synonyms, change-from-prior values if present, and the exact source input that was mapped to it.
- **Ambiguous or skipped entries** — show the exact source input, the candidate model(s) or skip reason, and the user-facing question or decision needed.

For CSV sources, every entry MUST include the actual CSV row information used for the decision, including the row ID and incoming finding name. Include relevant columns verbatim (for example category, parent ID, synonyms, and finding type) so the reviewer can compare the source row against the proposed model or match without opening the CSV.

## Step 8 — TUI handoff

Load `prompts/fragments/tui_handoff.md`. Tell the user how to launch the TUI. Wait for them to come back. The TUI step is **mandatory** for this skill.

## Step 9 — Read back responses and apply feedback

For each entry: "ok" or blank → no action; specific feedback → apply the change with Edit; question → answer and iterate. If substantive changes were made, re-generate the affected review files and re-surface to the user.

## Step 10 — CSV writeback (if source was a CSV)

Load `prompts/fragments/csv_writeback.md`. Inspect the CSV, decide columns with the user, extend the header if adding a new OIFM column, then run `scripts/finding_authoring/update_csv.py` with the mapping from step 4.

## Stop conditions

- All created findings and existing-model match decisions have passed TUI sign-off, all created findings have passed quality review, and (for CSV-sourced batches) the OIFM IDs are written back.

Report: count created, count already-existing (referenced by OIFM IDs), count synonyms added, count remaining unprocessed. Do **not** commit without explicit user permission.
