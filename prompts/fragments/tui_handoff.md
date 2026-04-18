# TUI handoff

After the review file(s) have been written to `reviews/`, hand off to the human for sign-off via the TUI. Used by batch and review flows — not by single-finding authoring.

## The handoff message

Tell the user exactly how to launch the TUI and what the key bindings are. Use the `!` prefix so the user can run it directly from the prompt without leaving the conversation.

### Single review file

> Review summary is ready. To review it, run:
>
> `! uv run --env-file .env scripts/review_summaries.py reviews/review_<label>.md`
>
> **Key bindings:**
> - `Ctrl+N` / `Ctrl+P` — next / previous entry
> - `Ctrl+R` — jump to next unanswered entry
> - `Ctrl+O` — mark current entry "ok" and move to next
> - Type in the Response box to leave comments or feedback
> - `Ctrl+S` — save all responses
> - `Ctrl+Q` — save and quit
>
> When you're done, come back and tell me — I'll read your responses and apply any changes.

### Multiple review files (batch)

> Review summaries are ready in `reviews/`. To review them, run:
>
> `! uv run --env-file .env scripts/review_summaries.py reviews/review_<label>*.md`
>
> (Or run with no arguments to load all review files in the directory: `! uv run --env-file .env scripts/review_summaries.py`.)
>
> Same key bindings as a single-file review. You can work through one file at a time or all at once. When you're done (or done with a group), come back and tell me — I'll read your responses and apply any changes.

## Reading responses back

When the user returns, read each review file and process responses per entry:

- **`ok` or blank** — no changes needed for that entry.
- **Specific feedback** — apply the requested change to the model file(s). Typical asks: tweak a synonym list, rename, drop a direction-of-change value, split a compound finding, extract a component, rewrite a description.
- **Questions** — answer them, then iterate. If a question uncovers work that requires another round of edits, re-generate the review file for the changed entries (see `review_file_generation.md`'s "Updating an existing review file" section).

## After applying feedback

- **Verify no new issues** — re-run `review_model.py` on the edited files. Fix any new errors before closing out the round.
- **If substantive changes were made**, regenerate the review file for those entries and hand off again — the user signs off on the corrected version before the batch is considered done.
- **Once everything is approved**, proceed to the final steps of your flow (CSV writeback in batch flows; report complete in review flows).

## Mandatory for batch and review; skipped for single authoring

- **`finding-batch`** — always run the TUI step. Many models at once means the user has to see the summary before approving.
- **`finding-review`** — always run the TUI step. Edits were applied to existing files and need explicit sign-off before the reviewer proceeds or reverts.
- **`finding-author`** (single interactive) — skip. The user is in the conversation as you work; show the final model inline and confirm directly.

## Don't

- Don't launch the TUI yourself — the user runs it. The `!` prefix in the handoff message is what they use.
- Don't interpret silence as approval. Wait for the user to say they're done.
- Don't edit the review file after the user has started responding unless you're doing the explicit "re-generate after feedback" update — and even then, preserve their response text exactly.
