# Soft Tissue Head CT Finding Batch

## Goal

Create or link finding models for the `soft_tissue` rows in `lists/headct_findings.csv`, then update the source CSV with the resulting OIFM IDs if new models are created.

## Plan

1. Parse `lists/headct_findings.csv` and isolate rows where `category == "soft_tissue"`.
2. Triage each row against existing `defs/*.fm.json` models using complementary search terms and direct filename/name checks.
3. Identify rows that are organizational parents, already represented by existing models, ambiguous, or candidates for new model creation.
4. Confirm session defaults before writing new models:
   - Source: `OIDM`
   - Contributors: `hoodcm`, `MGB`
   - Tags: `["head", "CT", "finding"]`
5. Draft model inputs for rows that need new models, keeping each finding scoped to one noun-phrase concept.
6. Create models with `scripts/finding_authoring/create_model.py --batch`.
7. Run mechanical review with `scripts/finding_authoring/review_model.py`.
8. Review model quality, apply focused fixes, and write review files for TUI sign-off.
9. After TUI sign-off, write OIFM IDs back to `lists/headct_findings.csv` using the existing CSV update workflow.
10. Run repository validation and update this plan plus any relevant user-facing documentation if the final state differs from the planned state.

## Status

- Started: 2026-04-28
- Current phase: complete

## Created Models Pending Review

- `defs/soft_tissue_hematoma.fm.json` — `OIFM_OIDM_251841`
- `defs/subgaleal_hematoma.fm.json` — `OIFM_OIDM_185082`
- `defs/cephalohematoma.fm.json` — `OIFM_OIDM_401242`
- `defs/tonsillolith.fm.json` — `OIFM_OIDM_661237`

## Review File

- `reviews/review_headct_soft_tissue_1.md` — includes four newly created models and nine mappings to existing models.

## Review Outcome

- TUI review completed.
- `soft tissue hematoma`, `subgaleal hematoma`, `tonsillolith`, and all existing-model mappings were confirmed.
- `cephalohematoma` was updated to keep only `cephalhematoma` as a synonym; broader/fabricated subperiosteal scalp synonyms were removed.
- `lists/headct_findings.csv` now records OIFM IDs for all 13 `soft_tissue` rows.
- `uv run scripts/validator.py` completed successfully and regenerated derived files.
