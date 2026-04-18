# Synonyms

## Why synonyms matter

Synonyms are how unstructured report text gets matched to finding models. Radiologists express the same observation many ways — formal terminology, abbreviations, colloquial shorthand, regional variants. **Be aggressive about collecting synonyms** — every additional synonym increases the chance the NLP pipeline matches report language to the right finding.

## Strictness: exact match only

Every synonym must mean the **exact same thing at the same level of specificity** as the canonical name. This constraint is strict because a bad synonym doesn't just fail to match — it matches the *wrong thing*, causing an incorrect observation that propagates downstream.

- **Subtypes are NOT synonyms.** `bullous emphysema` ≠ `emphysema`. `renal tumor` ≠ `renal lesion`. See `scope_and_specificity.md` for how to handle subtypes.
- **Different levels of generality are NOT synonyms.** `pleural lesion` ≠ `pleural abnormality` (a lesion is focal; an abnormality is any deviation).
- **Good synonyms**: `collapsed lung` = `atelectasis`; `chest port` = `implantable venous access port`; `MitraClip` = `percutaneous mitral valve clip`.
- **Never include the canonical name itself** as a synonym.

**The test:** "If a radiologist writes term A in a report, does it ALWAYS mean the same thing as term B, at the same level of specificity?" If not, they're not synonyms.

## Common traps

Radiologists often use related terms loosely in reports, which makes false equivalences tempting. The model must be precise even when report language is not.

- **Sign vs disease**: `Kerley B lines` ≠ `interstitial pulmonary edema` — the lines are a radiographic sign that can indicate edema, not the edema itself.
- **Consequence vs cause**: `aspiration pneumonia` ≠ `aspiration`.
- **Different pathophysiology**: `right ventricular hypertrophy` ≠ `right ventricular enlargement` — wall thickening vs chamber dilation.
- **Different procedure**: `kyphoplasty` ≠ `vertebroplasty` — kyphoplasty includes balloon inflation.
- **Component vs whole**: `Kerley B lines` ≠ `interstitial thickening` — the lines are one manifestation of thickening.
- **Structure vs state**: `cardiomegaly` ≠ `cardiac silhouette abnormality` — cardiomegaly is a specific state; the abnormality category is broader.
- **Device subtypes**: `nasogastric tube` ≠ `enteric tube` — NG tube is one specific enteric tube.
- **Too general for the finding**: `annuloplasty ring` ≠ `mitral annuloplasty ring` — the generic term could refer to tricuspid rings too.
- **Wrong anatomic scope**: `CABG clips` ≠ `mediastinal clips` — CABG clips have a specific surgical context.

## What to include as synonyms

Think through every way a radiologist might write this finding in a report:

- **Formal vs informal**: `peripherally inserted central catheter` / `PICC line` / `PICC`
- **Acronyms and abbreviations**: `ECMO catheter` for `extracorporeal membrane oxygenation catheter`
- **Eponyms**: `Kerley B lines` for `peripheral interstitial lines`
- **Brand names**: `MitraClip` for `percutaneous mitral valve clip`
- **British/American spelling variants** where applicable
- **Plural forms** where the model covers both singular and plural usage
- **Common report phrasings**: `fluid in the pleural space` for `pleural effusion`, `air under the diaphragm` for `pneumoperitoneum`

## Collision check (required before adding)

A synonym should belong to exactly one finding model. Before adding a synonym, run `findingmodel search "<proposed synonym>" --limit 3`:

- **Already on a different model that means the same thing** — you may have a duplicate model situation. Flag it for human review; do not add silently.
- **Already on a different model that means something different** — the term is ambiguous. Do NOT add it. Leave it off both models and flag the ambiguity.
- **Not found elsewhere** — safe to add.

The unscoped short form of a self-describing name (e.g., `mass` as a synonym on `pulmonary mass`) is the most common collision hazard — scope the check accordingly.
