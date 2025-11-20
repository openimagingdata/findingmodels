# Merge Report: Compression Fracture
**Timestamp:** 2025-11-19 22:22:18

**Existing Model:** Vertebral Compression Fracture (ID: OIFM_CDE_000230)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 10
  - acuity
  - location
  - number_of_vertebrae_affected
  - severity
  - morphology
  - bone_marrow_edema
  - adjacent_disc_involvement
  - soft_tissue_swelling
  - canal_compromise
  - neurological_compromise
- **Required attributes added:** 1
- **Total existing attributes:** 3
- **Total incoming attributes:** 12
- **Total final attributes:** 14

---

## Existing Attributes (3)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Acute or chronic compression, wedge, distraction or translated
fractures. Typically seen on lateral view. Usually chronicity cannot be reliably assessed so this is not differentiated. 
For compression or wedge fractures, there should be more than 20% loss in anterior height or central height as measured to the nearest normal vertebra or posterior vertebral body height (whichever is larger).  
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Vertebrae
- **Name:** Vertebrae
- **Type:** AttributeType.CHOICE
- **Description:** List all affected vertebrae, multichoice
- **Values:** C1, C2, C3, C4, C5, C6, C7, C8, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, S3, S4, S5
- **Max selected:** 30
- **Required:** False

### 3. Degree of compression
- **Name:** Degree of compression
- **Type:** AttributeType.NUMERIC
- **Unit:** degree
- **Range:** 0 - 100
- **Required:** False

---

## Incoming Attributes (12)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether a compression fracture is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. acuity
- **Name:** acuity
- **Type:** AttributeType.CHOICE
- **Description:** The acuity of the compression fracture
- **Values:** acute, chronic, subacute, healing
- **Max selected:** 1
- **Required:** True

### 3. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the compression fracture
- **Values:** thoracic, lumbar, cervical
- **Max selected:** 1
- **Required:** True

### 4. number_of_vertebrae_affected
- **Name:** number_of_vertebrae_affected
- **Type:** AttributeType.CHOICE
- **Description:** The number of vertebrae affected by the compression fracture
- **Values:** single, multiple, diffuse_involvement
- **Max selected:** 1
- **Required:** True

### 5. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of the compression fracture
- **Values:** mild, moderate, severe, collapse, complete_destruction
- **Max selected:** 1
- **Required:** True

### 6. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Description:** The morphology of the compression fracture
- **Values:** wedge-shaped, biconcave, crush, endplate_involvement, cortical_disruption
- **Max selected:** 1
- **Required:** True

### 7. bone_marrow_edema
- **Name:** bone_marrow_edema
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether bone marrow edema is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 8. adjacent_disc_involvement
- **Name:** adjacent_disc_involvement
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether adjacent disc involvement is present, absent, or shows degenerative changes
- **Values:** present, absent, degenerative_changes
- **Max selected:** 1
- **Required:** True

### 9. soft_tissue_swelling
- **Name:** soft_tissue_swelling
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether soft tissue swelling is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 10. canal_compromise
- **Name:** canal_compromise
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether canal compromise is present, absent, or shows stenosis
- **Values:** present, absent, stenosis
- **Max selected:** 1
- **Required:** True

### 11. paravertebral_hematoma
- **Name:** paravertebral_hematoma
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether paravertebral hematoma is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 12. neurological_compromise
- **Name:** neurological_compromise
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether neurological compromise is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Presence vs presence
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** I classified the relationship as 'subset' because all values in the incoming attribute ('present', 'absent') are included in the existing attribute ('absent', 'present', 'indeterminate', 'unknown'). The existing attribute has two additional values ('indeterminate' and 'unknown') that are not present in the incoming attribute. Consequently, it fulfills the criteria for a 'subset' relationship as all incoming values are in existing, and existing has additional values. All incoming values are in existing, and incoming has unique values: ['indeterminate', 'unknown']. Thus, existing attribute encompasses the incoming values while maintaining its own unique descriptors, which is characteristic of a 'subset'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

#### 2. Presence vs paravertebral_hematoma
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The EXISTING attribute has four values: [absent, present, indeterminate, unknown]. The INCOMING attribute has two values: [present, absent]. All incoming values ('present' and 'absent') are in the existing values, and the existing attribute has additional unique values ('indeterminate' and 'unknown'). Thus, all incoming values are in existing, and existing has additional unique values. This categorizes the relationship as 'subset'. All incoming values are in existing. Incoming has unique values: [indeterminate, unknown]. This relationship is 'subset'.

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown

### New Attributes Added (10)

#### 1. acuity
- **Type:** AttributeType.CHOICE
- **Values:** acute, chronic, subacute, healing
- **Description:** The acuity of the compression fracture

#### 2. location
- **Type:** AttributeType.CHOICE
- **Values:** thoracic, lumbar, cervical
- **Description:** The location of the compression fracture

#### 3. number_of_vertebrae_affected
- **Type:** AttributeType.CHOICE
- **Values:** single, multiple, diffuse_involvement
- **Description:** The number of vertebrae affected by the compression fracture

#### 4. severity
- **Type:** AttributeType.CHOICE
- **Values:** mild, moderate, severe, collapse, complete_destruction
- **Description:** The severity of the compression fracture

#### 5. morphology
- **Type:** AttributeType.CHOICE
- **Values:** wedge-shaped, biconcave, crush, endplate_involvement, cortical_disruption
- **Description:** The morphology of the compression fracture

#### 6. bone_marrow_edema
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Indicates whether bone marrow edema is present or absent

#### 7. adjacent_disc_involvement
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, degenerative_changes
- **Description:** Indicates whether adjacent disc involvement is present, absent, or shows degenerative changes

#### 8. soft_tissue_swelling
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Indicates whether soft tissue swelling is present or absent

#### 9. canal_compromise
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, stenosis
- **Description:** Indicates whether canal compromise is present, absent, or shows stenosis

#### 10. neurological_compromise
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Indicates whether neurological compromise is present or absent

### Required Attributes Added (1)

#### change from prior
- **Type:** choice
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

---

## Final Attributes (14)

### 1. acuity
- **Name:** acuity
- **Type:** AttributeType.CHOICE
- **Description:** The acuity of the compression fracture
- **Values:** acute, chronic, subacute, healing
- **Max selected:** 1
- **Required:** True

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the compression fracture
- **Values:** thoracic, lumbar, cervical
- **Max selected:** 1
- **Required:** True

### 3. number_of_vertebrae_affected
- **Name:** number_of_vertebrae_affected
- **Type:** AttributeType.CHOICE
- **Description:** The number of vertebrae affected by the compression fracture
- **Values:** single, multiple, diffuse_involvement
- **Max selected:** 1
- **Required:** True

### 4. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of the compression fracture
- **Values:** mild, moderate, severe, collapse, complete_destruction
- **Max selected:** 1
- **Required:** True

### 5. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Description:** The morphology of the compression fracture
- **Values:** wedge-shaped, biconcave, crush, endplate_involvement, cortical_disruption
- **Max selected:** 1
- **Required:** True

### 6. bone_marrow_edema
- **Name:** bone_marrow_edema
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether bone marrow edema is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 7. adjacent_disc_involvement
- **Name:** adjacent_disc_involvement
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether adjacent disc involvement is present, absent, or shows degenerative changes
- **Values:** present, absent, degenerative_changes
- **Max selected:** 1
- **Required:** True

### 8. soft_tissue_swelling
- **Name:** soft_tissue_swelling
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether soft tissue swelling is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 9. canal_compromise
- **Name:** canal_compromise
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether canal compromise is present, absent, or shows stenosis
- **Values:** present, absent, stenosis
- **Max selected:** 1
- **Required:** True

### 10. neurological_compromise
- **Name:** neurological_compromise
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether neurological compromise is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 11. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Acute or chronic compression, wedge, distraction or translated
fractures. Typically seen on lateral view. Usually chronicity cannot be reliably assessed so this is not differentiated. 
For compression or wedge fractures, there should be more than 20% loss in anterior height or central height as measured to the nearest normal vertebra or posterior vertebral body height (whichever is larger).  
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 12. Vertebrae
- **Name:** Vertebrae
- **Type:** AttributeType.CHOICE
- **Description:** List all affected vertebrae, multichoice
- **Values:** C1, C2, C3, C4, C5, C6, C7, C8, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, S3, S4, S5
- **Max selected:** 30
- **Required:** False

### 13. Degree of compression
- **Name:** Degree of compression
- **Type:** AttributeType.NUMERIC
- **Unit:** degree
- **Range:** 0 - 100
- **Required:** False

### 14. change from prior
- **Name:** change from prior
- **Type:** choice
- **Description:** Whether and how a Compression Fracture has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
