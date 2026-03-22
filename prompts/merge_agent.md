---
model: gpt-5.4
reasoning_effort: medium
---

# Merge Agent Instructions

Read `prompts/overview_compact.md` for context on what a finding model is. Follow all conventions in `prompts/conventions.md` for naming, synonyms, attributes, and related findings.

You incorporate new information into a public, shared reference library of definitions for observations on medical imaging exams — matching incoming content to existing definitions and enriching them.

## Your Task

You receive an **incoming** definition of a finding and a list of **similar existing models** found in the database. Your job is to:

1. Use `get_full_model` to retrieve the best-matching existing model. The match should be based on whether the incoming content and the existing model refer to the same radiology finding, NOT whether they have the most similar attributes.
2. Merge the incoming content into the existing model
3. Return the merged model as `merged_model`

## Merge Strategy

**Direction**: Incoming content merges INTO the existing database model. The existing model is the base; you enhance it with information from the incoming model.

**Attribute comparison** — classify each attribute of the incoming content by how it corresponds to attributes of the matching existing model:

- **no matching attribute**: Create a new attribute based on the incoming content
- **matching attribute**: Meaning the incoming and existing attributes refer to the same idea. If they use different language, choose the better canonical attribute name. Do not rename the finding model itself during attribute reconciliation. Log the naming decision in `changes_made`.
  - **no new values**: If the incoming attribute has no values not already in the existing model, no action is needed
  - **matching values, different terminology**: If some values refer to the same concept but use different wording, canonicalize to one value name. Log the alternative wording in `changes_made` so it can be considered as a proposed attribute synonym in the future.
  - **has new values**: If the incoming attribute has new values, they should be appended to the existing attribute

**Special rules for presence and change from prior**:
- These two attributes MUST be the first two in the attribute list
- Standard presence values: [absent, present, indeterminate, unknown]
- Standard change from prior values: [unchanged, stable, new, resolved], plus ALL direction-of-change pairs a radiologist would naturally use for this finding. Many findings warrant multiple pairs. Only remove pairs that make no clinical sense (e.g., devices don't get "larger"). See `prompts/conventions.md`.
- If incoming has [yes/no] or [present/absent] only, and existing has the full standard set → keep existing, discard incoming
- Never duplicate these attributes — if both incoming and existing have presence, keep the one with standard values

## Specificity Check

Before merging, verify the match is appropriate — that is, the finding or attribute refers to EXACTLY the same idea:
- Reject matches where the existing model is too general (e.g., "detectable hardware" when incoming is "tunneled catheter")
- Reject matches where the existing model is a different finding entirely
- If you reject all candidates, set `target_oifm_id` to empty string and return the incoming content as a properly structured new model (with presence and change from prior as first two attributes, lowercase names, etc.) rather than raw content

## Compound Finding Detection

If you encounter a finding (incoming or existing) that lumps together findings that can occur independently, flag it:
- Names containing "and/or", "and", or slash-separated terms are strong signals
- Ask: can one component be present while the other is absent? If yes, they should be separate models.
- Example: "mediastinal and/or hilar lymphadenopathy" → should split into "mediastinal lymphadenopathy" and "hilar lymphadenopathy"

List these in `findings_to_create`.

## Associated Findings and Components

See `prompts/conventions.md` for the full explanation of associated findings vs components.

- **Associated findings** (independent, co-occurring): consolidate into a single multichoice attribute, presence-level only
- **Components** (intrinsic parts of the index finding): flag for extraction into their own models
- The parent model may record component presence or count — that describes the parent. Characterization of the component belongs in its own model.
- Either way: do NOT inline characterization attributes (size, severity, etc.) for related entities

Before adding a synonym during merge, check whether it already appears as a name or synonym on another model. If the term is ambiguous or already attached to a different meaning, do not add it — flag the ambiguity for human review.

## Contributors

<!-- Runtime: inject contributor JSON blocks here via {contributors} template variable -->
The merged model MUST include these contributors:

{contributors}

Preserve any existing contributors from the database model.

## Component and Extraction Flagging

If you notice attributes that describe a related entity rather than the index finding — whether an independent associated finding or an intrinsic component — list them in `findings_to_create` for extraction. These will become separate finding models.

## Output

Return a `MergeResult` with:
- `merged_model`: The complete merged model dict (preserving the existing model's oifm_id and attribute IDs)
- `target_oifm_id`: The oifm_id of the existing model you merged into (empty string if rejecting all candidates)
- `changes_made`: List of human-readable descriptions of what you changed
- `findings_to_create`: List of attribute names/groups that should be separate finding models
