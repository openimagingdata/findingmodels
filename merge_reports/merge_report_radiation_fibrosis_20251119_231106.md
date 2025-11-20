# Merge Report: Radiation Fibrosis
**Timestamp:** 2025-11-19 23:11:06

**Existing Model:** interstitial lung fibrosis (ID: OIFM_GMTS_014491)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, presence not added)
- **New attributes added:** 10
  - status
  - severity
  - distribution
  - location
  - volume_loss
  - pleural_thickening
  - bronchiectasis
  - honeycombing
  - air_trapping
  - ground_glass_opacities
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 11
- **Total final attributes:** 12

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has four values: 'absent', 'present', 'indeterminate', 'unknown', while the incoming attribute has two values: 'Present' and 'Absent'. After normalizing for case, both attributes share the values 'present' and 'absent'. However, the existing attribute also includes 'indeterminate' and 'unknown' which are not found in the incoming attribute. Therefore, not all incoming values are in existing. The incoming attribute has no unique values since both of its values are present in the existing attribute. Thus, the presence of shared values but differing unique values leads to the classification of 'needs_review'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of interstitial lung fibrosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a interstitial lung fibrosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of radiation fibrosis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Status of radiation fibrosis
- **Values:** Stable, Progressive, Regressive, New development, Unchanged over time
- **Max selected:** 1
- **Required:** True

### 3. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Description:** Severity of radiation fibrosis
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 4. distribution
- **Name:** distribution
- **Type:** AttributeType.CHOICE
- **Description:** Distribution of radiation fibrosis
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Max selected:** 1
- **Required:** True

### 5. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Location of radiation fibrosis
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Max selected:** 1
- **Required:** True

### 6. volume_loss
- **Name:** volume_loss
- **Type:** AttributeType.CHOICE
- **Description:** Presence of volume loss
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. pleural_thickening
- **Name:** pleural_thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pleural thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. bronchiectasis
- **Name:** bronchiectasis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. honeycombing
- **Name:** honeycombing
- **Type:** AttributeType.CHOICE
- **Description:** Presence of honeycombing
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. air_trapping
- **Name:** air_trapping
- **Type:** AttributeType.CHOICE
- **Description:** Presence of air trapping
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. ground_glass_opacities
- **Name:** ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ground-glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (10)

#### 1. status
- **Type:** AttributeType.CHOICE
- **Values:** Stable, Progressive, Regressive, New development, Unchanged over time
- **Description:** Status of radiation fibrosis

#### 2. severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Description:** Severity of radiation fibrosis

#### 3. distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Description:** Distribution of radiation fibrosis

#### 4. location
- **Type:** AttributeType.CHOICE
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Description:** Location of radiation fibrosis

#### 5. volume_loss
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of volume loss

#### 6. pleural_thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pleural thickening

#### 7. bronchiectasis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of bronchiectasis

#### 8. honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of honeycombing

#### 9. air_trapping
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of air trapping

#### 10. ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of ground-glass opacities

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of interstitial lung fibrosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Status of radiation fibrosis
- **Values:** Stable, Progressive, Regressive, New development, Unchanged over time
- **Max selected:** 1
- **Required:** True

### 3. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Description:** Severity of radiation fibrosis
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 4. distribution
- **Name:** distribution
- **Type:** AttributeType.CHOICE
- **Description:** Distribution of radiation fibrosis
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Max selected:** 1
- **Required:** True

### 5. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Location of radiation fibrosis
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Max selected:** 1
- **Required:** True

### 6. volume_loss
- **Name:** volume_loss
- **Type:** AttributeType.CHOICE
- **Description:** Presence of volume loss
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. pleural_thickening
- **Name:** pleural_thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pleural thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. bronchiectasis
- **Name:** bronchiectasis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. honeycombing
- **Name:** honeycombing
- **Type:** AttributeType.CHOICE
- **Description:** Presence of honeycombing
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. air_trapping
- **Name:** air_trapping
- **Type:** AttributeType.CHOICE
- **Description:** Presence of air trapping
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. ground_glass_opacities
- **Name:** ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ground-glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 12. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a interstitial lung fibrosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
