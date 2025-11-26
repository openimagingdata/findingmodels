# Merge Report: Tracheomalacia
**Timestamp:** 2025-11-26 00:30:57

**Existing Model:** tracheomalacia (ID: OIFM_GMTS_022616)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Severity
  - Location
  - Extent
  - Degree of Collapse
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 6

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of tracheomalacia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a tracheomalacia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether tracheomalacia is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Airway Collapse
- **Name:** Airway Collapse
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether airway collapse is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Expiratory Air Trapping
- **Name:** Expiratory Air Trapping
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether expiratory air trapping is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Signs of Chronic Obstruction
- **Name:** Signs of Chronic Obstruction
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether signs of chronic obstruction are present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the severity of tracheomalacia.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of tracheomalacia.
- **Values:** Trachea - Proximal, Trachea - Mid, Trachea - Distal, Main Bronchus - Right, Main Bronchus - Left
- **Max selected:** 1
- **Required:** True

### 7. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the extent of tracheomalacia.
- **Values:** Focal, Segmental, Diffuse
- **Max selected:** 1
- **Required:** True

### 8. Degree of Collapse
- **Name:** Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the degree of airway collapse.
- **Values:** <50%, >50%
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (4)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Airway Collapse
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Airway Collapse' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. presence vs Expiratory Air Trapping
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Expiratory Air Trapping' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 4. presence vs Signs of Chronic Obstruction
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Signs of Chronic Obstruction' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (4)

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

#### 4. Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Values:** <50%, >50%
- **Description:** Indicates the degree of airway collapse.

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the severity of tracheomalacia.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of tracheomalacia.
- **Values:** Trachea - Proximal, Trachea - Mid, Trachea - Distal, Main Bronchus - Right, Main Bronchus - Left
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the extent of tracheomalacia.
- **Values:** Focal, Segmental, Diffuse
- **Max selected:** 1
- **Required:** True

### 4. Degree of Collapse
- **Name:** Degree of Collapse
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the degree of airway collapse.
- **Values:** <50%, >50%
- **Max selected:** 1
- **Required:** True

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of tracheomalacia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a tracheomalacia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
