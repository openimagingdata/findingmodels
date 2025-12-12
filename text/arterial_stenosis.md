# Arterial stenosis—`OIFM_OIDM_571942`

**Synonyms:** artery stenosis, arterial narrowing, narrowing of an artery

**Tags:** vascular, artery, stenosis, hemodynamics

Focal or diffuse narrowing of an artery causing luminal diameter reduction that may impair distal perfusion; typically characterized on imaging by degree of luminal narrowing, anatomic location, hemodynamic impact, and change over time.

## Attributes

### Presence—`OIFMA_OIDM_281684`

Whether arterial stenosis is identified on the study.  
**Codes**: SNOMED 705057003 Presence (property) (qualifier value)  
*(Select one)*

- **absent**: No arterial stenosis identified.  
_RADLEX RID28473 absent; SNOMED 2667000 Absent (qualifier value)_
- **present**: Arterial stenosis clearly identified.  
_RADLEX RID28472 present; SNOMED 52101004 Present (qualifier value)_
- **indeterminate**: Cannot determine presence of stenosis from available imaging.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_
- **unknown**: Presence of stenosis is unknown (e.g., limited study or missing information).  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Change from prior—`OIFMA_OIDM_560388`

Comparison of the stenosis with prior imaging examinations.  
**Codes**: RADLEX RID49896 change; SNOMED 263703002 Changed status (qualifier value)  
*(Select one)*

- **unchanged**: No measurable change compared with prior study.  
_RADLEX RID39268 unchanged; SNOMED 260388006 No status change (qualifier value)_
- **stable**: Stable appearance compared with prior study.  
_RADLEX RID5734 stable; SNOMED 58158008 Stable (qualifier value)_
- **new**: Stenosis not present on prior imaging.  
_RADLEX RID5720 new; SNOMED 7147002 New (qualifier value)_
- **resolved**: Previously seen stenosis is no longer present.  
- **increased**: Stenosis has progressed or increased in degree.  
_RADLEX RID36043 increased; SNOMED 35105006 Increased (qualifier value)_
- **decreased**: Stenosis has decreased in degree.  
_RADLEX RID36044 decreased; SNOMED 1250004 Decreased (qualifier value)_
- **larger**: Stenosis appears larger in extent.  
_RADLEX RID5791 enlarged; SNOMED 263768009 Greater (qualifier value)_
- **smaller**: Stenosis appears smaller in extent.  
_RADLEX RID38669 diminished; SNOMED 263796003 Lesser (qualifier value)_

### Degree—`OIFMA_OIDM_708406`

Estimated percent luminal narrowing at the most stenotic point.  
Mininum: 0  
Maximum: 100  
Unit: percent

### Severity—`OIFMA_OIDM_750180`

Qualitative categorization of stenosis severity, commonly derived from percent narrowing.  
**Codes**: SNOMED 246112005 Severity (attribute)  
*(Select one)*

- **mild**: Usually less than 50% luminal narrowing.  
_RADLEX RID5671 mild; SNOMED 255604002 Mild (qualifier value)_
- **moderate**: Typically 50-69% luminal narrowing.  
_RADLEX RID5672 moderate; SNOMED 1255665007 Moderate (qualifier value)_
- **severe**: Typically 70% or greater luminal narrowing, including near-occlusion.  
_RADLEX RID5673 severe; SNOMED 24484000 Severe (severity modifier) (qualifier value)_

### Hemodynamic significance—`OIFMA_OIDM_891579`

Imaging assessment of whether the stenosis is likely flow-limiting or causing downstream ischemia.  
*(Select one)*

- **not hemodynamically significant**: Unlikely to be flow-limiting based on imaging or flow data.  
- **hemodynamically significant**: Likely flow-limiting or associated with downstream ischemia.  
- **possibly significant**: Features suggest possible hemodynamic significance but not definitive.  
- **indeterminate**: Cannot assess hemodynamic significance from available data.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_
- **unknown**: Hemodynamic significance not recorded or study inadequate.  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Location—`OIFMA_OIDM_511302`

Anatomic arterial location(s) of the stenosis. Multiple selections allowed when more than one artery is involved.  
**Codes**: RADLEX RID39038 location; SNOMED 758637006 Anatomic location (property) (qualifier value)  
*(Select up to 5)*
- **internal carotid artery**  
- **common carotid artery**  
- **external carotid artery**  
- **vertebral artery**  
- **subclavian artery**  
- **axillary artery**  
- **brachial artery**  
- **renal artery**  
- **superior mesenteric artery**  
- **celiac artery**  
- **coronary artery**  
- **abdominal aorta**  
- **thoracic aorta**  
- **iliac artery**  
- **femoral artery**  
- **popliteal artery**  
- **tibial artery**  
- **peripheral artery unspecified**  
- **other**  
- **unknown**  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Length—`OIFMA_OIDM_413958`

Longitudinal extent of the stenotic segment measured along the vessel.  
Mininum: 0  
Maximum: 200  
Unit: mm

### Laterality—`OIFMA_OIDM_560221`

Side affected when applicable.  
*(Select one)*

- **left**  
- **right**  
- **bilateral**  
- **unknown**  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

---

**Contributors**

- Neil Bhatia, MD (OIDM) — [Email](mailto:NKBhatia@users.noreply.github.com) — [Link](https://github.com/NKBhatia)