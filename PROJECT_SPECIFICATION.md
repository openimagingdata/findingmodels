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

The main entry point is `hood_to_final_finding.py`. It takes Hood CT Chest definitions (Markdown and JSON) from CDEStaging, looks them up in a DuckDB index of existing finding models, and either creates new models or merges incoming definitions with existing ones.

**Data flow:**
- **Input**: `hood_CT_chest` definitions from [CDEStaging](https://github.com/openimagingdata/CDEStaging/tree/main/definitions/hood_CT_chest)
- **Existing models**: DuckDB index built from `original_defs`, `findings_from_cdes`, and `merged_findings`
- **Output**:
  - `defs/hood_final_models/` — direct output from the Hood pipeline
  - `defs/merged_findings/` — output from batch merging `hood_findings`

**Scripts:**
- `scripts/hood_to_final_finding.py` — Main pipeline (CDEStaging → hood_final_models)
- `scripts/hood_json_adapter.py` — Converts JSON definitions → hood_findings
- `scripts/markdown_to_finding_model_adapter.py` — Converts Markdown definitions → hood_findings
- `scripts/merge_findings.py` — CLI for merging one incoming model with existing
- `scripts/batch_merge_findings.py` — Batch merge of hood_findings → merged_findings

**AI agents** (pydantic-ai, GPT-4o-mini):
- Attribute classifier (presence / change_from_prior / other)
- Attribute relationship classifier (identical, enhanced, subset, needs_review, no_similarities)
- Specificity checker (reject too-general matches)
- Acronym expansion, eponym minimization, sub-finding extraction

---

## Part 2: How the Main Pipeline Works

`hood_to_final_finding.py` does **not** import agents or other scripts directly. It only imports from `scripts/hood_helpers`. All other dependencies live inside `hood_helpers`:

```
hood_to_final_finding.py
    └── scripts/hood_helpers
            ├── scripts/hood_json_adapter          (for JSON definitions)
            ├── scripts/markdown_to_finding_model_adapter   (for Markdown)
            ├── scripts/merge_findings             (find existing, classify, compare)
            │       └── agents/merge_agents         (classification, relationship)
            ├── scripts/merge_findings_helpers      (build final finding, reorder, etc.)
            ├── agents/specificity_agents          (reject general matches)
            └── agents/formatting_agents            (acronyms, eponyms, sub-findings)
```

**In plain terms:**
- The main script talks only to `hood_helpers`.
- `hood_helpers` uses the JSON/Markdown adapters to generate models from definitions.
- It uses `merge_findings` (and its agents) to find matches and merge attributes.
- It uses `merge_findings_helpers` for building and ordering the final model.
- It uses `specificity_agents` and `formatting_agents` for validation and formatting.

---

## Part 3: Accomplished & Pending

### What We Have Accomplished

| Requirement | Status | Where in Code |
|-------------|--------|---------------|
| Hood = incoming, existing DB = reference | Done | `hood_helpers.merge_with_existing`, `find_existing_model` |
| Specificity check (reject general matches) | Done | `hood_helpers.find_existing_model_with_specificity_check` |
| Presence and change_from_prior at top | Done | `merge_findings_helpers.reorder_attributes` |
| Hood contributor (MGB) in merged models | Done | `merge_findings_helpers.ensure_hood_contributor` |
| Presence with yes/no: keep existing if it has standard values | Done | `hood_helpers.ensure_required_attributes`, `merge_findings_helpers.ensure_standard_presence_values` |
| Lowercase, acronym expansion, eponym minimization | Done | `hood_helpers.apply_formatting_guidelines` |
| Full merge strategy (enhanced, identical, subset, etc.) | Done | `merge_agents`, `merge_findings.compare_attributes_within_group` |
| Sub-finding identification via LLM | Done | `hood_helpers.extract_sub_findings`, `formatting_agents` |
| Pipeline: lookup → generate or merge → ensure presence/change | Done | `hood_to_final_finding.process_single_file`, `hood_helpers` |

### What Still Needs to Be Accomplished

| Requirement | Status | Notes |
|-------------|--------|-------|
| **Save sub-findings as separate files** | Not done | Currently identified and logged only |
| **Association between main and sub-findings** | Future | Design TBD |
| Attribute name synonyms in schema | Partial | Need to verify findingmodel support |
| Value synonyms in schema | Partial | Need to verify findingmodel support |
| Locations (feasible regions, structure types) | Partial | `locations` exists; alignment with spec unclear |
| Modalities, life stages, sex phenotypes | Unclear | Need to verify schema and usage |
| Examples (maybe separate repo) | Not started | Decision pending |
| Skip/resume (e.g. `--skip-existing`) | Not done | Re-run overwrites output |
| LLM retry on transient failures | Not done | ModelRetry imported but unused |

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
| Main Hood pipeline | `scripts/hood_to_final_finding.py` |
| Hood logic (load, generate, merge, format, sub-findings) | `scripts/hood_helpers.py` |
| Merge helpers (presence, change, reorder, contributors) | `scripts/merge_findings_helpers.py` |
| Merge CLI, find_existing, classify | `scripts/merge_findings.py` |
| Attribute/relationship agents | `agents/merge_agents.py` |
| Specificity agent | `agents/specificity_agents.py` |
| Formatting agents | `agents/formatting_agents.py` |
| JSON adapter | `scripts/hood_json_adapter.py` |
| Markdown adapter | `scripts/markdown_to_finding_model_adapter.py` |

---

## Part 11: Open Questions

- How to represent associations between main finding and extracted sub-findings
- Where to store examples (same repo vs separate)
- Whether `needs_review` comparisons should have interactive or configurable review
- Schema support for attribute/value synonyms, modalities, life stages, sex phenotypes
