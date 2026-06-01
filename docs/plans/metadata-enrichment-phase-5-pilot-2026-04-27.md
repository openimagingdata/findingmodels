# Metadata Enrichment Phase 5 Pilot Run

> Superseded for active execution by `/Users/talkasab/repos/findingmodel-metadata/docs/plans/metadata-enrichment-current-readiness-2026-05-24.md`. Keep this file as historical evidence only; pull any still-useful decisions into the tool-repo active plan, review evidence register, or a stable reference doc before acting on them.


Status: Superseded for active execution; retained as historical evidence

## Goal

Run the representative metadata enrichment pilot and use the HTML review workflow as the gate before
broader enrichment. The pilot-enriched `defs/*.fm.json` files are branch working state for review and
iteration, not publishable artifacts.

## Execution Plan

1. Select about 150 representative pilot files with `scripts/metadata_select_pilot.py`.
2. Run pilot enrichment from the manifest with `scripts/metadata_assign_batch.py`, concurrency `3`,
   Logfire enabled, and `.metadata-runs/pilot-ontology-cache.duckdb`.
3. Generate the reviewer-facing app with `scripts/metadata_review_package.py`; use
   `.metadata-runs/review-current/index.html` as the primary review surface.
4. Complete human review in the review app and export the structured review JSON.
5. Ingest exported review JSON with `scripts/metadata_ingest_review.py`.
6. Run `scripts/validator.py` after pilot enrichment and any accepted fixes.
7. Review batch failures, warnings, low-confidence fields, auditor flags, ontology-cache evidence,
   and representative Logfire traces.
8. Triage every pilot item as accepted, fixed, or explicitly deferred with rationale before Phase 6.
9. Update this plan, `docs/metadata-enrichment-setup.md`, and any relevant changelog or development
   log documents with the final pilot outcome.

## Commands

```bash
uv run scripts/metadata_select_pilot.py \
  --defs-dir defs \
  --target-count 150 \
  --output-dir .metadata-runs/pilot
```

When running inside a sandboxed local environment, keep DuckDB extension/cache writes inside ignored
run artifacts:

```bash
env HOME=/Users/talkasab/repos/findingmodels-metadata/.metadata-runs/home \
  XDG_CACHE_HOME=/Users/talkasab/.cache \
  uv run --env-file .env scripts/metadata_assign_batch.py \
  --manifest .metadata-runs/pilot/pilot_manifest.json \
  --run-dir .metadata-runs/pilot-enrichment \
  --ontology-cache .metadata-runs/pilot-ontology-cache.duckdb \
  --concurrency 3 \
  --logfire
```

```bash
uv run --env-file .env scripts/metadata_assign_batch.py \
  --manifest .metadata-runs/pilot/pilot_manifest.json \
  --run-dir .metadata-runs/pilot-enrichment \
  --ontology-cache .metadata-runs/pilot-ontology-cache.duckdb \
  --concurrency 3 \
  --logfire
```

```bash
uv run --env-file .env scripts/metadata_review_package.py \
  --run-dir .metadata-runs/pilot-enrichment
```

```bash
uv run scripts/metadata_ingest_review.py <exported-review-json> \
  --output .metadata-runs/pilot-review-ingest.json
```

```bash
uv run scripts/validator.py
```

## Gate

Do not proceed to Phase 6 until the review export is ingested, every pilot item is accepted, fixed,
explicitly deferred with rationale, or marked not applicable with rationale, and the Phase 5 recovery
work in the coordinated package plan is complete.

Current gate status as of 2026-05-01:

- Pilot review is complete and ingested.
- A tracked resolution worksheet now exists at
  `docs/plans/metadata-enrichment-phase-5-feedback-resolution-2026-05-01.md`.
- Phase 6 remains blocked until the Phase 5 gate is explicitly closed in tracked documentation. The
  pilot feedback rows now have fixed, deferred-with-rationale, or not-applicable-with-rationale
  dispositions, and the deterministic pilot audit reports zero flags.
- Full-corpus enrichment must wait for explicit Phase 5 gate closure.
- Phase 5 recovery targeted rerun has started:
  - `.metadata-runs/phase5-targeted-rerun-hardened-v3/status.jsonl` completed 30 targeted items
    after deterministic anatomy exact-match expansion and single-item recovery for
    `early_intrauterine_pregnancy`.
  - `.metadata-runs/phase5-targeted-review-hardened-v3/index.html` contains the complete 30-item v3
    review app.
- The recovery gate source work is complete for Phase 5: confidence warnings are fixed in the
  targeted review data, the resolved targeted review app has been regenerated from the corrected
  source records, and final gate closure should be documented before Phase 6.
- The v3 targeted review export had 21 approved items and 9 feedback items. The v3 outputs were
  accepted into `defs/`, the 9 feedback items were corrected, and matching Markdown was regenerated
  for all 30 targeted items.
- A broader source patch pass applied the remaining unambiguous pilot feedback. The 150 pilot JSON
  records and their generated Markdown now validate, and the resolution worksheet records fixed,
  deferred-with-rationale, or not-applicable-with-rationale status for every pilot feedback row.
- The deterministic package auditor was rerun over the 150 pilot records using
  `.metadata-runs/phase5-recovery-ontology-cache.duckdb` with `scripts/metadata_audit.py
  --deterministic-only` and reports zero flags in
  `.metadata-runs/phase5-pilot-deterministic-audit/audit_summary.json`.
- A tracked feedback-to-tooling coverage matrix now exists at
  `docs/plans/metadata-enrichment-feedback-tooling-coverage-2026-05-05.md`. The current matrix shows
  that many reviewed records are corrected in source but still need clean-input tool evidence before
  a larger corpus run should be recommended.
- A 73-record clean-input dry run using the hardened tool completed successfully but did not
  reproduce enough reviewed corrections from clean inputs. The analysis is tracked at
  `docs/plans/metadata-enrichment-clean-input-rerun-analysis-2026-05-05.md`; it found 76 reviewed
  field mismatches across 58 of the 73 records, mostly expected time course and anatomy selection.
  The larger corpus run remains blocked by this tooling-coverage gap.
- Current post-feedback targeted review app:
  `.metadata-runs/phase5-targeted-review-resolved-v1/index.html`.

## Execution Notes

- Pilot selection completed with 150 files in `.metadata-runs/pilot/pilot_manifest.json`.
- Initial enrichment exposed two tooling issues before review:
  - DuckDB extension writes defaulted to the user home; the local pilot command now sets `HOME` to
    `.metadata-runs/home`.
  - Short ontology labels such as `T1` and `T2` produced invalid `IndexCode.display` values. The
    support package was patched so too-short ontology labels are omitted from `display`.
- The support package was also patched so ontology-cache connections avoid unnecessary FTS/VSS
  extension loading and close path-owned cache connections in assignment/audit paths.
- Local wheels were rebuilt from `/Users/talkasab/repos/findingmodel-metadata` and copied to
  `.metadata-runs/wheelhouse/current/`.
- Targeted retries completed all pilot items. Latest manifest status is 150 covered items with 150
  review artifacts and 150 audit artifacts.
- Review app regenerated at `.metadata-runs/review-current/index.html`.
- `uv run scripts/validator.py` completed successfully after pilot enrichment.
- Pre-review run summary:
  - model used: `openai:gpt-5.4-mini`
  - run warnings: 2 items, both ignored broader ontology selections
  - field confidence entries below high: 354 total (`250` medium, `104` low)
  - auditor flags: 63 total (`14` high, `45` medium, `4` low)
  - ontology cache rows: 751 (`202` canonical selected, `385` rejected candidate, `164` related
    candidate)
- Human review export was copied to
  `.metadata-runs/review-exports/talkasab-mgh-harvard-edu-metadata-enrichment-review-responses.json`.
- Review ingestion summary was written to `.metadata-runs/pilot-review-ingest.json`.
- Human review is complete: 150 total, 150 done, 46 approved, 104 feedback, 0 drafts, 0 remaining.
- `pilot-review-ingest.json` contains 105 actionable notes because
  `mta_scale_for_medial_temporal_lobe_atrophy__scheltens_classification_` was approved with a
  non-empty reviewer comment.
- Feedback themes requiring tool changes before full-corpus enrichment:
  - expected time course was the dominant issue;
  - anatomic location selection missed obvious anatomy or selected overly specific/wrong anatomy;
  - age and sex specificity were often too restrictive or omitted;
  - ontology/index-code feedback included missing expected codes, over-broad/over-specific codes,
    modality-specific codes on multi-modality findings, and inappropriate classification codes;
  - confidence output used invalid keys such as `ontology_decisions` and `anatomic_decisions`.

## Superseded Next Step

Carry out Phase 5 recovery before Phase 6:

1. Implement package/tool hardening from the coordinated plan in
   `/Users/talkasab/repos/findingmodel-metadata/docs/plans/coordinated-metadata-enrichment-and-dual-db-release-2026-04-26.md`.
2. Produce a tracked resolution worksheet for all 104 feedback items.
3. Mark each feedback item fixed, explicitly deferred with rationale, or not applicable with
   rationale.
4. Rebuild local wheels and refresh `.metadata-runs/wheelhouse/current/`.
5. Run the targeted rerun subset through `scripts/metadata_assign_batch.py`,
   `scripts/metadata_review_package.py`, and the HTML review app.
6. Run `scripts/validator.py`.
7. Advance only if the targeted rerun shows no unresolved systematic anatomy, time-course, age/sex,
   ontology-code, confidence, or auditor-coverage failure pattern.

## Review App Follow-Up

- Completed: Make potentially missing values visible in the main review surface instead of letting empty fields
  disappear, especially `anatomic_locations`.
- Completed: Keep the optional `etiologies` row visible even when blank, so reviewers can distinguish
  an intentionally empty etiology field from a missing display row.
- Completed: Use field confidence as a reviewer attention signal only when confidence is below high; do not add
  visible high-confidence labels to every field.
- Regenerated `.metadata-runs/review-current/index.html` after these review-surface changes.
- Completed: Make embedded review data an explicit generator mode. `index.html` embeds the dataset by
  default for single-file handoff, while `--no-embed-data` keeps the adjacent `review-data.json`
  loading mode available.
- Completed: Embedded mode separates the HTML review tool from the preserved dataset JSON:
  `.metadata-runs/review-current/` contains the active single-file `index.html` handoff, and
  `.metadata-runs/review-current-data/review-data.json` preserves the underlying review dataset.
- Completed: Require reviewer identity at page load when no reviewer identifier exists in local
  storage. The sidebar now shows the current reviewer and a change button instead of a persistent
  edit field, and the four queue counts are larger icon-only counters in one row.
- Completed: Created a separate concise single-file HTML quick-reference page for reviewers at
  `.metadata-runs/review-instructions/index.html`, with focused Playwright screenshots embedded
  directly in the page for portable handoff.
