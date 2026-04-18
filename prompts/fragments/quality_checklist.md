# Quality checklist

Apply this checklist to a finding model. Each item is a one-line summary of a rule; deeper reference lives in the companion rule fragments, which you only need to open when the one-liner isn't enough to decide an edge case.

**Context prerequisites:** `core_concept.md`. **Reference fragments for edge cases:** `naming.md`, `synonym_rules.md`, `presence_and_change.md`, `associated_vs_component.md`, `scope_and_specificity.md`.

## Scope and specificity

- [ ] The finding name is a **noun phrase** — not an adjective ("rotated" → "patient rotation"), not a clause ("image marker absent" → "image marker absence"), not a state ("stable cardiac silhouette" is not a finding at all). _(`core_concept.md`, `scope_and_specificity.md`)_
- [ ] Level of abstraction is right — not too broad ("infection", bare "mass") and not too narrow ("bibasilar consolidation" bakes location into the name). _(`scope_and_specificity.md`)_
- [ ] Broad findings are scoped to assessable anatomy (`chest wall fracture`, not `fracture`). _(`scope_and_specificity.md`)_
- [ ] The finding is not a compound that lumps independently-occurring findings. Names with "and/or", "and", or slashes are signals — split into separate models if components can occur alone. Log in `findings_to_create`; do not restructure in place. _(`scope_and_specificity.md`)_

## Naming

- [ ] Names use spaces, not underscores. Underscores are only for filenames. _(`naming.md`)_
- [ ] All names lowercase except justified proper nouns, eponyms, or acronyms kept as synonyms. Descriptions use normal sentence casing. _(`naming.md`)_
- [ ] Acronyms expanded in the canonical name (acronym kept as a synonym); brand names replaced with generic terms; eponyms minimized unless they ARE the standard term. _(`naming.md`)_
- [ ] No parenthetical qualifiers, no population qualifiers, no "with" clauses, no comma-separated lists in names. _(`naming.md`)_
- [ ] Generic descriptor names are scoped to anatomy (`pulmonary mass`, not `mass`); short form retained as a synonym. _(`naming.md`)_

## Synonyms

- [ ] Every synonym means the **exact same thing at the same level of specificity** — no subtypes, no supertypes, no signs-vs-disease, no close-but-different terms. _(`synonym_rules.md`)_
- [ ] Canonical name is not duplicated in the synonym list. _(`synonym_rules.md`)_
- [ ] Collision check was done: the synonym does not already appear on a different model that means something different. _(`synonym_rules.md`)_
- [ ] Useful synonyms are present — acronyms, eponyms, brand names, common report phrasings, spelling variants — aggressive collection is good as long as strictness holds. _(`synonym_rules.md`)_

## Presence and change from prior

- [ ] `presence` is the first attribute. Values include at minimum `absent`, `present`, `indeterminate`, `unknown`. No `[yes/no]` masquerading as presence. _(`presence_and_change.md`)_
- [ ] `change from prior` is the second attribute. Name uses spaces, not underscores. Values include at minimum `unchanged`, `stable`, `new`, `resolved`. If the attribute is entirely missing on an existing model, add it via `scripts/finding_authoring/add_change_from_prior.py <file> --pairs ...` — do not hand-build. _(`presence_and_change.md`)_
- [ ] `change from prior` includes every direction-of-change pair a radiologist would naturally use for this finding (`larger`/`smaller`, `increased`/`decreased`, `worsened`/`improved`). _(`presence_and_change.md`)_
- [ ] `change from prior` **excludes** pairs that make no clinical sense for this finding (devices don't `worsen`; congenital variants don't change; fractures don't get `larger`). _(`presence_and_change.md`)_
- [ ] No duplicate `presence` or `change from prior` attributes.
- [ ] Description grammar is natural English — articles agree, plural verbs with plural subjects, no awkward "a emphysema" constructions. _(`presence_and_change.md`)_

## Attributes

- [ ] Every choice attribute has at least 2 values.
- [ ] No attribute characterizes a related entity — no `solid component size`, no `effusion size` on a pneumonia model. Those details belong in the related model. _(`associated_vs_component.md`)_
- [ ] If associated findings are present, they are consolidated into a single multichoice `associated findings` attribute, presence-level only — not scattered as separate `presence of X` attributes. _(`associated_vs_component.md`)_
- [ ] Attribute descriptions are present and clinically appropriate (1-2 sentences).
- [ ] Numeric attributes have reasonable min / max / unit.

## Model-level fields

- [ ] `name` present, ≥ 5 characters.
- [ ] `description` present, ≥ 5 characters, clinically appropriate, no placeholder text (`None`, `N/A`, `TODO`), no self-referential meta-commentary.
- [ ] If a subtype is listed as a synonym, decide whether it should be an attribute value on this model (same attribute set applies) or a separate finding model (needs different characterization). _(`synonym_rules.md`, `scope_and_specificity.md`)_

## Extraction candidates (flag, don't restructure)

- [ ] Prefixed attributes (`solid component size`, `cystic component density`) or groups of attributes describing the same sub-entity → flag for extraction into a separate model. Decide whether each is an **associated finding** (independent) or a **component** (intrinsic). _(`associated_vs_component.md`)_
- [ ] Near-duplicate models — if two models in the repo appear to describe the same observation, flag for human review. Do not merge.

## Output shape (when reviewing as a sub-agent)

Return, for this one model:

- **Issues found** — list each failed checklist item with the specific location in the model (attribute name, value name, field) and a short description.
- **Suggested fixes** — for each issue, a concrete edit proposal. Direct text changes where possible; a restructuring suggestion otherwise.
- **Extraction candidates** — names of findings to create separately (components or associated findings with inline characterization). **Use the exact attribute name as it appears in the model** — do not rename or rephrase (e.g., if the attribute is `aneurysm`, flag `aneurysm`, not `aneurysmal dilation`).
- **Warnings** — items that need human judgment, not a mechanical fix.

Do **NOT** modify IDs (`oifm_id`, `oifma_id`, `value_code`) — they are preserved. Do **NOT** add `anatomic_locations` or `index_codes` — those are added in post-processing.

## Important things the checklist intentionally does NOT flag

- Radiologists use both descriptive observations and diagnostic terms. `pneumonia`, `cystic fibrosis`, `emphysema` are valid findings — do **not** question whether a diagnostic term "should" be a finding. _(`core_concept.md`)_
- Tags, additional domain attributes, and additional synonyms are **enrichment opportunities** — note useful suggestions, but don't treat missing ones as errors.
