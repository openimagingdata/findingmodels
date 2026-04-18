---
name: finding-author
description: >
  Use when the user wants to work with a single radiology finding interactively
  — checking whether it exists in defs/, adding a synonym to an existing model,
  or drafting a new finding model. Covers a small handful of findings discussed
  one at a time in conversation. For list/CSV/directory-driven creation, use
  finding-batch instead. For walking through existing model files to propose
  improvements, use finding-review.
allowed-tools: Bash, Read, Grep, Glob, Write, Edit, Agent
---

# finding-author

Interactive authoring for a single finding at a time. Three terminal outcomes: the finding already exists and nothing changes; the finding exists and a synonym is added; the finding does not exist and a new model is created.

All rules, CLI cheatsheets, and procedures live in `prompts/fragments/` and `prompts/defaults.yml`. This file is pure orchestration — load the fragment named at each step, then apply it.

## Orientation (read first, once per session)

- `prompts/fragments/core_concept.md` — what a finding model is.
- `prompts/fragments/session_defaults.md` + `prompts/defaults.yml` — confirm source / contributors / tags with the user at session start. Reuse the answer for the rest of the conversation.

## Step 1 — Search and triage

Load `prompts/fragments/search_and_triage.md`.

Generate 2-3 complementary search targets, run each, evaluate the pooled results yourself for exact semantic match. **Do not forward raw result lists to the user.** Report one of three outcomes:

- Exact match found → go to step 2a or do nothing if the user doesn't want changes.
- No match after reasonable search → go to step 2b.
- True ambiguity → surface only the ambiguous candidates with your reasoning, let the user decide.

## Step 2a — Synonym update on existing model

- Read the target `.fm.json` file.
- Load `prompts/fragments/synonym_rules.md`. Apply the collision check before adding.
- Edit the `synonyms` array with the Edit tool (add after `description` if no `synonyms` key exists). Do not duplicate existing synonyms.
- Show the diff to the user.

## Step 2b — Create a new model

### 2b.i — Draft

Load `prompts/fragments/naming.md`, `prompts/fragments/synonym_rules.md`, `prompts/fragments/scope_and_specificity.md`.

Apply the rules to draft the name, description, and synonym list. Expand acronyms, minimize eponyms, replace brand names, scope broad names, verify each synonym is truly equivalent.

### 2b.ii — Create

Load `prompts/fragments/create_invocation.md`. Invoke `scripts/finding_authoring/create_model.py` with the drafted inputs and the session's source / contributors / tags. Capture the `filepath|name|oifm_id` output.

### 2b.iii — Mechanical lint

Load `prompts/fragments/mechanical_lint.md`. Run `review_model.py` on the new file. Resolve ERRORs (re-run with `--fix` where appropriate); surface REVIEWs to the next step; address WARNINGs inline.

### 2b.iv — Quality review (sub-agent, clean context)

Spawn one sub-agent via the Agent tool with:

- Instructions: "Quality-review the finding model at `<path>`. Read `prompts/fragments/core_concept.md` and `prompts/fragments/quality_checklist.md` first. Return issues found, suggested fixes (concrete edits where possible), extraction candidates (using the exact attribute names from the model), and warnings."
- Context: the file path only. Do **not** pass other findings, drafts, or prior conversation.

Apply the sub-agent's suggested fixes to the file with Edit. Re-run `review_model.py` after fixes.

### 2b.v — Show and confirm

Show the final model to the user in chat (paste or summarize). **Skip the TUI step** — it is mandatory only for batch and review flows.

## Step 3 — Optional enrichment

If the user asks for a richer description, load `prompts/fragments/enrichment.md` and apply `findingmodel-ai make-info` + `fix_stub.py` as described. Re-run mechanical lint + quality review afterward if synonyms or description changed substantively.

## Stop conditions

- The finding already exists and no changes were requested.
- The synonym was added and confirmed.
- A new model was created, reviewed, and shown to the user.

In all three cases, report the final outcome clearly. Do **not** commit without explicit user permission.
