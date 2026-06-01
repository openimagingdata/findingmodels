# Metadata Regression Floor

Status: Seed set created 2026-05-05

This directory stores reviewed metadata expectations that every targeted metadata-enrichment rerun
should carry as a floor. The goal is to catch prompt or validator drift while fixing the current
clean-input mismatch classes.

Use `manifest.json` to run the selected records through `scripts/metadata_assign_batch.py`. Use
`regression-floor-v1.json` as data for comparison tooling. Each record stores only the metadata
fields that should be compared, not the full finding definition.

Compare a completed targeted run with:

```bash
uv run scripts/metadata_compare_regression_floor.py \
  --floor evals/regression_floor/regression-floor-v1.json \
  --run-dir .metadata-runs/phase6-targeted-v1/run
```

Coverage notes:

- The seed set uses records marked `targeted rerun evidence exists` in the feedback coverage matrix.
- The set covers time course, anatomy, measurement scope, device dwell/placement, broad whole-body
  findings, ontology exactness, pediatric age handling, sex-specific anatomy, and age-neutral cases.
- No reviewed PET/molecular-imaging pilot case was available in the coverage matrix. Add one before
  treating this as a complete regression floor for molecular imaging behavior.

Phase 6 targeted rerun result:

- Run directory: `.metadata-runs/phase6-targeted-v1/run`
- Records with outputs: 10 of 10 floor records
- Fields compared: 95
- Strict mismatches after correcting `tunneled_catheter` and `radiolucent_urinary_calculus`
  expectations: 1 `anatomic_locations` mismatch
- Deterministic audit flags on floor records: 0

Phase 6 floor-only rerun after deterministic parent-covers-parts normalization:

- Run directory: `.metadata-runs/phase6-targeted-v6-floor/run`
- Records with outputs: 10 of 10 floor records
- Fields compared: 95
- `radiolucent_urinary_calculus` now outputs only `urinary tract`
- Strict mismatches: 4, from other behavior classes
- Deterministic audit flags on floor records: 0
