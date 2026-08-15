# Hood Finding Taxonomies

Per-modality radiology finding taxonomies developed by Michael Hood
(@hoodcm). Exported 2026-08-15.

| File | Rows | OIFM IDs filled |
|---|---:|---:|
| `xr_chest_findings.csv` | 403 | 305 |
| `xr_msk_findings.csv` | 259 | 40 |
| `ct_head_findings.csv` | 520 | 449 |
| `ct_chest_abdomen_pelvis_findings.csv` | 2064 | 207 |
| `mg_breast_findings.csv` | 198 | 5 |
| `mri_spine_findings.csv` | 345 | 22 |
| **total** | **3789** | **1028** |

## Columns

```
name,category,parent,synonyms,finding_type,finding_cluster,oifm_id
```

## Structure

Each file is one hierarchy. `parent` holds the parent row's `name`; blank
means top-level. Parents are generic, children add specificity —
`lung_abnormality` -> `airspace_opacity` -> `air_bronchogram`. Rows are keyed
by `name`, unique within each file, so there is no separate ID column.

`category` is an independent anatomic grouping, not part of the hierarchy.
`finding_type` separates an observation from a diagnosis.

## OIFM IDs

Filled where the row matches a model that already exists — by exact name
against `ids.json` across all branches, plus IDs previously written back to
the old lists. Nothing was minted here. An ID can appear on two rows where
those earlier writebacks mapped two findings onto one model.

Blank rows are the ones needing triage.
