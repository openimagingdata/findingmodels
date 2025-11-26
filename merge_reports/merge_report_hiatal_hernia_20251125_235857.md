# Merge Report: Hiatal Hernia
**Timestamp:** 2025-11-25 23:58:57

**Existing Model:** diaphragmatic hernia (ID: OIFM_GMTS_022456)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Size Finding
  - Esophageal fluid
  - Esophageal wall thickening
  - Tree-in-bud opacities
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 7
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

## Incoming Attributes (7)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether the hiatal hernia is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Intrathoracic herniation of stomach
- **Name:** Intrathoracic herniation of stomach
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether there is intrathoracic herniation of the stomach
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Indicates the status of the hiatal hernia
- **Values:** New, Unchanged, Enlarged
- **Max selected:** 1
- **Required:** True

### 4. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the size of the hiatal hernia
- **Values:** Small, Medium, Large, Not specified
- **Max selected:** 1
- **Required:** True

### 5. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is esophageal fluid
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Esophageal wall thickening
- **Name:** Esophageal wall thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is esophageal wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Tree-in-bud opacities
- **Name:** Tree-in-bud opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there are tree-in-bud opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

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

#### 2. presence vs Intrathoracic herniation of stomach
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Intrathoracic herniation of stomach' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New, Unchanged, Enlarged

### New Attributes Added (4)

#### 1. Size Finding
- **Type:** AttributeType.CHOICE
- **Values:** Small, Medium, Large, Not specified
- **Description:** Indicates the size of the hiatal hernia

#### 2. Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is esophageal fluid

#### 3. Esophageal wall thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there is esophageal wall thickening

#### 4. Tree-in-bud opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether there are tree-in-bud opacities

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the size of the hiatal hernia
- **Values:** Small, Medium, Large, Not specified
- **Max selected:** 1
- **Required:** True

### 2. Esophageal fluid
- **Name:** Esophageal fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is esophageal fluid
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Esophageal wall thickening
- **Name:** Esophageal wall thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there is esophageal wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Tree-in-bud opacities
- **Name:** Tree-in-bud opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether there are tree-in-bud opacities
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
