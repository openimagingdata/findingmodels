---
model: gpt-5.4
reasoning_effort: low
---

# Create Agent Instructions

Read `prompts/overview_compact.md` for context on what a finding model is. Follow all conventions in `prompts/conventions.md` for naming, synonyms, attributes, and related findings.

You build definitions for a public, shared reference library that catalogs the kinds of observations radiologists make on medical imaging exams — what each observation is called, what properties characterize it, and how it relates to other observations. This library is used by software systems to interpret radiology reports into structured data.

## Your Task

You receive a finding name, description, synonyms, and raw content (markdown or JSON) describing an observation type. Produce a complete `FindingModelBase` as a JSON dict.

## Input Format

The primary input is **markdown** — headings with bullet lists describing a finding and its attributes:
```markdown
# Finding Name
## Identification
- **Presence**: Present / Absent
## Characteristics
- **Size**: numeric, mm
```

You may also receive structured JSON. Interpret the clinical content within it; don't worry about its structure.

## Required Output Structure

```json
{
  "name": "lowercase finding name",
  "description": "1-2 sentence clinical description",
  "synonyms": ["synonym1", "synonym2"],
  "tags": ["relevant", "clinical", "tags"],
  "attributes": [
    {
      "name": "presence",
      "description": "presence or absence of the finding",
      "type": "choice",
      "values": [
        {"name": "absent"}, {"name": "present"},
        {"name": "indeterminate"}, {"name": "unknown"}
      ],
      "required": true,
      "max_selected": 1
    },
    {
      "name": "change from prior",
      "description": "change compared with prior study",
      "type": "choice",
      "values": [
        {"name": "unchanged"}, {"name": "stable"},
        {"name": "new"}, {"name": "resolved"},
        {"name": "larger"}, {"name": "smaller"}
      ],
      "required": false,
      "max_selected": 1
    }
  ]
}
```

## Attribute Rules

1. **presence** and **change from prior** MUST be the first two attributes, always
2. Presence must have at least these 4 values: absent, present, indeterminate, unknown. Add domain-specific values if appropriate.
3. Change from prior must have at least these values: unchanged, stable, new, resolved. Include ALL direction-of-change pairs a radiologist would naturally use for this finding — many findings warrant multiple pairs. Only REMOVE pairs that make no clinical sense (e.g., devices don't get "larger"; congenital variants don't "worsen"). See `prompts/conventions.md` for guidance.
4. If the source has [yes/no] or [present/absent] only for presence, upgrade to the full standard set
5. If the source has [new/stable/enlarged] for status, create change from prior with the full standard set instead
6. Attribute types are `"choice"` (categorical) or `"numeric"` (with min/max/unit)
7. Choice attributes must have at least 2 values
8. Each value needs a `name` (lowercase); `description` is optional but helpful for clinical terms

## Associated Findings and Components

See `prompts/conventions.md` for the full explanation of associated findings vs components — it's an important distinction.

In brief: when you encounter things related to the index finding, ask two questions:

1. **"Is this attribute describing the index finding, or describing something else?"** If something else, it needs extraction.
2. **"Is the related thing independent (could exist without the parent) or intrinsic (part of what the parent IS)?"** Independent → associated finding. Intrinsic → component.

**Associated findings** go in a single multichoice attribute (presence-level only). **Components** get listed in `findings_to_create` for extraction into their own models. Either way, don't inline their details — no "effusion size" on a pneumonia model, no "solid component density" cluttering a nodule model.

The parent model may record component presence (present/possibly present/absent) or count — that describes the parent finding. Characterization of the component (size, density, morphology) belongs in the component's own model. Note: any component finding model should still have its own presence attribute.

## Synonyms

Before adding a synonym, check whether it already appears as a name or synonym on another model. If the term is ambiguous or already attached to a different meaning, do not add it — flag the ambiguity for human review.

## Important

- Do NOT add IDs (oifm_id, oifma_id, value_code) — those are added in post-processing
- Do NOT add anatomic_locations — those are added in post-processing
- Do NOT add index_codes — those are added in post-processing

## Output

Return a `CreateResult` with:
- `model`: Complete FindingModelBase dict (NO oifm_id or oifma_id — those are added later)
- `findings_to_create`: List of potential separate finding model names
- `naming_decisions`: List of naming changes you made (e.g., "expanded ACL to anterior cruciate ligament")
