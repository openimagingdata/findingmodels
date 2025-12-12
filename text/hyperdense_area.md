# Hyperdense area—`OIFM_OIDM_880403`

**Synonyms:** hyperdensity, hyperdense focus, high attenuation region, dense appearance on ct, hyperattenuation

**Tags:** ct, attenuation, imaging appearance, radiology finding

Area of increased attenuation on CT relative to surrounding tissue, representing high-density material (eg, calcification, acute hemorrhage, iodinated contrast, surgical material) and describing imaging appearance rather than a specific disease.

## Attributes

### Presence—`OIFMA_OIDM_782553`

Whether hyperdensity is visible on the study.  
**Codes**: SNOMED 705057003 Presence (property) (qualifier value)  
*(Select one)*

- **absent**: No hyperdensity identified.  
_RADLEX RID28473 absent; SNOMED 2667000 Absent (qualifier value)_
- **present**: Clearly visible hyperdensity.  
_RADLEX RID28472 present; SNOMED 52101004 Present (qualifier value)_
- **indeterminate**: Cannot confidently determine presence of hyperdensity.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_
- **unknown**: Presence not known or not assessed.  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Change from prior—`OIFMA_OIDM_329062`

Comparison of the hyperdensity to prior imaging when available.  
**Codes**: RADLEX RID49896 change; SNOMED 263703002 Changed status (qualifier value)  
*(Select one)*

- **unchanged**: No measurable change compared with prior exam.  
_RADLEX RID39268 unchanged; SNOMED 260388006 No status change (qualifier value)_
- **stable**: Stable appearance compared with prior exam.  
_RADLEX RID5734 stable; SNOMED 58158008 Stable (qualifier value)_
- **new**: Not present on prior exam; new finding.  
_RADLEX RID5720 new; SNOMED 7147002 New (qualifier value)_
- **resolved**: Previously seen hyperdensity is no longer present.  
- **increased**: Increase in attenuation or conspicuity compared with prior.  
_RADLEX RID36043 increased; SNOMED 35105006 Increased (qualifier value)_
- **decreased**: Decrease in attenuation or conspicuity compared with prior.  
_RADLEX RID36044 decreased; SNOMED 1250004 Decreased (qualifier value)_
- **larger**: Lesion or area increased in size compared with prior.  
_RADLEX RID5791 enlarged; SNOMED 263768009 Greater (qualifier value)_
- **smaller**: Lesion or area decreased in size compared with prior.  
_RADLEX RID38669 diminished; SNOMED 263796003 Lesser (qualifier value)_

### Attenuation hu—`OIFMA_OIDM_073431`

Measured CT attenuation of the hyperdense region in Hounsfield units (HU).  
Mininum: -1000  
Maximum: 5000  
Unit: HU

### Size cm—`OIFMA_OIDM_875194`

Greatest dimension of the hyperdense area measured on imaging.  
Mininum: 0.1  
Maximum: 50  
Unit: cm

### Likely cause—`OIFMA_OIDM_224599`

Most likely etiology or material responsible for the hyperdensity based on imaging appearance and clinical context.  
*(Select one)*

- **calcification**: Dystrophic or metastatic calcification.  
- **acute hemorrhage**: Blood products producing high attenuation consistent with acute/early hemorrhage.  
- **iodinated contrast**: Residual or intravascular/extra-vascular iodinated contrast material.  
- **surgical material**: Staples, packing, or other expected postoperative material.  
- **metallic foreign body**: Metal object or implant causing very high attenuation and possible streak artifact.  
- **beam hardening artifact**: Apparent hyperdensity due to CT artifact rather than true high-density material.  
- **other**: Other or unspecified high-density material.  
- **unknown**: Cause cannot be determined from imaging.  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Distribution—`OIFMA_OIDM_426956`

Spatial distribution of the hyperdensity within the imaged region.  
*(Select one)*

- **focal**: Single localized area of hyperdensity.  
- **multifocal**: Multiple discrete areas of hyperdensity.  
- **diffuse**: Widespread or confluent hyperdensity.  

---

**Contributors**

- Neil Bhatia, MD (OIDM) — [Email](mailto:NKBhatia@users.noreply.github.com) — [Link](https://github.com/NKBhatia)