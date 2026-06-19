# Review file generation

After a batch or set of models has been created/edited and has passed quality review, produce a human review file in `reviews/` that can be loaded by `scripts/review_summaries.py` for TUI sign-off.

This step is mechanical summarization — the models have already been reviewed. Read the files, restate each model briefly, flag only what needs human attention, and leave the response slot blank.

## Inputs you work from

- **Target review file path** — e.g., `reviews/review_cdestaging_chunk_1.md`.
- **List of changed or newly-created model files** — in display order.
- **Triage JSON** — e.g., `reviews/triage_cdestaging_chunk_1.json` for existing-match and skipped entries.
- **Context you already have** — edits made, quality-review warnings, judgment calls for sign-off.
- **Optional batch label** — e.g., "CDEStaging CT chest chunk 1 of 21".

## One entry per decision

The review file MUST include every chunk decision:

- **New model entries** — converted `.fm.json` files.
- **Existing-match entries** — triage linked CDEStaging source to DuckDB model; no new file created.
- **Skipped entries** — `user_skip` or unresolved `ambiguous` rows where convert was not run.

Preamble format: `<N> entries to review (X new, Y existing matches, Z skipped).`

## New model entry

For each converted file, produce one `###` entry with:

- `**Entry type:** new model`
- Finding name from the model.
- Source file, OIFM ID, description, synonyms, `change from prior` values.
- **CDEStaging fields:** source filename, source type (`json` or `md`), attribute count, anatomic location note.
- Questions/issues only when needed; otherwise `**Assessment:** Looks reasonable as written; confirm acceptable.`
- When Step 6 applied metadata changes, note what was changed (synonyms, description, tags, CFP winnow) so the reviewer can confirm. Flag only items that still need judgment.
- Note whether source-carried `presence` / `status` / `temporal change` attributes were removed in favor of the standard `presence` and `change from prior` attributes, or explicitly flag any remaining duplicate-standard concern for TUI review.
- Blank `**Response:**` slot.

## Existing-match entry

For each `exact_match` triage row without a new convert file:

- `**Entry type:** existing match`
- CDEStaging source filename and type.
- Search targets used, matched OIFM ID and name.
- Matched model file path if present under `defs/`.
- Description, synonyms, change-from-prior from matched model when available.
- `**Assessment:**` confirm DuckDB mapping is correct; no new model was created.

## Skipped entry

For `user_skip` or unresolved `ambiguous` rows:

- `**Entry type:** skipped`
- CDEStaging source, triage decision, search targets, reason.
- `**Assessment:**` confirm skip is acceptable.

Keep each entry short (8-15 lines). The TUI is for quick scanning.

## What to flag

- Naming or scope choices needing confirmation
- Synonym breadth/ambiguity — especially `(none)` or placeholder descriptions on JSON-derived models
- Metadata changes applied in Step 6 that may still need confirmation (unusual synonym, scope choice, aggressive CFP winnow)
- Incomplete or odd `change from prior` values
- Source-carried duplicate standard attributes (`status`, `temporal change`, finding-specific present/absent fields) that were removed or may still need removal
- Split/extraction/associated-finding decisions
- CDEStaging issues: attribute count vs source, MD outline mismatches, json-vs-md source
- **Triage mapping** — wrong existing model linked, or skip that should have converted

## Output format

Plain markdown. No code fences wrapping the whole file.

**Critical:** metadata `**Field:**` lines need **two trailing spaces** for TUI line breaks (except the last metadata line before a blank line).

Generator command:

```powershell
uv run python scripts/generate_cdestaging_review.py --label "CDEStaging chunk N" --output reviews/review_cdestaging_chunk_N.md --triage-file reviews/triage_cdestaging_chunk_N.json defs/from_cdestaging_ct_chest/<files...>
```

## Required structure

- One `###` heading per entry.
- Every entry ends with `**Response:**` (no extra blank line before `---`).
- Entries separated by `---`.
- Use actual values from disk and triage JSON.

## Batch sizing

~8-10 entries per review file.

## Updating after feedback

Preserve non-empty `**Response:**` text verbatim. Only update agent-authored summary for changed models.
