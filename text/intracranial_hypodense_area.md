# Intracranial hypodense area—`OIFM_OIDM_178692`

**Synonyms:** intracranial hypodensity, intracranial hypodensity, intracranial hypodense region, low attenuation within intracranial contents, low attenuation intracranial region, hypodense region of brain, hypodense area in brain

**Tags:** brain, ct, intracranial, hypodensity, head ct

Regions of decreased attenuation within the intracranial contents on CT imaging; may reflect edema, acute or chronic ischemia with encephalomalacia, or chronic gliosis. Correlate with MRI and clinical context for etiology and acuity.

## Attributes

### Presence—`OIFMA_OIDM_449727`

Whether intracranial hypodensity is visible on the current CT.  
**Codes**: SNOMED 705057003 Presence (property) (qualifier value)  
*(Select one)*

- **absent**: Intracranial hypodensity is not visible.  
_RADLEX RID28473 absent; SNOMED 2667000 Absent (qualifier value)_
- **present**: Intracranial hypodensity is clearly visible.  
_RADLEX RID28472 present; SNOMED 52101004 Present (qualifier value)_
- **indeterminate**: Presence cannot be determined due to image quality or confounding factors.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_
- **unknown**: Presence is unknown (insufficient information).  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Change from prior—`OIFMA_OIDM_094285`

Comparison of the hypodense region to prior imaging.  
**Codes**: RADLEX RID49896 change; SNOMED 263703002 Changed status (qualifier value)  
*(Select one)*

- **unchanged**: No measurable change compared to prior imaging.  
_RADLEX RID39268 unchanged; SNOMED 260388006 No status change (qualifier value)_
- **stable**: Stable appearance compared to prior imaging.  
_RADLEX RID5734 stable; SNOMED 58158008 Stable (qualifier value)_
- **new**: New hypodensity not present on prior imaging.  
_RADLEX RID5720 new; SNOMED 7147002 New (qualifier value)_
- **resolved**: Previously seen hypodensity has resolved.  
- **increased**: Hypodensity has increased compared to prior imaging.  
_RADLEX RID36043 increased; SNOMED 35105006 Increased (qualifier value)_
- **decreased**: Hypodensity has decreased compared to prior imaging.  
_RADLEX RID36044 decreased; SNOMED 1250004 Decreased (qualifier value)_
- **larger**: Hypodensity is larger in size compared to prior imaging.  
_RADLEX RID5791 enlarged; SNOMED 263768009 Greater (qualifier value)_
- **smaller**: Hypodensity is smaller in size compared to prior imaging.  
_RADLEX RID38669 diminished; SNOMED 263796003 Lesser (qualifier value)_
- **indeterminate**: Change cannot be reliably assessed.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Location—`OIFMA_OIDM_105558`

Anatomic location(s) of the hypodense region within the intracranial contents.  
**Codes**: RADLEX RID39038 location; SNOMED 758637006 Anatomic location (property) (qualifier value)  
*(Select up to 5)*
- **supratentorial**: Located above the tentorium.  
- **infratentorial**: Located below the tentorium.  
- **frontal lobe**: Located in the frontal lobe.  
- **parietal lobe**: Located in the parietal lobe.  
- **temporal lobe**: Located in the temporal lobe.  
- **occipital lobe**: Located in the occipital lobe.  
- **deep gray nuclei**: Involving basal ganglia or thalamus.  
- **periventricular**: Adjacent to the ventricles.  
- **cortical**: Primarily cortical.  
- **subcortical**: Primarily subcortical white matter.  
- **brainstem**: Involving midbrain, pons, or medulla.  
- **cerebellum**: Involving the cerebellum.  
- **diffuse**: Widespread or diffuse involvement.  
- **multifocal**: Multiple discrete regions.  

### Distribution—`OIFMA_OIDM_589157`

Pattern of involvement.  
*(Select one)*

- **focal**: Single localized focus.  
- **multifocal**: Multiple discrete foci.  
- **diffuse**: Widespread involvement without discrete focus.  
- **confluent**: Coalescent areas forming a larger region.  
- **patchy**: Scattered patchy involvement.  
- **watershed**: Watershed or borderzone distribution.  

### Size—`OIFMA_OIDM_154885`

Largest single dimension of the hypodense region measured on imaging.  
**Codes**: SNOMED 246115007 Size (attribute); RADLEX RID5772 size descriptor  
Mininum: 0.1  
Maximum: 30  
Unit: cm

### Number—`OIFMA_OIDM_381176`

Count of discrete hypodense foci when multifocal.  
Mininum: 1  
Maximum: 100  
Unit: count

### Attenuation—`OIFMA_OIDM_369844`

Degree of hypoattenuation relative to normal brain or CSF.  
*(Select one)*

- **mild**: Slightly lower attenuation than normal brain.  
_RADLEX RID5671 mild; SNOMED 255604002 Mild (qualifier value)_
- **moderate**: Clearly lower attenuation but not csf-like.  
_RADLEX RID5672 moderate; SNOMED 1255665007 Moderate (qualifier value)_
- **marked**: Markedly low attenuation, approaching csf density.  
- **csf like**: Attenuation similar to cerebrospinal fluid.  
- **indeterminate**: Cannot reliably grade attenuation.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Mass effect—`OIFMA_OIDM_204847`

Degree of mass effect caused by the hypodense region.  
*(Select one)*

- **none**: No mass effect.  
- **minimal**: Minimal local compression or effacement.  
- **moderate**: Moderate mass effect with some shift or ventricle effacement.  
_RADLEX RID5672 moderate; SNOMED 1255665007 Moderate (qualifier value)_
- **severe**: Marked mass effect with midline shift or herniation risk.  
_RADLEX RID5673 severe; SNOMED 24484000 Severe (severity modifier) (qualifier value)_
- **indeterminate**: Cannot assess mass effect.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Midline shift—`OIFMA_OIDM_294718`

Measured midline shift at the septum pellucidum or other standard landmark.  
Mininum: 0  
Maximum: 50  
Unit: mm

### Associated hemorrhage—`OIFMA_OIDM_461535`

Presence and type of hemorrhage associated with the hypodense region.  
*(Select one)*

- **none**: No hemorrhage identified.  
- **petechial**: Small petechial hemorrhages.  
- **intraparenchymal**: Intraparenchymal hematoma.  
- **subarachnoid**: Subarachnoid hemorrhage.  
- **subdural**: Subdural hemorrhage.  
- **epidural**: Epidural hemorrhage.  
- **indeterminate**: Hemorrhage presence/type cannot be determined.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Suggested etiology—`OIFMA_OIDM_506777`

Most likely cause(s) of the hypodensity based on imaging appearance and available history.  
*(Select up to 2)*
- **edema**: Vasogenic or interstitial edema.  
- **acute ischemia**: Acute infarct or ischemia.  
- **chronic ischemic change**: Chronic infarct or encephalomalacia.  
- **chronic gliosis**: Chronic gliotic change.  
- **tumor related**: Tumor-associated hypodensity (infiltrative or necrotic).  
- **demyelination**: Demyelinating disease such as multiple sclerosis.  
- **infection**: Infectious or inflammatory process.  
- **postoperative change**: Postsurgical encephalomalacia or change.  
- **other**: Other or unspecified cause.  
- **indeterminate**: Etiology cannot be determined from available data.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Acuity—`OIFMA_OIDM_084526`

Estimated timing of the process producing the hypodensity.  
*(Select one)*

- **acute**: Findings most consistent with an acute process.  
- **subacute**: Findings most consistent with a subacute process.  
- **chronic**: Chronic change without acute features.  
- **chronic encephalomalacia**: Long-standing encephalomalacic change.  
- **indeterminate**: Acuity cannot be estimated.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

### Contrast enhancement—`OIFMA_OIDM_635343`

Enhancement pattern if contrast-enhanced imaging is available.  
*(Select one)*

- **none**: No abnormal enhancement.  
- **ring**: Ring or rim enhancement.  
- **nodular**: Nodular or mass-like enhancement.  
- **patchy**: Patchy or heterogeneous enhancement.  
- **diffuse**: Diffuse enhancement.  
- **indeterminate**: Enhancement cannot be assessed.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_

---

**Contributors**

- Neil Bhatia, MD (OIDM) — [Email](mailto:NKBhatia@users.noreply.github.com) — [Link](https://github.com/NKBhatia)