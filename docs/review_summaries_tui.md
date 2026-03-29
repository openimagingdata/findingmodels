# Review Summaries TUI

`scripts/review_summaries.py` is a standalone Textual app for reviewing the markdown files in `reviews/` and editing each `**Response:**` block from the terminal.

If you want an agent to turn a batch of changed finding models into a TUI-compatible review file, use [the `new-finding` skill review-file prompt](../.claude/skills/new-finding/review_file_agent.md).

## Run It

From the repository root:

```bash
uv run scripts/review_summaries.py
```

That loads all `reviews/review_*.md` files.

To open a smaller set:

```bash
uv run scripts/review_summaries.py reviews/review_uncategorized.md
uv run scripts/review_summaries.py reviews
uv run scripts/review_summaries.py review_airway.md review_osseous_1.md review_other_chest_2.md
uv run scripts/review_summaries.py 'reviews/review_mediastinal_cardiac_*'
uv run scripts/review_summaries.py 'review_mediastinal_cardiac_*'
```

## What It Does

- Shows a navigable list of review entries on the left.
- Shows only the finding name in the entry list, without the source filename.
- Shows the current entry summary as rendered Markdown, including any `QUESTION` or `ISSUE` lines, on the right.
- Lets you edit the `Response` text in place.
- Writes changes back to the original markdown files when you save.
- Leaves unchanged entries untouched.

## Review Workflow

1. Ask the agent that created or updated the finding models to follow [the `new-finding` skill review-file prompt](../.claude/skills/new-finding/review_file_agent.md) and create a `reviews/review_*.md` file for those changed files.
2. Open that file in the TUI.
3. Add responses or use `Ctrl+O` to mark entries `ok`.
4. Save the file and tell the agent to read your completed responses from the review markdown.

Example generation request:

```text
Follow .claude/skills/new-finding/review_file_agent.md.

Create reviews/review_mediastinal_cardiac_4.md for these changed models:
- defs/abnormal_left_paratracheal_stripe.fm.json
- defs/abnormal_right_paratracheal_stripe.fm.json
- defs/tracheal_calcification.fm.json

Summarize each changed model briefly for human review. Flag only the specific questions or issues that need reviewer sign-off, and leave all Response fields blank.
```

## Keys

- `Ctrl+S`: save modified review files
- `Ctrl+Q`: save and quit
- `Ctrl+P`: previous entry
- `Ctrl+N`: next entry
- `Ctrl+R`: next entry with an empty response
- `Ctrl+O`: set the current response to `ok` and advance to the next entry
- `Tab`: cycle focus between widgets
- `Shift+Tab`: cycle focus backwards

When the entry list has focus, use the list’s native navigation keys such as `Up`, `Down`, `PageUp`, `PageDown`, `Home`, and `End`.

When the summary pane has focus, you can scroll it with the usual Textual navigation keys such as arrow keys, `PageUp`, `PageDown`, `Home`, and `End`.

## Validation Mode

If you want to confirm that the parser can round-trip the selected review files without opening the UI:

```bash
uv run scripts/review_summaries.py --check
```
