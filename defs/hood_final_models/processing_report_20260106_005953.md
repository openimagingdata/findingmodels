# Hood Definition Processing Report - Attribute Standardization

**Generated:** 2026-01-06 00:59:53
**Input Directory:** ../CDEStaging/definitions/hood_CT_chest
**Output Directory:** defs\hood_final_models

## Summary Statistics

- **Total files processed:** 9
- **Matches found in database:** 2
- **Merged with existing:** 2
- **Created new:** 7
- **Files with renamed attributes:** 1
- **Files with added attributes:** 8

### Presence Attributes
- **Exact match (kept as-is):** 8
- **Renamed (heuristic):** 0
- **Renamed (classification agent):** 1
- **Added (not found):** 0

### Change from Prior Attributes
- **Exact match (kept as-is):** 1
- **Renamed (heuristic):** 0
- **Renamed (classification agent):** 0
- **Added (not found):** 8

### Missing Attributes from Source
- **Files with missing attributes:** 2
- **Total missing attributes:** 3

## Per-Finding Details

### aberrant subclavian artery (`aberrant-subclavian-artery.md`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** renamed (classification agent) - Original: `aberrant subclavian status`
- **Change from prior:** added (not found)
- **Missing attributes from source:** `presence of aberrant subclavian artery`, `aneurysmal dilation`

### acromioclavicular joint degenerative changes (`acromioclavicular-joint-degenerative-changes.md`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### Adrenal Nodule (`adrenal-nodule.json`)
- **Database match:** Found - `Adrenal Nodule` (ID: OIFM_CDE_000003)
- **Result:** Merged with existing model
  - Attributes merged: 0
  - Attributes added: 3
  - Attributes created: 0
  - New attributes added: `size Finding`, `Hounsfield units (HU)`, `enhancement pattern`
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### Adrenal Thickening (`adrenal-thickening.json`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### Airway Mucus Plugging (`airway-mucus-plugging.json`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### Annular Calcifications (`annular-calcifications.json`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### anterolisthesis (`anterolisthesis.md`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### Aortic Atherosclerosis (`aortic-atherosclerosis.json`)
- **Database match:** Not found
- **Result:** Created new model
- **Presence:** exact match (kept as-is)
- **Change from prior:** added (not found)

### aortic dissection (`aortic-dissection.md`)
- **Database match:** Found - `aortic dissection` (ID: OIFM_MSFT_573630)
- **Result:** Merged with existing model
  - Attributes merged: 0
  - Attributes added: 7
  - Attributes created: 0
  - New attributes added: `type`, `extent`, `branch vessels involved`, `entry tear size`, `intimal flap`, `pericardial effusion`, `complication type`
- **Presence:** exact match (kept as-is)
- **Change from prior:** exact match (kept as-is)
- **Missing attributes from source:** `size of entry tear`


## Missing Attributes from Source

The following attributes were found in the source markdown but were not extracted into the final model:

### aberrant subclavian artery (`aberrant-subclavian-artery.md`)
- `presence of aberrant subclavian artery`
- `aneurysmal dilation`

### aortic dissection (`aortic-dissection.md`)
- `size of entry tear`
