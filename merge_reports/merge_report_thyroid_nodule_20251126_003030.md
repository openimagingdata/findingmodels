# Merge Report: Thyroid Nodule
**Timestamp:** 2025-11-26 00:30:30

**Existing Model:** thyroid lesion (ID: OIFM_GMTS_009272)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 10
  - Location
  - Size (cm)
  - Composition
  - Calcification
  - Margins
  - Enhancement
  - Prior Fine Needle Aspiration
  - Prior Fine Needle Aspiration Date
  - Invasion Into Adjacent Structures
  - Cervical Lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 13
- **Total final attributes:** 12

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of thyroid lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a thyroid lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence of Thyroid Nodule
- **Name:** Presence of Thyroid Nodule
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Thyroid Goiter
- **Name:** Thyroid Goiter
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New, Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Right lobe, Left lobe, Isthmus
- **Max selected:** 1
- **Required:** True

### 5. Size (cm)
- **Name:** Size (cm)
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** cm
- **Range:** 0 - 100
- **Required:** True

### 6. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Cystic, Solid, Mixed
- **Max selected:** 1
- **Required:** True

### 7. Calcification
- **Name:** Calcification
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Margins
- **Name:** Margins
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Smooth, Irregular, Lobulated
- **Max selected:** 1
- **Required:** True

### 9. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Prior Fine Needle Aspiration
- **Name:** Prior Fine Needle Aspiration
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 11. Prior Fine Needle Aspiration Date
- **Name:** Prior Fine Needle Aspiration Date
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Specify date, Not specified
- **Max selected:** 1
- **Required:** True

### 12. Invasion Into Adjacent Structures
- **Name:** Invasion Into Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Cervical Lymphadenopathy
- **Name:** Cervical Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (3)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Thyroid Nodule
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Thyroid Nodule' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Thyroid Goiter
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Thyroid Goiter' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New, Unchanged, Increased, Decreased

### New Attributes Added (10)

#### 1. Location
- **Type:** AttributeType.CHOICE
- **Values:** Right lobe, Left lobe, Isthmus

#### 2. Size (cm)
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Range:** 0 - 100

#### 3. Composition
- **Type:** AttributeType.CHOICE
- **Values:** Cystic, Solid, Mixed

#### 4. Calcification
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 5. Margins
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Irregular, Lobulated

#### 6. Enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 7. Prior Fine Needle Aspiration
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No

#### 8. Prior Fine Needle Aspiration Date
- **Type:** AttributeType.CHOICE
- **Values:** Specify date, Not specified

#### 9. Invasion Into Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 10. Cervical Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Right lobe, Left lobe, Isthmus
- **Max selected:** 1
- **Required:** True

### 2. Size (cm)
- **Name:** Size (cm)
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** cm
- **Range:** 0 - 100
- **Required:** True

### 3. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Cystic, Solid, Mixed
- **Max selected:** 1
- **Required:** True

### 4. Calcification
- **Name:** Calcification
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Margins
- **Name:** Margins
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Smooth, Irregular, Lobulated
- **Max selected:** 1
- **Required:** True

### 6. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Prior Fine Needle Aspiration
- **Name:** Prior Fine Needle Aspiration
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 8. Prior Fine Needle Aspiration Date
- **Name:** Prior Fine Needle Aspiration Date
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Specify date, Not specified
- **Max selected:** 1
- **Required:** True

### 9. Invasion Into Adjacent Structures
- **Name:** Invasion Into Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Cervical Lymphadenopathy
- **Name:** Cervical Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of thyroid lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 12. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a thyroid lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
