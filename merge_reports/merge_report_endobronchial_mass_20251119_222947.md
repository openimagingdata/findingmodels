# Merge Report: Endobronchial Mass
**Timestamp:** 2025-11-19 22:29:47

**Existing Model:** bronchial lesion (ID: OIFM_GMTS_015312)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 2
- **Review decisions made:** 2
  - Keep existing: 2
    - presence (kept, Airway Obstruction not added)
    - change from prior (kept, Status not added)
- **New attributes added:** 6
  - Presence
  - Location
  - Size Finding
  - Shape
  - Distal Atelectasis or Consolidation
  - Lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 8

---

## ⚠️ Attributes Needing Review (2)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Airway Obstruction
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** For the existing attribute 'presence', the values are ['absent', 'present', 'indeterminate', 'unknown']. In the incoming attribute 'Airway Obstruction', the values are ['Present', 'Absent']. When checking for overlaps, we find that both 'Present' and 'Absent' from the incoming attribute correspond to 'present' and 'absent' in the existing attribute when accounting for case insensitivity. 

The shared values are ['present', 'absent']. However, there are unique values in the existing attribute: 'indeterminate' and 'unknown' which are not present in the incoming attribute, and vice versa, the incoming attribute has no unique values since both its values are found in the existing attribute. 

Thus, we conclude that the relationship is 'needs_review' because there are shared values with each attribute containing unique values not found in the other. 

The existing attribute contains additional values that are critical to understanding the complete picture, which is why this is not classified as 'identical', 'enhanced', or 'subset'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### 2. change from prior vs Status
- **Relationship:** needs_review (confidence: 0.80)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'change from prior' has the following values: ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller']. The incoming attribute 'Status' has the values: ['New', 'Stable', 'Increasing', 'Decreasing']. When we normalize for case, we find that 'stable' and 'new' from incoming match exactly with 'stable' and 'new' from existing. However, 'increasing' matches with 'increased' but is not an exact match, and 'decreasing' matches with 'decreased' but is also not an exact match. Thus, the shared values are ['stable', 'new'], while the unique values in existing are ['unchanged', 'resolved', 'larger', 'smaller'] and the unique values in incoming are ['Increasing', 'Decreasing']. All incoming values are not in existing as 'Increasing' and 'Decreasing' do not have precise matches. Consequently, this relationship is classified as 'needs_review' due to overlapping but differing values.

- **Shared values:** stable, new
- **Existing only values:** unchanged, resolved, increased, larger, smaller
- **Incoming only values:** Increasing, Decreasing

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of bronchial lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a bronchial lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the endobronchial mass is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** The status of the endobronchial mass.
- **Values:** New, Stable, Increasing, Decreasing
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the endobronchial mass.
- **Values:** Specify location, None
- **Max selected:** 1
- **Required:** False

### 4. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Description:** The size of the endobronchial mass.
- **Unit:** cm
- **Required:** True

### 5. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Description:** The shape of the endobronchial mass.
- **Values:** Round, Irregular, Lobulated
- **Max selected:** 1
- **Required:** False

### 6. Airway Obstruction
- **Name:** Airway Obstruction
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is airway obstruction associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. Distal Atelectasis or Consolidation
- **Name:** Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (6)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether the endobronchial mass is present or absent.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Specify location, None
- **Description:** The location of the endobronchial mass.

#### 3. Size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Description:** The size of the endobronchial mass.

#### 4. Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Irregular, Lobulated
- **Description:** The shape of the endobronchial mass.

#### 5. Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.

#### 6. Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of bronchial lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a bronchial lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 3. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the endobronchial mass is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the endobronchial mass.
- **Values:** Specify location, None
- **Max selected:** 1
- **Required:** False

### 5. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Description:** The size of the endobronchial mass.
- **Unit:** cm
- **Required:** True

### 6. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Description:** The shape of the endobronchial mass.
- **Values:** Round, Irregular, Lobulated
- **Max selected:** 1
- **Required:** False

### 7. Distal Atelectasis or Consolidation
- **Name:** Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---
