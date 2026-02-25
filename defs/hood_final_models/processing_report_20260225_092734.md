# Hood Definition Processing Report - Attribute Standardization

**Generated:** 2026-02-25 09:27:34
**Input Directory:** ../CDEStaging/definitions/hood_CT_chest
**Output Directory:** defs\hood_final_models

## Summary Statistics

- **Total files processed:** 2
- **Matches found in database:** 0
- **Merged with existing:** 0
- **Created new:** 2
- **Files with renamed attributes:** 2
- **Files with added attributes:** 1

### Presence Attributes
- **Exact match (kept as-is):** 1
- **Renamed (heuristic):** 0
- **Renamed (classification agent):** 1
- **Added (not found):** 0

### Change from Prior Attributes
- **Exact match (kept as-is):** 0
- **Renamed (heuristic):** 1
- **Renamed (classification agent):** 0
- **Added (not found):** 1

### Missing Attributes from Source
- **Files with missing attributes:** 1
- **Total missing attributes:** 3

## Per-Finding Details

### aberrant subclavian artery (`aberrant-subclavian-artery.md`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** renamed (classification agent) - Original: `anomaly status`
- **Change from prior:** added (not found)
- **Missing attributes from source:** `presence of aberrant subclavian artery`, `compression of esophagus or trachea`, `aneurysmal dilation`

### acromioclavicular joint degenerative changes (`acromioclavicular-joint-degenerative-changes.md`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** renamed (heuristic) - Original: `status`


## Missing Attributes from Source

The following attributes were found in the source markdown but were not extracted into the final model:

### aberrant subclavian artery (`aberrant-subclavian-artery.md`)
- `presence of aberrant subclavian artery`
- `compression of esophagus or trachea`
- `aneurysmal dilation`
