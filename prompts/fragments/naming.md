# Naming

Rules for every name field in a finding model — finding name, attribute name, value name, synonym, tag.

## Casing and formatting

- **Spaces, not underscores**, in every JSON name field. Underscores are for filenames only.
- **All lowercase** by default. Exceptions: proper nouns, eponyms, and acronyms kept as synonyms.
- **Descriptions** use normal sentence casing.

## Canonical forms

- **Expand acronyms** in the canonical name; keep the acronym as a synonym.
  - "ECMO catheter" → name `extracorporeal membrane oxygenation catheter`, synonym `ECMO catheter`
- **Minimize eponyms** — prefer descriptive terms; keep the eponym as a synonym. Use clinical judgment; some eponyms *are* the standard term.
  - "Bochdalek hernia" → name `posterior diaphragmatic hernia`, synonym `Bochdalek hernia`
- **No brand names** as canonical names; use the generic/descriptive term; keep the brand as a synonym.
  - "Impella device" → name `percutaneous ventricular assist device`, synonym `Impella`

## Self-describing names

A finding name should be understandable on its own — someone scanning a list of thousands of models should be able to tell what each one is about from the name. Include enough anatomic or organ-system context for readability.

- "linear opacity" → `pulmonary linear opacity`
- "mass" → `pulmonary mass`, `mediastinal mass`, `renal mass`, etc.
- "lucency" → `pulmonary lucency`, `osseous lucent lesion`
- "sclerosis" → `osteosclerosis`

Keep the unscoped short form as a synonym so report text like "mass in the right upper lobe" still matches. Findings that are inherently self-describing don't need scoping: `cardiomegaly`, `pneumothorax`, `pleural effusion`.

Some findings are appropriately broad without anatomic scoping — `fracture`, `osseous abnormality` — where anatomy is captured as an attribute rather than baked into the name.

## Name conciseness

Finding names should be the **shortest unambiguous clinical term** for the observation. Qualifiers, context, and associated findings belong in attributes, tags, or the description — not in the name.

- **No parenthetical qualifiers.** Acronyms, brand names, and clarifications become synonyms.
  - "cardiac rhythm monitor (Zio Patch)" → name `cardiac rhythm monitor`, synonym `Zio Patch`
- **No population qualifiers in names.** Use tags.
  - "abdominal calcification in an infant" → name `abdominal calcification`, tag `pediatric`
- **No "with" clauses** embedding associated findings. Split into separate models.
  - "pneumonia with parapneumonic effusion" → `pneumonia` and `parapneumonic effusion`, each its own model
- **No comma-separated lists.** Split or simplify.

### Slashes — handle by type

- **Genuinely different findings** → split into separate models.
  - "encephalocele/meningocele" → two models
- **Locations or severities of the same finding** → simplify the name, make the distinction an attribute.
  - "cortical/subcortical hyperintensity" → name `gyriform hyperintensity`, attribute `location`
- **Truly interchangeable terms** → pick one, make the other a synonym.
  - "leukodystrophy/leukoencephalopathy" → name `leukodystrophy`, synonym `leukoencephalopathy`

## Filenames

Filenames are derived from the finding name by `model_file_name()`: lowercase, non-alphanumeric characters replaced with single underscores. **No consecutive underscores** — if the name would produce `__`, simplify the name per the rules above.
