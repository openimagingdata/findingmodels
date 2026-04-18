---
name: finding-review
description: >
  Use when the user names existing .fm.json files (by path, glob, or directory)
  and asks for review, audit, cleanup, or quality improvements — without
  creating new findings. Includes mechanical lint, per-file LLM quality review,
  and human TUI sign-off. For creating new findings, use finding-author or
  finding-batch.
allowed-tools: Bash, Read, Grep, Glob, Write, Edit, Agent
---

# finding-review

Review existing finding model files and improve them. Cross-file context isolation is mandatory: each file is reviewed by a fresh sub-agent with no exposure to its neighbors. Edits are applied first, then surfaced via the TUI — the user approves, requests changes, or reverts via git.

All rules, CLI cheatsheets, and procedures live in `prompts/fragments/`. This file is pure orchestration.

## Accepted entry points

- **Explicit list** of `.fm.json` paths, e.g., `defs/subdural_hematoma.fm.json defs/epidural_hematoma.fm.json`.
- **Glob** or **directory**, e.g., `defs/*_hemorrhage.fm.json` or everything in `defs/`.

## Orientation (read first)

- `prompts/fragments/core_concept.md` — what a finding model is.

## Step 1 — Guardrail: working tree must be clean

Run `git status --short defs/`. If `defs/` has uncommitted changes, **soft-refuse**:

> Your `defs/` working tree has uncommitted changes. Commit or stash them first so the review's edits can be diffed cleanly, or tell me "proceed anyway" to override.

There is no `--allow-dirty` CLI flag anywhere — this is a conversational override. If the user proceeds anyway, note that in your outcome summary.

## Step 2 — Resolve the file set

From the user's input, produce a concrete list of file paths. Show the list back to the user (count + first few paths) before touching anything.

## Step 3 — Mechanical lint with auto-fix on ERRORs

Load `prompts/fragments/mechanical_lint.md`. Run `scripts/finding_authoring/review_model.py --fix <files>` to auto-fix trivially fixable ERRORs (underscores → spaces, self-synonyms, etc.). Show the resulting diff summary to the user.

## Step 4 — Quality review pass (fan-out, sub-agents, parallel groups of 5)

For each file in the set, spawn one sub-agent via the Agent tool with:

- Instructions: "Quality-review the finding model at `<path>`. Read `prompts/fragments/core_concept.md` and `prompts/fragments/quality_checklist.md`. Return issues found, suggested fixes (concrete edits where possible), extraction candidates (use the exact attribute names from the model), and warnings."
- Context: one file path only. No neighbors, no batch context, no prior conversation.

Fan out in parallel groups of 5. Large sets pipeline groups of 5 sequentially.

## Step 5 — Apply edits

For each sub-agent's report, apply the concrete suggested fixes to the corresponding file with Edit. Extraction candidates and warnings get recorded for the review file, not applied directly.

## Step 6 — Write review files

Inline in the main skill (no sub-agent), load `prompts/fragments/review_file_generation.md` and write `reviews/review_<label>_<n>.md` files, splitting into groups of ~8-10 entries. Each entry summarizes what the finding is, what was changed, and what (if anything) still needs human sign-off.

## Step 7 — TUI handoff

Load `prompts/fragments/tui_handoff.md`. Tell the user how to launch the TUI. Wait for them to come back. The TUI step is **mandatory** for this skill.

## Step 8 — Read back responses and act

For each entry:

- **"ok" or blank** → accept the applied edits, no further action.
- **Specific feedback** → apply the requested change with Edit, then move on.
- **"revert" or equivalent** → `git checkout -- <path>` for that file to restore it to the pre-review state.
- **Question** → answer in chat; iterate if the answer implies further edits.

If substantive further changes were made after reviewer feedback, regenerate the affected review files and surface them for a second pass.

## Stop conditions

- All files have either been approved, reverted, or iterated to a state the user signed off on.

Report: count reviewed, count accepted, count reverted, count iterated. Flag any extraction candidates recorded during review — those become candidates for later `finding-author` or `finding-batch` sessions. Do **not** commit without explicit user permission.
