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

## Smoke Commands

Run these from this repository after the wheelhouse is populated.

```bash
uv run scripts/validator.py
```

```bash
uv run scripts/metadata_select_pilot.py --defs-dir defs --target-count 5 --output-dir .metadata-runs/smoke-pilot
```

```bash
uv run --env-file .env scripts/metadata_assign_batch.py --dry-run --logfire --run-dir .metadata-runs/smoke-enrichment --ontology-cache .metadata-runs/smoke-ontology-cache.duckdb --concurrency 3 defs/abdominal_abscess.fm.json defs/aortic_dissection.fm.json defs/adrenal_nodule.fm.json
```

```bash
uv run --env-file .env scripts/metadata_review_package.py --run-dir .metadata-runs/smoke-enrichment
```

Open:

```text
.metadata-runs/review-current/index.html
```

## Pilot Shape

For the real pilot, select about 150 files, run enrichment with concurrency `3`, generate the review
app at `.metadata-runs/review-current/index.html`, complete human review there, and ingest the
downloaded review JSON with `scripts/metadata_ingest_review.py`.
