# Merge Report: Radiation Fibrosis
**Timestamp:** 2025-11-26 00:28:56

**Existing Model:** interstitial lung fibrosis (ID: OIFM_GMTS_014491)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 9
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
- **Total final attributes:** 11

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of interstitial lung fibrosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a interstitial lung fibrosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of radiation fibrosis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Status of radiation fibrosis
- **Values:** Stable, Progressive, Regressive, New development, Unchanged over time
- **Max selected:** 1
- **Required:** True

### 3. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Severity of radiation fibrosis
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 4. distribution
- **Name:** distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Distribution of radiation fibrosis
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Max selected:** 1
- **Required:** True

### 5. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of radiation fibrosis
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Max selected:** 1
- **Required:** True

### 6. volume_loss
- **Name:** volume_loss
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of volume loss
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. pleural_thickening
- **Name:** pleural_thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. bronchiectasis
- **Name:** bronchiectasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. honeycombing
- **Name:** honeycombing
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of honeycombing
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. air_trapping
- **Name:** air_trapping
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of air trapping
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. ground_glass_opacities
- **Name:** ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ground-glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. change from prior vs status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** Stable, Progressive, Regressive, New development, Unchanged over time

### New Attributes Added (9)

#### 1. severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Description:** Severity of radiation fibrosis

#### 2. distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Description:** Distribution of radiation fibrosis

#### 3. location
- **Type:** AttributeType.CHOICE
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Description:** Location of radiation fibrosis

#### 4. volume_loss
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of volume loss

#### 5. pleural_thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pleural thickening

#### 6. bronchiectasis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of bronchiectasis

#### 7. honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of honeycombing

#### 8. air_trapping
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of air trapping

#### 9. ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of ground-glass opacities

### Required Attributes Added
None

---

## Final Attributes (11)

### 1. severity
- **Name:** severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Severity of radiation fibrosis
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 2. distribution
- **Name:** distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Distribution of radiation fibrosis
- **Values:** Localized, Diffuse, Peribronchovascular, Segmental
- **Max selected:** 1
- **Required:** True

### 3. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of radiation fibrosis
- **Values:** Right lung, Left lung, Bilateral, Specific lobe(s), Mediastinal, Subpleural
- **Max selected:** 1
- **Required:** True

### 4. volume_loss
- **Name:** volume_loss
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of volume loss
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. pleural_thickening
- **Name:** pleural_thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. bronchiectasis
- **Name:** bronchiectasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. honeycombing
- **Name:** honeycombing
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of honeycombing
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. air_trapping
- **Name:** air_trapping
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of air trapping
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. ground_glass_opacities
- **Name:** ground_glass_opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ground-glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of interstitial lung fibrosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 11. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a interstitial lung fibrosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
