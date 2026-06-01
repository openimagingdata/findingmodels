# Metadata Enrichment Plan History

Status: Historical consolidation; superseded by the tool-repo active plan
Date: 2026-05-24

## Purpose

This file consolidates the older metadata-enrichment planning and run-result documents in the data
repo so they no longer look like competing active plans.

The active plan lives in the tool repo:

- `/Users/talkasab/repos/findingmodel-metadata/docs/plans/metadata-enrichment-current-readiness-2026-05-24.md`

Older data-repo plan files are evidence and history. They should not be used as current execution
instructions unless their decisions have been pulled into the active plan or into a stable reference
document.

## Current Active Direction

For the data repo, the current direction is:

- preserve raw human review artifacts as provenance;
- keep metadata scripts and review tooling available;
- treat generated `defs/*.fm.json`, `text/*.md`, and `index.md` changes as untrusted until
  approved evidence is safely captured;
- clear generated source diffs from the active branch only after the tool-repo review evidence
  register satisfies Gate A;
- reapply approved source changes later only through an explicit approved-output application path.

## Still-Relevant Decisions Pulled Forward

- Human review is authoritative.
- The 150-item pilot human review export is complete and important evidence: 46 approved and 104
  feedback records.
- The 30-item targeted follow-up human review export is also authoritative and updates the latest
  effective review status for duplicated pilot records, producing the current 67 approved and 83
  feedback latest-status split.
- Feedback records must be dispositioned before another corpus batch.
- Generated source diffs are not gold.
- Phase 6/subagent triage is supporting evidence, not human gold.
- Regression-floor artifacts are useful but thin; they should be ported into the tool-repo review
  evidence/eval structure if used for readiness.
- The data repo should not carry release-bound generated source changes until the approved-output
  writeback path is proven.

## Historical Plan Groups

### Pilot review and feedback recovery

- `docs/plans/metadata-enrichment-phase-5-pilot-2026-04-27.md`
- `docs/plans/metadata-enrichment-phase-5-feedback-resolution-2026-05-01.md`
- `docs/plans/metadata-enrichment-feedback-tooling-coverage-2026-05-05.md`
- `docs/plans/metadata-enrichment-grading-compare-implementation-2026-05-05.md`
- `docs/plans/metadata-enrichment-clean-input-rerun-analysis-2026-05-05.md`
- `docs/plans/metadata-enrichment-clean-input-rerun-graded-comparison-2026-05-05.md`
- `docs/plans/metadata-enrichment-clean-input-mismatch-triage-2026-05-05.md`

These documents contain the most important human-review and feedback-resolution history. Their
review evidence should be harvested into the tool-repo review evidence register.

### Regression floor and dry-run results

- `docs/plans/metadata-enrichment-regression-floor-comparison-2026-05-05.md`
- `docs/plans/metadata-enrichment-regression-floor-results-*.md`
- `docs/plans/metadata-enrichment-200-record-dry-run-phase6-right-sized-v16-v17-2026-05-06.md`
- `docs/plans/metadata-enrichment-nongmts-gmts-review-pass-2026-05-09.md`

These are run-result records. Keep their useful facts, but do not treat them as active plans.

### Tooling and setup references

- `docs/metadata-enrichment-setup.md`
- `scripts/metadata_assign_batch.py`
- `scripts/metadata_audit.py`
- `scripts/metadata_review_package.py`
- `scripts/metadata_ingest_review.py`
- `scripts/metadata_apply_dry_run_outputs.py`
- `scripts/metadata_collate_review_decisions.py`

These scripts and setup notes remain useful operational material, but generated source updates must
wait for the Gate A evidence-preservation step.

### Separate data-repo work

- `docs/plans/definition_cleanup.md`
- `docs/plans/findingmodel-upstream-proposals.md`
- `docs/plans/prompt_length_research.md`
- `docs/plans/rebuild-finding-skills.md`

These are not part of the active metadata-enrichment cleanup unless explicitly pulled into a future
slice.

## Raw Review Evidence To Preserve

Known important local artifacts:

- `.metadata-runs/review-exports/talkasab-mgh-harvard-edu-metadata-enrichment-review-responses.json`
- `.metadata-runs/phase5-targeted-review-hardened-v3/talkasab-metadata-enrichment-review-responses.json`
- `.metadata-runs/pilot-review-ingest.json`
- `.metadata-runs/phase5-targeted-v3-review-ingest.json`
- `.metadata-runs/phase6-nongmts-gmts-review-v1/review-decisions.json`
- `.metadata-runs/phase6-nongmts-gmts-review-v1/review-data/review-data.json`
- `evals/regression_floor/regression-floor-v1.json`
- `evals/regression_floor/manifest.json`

## Closeout Audit: 2026-05-25

- Checked metadata/enrichment/prompt/pilot run-result plan files in this repo.
- Active execution remains in the tool repo:
  `/Users/talkasab/repos/findingmodel-metadata/docs/plans/metadata-enrichment-current-readiness-2026-05-24.md`.
- Metadata-enrichment plan/run-result files found in the closeout pass are marked superseded for
  active execution and retained as historical evidence.
- `docs/plans/prompt_length_research.md` is separate historical prompt research, not active
  metadata-enrichment cleanup direction.
