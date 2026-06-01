# Metadata Enrichment Setup

This branch uses unpublished metadata-aware packages from `../findingmodel-metadata`. The scripts in
`scripts/` use PEP 723 headers that expect local wheels in:

```text
.metadata-runs/wheelhouse/current/
```

## Build The Local Wheelhouse

From `../findingmodel-metadata`:

```bash
uv build --all-packages --wheel --out-dir /tmp/findingmodel-metadata-wheelhouse/current --no-create-gitignore
```

From this repository:

```bash
mkdir -p .metadata-runs/wheelhouse/current
cp /tmp/findingmodel-metadata-wheelhouse/current/*.whl .metadata-runs/wheelhouse/current/
```

The expected wheel files are:

```text
anatomic_locations-0.2.5-py3-none-any.whl
findingmodel-1.0.4-py3-none-any.whl
findingmodel_ai-0.2.1-py3-none-any.whl
oidm_common-0.2.7-py3-none-any.whl
oidm_maintenance-0.2.5-py3-none-any.whl
```

## Environment

Live enrichment commands read `.env` from this repository. It must include:

```text
OPENAI_API_KEY=...
BIONTOLOGY_API_KEY=...
```

Set `LOGFIRE_TOKEN` as well when running with `--logfire`.

For sandboxed local runs, keep DuckDB extension/cache writes inside ignored run artifacts by
prefixing live commands with:

```bash
env HOME=/Users/talkasab/repos/findingmodels-metadata/.metadata-runs/home XDG_CACHE_HOME=/Users/talkasab/.cache
```

## Smoke Commands

Run these from this repository after the wheelhouse is populated.

```bash
uv run scripts/validator.py
```

```bash
uv run scripts/metadata_select_pilot.py --defs-dir defs --target-count 5 --output-dir .metadata-runs/smoke-pilot
```

```bash
env HOME=/Users/talkasab/repos/findingmodels-metadata/.metadata-runs/home XDG_CACHE_HOME=/Users/talkasab/.cache uv run --env-file .env scripts/metadata_assign_batch.py --dry-run --logfire --run-dir .metadata-runs/smoke-enrichment --ontology-cache .metadata-runs/smoke-ontology-cache.duckdb --concurrency 3 defs/abdominal_abscess.fm.json defs/aortic_dissection.fm.json defs/adrenal_nodule.fm.json
```

```bash
uv run --env-file .env scripts/metadata_review_package.py --run-dir .metadata-runs/smoke-enrichment
```

By default, the generated `index.html` embeds the review dataset so the HTML file can be shared and
opened directly without a local server. In this mode, `review-current/` contains only `index.html` as
the active handoff artifact, and the preserved review JSON is written to the sibling
`review-current-data/review-data.json`. Use `--no-embed-data` only when you want `index.html` to load
an adjacent `review-data.json` file instead.

Open:

```text
.metadata-runs/review-current/index.html
```

## Pilot Shape

For the real pilot, select about 150 files, run enrichment with concurrency `3`, generate the review
app at `.metadata-runs/review-current/index.html`, complete human review there, and ingest the
downloaded review JSON with `scripts/metadata_ingest_review.py`.

If local wheel files are rebuilt without changing package versions, force `uv run` to reinstall them
with `--reinstall-package findingmodel --reinstall-package findingmodel-ai --reinstall-package
oidm-common --reinstall-package oidm-maintenance --reinstall-package anatomic-locations`.

## Phase 5 Recovery Notes

The Phase 5 recovery version of `scripts/metadata_assign_batch.py` opens one shared
`AnatomicLocationIndex` and passes it to both assignment and audit. After rebuilding local wheels
from `../findingmodel-metadata`, rerun commands with the same `--reinstall-package` options above so
the script uses the hardened confidence, anatomic-candidate, and auditor behavior.

The current Phase 5 recovery artifacts are local under `.metadata-runs/`. The latest complete
30-item targeted dry run after deterministic anatomy exact-match expansion is
`.metadata-runs/phase5-targeted-rerun-hardened-v3/`, with review app
`.metadata-runs/phase5-targeted-review-hardened-v3/index.html`. After human feedback was applied to
the source records, the current source-derived targeted review app is
`.metadata-runs/phase5-targeted-review-resolved-v1/index.html`, with preserved review data in
`.metadata-runs/phase5-targeted-review-resolved-v1-data/review-data.json`.

The Phase 5 deterministic audit uses `scripts/metadata_audit.py --deterministic-only` with the
merged recovery ontology cache at `.metadata-runs/phase5-recovery-ontology-cache.duckdb`, which
combines pilot evidence with accepted v3 targeted evidence. The latest pilot audit summary is
`.metadata-runs/phase5-pilot-deterministic-audit/audit_summary.json`.

Running `scripts/metadata_audit.py` without `--deterministic-only` also includes the LLM auditor
triage pass. Treat those flags as review signal, not as the deterministic gate result.

Use `scripts/metadata_review_package.py --source-only` only when reviewing current source JSON
directly rather than completed run outputs. Phase 6 remains blocked until the Phase 5 gate is
explicitly closed in tracked documentation.

## Approved Output Application

Reviewed metadata must be applied through the approved-output command, not by trusting generated
source diffs directly.

```bash
uv run scripts/metadata_apply_approved_outputs.py \
  --approved-outputs ../findingmodel-metadata/packages/findingmodel-ai/evals/fixtures/metadata_review_approved_outputs.json \
  --report-dir .metadata-runs/approved-output-apply \
  --write
```

The command writes `apply-report.json` plus per-record `before-after/*.before.json` and
`before-after/*.after.json` artifacts under the report directory. It verifies review-package and
reviewed-payload hashes before accepting approved records, and records before/after/source hashes in
the report. Items not present in the approved-output fixture are refused; this is how feedback and
unreviewed records stay out of the approved writeback path.

After applying approved outputs, regenerate derived text and the index:

```bash
uv run scripts/validator.py
```
