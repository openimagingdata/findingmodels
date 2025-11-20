# Merge Report: Thyroid Nodule
**Timestamp:** 2025-11-19 23:13:31

**Existing Model:** thyroid lesion (ID: OIFM_GMTS_009272)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 3
- **Review decisions made:** 3
  - Keep existing: 3
    - presence (kept, Presence of Thyroid Nodule not added)
    - presence (kept, Thyroid Goiter not added)
    - change from prior (kept, Status not added)
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

## ⚠️ Attributes Needing Review (3)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence of Thyroid Nodule
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The EXISTING attribute values are ['absent', 'present', 'indeterminate', 'unknown'], while the INCOMING attribute values (normalized for case) are ['present', 'absent']. Both attributes have the shared values 'absent' and 'present'. However, the EXISTING attribute includes unique values 'indeterminate' and 'unknown', which are not present in the INCOMING attribute. Consequently, there are some shared values, but each attribute has unique values not in the other. Therefore, this relationship is classified as 'needs_review'. The incoming values include unique values: [] (none).

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### 2. presence vs Thyroid Goiter
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' includes the values: ['absent', 'present', 'indeterminate', 'unknown'] while the incoming attribute 'Thyroid Goiter' includes the values: ['Present', 'Absent']. When we normalize the case differences, we have two shared values: 'present' and 'absent'. However, the existing attribute has the additional unique values: ['indeterminate', 'unknown']. The incoming attribute does not contain these values. 

Since there are shared values but also unique values in each attribute, this relationship is classified as 'needs_review'. All incoming values are in existing, but existing has unique values not in incoming. 

Incoming has unique values: ['Absent'] and shared values are ['present', 'absent']. The presence of unique values in both attributes justifies the 'needs_review' classification since merging these attributes might not be applicable until further evaluation.


- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown
- **Incoming only values:** Absent

### 3. change from prior vs Status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** Both attributes have some shared values, but they also contain unique values not present in the other. The shared values are: 'unchanged' (existing) and 'new' (incoming), as well as 'increased' and 'decreased' (both attributes). However, the existing attribute has unique values 'stable', 'resolved', 'larger', and 'smaller', while the incoming attribute has 'Status' which is not shared in the existing attribute. 

Notably, there is at least one shared value ('increased', 'decreased', 'new', 'unchanged'), but each attribute also has unique values that are not found in the other attribute. Thus, it is classified as 'needs_review'.

- **Shared values:** unchanged, new, increased, decreased
- **Existing only values:** stable, resolved, larger, smaller
- **Incoming only values:** New, Unchanged

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of thyroid lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a thyroid lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence of Thyroid Nodule
- **Name:** Presence of Thyroid Nodule
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New, Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Right lobe, Left lobe, Isthmus
- **Max selected:** 1
- **Required:** True

### 4. Size (cm)
- **Name:** Size (cm)
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Range:** 0 - 100
- **Required:** True

### 5. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Values:** Cystic, Solid, Mixed
- **Max selected:** 1
- **Required:** True

### 6. Calcification
- **Name:** Calcification
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Margins
- **Name:** Margins
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Irregular, Lobulated
- **Max selected:** 1
- **Required:** True

### 8. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Prior Fine Needle Aspiration
- **Name:** Prior Fine Needle Aspiration
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 10. Prior Fine Needle Aspiration Date
- **Name:** Prior Fine Needle Aspiration Date
- **Type:** AttributeType.CHOICE
- **Values:** Specify date, Not specified
- **Max selected:** 1
- **Required:** True

### 11. Invasion Into Adjacent Structures
- **Name:** Invasion Into Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Cervical Lymphadenopathy
- **Name:** Cervical Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Thyroid Goiter
- **Name:** Thyroid Goiter
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

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

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of thyroid lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a thyroid lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Right lobe, Left lobe, Isthmus
- **Max selected:** 1
- **Required:** True

### 4. Size (cm)
- **Name:** Size (cm)
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Range:** 0 - 100
- **Required:** True

### 5. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Values:** Cystic, Solid, Mixed
- **Max selected:** 1
- **Required:** True

### 6. Calcification
- **Name:** Calcification
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Margins
- **Name:** Margins
- **Type:** AttributeType.CHOICE
- **Values:** Smooth, Irregular, Lobulated
- **Max selected:** 1
- **Required:** True

### 8. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Prior Fine Needle Aspiration
- **Name:** Prior Fine Needle Aspiration
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 10. Prior Fine Needle Aspiration Date
- **Name:** Prior Fine Needle Aspiration Date
- **Type:** AttributeType.CHOICE
- **Values:** Specify date, Not specified
- **Max selected:** 1
- **Required:** True

### 11. Invasion Into Adjacent Structures
- **Name:** Invasion Into Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Cervical Lymphadenopathy
- **Name:** Cervical Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---
