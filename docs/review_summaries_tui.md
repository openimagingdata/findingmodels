# Review Summaries TUI

`scripts/review_summaries.py` is a standalone Textual app for reviewing the markdown files in `reviews/` and editing each `**Response:**` block from the terminal.

Review files are produced by the `finding-batch` and `finding-review` skills. The format is documented in [`prompts/fragments/review_file_generation.md`](../prompts/fragments/review_file_generation.md).

## Run It

From the repository root:

```bash
uv run --env-file .env scripts/review_summaries.py
```

That loads all `reviews/review_*.md` files.

To open a smaller set:

```bash
uv run --env-file .env scripts/review_summaries.py reviews/review_uncategorized.md
uv run --env-file .env scripts/review_summaries.py reviews
uv run --env-file .env scripts/review_summaries.py review_airway.md review_osseous_1.md review_other_chest_2.md
uv run --env-file .env scripts/review_summaries.py 'reviews/review_mediastinal_cardiac_*'
uv run --env-file .env scripts/review_summaries.py 'review_mediastinal_cardiac_*'
```

## What It Does

- Shows a navigable list of review entries on the left.
- Shows only the finding name in the entry list, without the source filename.
- Shows the current entry summary as rendered Markdown, including any `QUESTION` or `ISSUE` lines, on the right.
- Lets you edit the `Response` text in place.
- Writes changes back to the original markdown files when you save.
- Leaves unchanged entries untouched.

## Review Workflow

Both the `finding-batch` and `finding-review` skills generate `reviews/review_*.md` files and then hand them off to this TUI for human sign-off. The typical cycle:

1. The skill creates or edits finding models, runs mechanical and quality review, and writes one or more `reviews/review_<label>.md` files following `prompts/fragments/review_file_generation.md`.
2. The skill tells you the exact command to launch the TUI.
3. Open the file(s) in the TUI. Add responses or use `Ctrl+O` to mark entries `ok`.
4. Save the file(s) and tell the agent you're done.
5. The skill reads your completed responses and applies feedback (`ok` → accept; specific comments → apply change; questions → answer and iterate).

The review file format is strict (`###` heading per entry, `**Response:**` line before each separator). The TUI parses and round-trips that format.

## Keys

- `Ctrl+S`: save modified review files
- `Ctrl+Q`: save and quit
- `Ctrl+P`: previous entry
- `Ctrl+N`: next entry
- `Ctrl+R`: next entry with an empty response
- `Ctrl+O`: set the current response to `ok` and advance to the next entry
- `Tab`: cycle focus between widgets
- `Shift+Tab`: cycle focus backwards

When the entry list has focus, use the list's native navigation keys such as `Up`, `Down`, `PageUp`, `PageDown`, `Home`, and `End`.

When the summary pane has focus, you can scroll it with the usual Textual navigation keys such as arrow keys, `PageUp`, `PageDown`, `Home`, and `End`.

## Validation Mode

If you want to confirm that the parser can round-trip the selected review files without opening the UI:

```bash
uv run --env-file .env scripts/review_summaries.py --check
```
