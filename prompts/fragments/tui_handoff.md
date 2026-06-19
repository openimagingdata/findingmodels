# TUI handoff

After review file(s) are written to `reviews/`, hand off to the human for sign-off via the TUI.

## The handoff message

Tell the user how to launch the TUI. Use the `!` prefix for direct run from chat.

### Single review file

> Review summary is ready. To review it, run:
>
> `! uv run --env-file .env scripts/review_summaries.py reviews/review_<label>.md`
>
> **Key bindings:**
> - `Ctrl+N` / `Ctrl+P` — next / previous entry
> - `Ctrl+R` — jump to next unanswered entry
> - `Ctrl+O` — mark current entry "ok" and move to next
> - Type in the Response box for comments
> - `Ctrl+S` — save all responses
> - `Ctrl+Q` — save and quit
>
> While reviewing new models, confirm any note about source-carried `presence`, `status`, or `temporal change` attributes being removed in favor of the standard `presence` and `change from prior` attributes.
>
> When you're done, come back and tell me — I'll read your responses and apply any changes.

### Multiple review files

> `! uv run --env-file .env scripts/review_summaries.py reviews/review_<label>_*.md`
>
> Or load all: `! uv run --env-file .env scripts/review_summaries.py`

## Reading responses back

- **`ok` or blank** — no changes.
- **Specific feedback** — apply edits to model file(s).
- **Questions** — answer and iterate; re-generate review file for changed entries (preserve human response text).

## After applying feedback

- Re-run `review_model.py` on edited files.
- Regenerate review file and hand off again if substantive changes were made.

## Mandatory for

- **`finding-batch`**
- **`finding-cdestaging-batch`**
- **`finding-review`**

Skip for **`finding-author`** (single interactive).

## Don't

- Don't launch the TUI yourself.
- Don't interpret silence as approval.
- Don't erase human `**Response:**` text when re-generating.
