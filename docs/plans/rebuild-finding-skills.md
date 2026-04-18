# Plan: Rebuild the finding-model skill surface

## Status

- [x] Phase 0 — in-repo plan artifact
- [x] Phase 1 — rule fragments
- [x] Phase 2 — substep fragments + defaults.yml
- [x] Phase 3 — review fragments
- [x] Phase 4 — scripts move + in-flight fixes
- [x] Phase 5 — skills
- [x] Phase 6 — trigger-evals
- [x] Phase 7 — deletion
- [x] Phase 8 — docs + repo-level references (CHANGELOG deferred — no file in repo)
- [ ] Phase 9 — end-to-end verification
- [ ] Phase 10 — final plan-artifact update + PR

Branch: `content/headcts` (working branch confirmed by user; dedicated `chore/rebuild-finding-skills` branch not used).

## Context

The `new-finding` skill and the surrounding `prompts/` directory have grown by accretion across successive campaigns (CXR most recently, head CT next, knee MRI after that). Current state:

- One oversized skill tries to cover three different workflows (single interactive create, batch create, review of existing models) under a misleading "new-finding" name.
- `SKILL.md` (384 lines) duplicates most of `prompts/new_finding_workflow.md` (256 lines).
- `prompts/{create,merge,review,single}_agent.md` are legacy Pydantic-AI-style prompts that don't fit Claude Code sub-agents — yet `SKILL.md` tells Claude sub-agents to use them as instructions.
- Skill description uses coercive language and CXR-specific trigger phrases.
- `bulk_review_fix.py` is a CXR-specific one-shot with hard-coded device lists.
- The current tool does not actually work well end-to-end. We are rebuilding green-field, not migrating.

Goal: three purpose-built skills, each thin, sharing a library of small composable fragments. Every substep loads only the context it needs. No modality is baked in anywhere.

## Decisions (settled through grill-me)

1. **Three skills**, by input shape (not count):
   - `finding-author` — interactive work on a single finding in conversation (including synonym updates on existing models).
   - `finding-batch` — list / CSV / directory of source content → many models in one pass.
   - `finding-review` — walk existing `.fm.json` files (explicit list OR glob/directory) and improve them.
2. **Scripts live at repo root** under `scripts/finding_authoring/`. They are project scripts that operate on canonical repo state, not skill-private utilities. All three skills reference these stable paths.
3. **Green-field rebuild, not migration.** Delete the old skill, legacy agent prompts, and monolithic workflow doc. Mine them for content while writing new fragments; do not preserve their structure.
4. **Fragment library** in `prompts/fragments/`, plus `prompts/defaults.yml` for machine-readable session defaults. Each fragment is 20–80 lines, single-topic, loaded only by the substeps that need it.
5. **Quality checklist is self-contained** with one-line summaries per rule. Full rule fragments are loaded by *creation* substeps (where rules must be applied) and by reviewers only on uncertainty. Drift sync is handled informally for now — revisit if it becomes a real problem.
6. **Cross-finding context isolation in batch and review.** Drafting in batch and quality review in batch *and* review flows fan out as one sub-agent per finding, in parallel groups capped at 5. The main skill handles triage, assembly, script invocation, review-file writing, TUI handoff, and CSV writeback.
7. **Review-file generation is inline in the main skill**, not a sub-agent — task is mechanical, main skill already has the relevant context.
8. **`finding-review` applies edits → then reviews via TUI → user reverts or requests further changes.** Soft-refuse if `defs/` working tree is dirty; no heavier git machinery.
9. **No `finding-search` skill.** Pure read-only queries are rare enough that `finding-author`'s built-in search covers them.
10. **Zero modality anchoring anywhere** — skill descriptions, fragments, and trigger-evals describe behavior, not anatomy or modality. Trigger-eval example sets explicitly mix modalities.
11. **Drop Hood JSON input support.** Tied to a past campaign; future campaigns use CSV, markdown directories, or pasted lists.
12. **Phasing: family-by-family review** (option B). Rules fragments first, then substep fragments, then review fragments, then skills, then evals. One long-lived branch, one PR at the end.

## Target structure

```
.claude/skills/
    finding-author/
        SKILL.md
        trigger-eval.json
    finding-batch/
        SKILL.md
        trigger-eval.json
    finding-review/
        SKILL.md
        trigger-eval.json

scripts/
    finding_authoring/
        create_model.py
        fix_stub.py
        review_model.py
        update_csv.py

prompts/
    overview.md                      # kept — human-browsable long-form reference
    overview_compact.md              # kept — source material for core_concept.md fragment
    defaults.yml                     # NEW — contributor keys, source codes, tag defaults
    fragments/
        core_concept.md              # what a finding model is
        naming.md                    # lowercase / acronym / brand / eponym / self-describing / conciseness
        synonym_rules.md             # strictness + collision check procedure
        presence_and_change.md       # presence + change-from-prior discipline (winnowing)
        associated_vs_component.md   # independent-vs-intrinsic split
        scope_and_specificity.md     # subtype rule + compound "and/or" splitting
        session_defaults.md          # how to ask user + reference defaults.yml
        search_and_triage.md         # findingmodel search + triage decisions
        create_invocation.md         # create_model.py CLI cheatsheet
        mechanical_lint.md           # review_model.py CLI + severity interpretation
        quality_checklist.md         # self-contained, one-liner per rule
        review_file_generation.md    # output format + rules for reviews/review_*.md
        tui_handoff.md               # review_summaries.py prompt + keybindings
        csv_writeback.md             # update_csv.py
        enrichment.md                # make-info + fix_stub.py (author flow only)
```

**Deleted outright:**
- `.claude/skills/new-finding/` (the folder)
- `.claude/skills/new-finding.md` (parallel top-level skill file — second copy with same content)
- `.claude/skills/new-finding-workspace/`
- `prompts/{create,merge,review,single}_agent.md`
- `prompts/new_finding_workflow.md`
- `prompts/conventions.md` (after distillation into fragments)
- `prompts/naming_rules.md`
- `.claude/skills/new-finding/scripts/bulk_review_fix.py`

**Rewritten (not deleted):**
- `docs/review_summaries_tui.md` — currently points at `.claude/skills/new-finding/review_file_agent.md` in three places (lines 5, 38, 46). Must be updated to reference the `review_file_generation.md` fragment and whichever new skill owns it (`finding-batch` primarily, `finding-review` secondarily).

## Skill-level behavior

### `finding-author` (single interactive)

Activates when the user wants to work with a single radiology finding in conversation — check existence, add a synonym, or draft a new model. Not for list/CSV/directory work (→ `finding-batch`) and not for walking through existing files to improve them (→ `finding-review`).

Flow, main skill inline throughout:

1. Session-start: read `session_defaults.md` + `defaults.yml`, ask user to confirm source / contributors / tags if not yet set for this session.
2. Search: apply `search_and_triage.md`.
3. Triage decision with user.
4. If synonym update: read target file, collision-check, edit, show diff.
5. If create: apply `naming.md` + `synonym_rules.md` + `scope_and_specificity.md` to draft, call `create_model.py` per `create_invocation.md`.
6. Mechanical lint via `mechanical_lint.md`.
7. Quality review: spawn one sub-agent with `core_concept.md` + `quality_checklist.md` + the new file path. Apply fixes.
8. Show final model to user. No TUI step.
9. Optional enrichment per `enrichment.md`.

### `finding-batch` (list / CSV / directory → many models)

Activates only when user hands over a list, CSV, or directory as a unit of work, or explicitly says "batch". Otherwise → `finding-author` per-finding.

Input shapes: CSV (finding names + optional description/synonym columns), directory of markdown stubs, plain pasted list.

Flow:

1. Session-start (same as author).
2. Triage pass, main skill inline, whole batch visible: bulk search every row, classify match / close / no-match, surface cross-row duplicates to the user.
3. **Draft pass — fan-out, one sub-agent per no-match finding, parallel groups of 5.** Each sub-agent loads `core_concept.md` + `naming.md` + `synonym_rules.md` + `scope_and_specificity.md` + `session_defaults.md` + the row/content for its one finding only. Returns `{name, description, synonyms}`.
4. Main skill assembles batch config, runs `create_model.py --batch`.
5. Mechanical lint over created files.
6. **Quality review pass — fan-out, one sub-agent per created finding, parallel groups of 5.** Each sub-agent loads `core_concept.md` + `quality_checklist.md` + one file path.
7. Main skill applies fixes from quality reports.
8. Main skill writes `reviews/review_*.md` files inline per `review_file_generation.md`, splitting large batches into ~8-10-entry groups.
9. TUI handoff per `tui_handoff.md`. Mandatory.
10. User returns — main skill reads back responses, applies requested changes.
11. CSV writeback per `csv_writeback.md` if working from a CSV.

### `finding-review` (existing files)

Activates when user names existing `.fm.json` files by path, glob, or directory and asks to review / audit / improve — not create.

Flow:

1. Soft-refuse if `defs/` has uncommitted changes; prompt user to commit/stash or pass `--allow-dirty`.
2. Mechanical lint via `review_model.py --fix` on ERRORs only. Show diff to user.
3. **Quality review pass — fan-out, one sub-agent per file, parallel groups of 5.** Each sub-agent loads `core_concept.md` + `quality_checklist.md` + one file path. Returns suggested edits.
4. Main skill applies edits.
5. Main skill writes `reviews/review_*.md` per `review_file_generation.md`.
6. TUI handoff per `tui_handoff.md`. Mandatory.
7. User returns — main skill reads responses. For each entry: accept, revert via git, or iterate further edits.

## Sub-agent invocation pattern

All sub-agent spawns follow the same pattern:

- Sub-agent receives: the substep's instruction paragraph, an explicit list of fragment file paths to read, and the input artifact path(s) for its one finding / one file.
- Sub-agent does NOT see prior findings, prior conversation, or neighbor files.
- Main skill fans out in parallel groups of 5, collects structured returns (JSON for draft, issues list for review), and proceeds.
- The fragments plus the input are the entire context; no shared preamble from the main skill leaks in.

## Skill descriptions (behavior-only, no modality)

```
finding-author:
  Use when the user wants to work with a single radiology finding interactively —
  checking whether it exists in defs/, adding a synonym to an existing model,
  or drafting a new finding model. Covers a small handful of findings discussed
  one at a time in conversation. For list/CSV/directory-driven creation, use
  finding-batch instead. For walking through existing model files to propose
  improvements, use finding-review.

finding-batch:
  Use when the user hands over a list, CSV, or directory of source content
  describing many findings at once and asks to create models for them in bulk.
  Includes triage, per-finding drafting, mechanical + quality review, human
  TUI sign-off, and CSV writeback. For one-at-a-time interactive work, use
  finding-author.

finding-review:
  Use when the user names existing .fm.json files (by path, glob, or directory)
  and asks for review, audit, cleanup, or quality improvements — without creating
  new findings. Includes mechanical lint, per-file LLM quality review, and human
  TUI sign-off. For creating new findings, use finding-author or finding-batch.
```

Each description ends with a negative cross-reference to the sibling skills — the most reliable disambiguator in practice.

## `defaults.yml` schema

```yaml
contributors:
  people:
    <key>: { name: "...", email: "...", organization_code: "..." }
  organizations:
    <code>: { name: "...", url: "..." }

sources:
  <code>: { description: "..." }

tag_defaults:
  # Suggested tag sets by context; skill asks user to confirm per session.
  - name: head-ct
    tags: ["head", "CT", "finding"]
  - name: knee-mri
    tags: ["knee", "MRI", "finding"]
```

`session_defaults.md` tells Claude: read this file, ask user which source / contributors / tags apply to this session, reuse the answer for the rest of the conversation.

## Trigger-evals

One JSON per skill. Each contains `should_trigger: true` cases that sound like the skill's domain and `should_trigger: false` cases that should route elsewhere. Example prompts explicitly mix modalities (head CT, knee MRI, abdominal US, CXR) so no modality vocabulary becomes an activation anchor. Each skill's eval includes the other two skills' positive prompts as `should_trigger: false` boundary cases.

## Execution phasing (green-field, one PR)

New branch off `main`: `chore/rebuild-finding-skills`.

**Phase 0 — in-repo plan artifact.** Per the user's global CLAUDE.md rule that plans must be tracked in the repository, copy this plan to `docs/plans/rebuild-finding-skills.md` (create `docs/plans/` if absent). Each subsequent phase updates that file to record progress and decisions. `/Users/talkasab/.claude/plans/misty-floating-naur.md` is the draft; the tracked repo copy is the source of truth during execution.

**Phase 1 — rule fragments (first review checkpoint).**
Write `core_concept.md`, `naming.md`, `synonym_rules.md`, `presence_and_change.md`, `associated_vs_component.md`, `scope_and_specificity.md`. User reviews this family before phase 2.

**Phase 2 — substep fragments.**
Write `session_defaults.md`, `search_and_triage.md`, `create_invocation.md`, `mechanical_lint.md`, `csv_writeback.md`, `enrichment.md`. Write `prompts/defaults.yml`. User reviews.

**Phase 3 — review fragments.**
Write `quality_checklist.md`, `review_file_generation.md`, `tui_handoff.md`. User reviews.

**Phase 4 — scripts move + in-flight fixes.**
Move `create_model.py`, `fix_stub.py`, `review_model.py`, `update_csv.py` from `.claude/skills/new-finding/scripts/` to `scripts/finding_authoring/`. Drop `bulk_review_fix.py` entirely. Two addenda inside this phase:

1. **External-reference grep first.** Before moving, grep the repo for any reference to `.claude/skills/new-finding/scripts/` outside the skill folder itself. Anything found outside the folder must be updated in the same commit as the move, or the reference silently breaks.
2. **Fix the CONTRIBUTORS dict gap.** `create_model.py` and `fix_stub.py` each contain a `CONTRIBUTORS` dict missing entries for `MGB`, `MSFT`, and `RSNA` — organization codes referenced as `organization_code` on the person entries. `prompts/defaults.yml` now lists all of them. Add matching entries to both scripts (sync the two dicts) so a user invoking `--contributor talkasab MGB` does not fail.

**Phase 5 — skills.**
Write `finding-author/SKILL.md`, `finding-batch/SKILL.md`, `finding-review/SKILL.md`. User reviews.

**Phase 6 — trigger-evals.**
Write one JSON per skill, modality-mixed, with cross-skill boundary cases.

**Phase 7 — deletion.**
Delete `.claude/skills/new-finding/`, `.claude/skills/new-finding.md` (the duplicate top-level file), `.claude/skills/new-finding-workspace/`, `prompts/{create,merge,review,single}_agent.md`, `prompts/new_finding_workflow.md`, `prompts/conventions.md`, `prompts/naming_rules.md`. Keep `prompts/proposed_attribute_synonyms.md` — it tracks alternative value wordings for a future schema upgrade.

**Phase 8 — docs + repo-level references.** Rewrite `docs/review_summaries_tui.md` to reference the new fragment (`prompts/fragments/review_file_generation.md`) and the owning skills (`finding-batch`, `finding-review`). Update `CLAUDE.md` (the project one, not the user's global) to replace `new-finding` references with the three new skill names. Update the `CHANGELOG.md` with a user-facing one-liner: "Replaced new-finding skill with finding-author, finding-batch, and finding-review — narrower activation, cross-finding context isolation in batch and review flows." Grep the repo for `new-finding`, `new_finding_workflow`, `{create,merge,review,single}_agent`, `bulk_review_fix`, `new-finding-workspace` — every match must either be under the tracked plan artifact or inside `CHANGELOG.md`.

**Phase 9 — end-to-end verification** (below). This phase must come AFTER deletion and docs migration so the zero-dead-reference check in verification is meaningful.

**Phase 10 — final plan-artifact update + PR.** Mark `docs/plans/rebuild-finding-skills.md` complete (status block at top). Open PR.

## Verification (phase 9)

**Ground rules for verification:**

- All verification runs happen on a **scratch/throwaway branch** forked from the refactor branch, or with changes explicitly reverted at the end via `git checkout defs/ lists/ text/ index.md ids.json`. Verification must NOT land real product-data changes in the PR. Only the infra changes (skills, fragments, scripts move, docs) ship.
- After any `.fm.json` create/edit in verification, run `uv run scripts/validator.py` and confirm `text/`, `index.md`, `ids.json` regenerate cleanly. This is the repo-required workflow per `CLAUDE.md`. Failure here is a verification failure regardless of whether the skill "looked fine" in chat.

**Flow verifications:**

- **finding-author single-create**: pick any finding the repo lacks (cross modalities — don't reuse the same head-CT example every run). Confirm session-start asks source/contributors/tags, search runs, triage question asked, `create_model.py` invoked, mechanical lint runs, quality-review sub-agent fires, final model shown, NO TUI step. Then run `uv run scripts/validator.py`. Then revert.
- **finding-author synonym-update**: pick an existing model; add a throwaway synonym. Confirm collision check runs, edit applied, diff shown. Run validator. Revert.
- **finding-batch CSV**: use a synthetic 5-row CSV in a temp path (not `lists/headct_findings.csv`, to keep product lists untouched). Confirm triage table, per-finding draft sub-agents (verify no cross-finding contamination by reading transcript), batch creation, per-file review sub-agents, `reviews/review_*.md` written, TUI handoff surfaced, CSV writeback after approval. Run validator. Revert.
- **finding-batch directory of markdown**: stage 3-4 markdown stubs in a temp dir. Confirm same flow, no CSV writeback. Validator. Revert.
- **finding-batch pasted list**: paste 3-5 finding names in chat. Confirm same flow. Validator. Revert.
- **finding-review explicit list**: pick 3 existing `.fm.json` files. Confirm soft-refuse on dirty defs/, mechanical auto-fix, per-file quality sub-agents, edits applied, review file written, TUI surfaced. Validator. Revert.
- **finding-review glob**: run against a small glob like `defs/*_fracture.fm.json`. Same flow. Validator. Revert.

**Skill activation:**

- Run each skill's `trigger-eval.json` against its description; confirm `should_trigger` values match. Cross-skill boundary prompts verify that exactly one skill activates per prompt (no dual-fire, no wrong-fire).
- Trigger-eval location compatibility check: before committing to `.claude/skills/<skill>/trigger-eval.json` per-skill, verify the evaluation tooling (whatever currently consumes `.claude/skills/new-finding-workspace/trigger-eval.json`) accepts the new location. If the tooling requires a centralized `*-workspace/` sibling, adjust the target structure accordingly during Phase 6. This is a prerequisite check, not a post-hoc finding.

**Repo-level hygiene:**

- **No dead references**: grep the repo for `new-finding`, `new_finding_workflow`, `{create,merge,review,single}_agent`, `bulk_review_fix`, `new-finding-workspace` — expect zero matches anywhere except inside `CHANGELOG.md` (which legitimately records the rename) and inside `docs/plans/rebuild-finding-skills.md` (the tracked plan history).
- **No orphan skill files**: confirm `.claude/skills/` contains exactly the three new skill folders and no stray `new-finding*.md` or `new-finding*/` entries.
- **Skill-file size**: each `SKILL.md` ≤ 100 lines; each fragment ≤ 80 lines (soft target).

## Clarifications from reviewer

- **`--allow-dirty` is a conversational override, not a CLI flag.** `finding-review`'s soft-refuse on dirty `defs/` is implemented in skill prose, not in `review_model.py`. The skill prompt tells the user: "Your `defs/` working tree has uncommitted changes. Commit or stash first, or tell me 'proceed anyway' to override." There is no flag on any Python script; the override is the user saying so in chat. `SKILL.md` for `finding-review` must state this explicitly.
- **Trigger-eval location compatibility** is called out as a Phase-6 prerequisite check above rather than a post-hoc discovery.
