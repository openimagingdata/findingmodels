# Merge Report: Tracheomalacia
**Timestamp:** 2025-11-19 23:14:14

**Existing Model:** tracheomalacia (ID: OIFM_GMTS_022616)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Presence not added)
- **New attributes added:** 7
  - Severity
  - Location
  - Extent
  - Airway Collapse
  - Degree of Collapse
  - Expiratory Air Trapping
  - Signs of Chronic Obstruction
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 9

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has values: ['absent', 'present', 'indeterminate', 'unknown'] and the incoming attribute has values: ['Present', 'Absent']. There is overlap between the two attributes as 'absent' is present in the existing and 'present' is in incoming (considering case insensitivity). However, the existing attribute has additional values 'indeterminate' and 'unknown' which are not present in the incoming attribute. The incoming attribute only contributes 'Present' (case-insensitive to 'present') and 'Absent' (case-insensitive to 'absent'). Thus, this situation satisfies the condition for 'needs_review' since there are shared values ('absent', 'present'), but each attribute has unique values not in the other.

- **Shared values:** Present, Absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of tracheomalacia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a tracheomalacia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether tracheomalacia is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the severity of tracheomalacia.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of tracheomalacia.
- **Values:** Trachea - Proximal, Trachea - Mid, Trachea - Distal, Main Bronchus - Right, Main Bronchus - Left
- **Max selected:** 1
- **Required:** True

### 4. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the extent of tracheomalacia.
- **Values:** Focal, Segmental, Diffuse
- **Max selected:** 1
- **Required:** True

### 5. Airway Collapse
- **Name:** Airway Collapse
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether airway collapse is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Degree of Collapse
- **Name:** Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the degree of airway collapse.
- **Values:** <50%, >50%
- **Max selected:** 1
- **Required:** True

### 7. Expiratory Air Trapping
- **Name:** Expiratory Air Trapping
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether expiratory air trapping is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Signs of Chronic Obstruction
- **Name:** Signs of Chronic Obstruction
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether signs of chronic obstruction are present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (7)

#### 1. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Description:** Indicates the severity of tracheomalacia.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Trachea - Proximal, Trachea - Mid, Trachea - Distal, Main Bronchus - Right, Main Bronchus - Left
- **Description:** Indicates the location of tracheomalacia.

#### 3. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Focal, Segmental, Diffuse
- **Description:** Indicates the extent of tracheomalacia.

#### 4. Airway Collapse
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether airway collapse is present or absent.

#### 5. Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Values:** <50%, >50%
- **Description:** Indicates the degree of airway collapse.

#### 6. Expiratory Air Trapping
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether expiratory air trapping is present or absent.

#### 7. Signs of Chronic Obstruction
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether signs of chronic obstruction are present or absent.

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of tracheomalacia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the severity of tracheomalacia.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of tracheomalacia.
- **Values:** Trachea - Proximal, Trachea - Mid, Trachea - Distal, Main Bronchus - Right, Main Bronchus - Left
- **Max selected:** 1
- **Required:** True

### 4. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the extent of tracheomalacia.
- **Values:** Focal, Segmental, Diffuse
- **Max selected:** 1
- **Required:** True

### 5. Airway Collapse
- **Name:** Airway Collapse
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether airway collapse is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Degree of Collapse
- **Name:** Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the degree of airway collapse.
- **Values:** <50%, >50%
- **Max selected:** 1
- **Required:** True

### 7. Expiratory Air Trapping
- **Name:** Expiratory Air Trapping
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether expiratory air trapping is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Signs of Chronic Obstruction
- **Name:** Signs of Chronic Obstruction
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether signs of chronic obstruction are present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a tracheomalacia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
