# Associated findings vs components

When building a finding model, you will encounter related things that are not the index finding itself but are connected to it. There are two fundamentally different kinds of related thing, and recognizing which is which matters.

## Associated findings (co-occurring but independent)

An **associated finding** is a separate, independent finding that happens to co-occur with the index finding. It has its own lifecycle — it can appear, change, or resolve independently.

**Independence test:** could you see this related thing *without* the index finding, or vice versa? If yes, it's an associated finding.

Example: pneumonia and pleural effusion. A patient can have pneumonia without effusion, or effusion without pneumonia. They co-occur frequently but are separate entities with their own attributes (effusion has its own size, laterality, character).

### How to model

One multichoice `associated findings` attribute on the index model — a checklist of what else to look for, **presence-level only**. Each value should reference the name of an actual finding model.

```json
{
  "name": "associated findings",
  "type": "choice",
  "max_selected": 10,
  "values": [
    {"name": "parapneumonic effusion"},
    {"name": "air bronchograms"},
    {"name": "septic emboli"},
    {"name": "lung abscess"}
  ]
}
```

Rules:

- **One attribute, many values.** Consolidate all associated findings into one multichoice attribute — not scattered across separate `presence of X` attributes.
- **Presence-level only.** No size, severity, laterality, or other characterization. Those details live in the associated finding's own model.
- **Values should reference finding model names** so the association is machine-resolvable.

## Components (intrinsic parts that warrant their own model)

A **component** is a structural part of the index finding itself — not a separate entity, but a piece of it complex enough to justify its own model. Think of it like extracting an address record from a contact record: the address isn't independent, but inlining all its fields would clutter the parent.

**Independence test:** would you ever document this thing as a standalone observation without its parent? If not, it's a component.

Example: a mixed pulmonary nodule has a solid component and a ground-glass component. Each has measurable size, density, and morphology. They aren't separate findings — they're parts of what the nodule IS — but inlining attributes like `solid component size`, `solid component density`, `ground-glass component size` would clutter the parent.

### How to model

Extract components into their own finding model definitions. Each component gets a full model with its own `presence` and `change from prior` as the first two attributes, just like any other finding.

**What the parent model CAN record about a component:** presence and count, because those describe the parent:

- Either/or components: a choice attribute with values `present`, `possibly present`, `absent`.
- Countable components: a numeric count attribute.

**What the parent model must NOT do:** characterize the component (size, density, morphology, severity). Those details belong in the component's own model, not in the parent.

## Recognizing what needs extraction

When reviewing source material or an existing model, these signals mean something needs extraction:

- **Prefixed attributes** — `solid component size`, `cystic component density`. The prefix names a sub-entity.
- **Attribute groups** — 2+ attributes that all describe the same sub-entity rather than the index finding.
- **Characterization beyond presence** — size, severity, morphology of something other than the index finding.

Two questions to ask:

1. **"Is this attribute describing the index finding, or describing something else?"** If something else → flag for extraction.
2. **"Is that something else independent or intrinsic?"** Independent → associated finding. Intrinsic → component.

Either way, flag the finding for extraction. In agent output, both appear in the `findings_to_create` field — the reviewer/extractor decides the associated-vs-component split when building the new model.
