# Merge Report: Pneumothorax
**Timestamp:** 2025-11-26 00:19:04

**Existing Model:** pneumothorax (ID: OIFM_GMTS_023339)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 10
  - Size Finding
  - Location
  - Distribution
  - Subcutaneous emphysema
  - Rib fractures
  - Pleural effusion
  - Lung collapse
  - Pleural adhesions
  - Mediastinal shift
  - Herniation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 13
- **Total final attributes:** 12

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of pneumothorax
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a pneumothorax has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of pneumothorax.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Chest tube
- **Name:** Chest tube
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of chest tube.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Status of pneumothorax.
- **Values:** Acute, Chronic, Resolving, Newly identified, Increased, Decreased, Resolved, Persisting
- **Max selected:** 1
- **Required:** True

### 4. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Size of pneumothorax.
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Max selected:** 1
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of pneumothorax.
- **Values:** Right, Left, Bilateral
- **Max selected:** 1
- **Required:** True

### 6. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Distribution of pneumothorax.
- **Values:** Apical, Basilar, Diffuse, Localized
- **Max selected:** 1
- **Required:** True

### 7. Subcutaneous emphysema
- **Name:** Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of subcutaneous emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Rib fractures
- **Name:** Rib fractures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of rib fractures.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural effusion.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Lung collapse
- **Name:** Lung collapse
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of lung collapse.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pleural adhesions
- **Name:** Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural adhesions.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Mediastinal shift
- **Name:** Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of mediastinal shift.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Herniation
- **Name:** Herniation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of herniation.
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

#### 2. presence vs Chest tube
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Chest tube' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** Acute, Chronic, Resolving, Newly identified, Increased, Decreased, Resolved, Persisting

### New Attributes Added (10)

#### 1. Size Finding
- **Type:** AttributeType.CHOICE
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Description:** Size of pneumothorax.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left, Bilateral
- **Description:** Location of pneumothorax.

#### 3. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Apical, Basilar, Diffuse, Localized
- **Description:** Distribution of pneumothorax.

#### 4. Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of subcutaneous emphysema.

#### 5. Rib fractures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of rib fractures.

#### 6. Pleural effusion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pleural effusion.

#### 7. Lung collapse
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of lung collapse.

#### 8. Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pleural adhesions.

#### 9. Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of mediastinal shift.

#### 10. Herniation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of herniation.

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Size of pneumothorax.
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of pneumothorax.
- **Values:** Right, Left, Bilateral
- **Max selected:** 1
- **Required:** True

### 3. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Distribution of pneumothorax.
- **Values:** Apical, Basilar, Diffuse, Localized
- **Max selected:** 1
- **Required:** True

### 4. Subcutaneous emphysema
- **Name:** Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of subcutaneous emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Rib fractures
- **Name:** Rib fractures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of rib fractures.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural effusion.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Lung collapse
- **Name:** Lung collapse
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of lung collapse.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Pleural adhesions
- **Name:** Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of pleural adhesions.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Mediastinal shift
- **Name:** Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of mediastinal shift.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Herniation
- **Name:** Herniation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of herniation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumothorax
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 12. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumothorax has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
