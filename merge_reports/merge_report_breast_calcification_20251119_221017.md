# Merge Report: Breast Calcification
**Timestamp:** 2025-11-19 22:10:17

**Existing Model:** breast calcification cluster (ID: OIFM_MSFT_914493)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 4
- **Review decisions made:** 4
  - Keep existing: 4
    - calcification cluster presence (kept, Presence of Breast Calcification not added)
    - location (kept, Location not added)
    - calcification cluster presence (kept, Dermal Calcifications not added)
    - calcification cluster presence (kept, Vascular Calcifications not added)
- **New attributes added:** 6
  - Status
  - Distribution Pattern
  - Morphology
  - Breast Skin Thickening
  - Breast Mass
  - Axillary Lymphadenopathy
- **Required attributes added:** 1
- **Total existing attributes:** 3
- **Total incoming attributes:** 10
- **Total final attributes:** 10

---

## ⚠️ Attributes Needing Review (4)

*These attributes were reviewed and decisions were made.*

### 1. calcification cluster presence vs Presence of Breast Calcification
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has values: ['absent', 'present', 'indeterminant', 'unknown']. The incoming attribute has values: ['Present', 'Absent']. There are shared values between the two attributes: 'Present' and 'Absent' (case-insensitive). However, the existing attribute also includes additional unique values: 'indeterminant' and 'unknown', which are not found in the incoming attribute. Conversely, the incoming attribute has no unique values as both its values are present in the existing attribute. Therefore, while there is an overlap (shared values), each attribute contains unique values not found in the other. This leads to the classification of 'needs_review'. The critical point is that if one attribute lacks unique values, it cannot be classified as 'needs_review'.

- **Shared values:** Present, Absent
- **Existing only values:** indeterminant, unknown

### 2. location vs Location
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values ['right breast', 'left breast'] whereas the incoming attribute has the values ['Right breast', 'Left breast', 'Bilateral']. Upon normalization for case, we see that the shared values are ['right breast', 'left breast'] and the unique value in the incoming attribute is ['Bilateral']. All incoming values are not in existing, as 'Bilateral' is present in incoming but absent in existing. Therefore, there is an overlap in values, which categorizes the relationship as 'needs_review'. The incoming attribute does have unique values that differentiate it from the existing attribute. This is why I did not classify it as 'subset' or 'enhanced'. Hence, the relationship is classified as 'needs_review'.

- **Shared values:** right breast, left breast
- **Incoming only values:** Bilateral

### 3. calcification cluster presence vs Dermal Calcifications
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute values are ['absent', 'present', 'indeterminant', 'unknown'] and the incoming attribute values are ['Present', 'Absent']. Comparing these case-insensitively, we find that 'Present' matches with 'present' and 'Absent' matches with 'absent'. However, the existing attribute contains additional values 'indeterminant' and 'unknown' that are not present in the incoming attribute. Therefore, there are shared values: ['present', 'absent'] and unique values: existing has ['indeterminant', 'unknown'] and incoming has none unique. This leads to the classification of 'needs_review'.

- **Shared values:** present, absent
- **Existing only values:** indeterminant, unknown

### 4. calcification cluster presence vs Vascular Calcifications
- **Relationship:** needs_review (confidence: 0.95)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'calcification cluster presence' has values: ['absent', 'present', 'indeterminant', 'unknown']. The incoming attribute 'Vascular Calcifications' has values: ['Present', 'Absent']. 

Firstly, when I checked if all values from one attribute are contained in the other:
- 'absent' and 'present' from the incoming attribute are also present in the existing attribute (after normalizing case), but 'indeterminant' and 'unknown' are unique to the existing attribute.

Therefore, it confirms that not all incoming values are in existing (as 'indeterminant' and 'unknown' are not present in the incoming).

Next, I assessed the overlap:
- There are shared values: 'absent' and 'present'.
- 'indeterminant' and 'unknown' are unique to existing, while incoming has no unique values as both its values are found in existing.

Thus, the relationship is classified as 'needs_review' because while there are some shared values, incoming does not have any unique values and still holds some unique values in existing. This requires further investigation to clarify the relationship.

- **Shared values:** present, absent
- **Existing only values:** indeterminant, unknown

---

## Existing Attributes (3)

### 1. calcification cluster presence
- **Name:** calcification cluster presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether breast calcification cluster is present, absent, indeterminate, or unknown.
- **Values:** absent, present, indeterminant, unknown
- **Max selected:** 1
- **Required:** True

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the breast calcification cluster.
- **Values:** right breast, left breast
- **Max selected:** 1
- **Required:** True

### 3. number of calcifications
- **Name:** number of calcifications
- **Type:** AttributeType.NUMERIC
- **Description:** Number of breast calcifications in cluster identified.
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence of Breast Calcification
- **Name:** Presence of Breast Calcification
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of breast calcification.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the breast calcification.
- **Values:** New, Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the breast calcification.
- **Values:** Right breast, Left breast, Bilateral
- **Max selected:** 1
- **Required:** True

### 4. Distribution Pattern
- **Name:** Distribution Pattern
- **Type:** AttributeType.CHOICE
- **Description:** Pattern of distribution of the breast calcification.
- **Values:** Diffuse, Regional, Linear, Segmental, Grouped, Clustered
- **Max selected:** 1
- **Required:** True

### 5. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Description:** Morphology of the breast calcification.
- **Values:** Round, Punctate, Vascular, Coarse, Fine Pleomorphic, Fine Linear or Fine Linear Branching
- **Max selected:** 1
- **Required:** True

### 6. Breast Skin Thickening
- **Name:** Breast Skin Thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of breast skin thickening.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Dermal Calcifications
- **Name:** Dermal Calcifications
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of dermal calcifications.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Vascular Calcifications
- **Name:** Vascular Calcifications
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of vascular calcifications.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Breast Mass
- **Name:** Breast Mass
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of a breast mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Axillary Lymphadenopathy
- **Name:** Axillary Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of axillary lymphadenopathy.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (6)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New, Unchanged, Increased, Decreased
- **Description:** Status of the breast calcification.

#### 2. Distribution Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Diffuse, Regional, Linear, Segmental, Grouped, Clustered
- **Description:** Pattern of distribution of the breast calcification.

#### 3. Morphology
- **Type:** AttributeType.CHOICE
- **Values:** Round, Punctate, Vascular, Coarse, Fine Pleomorphic, Fine Linear or Fine Linear Branching
- **Description:** Morphology of the breast calcification.

#### 4. Breast Skin Thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence or absence of breast skin thickening.

#### 5. Breast Mass
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence or absence of a breast mass.

#### 6. Axillary Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence or absence of axillary lymphadenopathy.

### Required Attributes Added (1)

#### presence
- **Type:** choice
- **Values:** absent, present, indeterminate, unknown

---

## Final Attributes (10)

### 1. calcification cluster presence
- **Name:** calcification cluster presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether breast calcification cluster is present, absent, indeterminate, or unknown.
- **Values:** absent, present, indeterminant, unknown
- **Max selected:** 1
- **Required:** True

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the breast calcification cluster.
- **Values:** right breast, left breast
- **Max selected:** 1
- **Required:** True

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the breast calcification.
- **Values:** New, Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 4. Distribution Pattern
- **Name:** Distribution Pattern
- **Type:** AttributeType.CHOICE
- **Description:** Pattern of distribution of the breast calcification.
- **Values:** Diffuse, Regional, Linear, Segmental, Grouped, Clustered
- **Max selected:** 1
- **Required:** True

### 5. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Description:** Morphology of the breast calcification.
- **Values:** Round, Punctate, Vascular, Coarse, Fine Pleomorphic, Fine Linear or Fine Linear Branching
- **Max selected:** 1
- **Required:** True

### 6. Breast Skin Thickening
- **Name:** Breast Skin Thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of breast skin thickening.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Breast Mass
- **Name:** Breast Mass
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of a breast mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Axillary Lymphadenopathy
- **Name:** Axillary Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of axillary lymphadenopathy.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. number of calcifications
- **Name:** number of calcifications
- **Type:** AttributeType.NUMERIC
- **Description:** Number of breast calcifications in cluster identified.
- **Required:** False

### 10. presence
- **Name:** presence
- **Type:** choice
- **Description:** Presence or absence of Breast Calcification
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
