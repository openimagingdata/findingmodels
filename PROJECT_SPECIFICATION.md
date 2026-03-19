# Finding Models Project — Specification & Status

> **Purpose**: This document guides AI-assisted development and human readers. It defines requirements, current state, completed work, and remaining tasks. Reference it when building or modifying the project.

---

## Quick Reference

| Topic | Section |
|-------|---------|
| Project overview | [Part 1: Top-Down Overview](#part-1-top-down-overview) |
| Script & agent dependencies | [Part 2: How the Main Pipeline Works](#part-2-how-the-main-pipeline-works) |
| What's done vs. pending | [Part 3: Accomplished & Pending](#part-3-accomplished--pending) |
| Model rules (naming, location, etc.) | [Part 4: Finding Model Rules](#part-4-finding-model-rules) |
| Target schema elements | [Part 5: Finding Model Schema](#part-5-finding-model-schema) |
| Pipeline flow (step by step) | [Part 6: Pipeline Instructions](#part-6-pipeline-instructions) |
| Merge strategy details | [Part 7: Merge Strategy](#part-7-merge-strategy) |
| Sub-findings direction | [Part 8: Sub-findings](#part-8-sub-findings) |
| AI implementation checklist | [Part 9: Implementation Checklist](#part-9-implementation-checklist-for-ai) |
| Where to find code | [Part 10: Key File References](#part-10-key-file-references) |
| Unresolved questions | [Part 11: Open Questions](#part-11-open-questions) |

---

## Part 1: Top-Down Overview

### What We Have

The main entry point is `single_agent_pipeline.py`. It takes Hood CT Chest definitions (Markdown and JSON) from CDEStaging, looks them up in a DuckDB index of existing finding models, and either creates new models or merges incoming definitions with existing ones.

**Data flow:**
- **Input**: `hood_CT_chest` definitions from [CDEStaging](https://github.com/openimagingdata/CDEStaging/tree/main/definitions/hood_CT_chest)
- **Existing models**: DuckDB index (path from `DUCKDB_INDEX_PATH` or `--db-path`). The index is supplied externally; this repo does not contain the code that populates it.
- **Output**:
  - `defs/hood_final_models/` — direct output from `single_agent_pipeline.py`
  - `defs/merged_findings/` — output from `batch_merge_findings.py` (a separate pipeline; see below)

**Layout:** Scripts in `scripts/` are CLI entry points. Library code (loaders, adapters) lives in `findingmodels/hood/`. Processing is handled by `agents/single_agent.py`.

**Scripts:**
- `scripts/single_agent_pipeline.py` — Main single-agent pipeline (CDEStaging → output). `scripts/hood_to_final_finding.py` is a thin shim that runs the same script.
- `scripts/merge_findings.py` — CLI for merging one incoming model with existing
- `scripts/batch_merge_findings.py` — **Different pipeline**: takes already-converted `hood_findings` (.fm.json), merges each with the DuckDB index, outputs to `merged_findings`. Does not read from CDEStaging.

**AI agents** (pydantic-ai, GPT-5.4, single agent with tools):
- Single `single_agent` with tools: search, get_model, create_from_markdown, adapt_hood_json, add_ids, add_standard_codes
- Agent handles: specificity check, merge strategy, formatting (lowercase, acronyms, eponyms), attribute classification

---

## Part 2: How the Main Pipeline Works

`single_agent_pipeline.py` loads definitions via `findingmodels.hood` and delegates processing to the single Hood agent:

```
single_agent_pipeline.py
    └── findingmodels.hood
            ├── loaders              (file I/O, should_process_file, load_definition)
            └── hood_json_adapter    (used by agent for JSON definitions)
    └── agents/single_agent            (single agent with pydantic-ai tools)
            └── Tools: search_finding_models, get_full_model, create_from_markdown,
                       adapt_hood_json, add_ids_to_finding_model, add_standard_codes
```

**In plain terms:**
- The main script loads definitions via `findingmodels.hood.loaders`.
- The Hood agent receives the content and uses its tools to search, match, merge, format, and produce the final model.
- `merge_findings.py` uses the same agent for incoming .fm.json files.

---

## Part 3: Accomplished & Pending

### What We Have Accomplished

| Requirement | Status | Where in Code | Notes |
|-------------|--------|---------------|-------|
| Hood = incoming, existing DB = reference | Done | `agents.single_agent` (merge via tools) | Hood definitions are merged into existing models, not the other way around |
| Specificity check (reject general matches) | Done | `agents.single_agent` (system prompt + tools) | Prevents matching e.g. "tunneled catheter" to "detectable hardware" |
| Presence and change_from_prior at top | Done | `agents.single_agent` (system prompt) | Agent applies ordering per spec |
| Hood contributor (MGB) in merged models | Done | `agents.single_agent` (system prompt) | MGB contributor added to merged output |
| Presence with yes/no: keep existing if it has standard values | Done | `agents.single_agent` (system prompt + merge logic) | Incoming [yes, no] discarded when existing has standard values |
| Lowercase, acronym expansion, eponym minimization | Done | `agents.single_agent` (system prompt) | Names formatted per spec |
| Full merge strategy (enhanced, identical, subset, etc.) | Done | `agents.single_agent` (system prompt + tools) | All five relationship types supported |
| Sub-finding identification via LLM | Pending | Agent can be extended | Components identified; models not yet saved to disk |
| Pipeline: lookup → generate or merge → ensure presence/change | Done | `single_agent_pipeline.process_single_file`, `agents.single_agent` | End-to-end flow from CDEStaging to output |

### What Still Needs to Be Accomplished

| Requirement | Status | Notes |
|-------------|--------|-------|
| **Save sub-findings as separate files** | Not done | Sub-findings identified and logged but not written to disk |
| **Association between main and sub-findings** | Future | Design TBD |
| Skip/resume (e.g. `--skip-existing`) | Not done | Re-run overwrites output; no way to skip already-processed findings |
| LLM retry on transient failures | Not done | ModelRetry imported but unused; no retry on API timeouts |

---

## Part 4: Finding Model Rules

Rules for how finding models should be structured and named.

**Naming & formatting:**
- Use lowercase for model names, attribute names, and values. Descriptions may use normal casing.
- Eponyms can be uppercase but should be minimized; prefer descriptive terms when possible.
- Spell out acronyms in model/finding names. Add compact forms as synonyms (e.g., "anterior cruciate ligament tear" with synonyms "ACL tear", "ACL injury").

**Location:**
- Describe where the finding can occur using a subset of nodes in the anatomic location set.
- Do not add separate location attributes.

**Associated findings:**
- Avoid an "associated findings" attribute. Define related items as separate findings instead.

**Sub-findings:**
- If multiple attributes describe a sub-finding (e.g., component-specific properties), extract it as a separate finding (e.g., "solid component of mixed pulmonary nodule"). How to represent associations is a separate design problem.

---

## Part 5: Finding Model Schema

Target elements that a finding model should support:

| Element | Description |
|---------|-------------|
| Attribute name synonyms | Alternative names for attributes |
| Value synonyms | Alternative names for choice values |
| Locations | Feasible regions and structure types |
| Modalities | Modalities that can show the finding |
| Life stages | Applicable life stages |
| Sex phenotypes | Applicable sex phenotypes |
| Examples | Possibly in a separate repository |

---

## Part 6: Pipeline Instructions

**Input:** Each definition (MD or JSON) in `hood_CT_chest`:  
[https://github.com/openimagingdata/CDEStaging/tree/main/definitions/hood_CT_chest](https://github.com/openimagingdata/CDEStaging/tree/main/definitions/hood_CT_chest)

**Flow:**
1. Look up an existing model in the database.
2. Do **not** match on more general terms (e.g., "tunneled catheter" is specific; "detectable hardware on chest X-ray" is too general).
3. **If no match:** Use findingmodel tools + LLM to generate a model. Ensure presence and change_from_prior exist and are merged correctly.
4. **If match:** Apply the merge strategy using either JSON or Markdown source.

---

## Part 7: Merge Strategy

**Direction:** Hood definitions = incoming. Existing database (Gamuts, CDE, etc.) = existing (reference).

**Attribute order:** Presence and change_from_prior must appear first.

**Contributors:** Hood contributor (MGB) must be included in merged models.

**Attribute relationships:**

| Relationship | Meaning | Action |
|--------------|---------|--------|
| **enhanced** | Incoming has all existing values plus more | Merge — add new values to existing attribute |
| **identical** | Same values | No merge |
| **subset** | Existing has all incoming values plus more | No merge |
| **needs_review** | Some shared values; each has unique values | Auto-merge for now; review workflow may be added later |
| **no_similarities** | No shared values | Add as new attribute, *unless* both are presence/change_from_prior |

**Presence special case:** If incoming has [yes, no] and existing has standard presence values [absent, present, indeterminate, unknown], and both are classified as presence, discard incoming and keep existing. Same logic for change_from_prior to avoid duplicates or incomplete attributes.

---

## Part 8: Sub-findings

- **Extract** sub-findings as separate findings (e.g., "solid component of mixed pulmonary nodule").
- How to link main finding and sub-findings is a separate design problem.
- **Current behavior:** Sub-finding models are created and logged; they are not written to disk.

---

## Part 9: Implementation Checklist for AI

When modifying or extending the project, ensure:

- [ ] Presence and change_from_prior are first in the attribute list
- [ ] Hood contributor (MGB) is in contributors for Hood-sourced or merged models
- [ ] Specificity check rejects general-term matches
- [ ] Presence/change_from_prior with non-standard values (e.g., yes/no) are not added as duplicates when existing has standard values
- [ ] Naming: lowercase, acronyms expanded, eponyms minimized
- [ ] Sub-findings: when implemented, write extracted models to disk
- [ ] Do not add an "associated findings" attribute; use separate findings
- [ ] Location expressed via feasible anatomic nodes, not separate location attributes

---

## Part 10: Key File References

| Concern | File(s) |
|---------|---------|
| Main Hood pipeline (CLI) | `scripts/single_agent_pipeline.py` |
| Hood agent (single agent with tools) | `agents/single_agent.py` |
| Hood library (loaders, adapters) | `findingmodels/hood/` |
| Merge CLI | `scripts/merge_findings.py` |
| Batch merge (separate pipeline) | `scripts/batch_merge_findings.py` |
| Merge helpers (legacy; used for reference) | `scripts/merge_findings_helpers.py` |
| JSON adapter | `findingmodels/hood/hood_json_adapter.py` |
| Markdown adapter | `findingmodels/hood/markdown_to_finding_model_adapter.py` |
| Finding model schema | `schema/finding_model.schema.json` |
| Dependencies | `findingmodel>=0.6.0,<1.0`, `pydantic-ai` |

---

## Part 11: Open Questions

- How to represent associations between main finding and extracted sub-findings
- Where to store examples (same repo vs separate)
- Whether `needs_review` comparisons should have interactive or configurable review
- Whether the Hood pipeline should populate schema fields (synonyms, locations, modalities, life_stages, sex_phenotypes, examples)
