# Naming and Synonym Rules

These rules apply to all finding model names, attribute names, value names, synonyms, and tags.

## Spacing and Casing

- **No underscores in names.** All names use **spaces**, not underscores. Underscores are only for filenames.
- **Lowercase by default.** Finding names, attribute names, value names, synonyms, and tags are all lowercase.
  - Exception: proper nouns retain capitalization (e.g., "Hounsfield units", "Bochdalek hernia" as a synonym)
- **Descriptions** may use normal sentence casing.

## Acronyms

- Expand acronyms in canonical names. Add the acronym as a synonym (for model-level) or note it in the description (for attributes).
  - Example: "ACL tear" → name: "anterior cruciate ligament tear", synonyms: ["ACL tear"]
  - Example: attribute "HU" → "Hounsfield units"

## Eponyms

- Minimize eponyms. Prefer the descriptive term as the canonical name; keep the eponym as a synonym.
  - Example: "Bochdalek hernia" → name: "posterior diaphragmatic hernia", synonyms: ["Bochdalek hernia"]

## Brand and Trade Names

- Never use brand/trade names as canonical names. Use the generic/descriptive term; keep the brand as a synonym.
  - Example: "Impella device" → name: "percutaneous ventricular assist device", synonyms: ["Impella"]

## Synonym Strictness

Synonyms must mean the **exact same thing**. A subtype, a more specific term, or a more general term is NOT a synonym.

- "bullous emphysema" is NOT a synonym for "emphysema" (it's a specific subtype)
- "renal tumor" is NOT a synonym for "renal lesion" (more specific ≠ synonym)
- Litmus test: "If I see term A in a report, does it **always** mean the same thing as term B?" If not, they are not synonyms.
