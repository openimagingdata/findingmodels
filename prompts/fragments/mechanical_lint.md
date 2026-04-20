# Mechanical lint

`scripts/finding_authoring/review_model.py` runs a fast, deterministic set of checks on one or more `.fm.json` files. No LLM judgment involved — pure pattern checks.

## Running it

```bash
# Single file
uv run --env-file .env scripts/finding_authoring/review_model.py defs/<filename>.fm.json

# Multiple files or a glob
uv run --env-file .env scripts/finding_authoring/review_model.py defs/*.fm.json

# Auto-fix what is safely auto-fixable (underscores → spaces, self-synonyms removed, etc.)
uv run --env-file .env scripts/finding_authoring/review_model.py --fix defs/<filename>.fm.json

# Errors only (skip warnings and review items)
uv run --env-file .env scripts/finding_authoring/review_model.py --errors-only defs/*.fm.json

# Machine-readable output
uv run --env-file .env scripts/finding_authoring/review_model.py --json defs/<filename>.fm.json
```

## What it checks

- Underscores in JSON name fields (should be spaces)
- Lowercase convention on names and synonyms
- Standard attribute structure: `presence` first with required values, `change from prior` second with required minimum values
- Choice attributes have ≥ 2 values
- `associated findings` structure (one multichoice attribute, not scattered `presence of X`)
- Contributor completeness
- Placeholder or empty descriptions
- Duplicate presence / change-from-prior attributes

## Severity levels

The script labels each finding with one of three levels — the distinction matters for how you respond.

- **ERROR** — a definite problem. Auto-fixable by `--fix` where the fix is unambiguous. Every ERROR must be resolved.
- **WARNING** — likely a problem but needs human confirmation. Not auto-fixed. Address each one; if you're intentionally overriding, note why.
- **REVIEW** — needs LLM judgment. The script flags the location and what to look at; the quality-review step (`quality_checklist.md`) is where these get resolved.

## Companion helper for the "missing change from prior" ERROR

Older models sometimes have only a `presence` attribute and fail the lint with "Model has 1 attribute — need at least 2." Add the missing attribute with:

```bash
uv run --env-file .env scripts/finding_authoring/add_change_from_prior.py \
    defs/<file>.fm.json \
    --pairs larger-smaller,worsened-improved
```

`--pairs` is comma-separated: `larger-smaller`, `increased-decreased`, `worsened-improved`. Omit for the minimum set (`unchanged, stable, new, resolved`). The helper allocates exactly one new `oifma_id` and leaves all existing IDs untouched — do **not** hand-build attributes or use `findingmodel.tools.add_ids_to_model`, which strips and regenerates IDs when the model is loaded as a base class.

### Winnowing or extending an existing change-from-prior

When the attribute exists but quality review wants to drop/add specific direction values (the common "winnow after create_model.py" pattern), use:

```bash
# Drop inappropriate pairs
uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \
    defs/<file>.fm.json --remove larger,smaller

# Add missing pairs
uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \
    defs/<file>.fm.json --add worsened,improved

# Both in one call
uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \
    defs/<file>.fm.json --remove increased,decreased --add worsened,improved
```

Core values (`unchanged`, `stable`, `new`, `resolved`) cannot be removed. Existing `value_code`s are preserved for values that remain; new values get fresh codes beyond the highest currently used. Idempotent — adding a value already present is a no-op.

### Renaming a finding model

When quality review decides the canonical name should change (e.g., scope-anchor fix like `parenchymal hypoattenuation` → `brain parenchymal hypoattenuation`), use:

```bash
uv run --env-file .env scripts/finding_authoring/rename_model.py \
    defs/<old_file>.fm.json --new-name "new canonical name"
```

This renames the file on disk, updates the `name` field, and updates every attribute/value description that embeds the old name. Preserves `oifm_id`, all `oifma_id`s, and all `value_code`s.

## Using it in flow

- **Authoring flow.** Run without `--fix` after `create_model.py` to see ERRORs and WARNINGs. Fix ERRORs (or re-run with `--fix`). Pass REVIEWs to the quality-review sub-agent.
- **Review flow.** Run `--fix` first to clear the trivially-fixable ERRORs on the files being reviewed, then hand the same files to per-file quality-review sub-agents.

## Do not

- Do not treat WARNINGs as optional — resolve them.
- Do not use `--fix` blindly on files with uncommitted changes. If `defs/` is dirty, commit or stash first. `finding-review` soft-refuses in that state; single-create flows should still sanity-check.
- Do not run `--fix` to make the lint "pass" while ignoring what it was pointing at. Fixes are mechanical, not semantic — always eyeball the diff.
