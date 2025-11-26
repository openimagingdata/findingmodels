# Merge Report: Endobronchial Mass
**Timestamp:** 2025-11-25 23:53:04

**Existing Model:** bronchial lesion (ID: OIFM_GMTS_015312)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 5
  - Location
  - Size Finding
  - Shape
  - Distal Atelectasis or Consolidation
  - Lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 7

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of bronchial lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a bronchial lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether the endobronchial mass is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Airway Obstruction
- **Name:** Airway Obstruction
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether there is airway obstruction associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** The status of the endobronchial mass.
- **Values:** New, Stable, Increasing, Decreasing
- **Max selected:** 1
- **Required:** False

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the endobronchial mass.
- **Values:** Specify location, None
- **Max selected:** 1
- **Required:** False

### 5. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The size of the endobronchial mass.
- **Unit:** cm
- **Required:** True

### 6. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The shape of the endobronchial mass.
- **Values:** Round, Irregular, Lobulated
- **Max selected:** 1
- **Required:** False

### 7. Distal Atelectasis or Consolidation
- **Name:** Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (3)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Airway Obstruction
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Airway Obstruction' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New, Stable, Increasing, Decreasing

### New Attributes Added (5)

#### 1. Location
- **Type:** AttributeType.CHOICE
- **Values:** Specify location, None
- **Description:** The location of the endobronchial mass.

#### 2. Size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Description:** The size of the endobronchial mass.

#### 3. Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Irregular, Lobulated
- **Description:** The shape of the endobronchial mass.

#### 4. Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.

#### 5. Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.

### Required Attributes Added
None

---

## Final Attributes (7)

### 1. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the endobronchial mass.
- **Values:** Specify location, None
- **Max selected:** 1
- **Required:** False

### 2. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The size of the endobronchial mass.
- **Unit:** cm
- **Required:** True

### 3. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The shape of the endobronchial mass.
- **Values:** Round, Irregular, Lobulated
- **Max selected:** 1
- **Required:** False

### 4. Distal Atelectasis or Consolidation
- **Name:** Distal Atelectasis or Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is distal atelectasis or consolidation associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is lymphadenopathy associated with the endobronchial mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of bronchial lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 7. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a bronchial lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
