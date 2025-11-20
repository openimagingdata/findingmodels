# Merge Report: Healed Rib Fracture
**Timestamp:** 2025-11-19 22:35:16

**Existing Model:** Chronic Rib Fracture (ID: OIFM_CDE_000261)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - Side (kept, Side Finding not added)
- **New attributes added:** 4
  - Status
  - Multiplicity
  - Level
  - Location
- **Required attributes added:** 0
- **Total existing attributes:** 3
- **Total incoming attributes:** 5
- **Total final attributes:** 7

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. Side vs Side Finding
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'Side' has values: ['left', 'right', 'bilateral']. The incoming attribute 'Side Finding' has values: ['bilateral', 'left', 'right']. When comparing these values, all values from the existing attribute are present in the incoming attribute after normalizing for case: 'left' is equivalent to 'Left', 'right' to 'Right', and 'bilateral' to 'Bilateral'. However, there are no unique values in either attribute; both have the same values, only differing in case. Therefore, the attributes have completely overlapping values, leading them to be classified as 'needs_review'. Since there are shared values but each has the same set without additional unique values, we cannot classify them as 'identical'. This leads to the conclusion that while they appear the same, the differences in naming conventions lead us to suggest further review instead. 

All incoming values are in existing.
Incoming has no unique values: []
This relationship is classified as 'needs_review'.

- **Shared values:** left, right, bilateral

---

## Existing Attributes (3)

### 1. Fracture
- **Name:** Fracture
- **Type:** AttributeType.CHOICE
- **Description:** Cortical breach of a rib with surrounding callus formation or union. 
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Description:** Rib fracture laterality
- **Values:** left, right, bilateral
- **Max selected:** 1
- **Required:** False

### 3. Ribs
- **Name:** Ribs
- **Type:** AttributeType.CHOICE
- **Description:** Describe number(s) of rib(s) affected
- **Values:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (5)

### 1. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Description:** Multiplicity of the rib fracture
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 2. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** Side of the rib fracture
- **Values:** Bilateral, Left, Right
- **Max selected:** 1
- **Required:** True

### 3. Level
- **Name:** Level
- **Type:** AttributeType.CHOICE
- **Description:** Level of the rib fracture
- **Values:** First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Ninth, Tenth, Eleventh, Twelfth, Upper, Lower
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the rib fracture
- **Values:** Anterior, Posterior, Lateral, Anterolateral, Posterolateral
- **Max selected:** 1
- **Required:** True

### 5. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the rib fracture
- **Values:** Subacute, Healing, Remote, Healed, Chronic, Old, Old healed
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (4)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** Subacute, Healing, Remote, Healed, Chronic, Old, Old healed
- **Description:** Status of the rib fracture

#### 2. Multiplicity
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Multiplicity of the rib fracture

#### 3. Level
- **Type:** AttributeType.CHOICE
- **Values:** First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Ninth, Tenth, Eleventh, Twelfth, Upper, Lower
- **Description:** Level of the rib fracture

#### 4. Location
- **Type:** AttributeType.CHOICE
- **Values:** Anterior, Posterior, Lateral, Anterolateral, Posterolateral
- **Description:** Location of the rib fracture

### Required Attributes Added
None

---

## Final Attributes (7)

### 1. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Description:** Rib fracture laterality
- **Values:** left, right, bilateral
- **Max selected:** 1
- **Required:** False

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the rib fracture
- **Values:** Subacute, Healing, Remote, Healed, Chronic, Old, Old healed
- **Max selected:** 1
- **Required:** True

### 3. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Description:** Multiplicity of the rib fracture
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 4. Level
- **Name:** Level
- **Type:** AttributeType.CHOICE
- **Description:** Level of the rib fracture
- **Values:** First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Ninth, Tenth, Eleventh, Twelfth, Upper, Lower
- **Max selected:** 1
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the rib fracture
- **Values:** Anterior, Posterior, Lateral, Anterolateral, Posterolateral
- **Max selected:** 1
- **Required:** True

### 6. Fracture
- **Name:** Fracture
- **Type:** AttributeType.CHOICE
- **Description:** Cortical breach of a rib with surrounding callus formation or union. 
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 7. Ribs
- **Name:** Ribs
- **Type:** AttributeType.CHOICE
- **Description:** Describe number(s) of rib(s) affected
- **Values:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- **Max selected:** 1
- **Required:** False

---
