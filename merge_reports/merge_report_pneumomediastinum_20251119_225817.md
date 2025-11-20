# Merge Report: Pneumomediastinum
**Timestamp:** 2025-11-19 22:58:17

**Existing Model:** pneumomediastinum (ID: OIFM_GMTS_023340)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Presence of Pneumomediastinum
  - Extent
  - Associated Injuries
  - Subcutaneous Emphysema
  - Pneumothorax
  - Other Air Leaks
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 6
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumomediastinum
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumomediastinum has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence of Pneumomediastinum
- **Name:** Presence of Pneumomediastinum
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Extensive
- **Max selected:** 1
- **Required:** True

### 3. Associated Injuries
- **Name:** Associated Injuries
- **Type:** AttributeType.CHOICE
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None
- **Max selected:** 1
- **Required:** True

### 4. Subcutaneous Emphysema
- **Name:** Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Other Air Leaks
- **Name:** Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (6)

#### 1. Presence of Pneumomediastinum
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No

#### 2. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Extensive

#### 3. Associated Injuries
- **Type:** AttributeType.CHOICE
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None

#### 4. Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 5. Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 6. Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Presence of Pneumomediastinum
- **Name:** Presence of Pneumomediastinum
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Extensive
- **Max selected:** 1
- **Required:** True

### 3. Associated Injuries
- **Name:** Associated Injuries
- **Type:** AttributeType.CHOICE
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None
- **Max selected:** 1
- **Required:** True

### 4. Subcutaneous Emphysema
- **Name:** Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Other Air Leaks
- **Name:** Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumomediastinum
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumomediastinum has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
