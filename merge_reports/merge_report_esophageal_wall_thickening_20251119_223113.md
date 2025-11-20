# Merge Report: Esophageal Wall Thickening
**Timestamp:** 2025-11-19 22:31:13

**Existing Model:** esophageal wall thickening (ID: OIFM_GMTS_000195)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - change from prior (kept, Status not added)
- **New attributes added:** 9
  - Presence of Esophageal Wall Thickening
  - Location
  - Extent
  - Thickness
  - Mucosal enhancement
  - Mediastinal lymphadenopathy
  - Esophageal mass
  - Esophageal fluid
  - Hiatal hernia
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 11

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. change from prior vs Status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing values are ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller'] and the incoming values are ['New', 'Unchanged', 'Increased', 'Decreased']. After normalizing for case sensitivity, the shared values are ['unchanged', 'new', 'increased', 'decreased']. There are some shared values, but both attributes also include unique values that are not found in the other. The existing has 'stable', 'resolved', 'larger', and 'smaller', while the incoming has no unique values. Hence, the relationship is classified as 'needs_review'.

- **Shared values:** unchanged, increased, decreased, new
- **Existing only values:** stable, resolved, larger, smaller

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of esophageal wall thickening
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a esophageal wall thickening has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence of Esophageal Wall Thickening
- **Name:** Presence of Esophageal Wall Thickening
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
- **Values:** Upper, Middle, Lower
- **Max selected:** 1
- **Required:** True

### 4. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Values:** Focal, Diffuse
- **Max selected:** 1
- **Required:** True

### 5. Thickness
- **Name:** Thickness
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** True

### 6. Mucosal enhancement
- **Name:** Mucosal enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Mediastinal lymphadenopathy
- **Name:** Mediastinal lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Esophageal mass
- **Name:** Esophageal mass
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Hiatal hernia
- **Name:** Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (9)

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

#### 7. Esophageal mass
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 8. Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 9. Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (11)

### 1. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a esophageal wall thickening has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 2. Presence of Esophageal Wall Thickening
- **Name:** Presence of Esophageal Wall Thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper, Middle, Lower
- **Max selected:** 1
- **Required:** True

### 4. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Values:** Focal, Diffuse
- **Max selected:** 1
- **Required:** True

### 5. Thickness
- **Name:** Thickness
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** True

### 6. Mucosal enhancement
- **Name:** Mucosal enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Mediastinal lymphadenopathy
- **Name:** Mediastinal lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Esophageal mass
- **Name:** Esophageal mass
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Hiatal hernia
- **Name:** Hiatal hernia
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of esophageal wall thickening
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
