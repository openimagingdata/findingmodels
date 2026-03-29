---
model: gpt-5.4
reasoning_effort: low
---

# Review File Agent Instructions

You have already created or updated one or more finding model files. Your job now is to prepare a concise human review file for the TUI.

This is not a fresh end-to-end review pass. Do not broaden the task. Do not rewrite the models in this step. Read the changed files, use the context you already have from working on them, and write a `reviews/review_*.md` file with one summary entry per changed model.

The output must be compatible with `scripts/review_summaries.py`.

## Inputs

You will be given:

- a target review file path such as `reviews/review_airway.md`
- a list of changed or new finding model files
- optionally a batch label or brief note about what changed

## What To Do

For each changed file:

- read the current model contents
- summarize the model briefly for the reviewer
- surface only the specific points that need human attention or sign-off
- leave a blank `Response` slot for the human

Keep the entries concise. The goal is to help a human quickly review the changed models in the terminal, not to restate every convention or dump a long audit log.

## What To Flag

Flag only concrete review points that are worth a human response, such as:

- a naming or scope choice that still needs confirmation
- a synonym that may be too broad, ambiguous, or missing an important alternative
- a `change from prior` value set that may be incomplete or may include a value that does not make sense
- a likely split, extraction, or associated-finding decision
- any non-obvious judgment call you want the reviewer to approve

If a changed model looks fine, do not invent issues. Add a short assessment instead.

## Output Format

Write plain markdown to the requested review file path using this structure:

```markdown
# Review: <label>

<N> models to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### <finding name>
**Source file:** <relative path>  
**ID:** <oifm id or `none assigned`>  
**Description:** <description or `missing`>  
**Synonyms:** <comma-separated synonyms or `none listed`>  
**Change from prior:** <comma-separated values or `missing`>  
**QUESTION:** <specific question for the reviewer>
**ISSUE 1:** <specific issue>
**ISSUE 2:** <specific issue>
**Suggested fix:** <short proposed resolution if useful>

**Response:**  

---
```

## Required Rules

- Create exactly one `###` entry per changed model file.
- Keep the same order as the provided file list unless told otherwise.
- Use the actual values from the changed file. Do not invent missing content.
- Keep each entry short and review-oriented.
- Use `**Assessment:** Looks reasonable as written; confirm acceptable.` when there is nothing specific to flag.
- Put all summary text before the `**Response:**` line.
- Make the response line exactly `**Response:**` with a blank response unless told to preserve existing human responses.
- Use `---` only between entries and after the intro block.
- Do not wrap the output in code fences.
- Do not output JSON.

## Compatibility Requirements

The review file must remain compatible with `scripts/review_summaries.py`. That means:

- every entry must have a `###` heading
- every entry must have a `**Response:**` line
- entries must be separated by `---`
- the review content must appear before the `**Response:**` line

## Existing Review Files

If you are updating an existing `reviews/review_*.md` file:

- preserve non-empty human `**Response:**` text exactly
- do not erase human comments
- only update the agent-authored summary text when explicitly asked

## Recommended Wrapper Prompt

Use this pattern when asking an agent to generate the review file:

```text
Follow .claude/skills/new-finding/review_file_agent.md.

Create reviews/review_mediastinal_cardiac_4.md for these changed models:
- defs/abnormal_left_paratracheal_stripe.fm.json
- defs/abnormal_right_paratracheal_stripe.fm.json
- defs/tracheal_calcification.fm.json

Summarize each changed model briefly for human review. Flag only the specific questions or issues that need reviewer sign-off, and leave all Response fields blank.
```
