# Merge Report: Pericardial Effusion
**Timestamp:** 2025-11-19 22:54:17

**Existing Model:** pericardial effusion (ID: OIFM_GMTS_003706)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 5
  - size Finding
  - density
  - pericardial enhancement
  - pericardial thickening
  - pericardial calcification
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 5
- **Total final attributes:** 7

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial effusion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pericardial effusion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (5)

### 1. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** The size of the pericardial effusion
- **Values:** trace, small, moderate, large
- **Max selected:** 1
- **Required:** True

### 2. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** The density of the pericardial effusion
- **Values:** fluid, intermediate, hemopericardium
- **Max selected:** 1
- **Required:** True

### 3. pericardial enhancement
- **Name:** pericardial enhancement
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial enhancement
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 4. pericardial thickening
- **Name:** pericardial thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial thickening
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 5. pericardial calcification
- **Name:** pericardial calcification
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial calcification
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (5)

#### 1. size Finding
- **Type:** AttributeType.CHOICE
- **Values:** trace, small, moderate, large
- **Description:** The size of the pericardial effusion

#### 2. density
- **Type:** AttributeType.CHOICE
- **Values:** fluid, intermediate, hemopericardium
- **Description:** The density of the pericardial effusion

#### 3. pericardial enhancement
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence or absence of pericardial enhancement

#### 4. pericardial thickening
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence or absence of pericardial thickening

#### 5. pericardial calcification
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence or absence of pericardial calcification

### Required Attributes Added
None

---

## Final Attributes (7)

### 1. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** The size of the pericardial effusion
- **Values:** trace, small, moderate, large
- **Max selected:** 1
- **Required:** True

### 2. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** The density of the pericardial effusion
- **Values:** fluid, intermediate, hemopericardium
- **Max selected:** 1
- **Required:** True

### 3. pericardial enhancement
- **Name:** pericardial enhancement
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial enhancement
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 4. pericardial thickening
- **Name:** pericardial thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial thickening
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 5. pericardial calcification
- **Name:** pericardial calcification
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial calcification
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 6. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pericardial effusion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 7. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pericardial effusion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
