# Merge Report: Interlobular Septal Thickening
**Timestamp:** 2025-11-19 22:39:37

**Existing Model:** acute diffuse fine reticular lung opacities (ID: OIFM_GMTS_014420)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - change from prior (kept, Status not added)
- **New attributes added:** 12
  - Presence
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
- **Total final attributes:** 14

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. change from prior vs Status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute values are: ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller']. The incoming attribute values are: ['New', 'Stable', 'Worsened', 'Improved', 'Progressing']. The shared values between these two attributes are: ['Stable', 'New'] (case-insensitive). The existing attribute has unique values: ['unchanged', 'resolved', 'increased', 'decreased', 'larger', 'smaller'], while the incoming attribute has unique values: ['Worsened', 'Improved', 'Progressing']. Some incoming values are not in existing, as 'Worsened', 'Improved', and 'Progressing' are absent from the existing definitions. Similarly, 'unchanged', 'resolved', 'increased', 'decreased', 'larger', and 'smaller' are not in the incoming attribute. Thus, the relationship is classified as 'needs_review' because there are overlaps but also unique values on both sides.

- **Shared values:** Stable, New
- **Existing only values:** unchanged, resolved, increased, decreased, larger, smaller
- **Incoming only values:** Worsened, Improved, Progressing

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of acute diffuse fine reticular lung opacities
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a acute diffuse fine reticular lung opacities has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New, Stable, Worsened, Improved, Progressing
- **Max selected:** 1
- **Required:** True

### 3. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 4. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs
- **Max selected:** 1
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments
- **Max selected:** 1
- **Required:** True

### 6. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns
- **Max selected:** 1
- **Required:** True

### 7. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Ground-glass opacities
- **Name:** Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Honeycombing
- **Name:** Honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pulmonary edema
- **Name:** Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Indicated by other findings, Not indicated
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (12)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 2. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe

#### 3. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs

#### 4. Location
- **Type:** AttributeType.CHOICE
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments

#### 5. Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns

#### 6. Pleural effusion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 7. Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 8. Honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 9. Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 10. Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 11. Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 12. Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Indicated by other findings, Not indicated

### Required Attributes Added
None

---

## Final Attributes (14)

### 1. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a acute diffuse fine reticular lung opacities has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 2. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 4. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Diffuse, Bilateral, Patchy, Throughout the lungs
- **Max selected:** 1
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Bilateral, Unilateral, Periphery, Central, Specific lobes or segments
- **Max selected:** 1
- **Required:** True

### 6. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Nodular, Irregular, Kerley lines, Reticular patterns
- **Max selected:** 1
- **Required:** True

### 7. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Ground-glass opacities
- **Name:** Ground-glass opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Honeycombing
- **Name:** Honeycombing
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pulmonary edema
- **Name:** Pulmonary edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Indicated by other findings, Not indicated
- **Max selected:** 1
- **Required:** True

### 14. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of acute diffuse fine reticular lung opacities
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
