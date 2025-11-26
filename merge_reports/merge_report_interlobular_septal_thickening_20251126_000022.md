# Merge Report: Interlobular Septal Thickening
**Timestamp:** 2025-11-26 00:00:22

**Existing Model:** chronic kerley lines (ID: OIFM_GMTS_014427)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 11
  - Severity
  - Distribution
  - Location
  - Pattern
  - Pleural effusion
  - Ground-glass opacities
  - Honeycombing
  - Consolidation
  - Pulmonary edema
  - Lymphadenopathy
  - Pulmonary hypertension
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 13
- **Total final attributes:** 13

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of chronic kerley lines
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a chronic kerley lines has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New, Stable, Worsened, Improved, Progressing
- **Max selected:** 1
- **Required:** True

### 3. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 4. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs
- **Max selected:** 1
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments
- **Max selected:** 1
- **Required:** True

### 6. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns
- **Max selected:** 1
- **Required:** True

### 7. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Ground-glass opacities
- **Name:** Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Honeycombing
- **Name:** Honeycombing
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pulmonary edema
- **Name:** Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Indicated by other findings, Not indicated
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New, Stable, Worsened, Improved, Progressing

### New Attributes Added (11)

#### 1. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe

#### 2. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs

#### 3. Location
- **Type:** AttributeType.CHOICE
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments

#### 4. Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns

#### 5. Pleural effusion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 6. Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 7. Honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 8. Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 9. Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 10. Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 11. Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Indicated by other findings, Not indicated

### Required Attributes Added
None

---

## Final Attributes (13)

### 1. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 2. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments
- **Max selected:** 1
- **Required:** True

### 4. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns
- **Max selected:** 1
- **Required:** True

### 5. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Ground-glass opacities
- **Name:** Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Honeycombing
- **Name:** Honeycombing
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Pulmonary edema
- **Name:** Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Indicated by other findings, Not indicated
- **Max selected:** 1
- **Required:** True

### 12. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of chronic kerley lines
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 13. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a chronic kerley lines has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
