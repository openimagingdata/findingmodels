# Merge Report: Pneumomediastinum
**Timestamp:** 2025-11-26 00:18:26

**Existing Model:** pneumomediastinum (ID: OIFM_GMTS_023340)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 5
  - Extent
  - Associated Injuries
  - Subcutaneous Emphysema
  - Pneumothorax
  - Other Air Leaks
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 6
- **Total final attributes:** 7

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of pneumomediastinum
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a pneumomediastinum has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence of Pneumomediastinum
- **Name:** Presence of Pneumomediastinum
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Localized, Extensive
- **Max selected:** 1
- **Required:** True

### 3. Associated Injuries
- **Name:** Associated Injuries
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None
- **Max selected:** 1
- **Required:** True

### 4. Subcutaneous Emphysema
- **Name:** Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Other Air Leaks
- **Name:** Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Pneumomediastinum
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Pneumomediastinum' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

### New Attributes Added (5)

#### 1. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Localized, Extensive

#### 2. Associated Injuries
- **Type:** AttributeType.CHOICE
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None

#### 3. Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 4. Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 5. Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (7)

### 1. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Localized, Extensive
- **Max selected:** 1
- **Required:** True

### 2. Associated Injuries
- **Name:** Associated Injuries
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Tracheal Injury, Bronchial Injury, Esophageal Injury, None
- **Max selected:** 1
- **Required:** True

### 3. Subcutaneous Emphysema
- **Name:** Subcutaneous Emphysema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Other Air Leaks
- **Name:** Other Air Leaks
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumomediastinum
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 7. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumomediastinum has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
