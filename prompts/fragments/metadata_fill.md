# Metadata fill (post-convert)

After mechanical convert, fill judgment/metadata fields the agent owns — analogous to head CT `finding-batch` Step 3 draft, but applied during quality review because CDEStaging sources already carry domain attributes.

## Read both files

For each finding, read:

1. **Converted model** — `defs/from_cdestaging_ct_chest/<name>.fm.json`
2. **CDEStaging source** — `../CDEStaging/definitions/hood_CT_chest/<source-file>`

Resolve the source filename from the model stem (hyphen/underscore variants; prefer `.json` over `.md` when both exist).

## JSON-derived models

Convert copies structure from source JSON. The agent **must propose**:

| Field | When to act | Rules |
|-------|-------------|-------|
| **synonyms** | Missing or thin list | `synonym_rules.md` — aggressive but strict; run collision check |
| **description** | Placeholder (`Description for …`), empty, or &lt; 5 meaningful chars | 1–2 clinical sentences per `naming.md` / `core_concept.md` |
| **tags** | Only default `chest`, `CT`, `finding` | Add etiology/anatomy/device tags if clinically useful; keep defaults |
| **name** | Fails naming rules | `naming.md` — expand acronyms, scope generics; do not rewrite domain attrs |
| **change from prior** | Full value set from convert | Winnow per `presence_and_change.md`; recommend `--remove` / `--add` for `modify_change_from_prior.py` |

**Do not** rewrite domain attributes from JSON unless source JSON and model clearly disagree (missing attr, wrong values). Flag attr mismatches as issues with concrete fixes.

## MD-derived models

Convert uses `create_model_from_markdown`. The agent **must**:

| Field | When to act | Rules |
|-------|-------------|-------|
| **domain attributes** | Model vs MD outline mismatch | Propose fixes to match MD; do not invent attrs absent from source |
| **synonyms** | Audit LLM output | Add/remove per `synonym_rules.md` |
| **description** | Thin or generic | Improve if needed; keep clinically accurate to MD |
| **tags** | Default or missing clinical tags | Same as JSON path |
| **name** | Naming issues | `naming.md` |
| **change from prior** | Winnow | `presence_and_change.md` |

## metadata_proposals output block

Return this block in addition to checklist results:

```
### metadata_proposals

- **synonyms_add:** ["term1", "term2"]
- **synonyms_remove:** ["bad term"]
- **description:** "Proposed one- to two-sentence description." (omit if current is adequate)
- **tags_add:** ["vascular"] (omit if defaults only are fine)
- **tags_remove:** [] (omit if none)
- **cfp_pairs_keep:** larger-smaller, increased-decreased (or "minimum only")
- **cfp_remove:** larger, smaller (values to winnow via modify_change_from_prior.py)
- **cfp_add:** worsened, improved (values to add if missing)
- **name_change:** "proposed canonical name" (omit if current name is fine)
```

Omit keys with nothing to propose. Proposals are applied after TUI sign-off unless the user asks to apply immediately.

## What not to do

- Do not call `create_info_from_name` or other findingmodel-ai enrichment during review.
- Do not add `anatomic_locations` — locations pilot is separate (`--no-enrich-locations` on bulk convert).
- Do not modify `oifm_id`, `oifma_id`, or `value_code` by hand.
- Do not use neighbor models for context — one finding per sub-agent.
