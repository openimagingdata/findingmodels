# Merge Report: Esophageal Wall Thickening
**Timestamp:** 2025-11-25 23:53:51

**Existing Model:** esophageal wall thickening (ID: OIFM_GMTS_000195)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 8
  - Presence of Esophageal Wall Thickening
  - Location
  - Extent
  - Thickness
  - Mucosal enhancement
  - Mediastinal lymphadenopathy
  - Esophageal fluid
  - Hiatal hernia
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 10

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of esophageal wall thickening
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a esophageal wall thickening has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Esophageal mass
- **Name:** Esophageal mass
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New, Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 3. Presence of Esophageal Wall Thickening
- **Name:** Presence of Esophageal Wall Thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Upper, Middle, Lower
- **Max selected:** 1
- **Required:** True

### 5. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Focal, Diffuse
- **Max selected:** 1
- **Required:** True

### 6. Thickness
- **Name:** Thickness
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** True

### 7. Mucosal enhancement
- **Name:** Mucosal enhancement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Mediastinal lymphadenopathy
- **Name:** Mediastinal lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Hiatal hernia
- **Name:** Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Esophageal mass
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Esophageal mass' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New, Unchanged, Increased, Decreased

### New Attributes Added (8)

#### 1. Presence of Esophageal Wall Thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper, Middle, Lower

#### 3. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Focal, Diffuse

#### 4. Thickness
- **Type:** AttributeType.NUMERIC
- **Unit:** mm

#### 5. Mucosal enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 6. Mediastinal lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 7. Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 8. Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (10)

### 1. Presence of Esophageal Wall Thickening
- **Name:** Presence of Esophageal Wall Thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Upper, Middle, Lower
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Focal, Diffuse
- **Max selected:** 1
- **Required:** True

### 4. Thickness
- **Name:** Thickness
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** True

### 5. Mucosal enhancement
- **Name:** Mucosal enhancement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Mediastinal lymphadenopathy
- **Name:** Mediastinal lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Hiatal hernia
- **Name:** Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of esophageal wall thickening
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a esophageal wall thickening has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
