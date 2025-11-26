# Merge Report: Morgagni Hernia
**Timestamp:** 2025-11-26 00:07:05

**Existing Model:** diaphragmatic hernia (ID: OIFM_GMTS_022456)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Side Finding
  - Size Finding
  - Contents
  - Cardiac or Mediastinal Displacement
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 6
- **Total final attributes:** 6

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of diaphragmatic hernia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a diaphragmatic hernia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence of Morgagni Hernia
- **Name:** Presence of Morgagni Hernia
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Whether a Morgagni Hernia is present or not
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Other Diaphragmatic Hernias
- **Name:** Other Diaphragmatic Hernias
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Whether there are other diaphragmatic hernias present
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The side of the Morgagni Hernia
- **Values:** Left, Right, Bilateral
- **Max selected:** 1
- **Required:** True

### 4. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The size of the Morgagni Hernia
- **Values:** Small, Medium, Large
- **Max selected:** 1
- **Required:** True

### 5. Contents
- **Name:** Contents
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The contents of the Morgagni Hernia
- **Values:** Fat, Bowel, Both, Other
- **Max selected:** 1
- **Required:** True

### 6. Cardiac or Mediastinal Displacement
- **Name:** Cardiac or Mediastinal Displacement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether there is associated cardiac or mediastinal displacement
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Morgagni Hernia
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Morgagni Hernia' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

#### 2. presence vs Other Diaphragmatic Hernias
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Other Diaphragmatic Hernias' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (4)

#### 1. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, Bilateral
- **Description:** The side of the Morgagni Hernia

#### 2. Size Finding
- **Type:** AttributeType.CHOICE
- **Values:** Small, Medium, Large
- **Description:** The size of the Morgagni Hernia

#### 3. Contents
- **Type:** AttributeType.CHOICE
- **Values:** Fat, Bowel, Both, Other
- **Description:** The contents of the Morgagni Hernia

#### 4. Cardiac or Mediastinal Displacement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether there is associated cardiac or mediastinal displacement

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The side of the Morgagni Hernia
- **Values:** Left, Right, Bilateral
- **Max selected:** 1
- **Required:** True

### 2. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The size of the Morgagni Hernia
- **Values:** Small, Medium, Large
- **Max selected:** 1
- **Required:** True

### 3. Contents
- **Name:** Contents
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The contents of the Morgagni Hernia
- **Values:** Fat, Bowel, Both, Other
- **Max selected:** 1
- **Required:** True

### 4. Cardiac or Mediastinal Displacement
- **Name:** Cardiac or Mediastinal Displacement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether there is associated cardiac or mediastinal displacement
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of diaphragmatic hernia
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a diaphragmatic hernia has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
