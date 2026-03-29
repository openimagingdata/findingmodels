---
name: new-finding
description: >
  REQUIRED for any task involving finding models in this repository. This skill contains the ONLY correct workflow
  for searching, creating, or modifying .fm.json finding model files -- including the bundled scripts for model
  creation (create_model.py), contributor data, ID generation rules, and canonical JSON formatting requirements.
  Without this skill, you will produce incorrect output.

  ALWAYS use this skill when the user: mentions any radiology finding by name (e.g. "pneumothorax",
  "cardiomegaly", "pleural effusion"), asks to add or create a finding or finding model, wants to check
  if a finding exists ("do we have X"), provides a list of findings to process or import, references the
  Hood CXR taxonomy, pastes finding names from a spreadsheet/CSV, wants to add a synonym to an existing
  model, says "new finding", or discusses whether a .fm.json file needs to be created. Even if the request
  seems simple, ALWAYS consult this skill first -- it contains critical context about the findingmodel CLI
  tools and project conventions that you cannot infer on your own.
allowed-tools: Bash, Read, Grep, Glob, Write, Edit
---

# New Finding Model Skill

Process suggested radiology findings: search the index for existing matches, update synonyms on existing models, or create new finding model stubs.

**Bundled scripts** (in `.claude/skills/new-finding/scripts/`):
- `create_model.py` — Create complete finding models with IDs, codes, and contributor (primary creation tool)
- `fix_stub.py` — Post-process existing stubs: add contributor, override name/description/synonyms
- `review_model.py` — Mechanical quality checks on finding models (naming, structure, standard attributes)
- `update_csv.py` — Update a CSV tracking file with OIFM IDs

**Bundled handoff prompt**:
- `.claude/skills/new-finding/review_file_agent.md` — Turn changed model files into `reviews/review_*.md` summaries for the review TUI

## Session Setup

On first invocation in a session, confirm defaults with the user:
- **Source code** for OIFM IDs (e.g., `OIDM`)
- **Contributors**: Both a person AND an organization when possible. Ask the user which contributor(s) to use.
- **Tags** (e.g., `chest`, `XR`, `finding`)

Reuse these defaults for all subsequent findings unless the user overrides.

Available contributor keys (defined in the scripts):
- People: `hoodcm` (MGB), `HeatherChase` (MSFT), `radngandhi` (RSNA), `talkasab` (MGB)
- Orgs: `OIDM`, `GMTS`, `CDE`, `MGB`

## Conventions

Read **`prompts/overview_compact.md`** for context on what a finding model is. All naming, synonym, attribute, associated finding, and component rules are defined in **`prompts/conventions.md`**. Read and follow both documents. They define what an imaging finding is, how to name models, what makes a valid synonym, how to configure standard attributes (including direction-of-change winnowing), how to handle associated findings vs components, and when to split compound findings.

The `create_model.py` script generates standard presence and change-from-prior attributes automatically, but the direction-of-change values it generates may not all be appropriate — the review step catches and removes inappropriate ones.

## Single-Finding Workflow

### 1. Search for Existing Matches

```bash
uv run findingmodel search "<finding_name>" --limit 5
```

Present the results table to the user. The search uses hybrid full-text + semantic matching, so it catches synonyms and related terms.

If 0 results come back, try a broader or alternate phrasing before concluding the finding doesn't exist (e.g., search for the key anatomic term alone, or a common synonym).

### 2. Triage Decision (let the user decide)

Show results and ask — do NOT decide automatically:
- **Match found**: "This finding already exists as [name] ([ID]). Would you like to view it or add a synonym?"
- **Close matches**: "These are close matches. Is any of these the same finding? I can add your suggested name as a synonym."
- **No matches**: "No existing match found. Shall I create a new finding model?"

**Specificity check**: When evaluating matches, verify the match is appropriate — that the existing model refers to the same finding at the same level of specificity. Reject matches where the existing model is too general (e.g., "detectable hardware" when incoming is "tunneled catheter") or a different finding entirely.

### 3a. Synonym Update

If the user wants to add a synonym to an existing finding:

1. Find the file:
   ```bash
   uv run python -c "from findingmodel.common import model_file_name; print(model_file_name('<matched_finding_name>'))"
   ```
   Then confirm: `ls defs/<result>.fm.json`

2. Read the `.fm.json` file with the Read tool.

3. **Check for collisions** before adding — search for the proposed synonym to see if it's already used by another model:
   ```bash
   uv run findingmodel search "<proposed synonym>" --limit 3
   ```
   If it appears on a different model, flag the ambiguity (see collision rules in `prompts/conventions.md`).

4. Use the Edit tool to add the new synonym to the `synonyms` array. If `synonyms` doesn't exist, add it after the `description` field.

5. Avoid adding duplicates — check existing synonyms first.

6. Show the user the change.

### 3b. New Model Creation

> **CRITICAL: Creation is NOT complete until the review process passes. A model that has been created but not reviewed is UNFINISHED WORK. Never present an unreviewed model to the user or move on to the next finding.**

#### Step 1: Draft (apply naming rules)

Before calling `create_model.py`, apply the Naming Conventions above to your inputs:
- **Expand acronyms** in the canonical name (keep acronym as synonym)
- **Expand brand names** to generic/descriptive terms (keep brand as synonym)
- **Minimize eponyms** where a descriptive term is standard (keep eponym as synonym)
- **Verify synonyms** — each must mean the exact same thing, not a subtype or supertype
- **All names lowercase** except justified proper nouns

#### Step 2: Create

```bash
uv run .claude/skills/new-finding/scripts/create_model.py \
    --name "<finding_name>" \
    --description "<description>" \
    --synonyms "synonym1" "synonym2" \
    --contributor <person_key> <org_key> \
    --source <source_code> \
    --output defs/<filename>
```

Output: `filepath|name|oifm_id`

To determine the filename:
```bash
uv run python -c "from findingmodel.common import model_file_name; print(model_file_name('<finding_name>'))"
```

> **Note**: The FindingModelBase schema requires at least 1 synonym if the synonyms list is provided. If a finding has no meaningful synonyms, omit the `--synonyms` flag entirely.

#### Step 3: Review (MANDATORY — do not skip)

Every created model MUST pass both mechanical and LLM review before it is considered done.

1. **Mechanical lint** — run `review_model.py` on the created file(s):
   ```bash
   uv run .claude/skills/new-finding/scripts/review_model.py defs/<filename>
   ```

2. **LLM sub-agent review** — launch a sub-agent with `prompts/review_agent.md` as its instructions. The sub-agent reads that prompt for the full quality checklist, then reads and reviews each created model file. It returns issues found and suggested fixes. This catches things the script cannot:
   - Are the direction-of-change values in "change from prior" clinically appropriate? (e.g., emphysema doesn't get "larger" or "smaller" — it "worsens" or "improves"; a fracture doesn't "improve" — it "heals")
   - Are synonyms truly synonymous or are they subtypes?
   - Are acronyms/brand names/eponyms properly handled?
   - Is the description clinically accurate?

3. **Fix ALL issues** found by either check. Re-run until clean.

4. **Only then** show the final model to the user.

#### Step 4: Human Review via TUI

After the model passes agent review, prepare it for human sign-off:

1. **Generate the review file** — use a sub-agent with `.claude/skills/new-finding/review_file_agent.md` to create a `reviews/review_<label>.md` file summarizing the changed model(s).

2. **Tell the user how to review.** Present something like:

   > Review summaries are ready. To review them, run:
   >
   > `! uv run scripts/review_summaries.py reviews/review_<label>.md`
   >
   > **Quick reference:**
   > - **Ctrl+N / Ctrl+P** — next / previous entry
   > - **Ctrl+R** — jump to next unanswered entry
   > - **Ctrl+O** — mark current entry "ok" and move to next
   > - **Type in the Response box** to leave comments or feedback
   > - **Ctrl+S** — save all responses
   > - **Ctrl+Q** — save and quit
   >
   > When you're done, come back and tell me — I'll read your responses and apply any changes.

3. **Read back the responses** — when the user returns, read the review file and apply their feedback:
   - "ok" or blank → no changes needed
   - Specific feedback → apply the requested changes to the model file(s)
   - Questions → answer them and iterate

4. If changes were made based on feedback, re-generate the review file for the updated models and repeat until the user approves.

### 4. Optional Enrichment

After creation, offer: "Would you like a detailed description with citations?"
```bash
uv run findingmodel-ai make-info "<finding_name>" --detailed
```
If yes, use `fix_stub.py` to incorporate the enriched description and any useful synonyms:
```bash
uv run .claude/skills/new-finding/scripts/fix_stub.py \
    defs/<filename> \
    --description "<enriched_description>" \
    --synonyms "existing1" "existing2" "new_synonym"
```

## Batch Workflow

When processing many findings at once (e.g., from a CSV or list), use this more efficient pattern:

### Phase 1: Bulk Search

Search all findings quickly using `--limit 1` or `--limit 2` for triage:
```bash
uv run findingmodel search "finding1" --limit 1
uv run findingmodel search "finding2" --limit 1
# ... etc
```

Compile results into three groups:
- **Direct matches** — finding already exists (report to user)
- **Close matches** — need user decision (synonym or new?)
- **No matches** — will need new models

### Phase 2: Draft Batch Config

Build the batch JSON config, applying the Naming Conventions to every entry:
- Expand acronyms in canonical names (acronym becomes synonym)
- Replace brand names with generic terms (brand becomes synonym)
- Minimize eponyms where descriptive term is standard
- Verify each synonym is truly synonymous — not a subtype, supertype, or different finding
- All names lowercase except justified proper nouns

You have radiology domain knowledge — write concise, accurate descriptions and curated synonyms yourself. This is faster and more accurate than calling make-info for each one.

### Phase 3: Create

```bash
uv run .claude/skills/new-finding/scripts/create_model.py --batch << 'EOF'
{
    "source": "<source_code>",
    "contributors": ["<person_key>", "<org_key>"],
    "tags": ["chest", "XR", "finding"],
    "models": [
        {
            "name": "finding one",
            "description": "Description of finding one.",
            "synonyms": ["synonym a", "synonym b"]
        },
        {
            "name": "finding two",
            "description": "Description of finding two.",
            "synonyms": ["synonym c"]
        }
    ]
}
EOF
```

Output is `filepath|name|oifm_id` per line — use this to build CSV update mappings.

### Phase 4: Review (MANDATORY — do not skip)

> **CRITICAL: The batch is NOT done until every model passes review. Do NOT update the CSV or report completion until review passes.**

Run both mechanical and LLM review on the created batch:

1. **Mechanical lint**:
   ```bash
   uv run .claude/skills/new-finding/scripts/review_model.py defs/finding_one.fm.json defs/finding_two.fm.json
   ```

2. **LLM sub-agent review**: Launch a sub-agent with `prompts/review_agent.md` as its instructions. The sub-agent reads that prompt for the full quality checklist, then reads and reviews each created model file. This catches what the script cannot — inappropriate direction-of-change values, synonym strictness, acronym/brand/eponym handling, clinical accuracy.

3. **Fix ALL issues. Re-run until clean.** If names change, rename the files to match.

### Phase 4b: Human Review via TUI

After the batch passes agent review, prepare it for human sign-off:

1. **Generate review files** — use a sub-agent with `.claude/skills/new-finding/review_file_agent.md` to create `reviews/review_<label>.md` files. Split large batches into groups of ~8-10 models per file for manageable review.

2. **Tell the user how to review.** Present something like:

   > Review summaries are ready in `reviews/`. To review them, run:
   >
   > `! uv run scripts/review_summaries.py reviews/review_<label>*.md`
   >
   > (Or run with no arguments to load all review files: `! uv run scripts/review_summaries.py`)
   >
   > **Quick reference:**
   > - **Ctrl+N / Ctrl+P** — next / previous entry
   > - **Ctrl+R** — jump to next unanswered entry
   > - **Ctrl+O** — mark current entry "ok" and move to next
   > - **Type in the Response box** to leave comments or feedback
   > - **Ctrl+S** — save all responses
   > - **Ctrl+Q** — save and quit
   >
   > You can review one file at a time or all at once. When you're done (or done with a batch), come back and tell me — I'll read your responses and apply any changes.

3. **Read back the responses** — when the user returns, read each review file and apply their feedback. "ok" = approved. Specific comments = make the requested changes. Questions = answer and iterate.

4. If changes were made, re-generate review files for updated models and repeat until approved.

### Phase 5: CSV Tracking Update

If working from a CSV with a row ID column and an OIFM ID column:
```bash
uv run .claude/skills/new-finding/scripts/update_csv.py \
    lists/cxr_findings.csv \
    --id-column 0 \
    --oifm-column 6 \
    --mapping 'FID0010=OIFM_OIDM_207240,FID0011=OIFM_OIDM_449436'
```

Or pipe a JSON mapping:
```bash
echo '{"FID0010": "OIFM_OIDM_207240", "FID0011": "OIFM_OIDM_449436"}' | \
uv run .claude/skills/new-finding/scripts/update_csv.py \
    lists/cxr_findings.csv \
    --id-column 0 \
    --oifm-column 6 \
    --mapping-stdin
```

### Batch Summary

At the end, summarize:
- How many findings were processed
- How many already existed (with OIFM IDs)
- How many synonyms were added
- How many new models were created
- How many remain unprocessed

## Writing Descriptions and Synonyms

You have radiology domain knowledge — write concise, accurate descriptions and curated synonyms yourself rather than deferring to make-info for routine findings. Follow `prompts/conventions.md` for all naming, synonym, and description rules.

## Standalone Review Workflow

For reviewing existing models outside the creation flow (e.g., auditing or cleanup), use `review_model.py` for fast mechanical checks, then apply LLM judgment for the items it flags.

### Step 1: Run Mechanical Review

```bash
# Single file
uv run .claude/skills/new-finding/scripts/review_model.py defs/<filename>

# All models (or a glob)
uv run .claude/skills/new-finding/scripts/review_model.py defs/*.fm.json

# Auto-fix what's possible (underscores → spaces, remove self-synonyms, etc.)
uv run .claude/skills/new-finding/scripts/review_model.py --fix defs/<filename>

# Errors only (skip warnings and review items)
uv run .claude/skills/new-finding/scripts/review_model.py --errors-only defs/*.fm.json
```

The script checks: underscores in names, lowercase convention, standard attribute structure (presence first, change from prior second with required values), choice attributes have >= 2 values, proper associated-findings structure, contributor completeness, placeholder descriptions.

Issue levels:
- **ERROR** — definite problem, auto-fixable with `--fix` where possible
- **WARNING** — likely problem, needs human confirmation
- **REVIEW** — needs LLM judgment (e.g., is this capitalization a proper noun?)

### Step 2: LLM-Assisted Review

Launch a sub-agent with `prompts/review_agent.md` as its instructions. The sub-agent reads that prompt for the full quality checklist, then reads and reviews the model file(s). It covers:

- Naming: capitalization, acronyms, eponyms, brand names, underscores
- Synonym strictness: exact same meaning only, no subtypes/supertypes
- Attribute quality: standard attributes present, values appropriate
- Sub-finding detection: attributes that should be separate models
- Compound finding splitting: names with "and/or" or slashes
- Clinical appropriateness: descriptions, specificity, completeness
- Direction-of-change: include all pairs a radiologist would naturally use, remove only nonsensical ones

The sub-agent returns issues found and suggested fixes. Apply the fixes.

## Legacy: make-stub-model

The `findingmodel-ai make-stub-model` CLI is still available but has drawbacks:
- It uses AI to normalize the finding name, which may rename it unexpectedly
- It can fail intermittently (retry once on failure)
- It requires a separate `fix_stub.py` step to add contributor and fix name/description

Prefer `create_model.py` for all new model creation. Use `fix_stub.py` only when you need to post-process an existing stub that was created by `make-stub-model`.

## Critical Constraints

- **Never generate OIFM/OIFMA IDs manually** — `create_model.py` and `--with-ids` handle this, checking the index for uniqueness
- **Never edit generated files**: `text/*.md`, `index.md`, `ids.json` are auto-generated by the validator
- **Do NOT run `scripts/validator.py`** — validation is handled separately outside this skill
- **Canonical JSON format**: 2-space indent, no null fields (`exclude_none=True`)
- **Do NOT commit** without explicit user permission
- **Always show results** to the user before taking action
- **Import path**: Use `from findingmodel.common import model_file_name` (NOT `from findingmodel import model_file_name`)
- **Shell escaping**: For multi-line Python, use heredocs (`<< 'PYEOF'`) rather than `python -c` to avoid escaping issues
- **Naming and synonym rules** are in `prompts/conventions.md` — follow them
