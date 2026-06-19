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

For CDEStaging chunk outputs, use paths under `defs/from_cdestaging_ct_chest/`.

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

## Companion helpers

When `change from prior` needs to be added or winnowed:

- `scripts/finding_authoring/add_change_from_prior.py` — add missing `change from prior` attribute
- `scripts/finding_authoring/modify_change_from_prior.py` — add/remove direction-of-change values

Do **not** hand-build attributes in ways that regenerate IDs.

## Using it in flow

- **CDEStaging batch.** After convert, run `--fix` on the chunk's output files. Pass remaining REVIEW items to quality-review sub-agents per `quality_checklist.md`.
- **Review flow.** Run `--fix` first to clear trivially-fixable ERRORs, then hand files to per-file quality-review sub-agents.

## Do not

- Do not treat WARNINGs as optional — resolve them.
- Do not use `--fix` blindly on files with uncommitted changes you care about. Eyeball the diff.
- Do not run `--fix` to make the lint "pass" while ignoring what it was pointing at. Fixes are mechanical, not semantic.
