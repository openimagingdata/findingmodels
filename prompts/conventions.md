# Finding Model Conventions

Concrete rules for creating, reviewing, and merging finding models. For context on *why* these rules exist, see `prompts/overview.md` or `prompts/overview_compact.md`.

## Naming

All names (finding, attribute, value, synonym, tag) follow these rules:

- **Spaces, not underscores** in all JSON name fields. Underscores are for filenames only.
- **All lowercase** by default. Exceptions: proper nouns, eponyms, and acronyms used as synonyms.
- **Descriptions** use normal sentence casing.
- **Expand acronyms** in canonical names; keep acronym as synonym. ("ECMO catheter" → name: `"extracorporeal membrane oxygenation catheter"`, synonym: `"ECMO catheter"`)
- **Minimize eponyms** — prefer descriptive terms; keep eponym as synonym. ("Bochdalek hernia" → name: `"posterior diaphragmatic hernia"`, synonym: `"Bochdalek hernia"`) Use clinical judgment — some eponyms ARE the standard term.
- **No brand names** as canonical names — use generic/descriptive term; keep brand as synonym. ("Impella device" → name: `"percutaneous ventricular assist device"`, synonym: `"Impella"`)

### Self-Describing Names

A finding name should be understandable on its own — someone scanning a list of 2,000 models should be able to tell what each one is about without reading the description. Include enough anatomic or organ-system context to make the name self-describing.

- "linear opacity" → `"pulmonary linear opacity"` — immediately clear what you're talking about
- "interstitial thickening" → `"pulmonary interstitial thickening"`
- "architectural distortion" → `"pulmonary architectural distortion"`
- "fissure thickening" → `"pulmonary fissure thickening"`
- "mass" → `"pulmonary mass"`, `"mediastinal mass"`, `"renal mass"`, etc.
- "lucency" → `"pulmonary lucency"`, `"osseous lucent lesion"`, etc.
- "hyperinflation" → `"pulmonary hyperinflation"`
- "sclerosis" → `"osteosclerosis"`

The unscoped short form (e.g., "linear opacity", "mass") should be kept as a synonym so it still matches in report text where the context makes the anatomy clear.

Findings that are inherently self-describing don't need additional context — "cardiomegaly", "pneumothorax", "pleural effusion" already communicate what they are.

Note: this is about **readability**, not just disambiguation. Even if "cephalization" technically only refers to pulmonary vasculature, "cephalization of pulmonary vasculature" is immediately clear while "cephalization" requires domain knowledge to parse.

Some findings are appropriately broad without anatomic scoping — "fracture", "osseous abnormality", "soft tissue abnormality" are general-purpose findings where anatomy is captured as an attribute, not in the name.

### Name Conciseness

Finding names should be the **shortest unambiguous clinical term** for the observation. Qualifiers, context, and associated findings belong in attributes, tags, or the description — not in the name.

- **No parenthetical qualifiers.** Acronyms, brand names, and clarifications become synonyms.
  - "cardiac rhythm monitor (Zio Patch)" → name: `"cardiac rhythm monitor"`, synonym: `"Zio Patch"`
  - "spinal cord compression scale (ESCC)" → name: `"spinal cord compression scale"`, synonym: `"ESCC"`

- **No population qualifiers in names.** Use tags instead.
  - "abdominal calcification in an infant" → name: `"abdominal calcification"`, tag: `"pediatric"`

- **No "with" clauses** embedding associated findings. These should be separate models.
  - "pneumonia with parapneumonic effusion" → separate models: `"pneumonia"` and `"parapneumonic effusion"`
  - "arthritis with joint erosion" → separate models: `"arthritis"` and `"joint erosion"`

- **No comma-separated lists.** Split into separate models or simplify.
  - "fragmented, irregular, or sclerotic carpal or tarsal bones" → consider splitting by anatomy and simplifying the description

- **Slashes** — handle by type:
  - If the slash separates **genuinely different findings** → split into separate models ("encephalocele/meningocele" → two models)
  - If the slash separates **locations or severities of the same finding** → simplify the name, make the distinction an attribute ("cortical/subcortical hyperintensity" → name: `"gyriform hyperintensity"`, attribute: location)
  - If the slash separates **truly interchangeable terms** → pick one, make the other a synonym ("leukodystrophy/leukoencephalopathy" → name: `"leukodystrophy"`, synonym: `"leukoencephalopathy"`)

### Filenames

Filenames are derived from the finding name by `model_file_name()`: lowercase, non-alphanumeric characters replaced with single underscores. **No consecutive underscores** — if the name contains punctuation that would produce `__`, the name itself should be simplified (see rules above).

## Synonyms

### Why Synonyms Matter

Synonyms are how unstructured report text gets matched to finding models. Radiologists express the same observation in many different ways — formal terminology, abbreviations, colloquial shorthand, regional variations. The more synonyms a model has, the more likely the NLP pipeline will correctly match report language to the right finding. **Be aggressive about collecting synonyms** — capture every way a radiologist might refer to this finding in a report.

### Quality: Exact Matches Only

Every synonym must mean the **exact same thing at the same level of specificity** as the canonical name. This constraint is strict because a bad synonym doesn't just fail to match — it matches the **wrong thing**, causing an incorrect observation that propagates downstream.

- **Subtypes are NOT synonyms.** "bullous emphysema" ≠ "emphysema" (subtype). "renal tumor" ≠ "renal lesion" (more specific). Don't add subtypes as synonyms to compensate for NLP matching gaps — the matching system handles subtype-to-parent matching at a different layer.
- **Different levels of generality are NOT synonyms.** "pleural lesion" ≠ "pleural abnormality" ("lesion" implies focal; "abnormality" is any deviation from normal). "pleural density" ≠ "pleural abnormality" (specific observation vs. broad category).
- **Good synonyms** are different words for the same concept at the same level: "collapsed lung" = "atelectasis"; "pleural disease" = "pleural abnormality"; "chest port" = "implantable venous access port".
- Do NOT include the canonical name itself as a synonym.
- **The test:** "If a radiologist writes term A in a report, does it ALWAYS mean the same thing as term B, at the same level of specificity?" If not, they're not synonyms.

**Be aware that radiologists often use related terms loosely in reports**, which makes these false equivalences tempting. But the finding model needs to be precise even when report language is not. Common traps:

- **Sign vs disease**: "Kerley B lines" ≠ "interstitial pulmonary edema" — Kerley lines are a radiographic sign that can indicate edema, but they're not the same thing
- **Consequence vs cause**: "aspiration pneumonia" ≠ "aspiration" — pneumonia is a consequence of aspiration, not a synonym for it
- **Different pathophysiology**: "right ventricular hypertrophy" ≠ "right ventricular enlargement" — hypertrophy is wall thickening, enlargement is chamber dilation; different processes with different imaging appearances
- **Different procedure**: "kyphoplasty" ≠ "vertebroplasty" — both involve cement injection into vertebrae, but kyphoplasty includes balloon inflation; they are distinct procedures
- **Component vs whole**: "Kerley B lines" ≠ "interstitial thickening" — Kerley B lines are one manifestation of interstitial thickening, not the whole thing
- **Structure vs state**: "cardiomegaly" ≠ "cardiac silhouette abnormality" — cardiomegaly is a specific state (enlarged); the abnormality category is broader
- **Device subtypes**: "nasogastric tube" ≠ "enteric tube" — NG tube is a specific type of enteric tube; similarly "mechanical mitral valve" ≠ "mitral valve replacement" (subtype of prosthesis)
- **Too general for the finding**: "annuloplasty ring" ≠ "mitral annuloplasty ring" — the generic term could refer to tricuspid or other annuloplasty rings too
- **Different anatomic location**: "CABG clips" ≠ "mediastinal clips" — CABG clips are a specific use case in a specific surgical context; "rib cerclage wires" ≠ "cerclage wire" — scoped to ribs when the finding is general

### What To Do With Subtypes

When you encounter a potential subtype (e.g., "linear atelectasis" relative to "atelectasis"), decide whether it's an **attribute value** on the parent or a **separate finding model**:

- **Attribute value**: If the subtype is the same observation with a qualifier, it's a type/morphology value on the parent. "Linear atelectasis", "plate-like atelectasis", "round atelectasis" → add a `"morphology"` attribute on the atelectasis model with these as values. They're all atelectasis, just with different shapes.
- **Separate finding model**: If the subtype is a fundamentally distinct observation that a radiologist would recognize as a different entity, it warrants its own model. "Tension pneumothorax" isn't "pneumothorax, type: tension" — it's a distinct clinical entity with its own urgency, specific signs (mediastinal shift, hemidiaphragm depression), and management implications.

The question: **"Is this a fundamentally distinct observation, or the same observation with a qualifier?"** If a radiologist would recognize this as a distinct entity requiring its own characterization — not just the parent finding with a label attached — it warrants its own model. A practical signal: you'd need different attributes to describe it.

### Collision Detection

A synonym should belong to exactly one finding model. Before adding a synonym, use `findingmodel search` (the same search used for finding existing matches) to check whether the term is already used by another model:

- If the term already appears as a name or synonym on **a different model that means the same thing**, you may have a duplicate model situation — flag it.
- If the term already appears on **a different model that means something different**, do NOT add it as a synonym here. The term is ambiguous — it could refer to either finding depending on context. Leave it off both models for now and flag the ambiguity for human review.
- If the term is not found elsewhere, add it.

### What to Include as Synonyms

Think about all the ways a radiologist might express this finding in a report:
- **Formal vs informal**: "peripherally inserted central catheter" / "PICC line" / "PICC"
- **Acronyms and abbreviations**: "ECMO catheter" for "extracorporeal membrane oxygenation catheter"
- **Eponyms**: "Kerley B lines" for "peripheral interstitial lines"
- **Brand names**: "MitraClip" for "percutaneous mitral valve clip"
- **British/American spelling variants**: if applicable
- **Plural forms**: "lung nodules" as synonym for "pulmonary nodule" (if the model covers both singular and plural usage)
- **Common report phrasings**: "fluid in the pleural space" for "pleural effusion", "air under the diaphragm" for "pneumoperitoneum"

## Standard Attributes

Every finding model has two required standard attributes as its first two attributes.

### 1. presence (first attribute, always)

Values: `absent`, `present`, `indeterminate`, `unknown`. Upgrade [yes/no] or [present/absent] to the full set.

### 2. change from prior (second attribute, always)

Minimum values: `unchanged`, `stable`, `new`, `resolved`. Plus at least one clinically appropriate direction pair:

- `larger`/`smaller` — masses, effusions, structures with measurable size
- `increased`/`decreased` — quantities, density, extent
- `worsened`/`improved` — conditions, disease states

**Include ALL pairs a radiologist would actually use to describe change in this finding.** The goal is not to pick the single best pair, but to capture every descriptor a radiologist might reach for. A pleural effusion could be described as "larger", "increased", or "worsened" — include all three pairs if they're all natural language a radiologist would use.

**Exclude pairs that make no clinical sense:**
- **Devices/hardware**: no direction pairs (devices don't grow or worsen)
- **Congenital variants**: no direction pairs (they don't change)
- **Postsurgical states**: no direction pairs (they're permanent)
- **Technique/quality**: no direction pairs (per-image observations)

**Guidance for other findings** (include all that apply):
- A finding with measurable size → include `larger`/`smaller`
- A finding that can increase/decrease in extent or degree → include `increased`/`decreased`
- A finding that is a condition/process → include `worsened`/`improved`
- Many findings qualify for multiple pairs — that's fine

Note: attribute name uses spaces (`"change from prior"`), NOT underscores.

### Description Grammar

- Plural nouns need plural verbs: "Surgical clips **are** absent"
- Articles must agree: "Whether and how **an** aortic stent..."
- Mass/uncountable nouns: no article ("Whether and how emphysema has changed")
- "Presence of X is unknown" — "Presence" is always the subject, always singular

## Related Findings: Associated Findings vs Components

When building a finding model, you will encounter things related to the index finding that need their own models. There are two fundamentally different kinds of related things, and recognizing which is which matters:

### Associated Findings (co-occurring but independent)

An associated finding is a **separate, independent finding** that happens to co-occur with the index finding. It has its own lifecycle — it can appear, change, or resolve independently of the index finding.

**The independence test:** Could you see this related thing without the index finding, or vice versa? If yes, it's an associated finding.

Example: Pneumonia and pleural effusion are associated findings. A patient can have pneumonia without effusion, or effusion without pneumonia. They co-occur frequently, but they're separate entities with their own attributes (the effusion has its own size, laterality, character).

**How to model:** A single multichoice `"associated findings"` attribute on the index model — a checklist of what else to look for, presence-level only. No characterization of the associated findings here; their details live in their own models and observations.

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
- **One attribute, many values.** Consolidate all associated findings into one multichoice attribute — not scattered across separate presence attributes.
- **Presence-level only.** No size, severity, or other characterization. That belongs in the associated finding's own model.
- **Values should reference finding models** by name, ideally with OIFM codes, so the association is machine-resolvable.

### Components (intrinsic parts that are too complex to inline)

A component is a **structural part of the index finding itself** — not a separate entity, but a piece of it that has enough complexity to warrant its own model definition. Think of it like defining a separate class for an address within a contact record: the address isn't an independent entity, but it's complex enough that inlining all its fields would clutter the parent.

**The independence test:** Would you ever document this thing as a standalone observation without its parent? If not, it's a component. A "solid component" doesn't exist without a parent nodule. A "cystic portion" doesn't exist without the parent mass.

Example: A mixed pulmonary nodule has a solid component and a ground-glass component. Each has its own measurable size, density, and morphology. These aren't separate findings — they're parts of what the nodule IS. But they're complex enough that modeling them inline (with prefixed attributes like "solid component size", "solid component density", "ground-glass component size"...) would clutter the nodule model.

**How to model:** Extract components into their own finding model definitions so they can have proper attributes. The relationship between a component observation and its parent observation is handled at the Observation layer, not in the finding model attributes.

**What the parent model CAN include about a component:** The parent model may note whether a component exists and how many — that's still describing the parent finding, not characterizing the component:
- For a component that's either there or not: a choice attribute with values like `present`, `possibly present`, `absent`
- For a component you could have many of: a numeric count attribute

What the parent model should NOT do is characterize the component itself (size, density, morphology) — those details belong in the component's own model.

**Component models are full finding models.** When extracted, a component gets its own complete finding model definition with its own `presence` and `change from prior` as the first two attributes, just like any other finding.

> **Terminology note:** In agent output schemas, both associated findings and components flagged for extraction are reported in the `findings_to_create` field.

### Recognizing What Needs Extraction

When reviewing source material or existing models, look for these signals that something should be extracted:

- **Prefixed attributes**: "solid component size", "cystic component density" — the prefix names a sub-entity
- **Attribute groups**: 2+ attributes that all describe the same sub-entity rather than the index finding
- **Characterization beyond presence**: if you're capturing size, severity, morphology, or other properties of something other than the index finding, that something needs its own model — whether it's an associated finding or a component

The key question: **"Is this attribute describing the index finding, or describing something else?"** If something else, decide: is it independent (associated finding) or intrinsic (component)? Either way, it needs its own model.

## Compound Finding Detection

- Models should not lump together independently-occurring findings
- Signals: "and/or", "and", or slash separators in names
- Test: can one component be present while the other is absent? If yes → separate models
- Example: "mediastinal and/or hilar lymphadenopathy" → split

## Descriptions

- 1-2 concise sentences, clinically accurate, written for a radiologist audience
- No placeholder text ("None", "N/A", "TODO")

For guidance on appropriate specificity and scope of findings, see `prompts/overview.md`.
