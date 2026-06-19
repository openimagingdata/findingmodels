# Presence and change-from-prior

Every finding model has two required standard attributes as its first two attributes, in this order.

## 1. presence (first attribute, always)

- Attribute name: `presence` (lowercase, with space in multi-word names in this library — the attribute is a single word here).
- Values: `absent`, `present`, `indeterminate`, `unknown`.
- `max_selected: 1`, `required: true`.
- Upgrade any `[yes/no]` or bare `[present/absent]` source to the full four-value set.

## 2. change from prior (second attribute, always)

- Attribute name uses spaces: `change from prior` — **not** `change_from_prior`.
- Minimum values: `unchanged`, `stable`, `new`, `resolved`.
- Plus **at least one clinically appropriate direction-of-change pair**:
  - `larger` / `smaller` — masses, effusions, structures with measurable size
  - `increased` / `decreased` — quantities, density, extent
  - `worsened` / `improved` — conditions, disease states

## Include every pair a radiologist would actually use

The goal is not to pick the single best pair but to **capture every descriptor a radiologist might reach for**. A pleural effusion can be described as "larger", "increased", or "worsened" — include all three pairs. Over-inclusion is cheap; under-inclusion causes missed matches.

Guidance (include all that apply):

- Finding with measurable size → `larger` / `smaller`
- Finding that can increase/decrease in extent or degree → `increased` / `decreased`
- Finding that is a condition or process → `worsened` / `improved`

## Exclude pairs that make no clinical sense

Some categories of finding get the minimum set only (`unchanged`, `stable`, `new`, `resolved`) with no direction pairs:

- **Devices / hardware** — a pacemaker doesn't get "larger" or "worsened"
- **Congenital variants** — default to no direction pairs (typically fixed). **But** include direction pairs (usually `increased`/`decreased`) if the variant's severity is commonly reported as changing after trauma or corrective surgery. Example: `nasal septal deviation` can worsen post-trauma or improve post-septoplasty.
- **Postsurgical states** — they're permanent
- **Technique / quality observations** — per-image, not longitudinal

Also exclude individual pairs that make no sense for a specific finding even if other pairs apply. A fracture can be new, resolved (healed), or unchanged, but it doesn't "get larger" in the usual sense — drop `larger` / `smaller`. A congenital variant doesn't `worsen`.

## Description grammar

The `change from prior` attribute description should read naturally:

- Plural nouns need plural verbs: "Surgical clips **are** absent" not "is absent".
- Articles must agree: "Whether and how **an** aortic stent…" not "Whether and how a aortic stent…".
- Mass / uncountable nouns take no article: "Whether and how emphysema has changed" not "Whether and how an emphysema…".
- "Presence of X is unknown" — `Presence` is always the subject, always singular.

## CDEStaging convert vs quality review

CDEStaging convert emits the **full** direction-of-change value set via `ensure_standard_attributes`. Quality review **winnows** inappropriate pairs per the rules above.

Use `scripts/finding_authoring/modify_change_from_prior.py` to remove or add direction values:

```bash
# Winnow: remove pairs that don't fit
uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \
  defs/from_cdestaging_ct_chest/foo.fm.json --remove larger,smaller

# Add pairs for a condition/process
uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \
  defs/from_cdestaging_ct_chest/foo.fm.json --add worsened,improved
```

If `change from prior` is entirely missing, use `scripts/finding_authoring/add_change_from_prior.py --pairs ...` (see `mechanical_lint.md`).
