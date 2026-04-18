# CSV writeback

Used only in the batch flow when the source CSV should have OIFM IDs written back into it. CSV structure varies by project — **inspect first, decide with the user, then write**. Do not assume column positions.

## What you can assume

- The CSV has a header row.
- Every row has some form of **row ID** the user is using to track findings through the pipeline. Its column position is unknown until you look.
- You may or may not find an existing **OIFM ID column**. If none, you add one.

Everything else (delimiter, other columns, quoting, trailing blank lines) is per-file.

## Step 1 — inspect the CSV

```bash
head -1 <csv>           # header row
head -3 <csv>           # first couple of data rows for shape
```

Show the header and first data row to the user. Confirm:

- Which column is the row ID?
- Is there already an OIFM ID column? If yes, which one?
- If not, should we append a new `oifm_id` column to the end?

Record both column indexes (0-based) before proceeding.

## Step 2 — add the OIFM column if needed

`update_csv.py` will silently pad rows to reach the requested `--oifm-column` index, but it will **not** write a header name for a brand-new column. If you're adding the column, update the header yourself first so the new column has a name:

1. Read the CSV with the Read tool.
2. Append `,oifm_id` (or the user's preferred column name) to the header line.
3. Write the updated header back.
4. Use the new column index (`len(old_header_fields)`) for `--oifm-column`.

If the column already exists, skip this step and reuse its index.

## Step 3 — build the mapping

After `create_model.py --batch` finishes, its stdout is one `filepath|name|oifm_id` line per created model. Parse that output alongside the incoming batch (which knew each finding's source row ID) to build a `{rowID: oifm_id}` mapping. Feed the mapping to `update_csv.py` via `--mapping-stdin`.

## Step 4 — invoke

```bash
uv run --env-file .env scripts/finding_authoring/update_csv.py \
    <path/to/file.csv> \
    --id-column <N> \
    --oifm-column <N> \
    --mapping-stdin < mapping.json
```

Alternative mapping sources:

```bash
# Inline JSON
uv run --env-file .env scripts/finding_authoring/update_csv.py <csv> \
    --id-column <N> --oifm-column <N> \
    --mapping-json '{"<rowID>": "OIFM_..."}'

# Short comma-separated list on the command line
uv run --env-file .env scripts/finding_authoring/update_csv.py <csv> \
    --id-column <N> --oifm-column <N> \
    --mapping '<rowID>=OIFM_...,<rowID>=OIFM_...'
```

Exactly one of `--mapping`, `--mapping-json`, or `--mapping-stdin` must be provided.

## Script behavior worth knowing

- Rows whose row ID isn't in the mapping are left untouched.
- Rows whose OIFM column **already starts with `OIFM`** are left untouched (idempotent — re-running a mapping won't overwrite existing IDs).
- Rows shorter than the OIFM column are padded with empty strings up to the target column.
- Quoted fields containing commas are handled via Python's `csv` module, so arbitrary CSV dialects round-trip correctly.

## When to run it

Only after the batch has been **fully reviewed and approved** — quality review applied, human TUI sign-off returned, final edits landed. CSV writeback is the last step of the batch flow; OIFM IDs are only durable once everything upstream is settled.

## Don't

- Don't invent OIFM IDs — only write back IDs produced by `create_model.py`.
- Don't write to the real tracking CSV during verification runs. Use a scratch copy.
- Don't assume a previous campaign's column layout applies to this CSV. Always inspect.
- Don't let a `--mapping` argument silently drop entries — if the user expects 12 IDs written and the command reports fewer, stop and diagnose.
