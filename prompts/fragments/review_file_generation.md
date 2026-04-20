# Review file generation

After a batch or set of models has been created/edited and has passed quality review, produce a human review file in `reviews/` that can be loaded by `scripts/review_summaries.py` for TUI sign-off.

This step is mechanical summarization — the models have already been reviewed, and you already have their contents and the issues that were surfaced. Do not run another end-to-end review here. Read the files, restate each model briefly, flag only the things that genuinely need human attention, and leave the response slot blank.

## Inputs you work from

- **Target review file path** — e.g., `reviews/review_headct_hemorrhage_1.md`.
- **List of changed or newly-created model files** — in the order they should appear in the review file.
- **Context you already have** — the edits you made, the quality-review warnings that weren't auto-resolvable, any judgment calls you want the reviewer to sign off on.
- **Optional batch label or note** — e.g., "head CT hemorrhage batch 1 of 3".

## One entry per file

For each changed file, produce one `###` entry with:

- A one-line description of the finding (name from the model).
- The concrete fields a reviewer will want to eyeball: source file, OIFM ID, description, synonyms, `change from prior` values.
- **Only** the specific questions, issues, or judgment calls that need reviewer attention. If nothing specific needs flagging, write a short assessment line instead.
- A blank `**Response:**` slot.

Keep each entry short — typically 8-15 lines total. The TUI is for quick scanning, not re-review.

## What to flag

- A naming or scope choice that still needs confirmation
- A synonym that may be too broad, ambiguous, or whose absence might be surprising
- A `change from prior` set that might be incomplete or contain a value that doesn't make sense
- A likely split, extraction, or associated-finding decision (name(s) to create separately)
- Any non-obvious judgment call you want the reviewer to approve

If a changed model looks fine, write `**Assessment:** Looks reasonable as written; confirm acceptable.` — do not invent issues.

## Output format

Write plain markdown to the requested review file path. No code fences wrapping the whole file. No JSON.

**Critical formatting rule:** each `**Field:**` line in the metadata block must end with **two trailing spaces** (markdown hard line break), otherwise `MarkdownViewer` renders all five fields as one unreadable paragraph. The trailing spaces are invisible in the source but essential for the TUI. Separate paragraphs (QUESTION / ISSUE / Assessment / Response) use blank lines instead.

```
# Review: <label>

<N> models to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### <finding name>

**Source file:** `defs/<file>.fm.json`  ← two trailing spaces
**ID:** `<oifm_id>`  ← two trailing spaces
**Description:** <description>  ← two trailing spaces
**Synonyms:** <comma-separated or `(none)`>  ← two trailing spaces
**Change from prior:** <comma-separated values>

**QUESTION:** <specific question for reviewer>

**ISSUE 1:** <specific issue>

**Suggested fix:** <short proposal if useful>

**Response:** 

---

### <next finding>
...
```

Notes on the example:
- The `← two trailing spaces` annotations are for illustration only; the actual file just has two spaces at line-end (not the arrow).
- The last metadata line (`**Change from prior:**`) does NOT need trailing spaces because a blank line follows it — that already terminates the paragraph.
- Code-formatting (backticks) on paths and IDs makes the TUI render more readable.

## Required structure (for `review_summaries.py` compatibility)

- Exactly one `###` heading per changed model.
- Entries in the order of the provided file list unless told otherwise.
- Every entry ends with an exact `**Response:**` line followed by a blank line.
- Entries separated by `---` lines.
- All summary / issue / question content appears **before** the `**Response:**` line.
- Use actual values from each file — do not invent missing content.
- Do not wrap the file in a fenced code block.

## Batch sizing

Split large batches into review files of **~8-10 entries each**. `reviews/review_<label>_1.md`, `reviews/review_<label>_2.md`, etc. Longer files are harder to work through in one sitting.

## Updating an existing review file

If you're re-generating a review file after the human provided feedback and you applied changes:

- **Preserve non-empty `**Response:**` text verbatim.** Do not erase human comments.
- Only update the agent-authored summary text for entries whose models changed.
- If an entry's model was deleted or split, note that at the top of the entry and preserve the reviewer's prior response for context.
