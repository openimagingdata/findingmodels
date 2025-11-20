# Merge Report: Adrenal Thickening
**Timestamp:** 2025-11-19 21:53:25

**Existing Model:** adrenal enlargement (ID: OIFM_GMTS_022561)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - laterality
  - thickness
  - homogeneity
  - lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 5
- **Total final attributes:** 6

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of adrenal enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a adrenal enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (5)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of adrenal thickening
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. laterality
- **Name:** laterality
- **Type:** AttributeType.CHOICE
- **Description:** Laterality of the adrenal thickening
- **Values:** right, left, bilateral
- **Max selected:** 1
- **Required:** True

### 3. thickness
- **Name:** thickness
- **Type:** AttributeType.CHOICE
- **Description:** Severity of the adrenal thickening
- **Values:** mild, moderate, severe
- **Max selected:** 1
- **Required:** True

### 4. homogeneity
- **Name:** homogeneity
- **Type:** AttributeType.CHOICE
- **Description:** Homogeneity of the adrenal thickening
- **Values:** homogeneous, heterogeneous
- **Max selected:** 1
- **Required:** True

### 5. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence of lymphadenopathy
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** I classified this relationship as 'subset' because all the incoming values ('present', 'absent') are included in the existing values ('absent', 'present', 'indeterminate', 'unknown'). Additionally, the existing attribute contains unique values: ['indeterminate', 'unknown'] that are not present in the incoming attribute. Therefore, 'Incoming has no unique values'. Since all incoming values are in existing and existing has more values, this is correctly categorized as 'subset'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### New Attributes Added (4)

#### 1. laterality
- **Type:** AttributeType.CHOICE
- **Values:** right, left, bilateral
- **Description:** Laterality of the adrenal thickening

#### 2. thickness
- **Type:** AttributeType.CHOICE
- **Values:** mild, moderate, severe
- **Description:** Severity of the adrenal thickening

#### 3. homogeneity
- **Type:** AttributeType.CHOICE
- **Values:** homogeneous, heterogeneous
- **Description:** Homogeneity of the adrenal thickening

#### 4. lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence of lymphadenopathy

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. laterality
- **Name:** laterality
- **Type:** AttributeType.CHOICE
- **Description:** Laterality of the adrenal thickening
- **Values:** right, left, bilateral
- **Max selected:** 1
- **Required:** True

### 2. thickness
- **Name:** thickness
- **Type:** AttributeType.CHOICE
- **Description:** Severity of the adrenal thickening
- **Values:** mild, moderate, severe
- **Max selected:** 1
- **Required:** True

### 3. homogeneity
- **Name:** homogeneity
- **Type:** AttributeType.CHOICE
- **Description:** Homogeneity of the adrenal thickening
- **Values:** homogeneous, heterogeneous
- **Max selected:** 1
- **Required:** True

### 4. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence of lymphadenopathy
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of adrenal enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a adrenal enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
