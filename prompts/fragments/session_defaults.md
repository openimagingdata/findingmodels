# Session defaults (CDEStaging CT chest batch)

Every finding model in the CDEStaging batch uses the same **source code**, **contributors**, and **default tags** unless the user overrides for a specific finding.

## CDEStaging batch defaults (use unless user says otherwise)

| Setting | Value |
|---------|-------|
| **Source code** (OIFM IDs) | `MGB` |
| **Contributors** | OIDM organization + Hood person (`hoodcm`) — already applied by convert postprocess |
| **Default tags** | `chest`, `CT`, `finding` |

Convert applies default tags mechanically when metadata enrichment is off. The agent may add clinically useful tags (e.g., `vascular`, `device`, `congenital`) during quality review — do not remove the default trio unless there is a good reason.

## JSON vs MD metadata ownership

| Source type | Convert provides | Agent fills in review |
|-------------|------------------|----------------------|
| **JSON** | name, description (or placeholder), domain attributes, default tags | synonyms, real description if placeholder, tag refinements, CFP winnow, naming fixes |
| **MD** | name, description, domain attributes (via `create_model_from_markdown`), default tags if missing | audit vs source MD, synonym fixes, tag refinements, CFP winnow, attr fixes vs outline |

## CDEStaging source path

Source definitions live at:

```
../CDEStaging/definitions/hood_CT_chest/<source-filename>
```

Resolve the source file for a converted model by matching the output stem to `*.json` or `*.md` (prefer JSON when both exist). See `scripts/generate_cdestaging_review.py` `source_type_for_stem` for the stem-resolution pattern.

## Posture: apply, then sign off

Apply metadata proposals to `.fm.json` files after quality review (Step 6), then write the review file from the updated models on disk. The TUI confirms what was applied; Step 9 handles any additional feedback.

Never commit without explicit user permission.
