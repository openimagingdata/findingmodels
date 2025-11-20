# Merge Report: Pneumothorax
**Timestamp:** 2025-11-19 22:59:28

**Existing Model:** pneumothorax (ID: OIFM_GMTS_023339)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 3
- **Review decisions made:** 3
  - Keep existing: 3
    - presence (kept, Pleural effusion not added)
    - presence (kept, Herniation not added)
    - change from prior (kept, Status not added)
- **New attributes added:** 10
  - Presence
  - Chest tube
  - Size Finding
  - Location
  - Distribution
  - Subcutaneous emphysema
  - Rib fractures
  - Lung collapse
  - Pleural adhesions
  - Mediastinal shift
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 13
- **Total final attributes:** 12

---

## ⚠️ Attributes Needing Review (3)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Pleural effusion
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has the values ['absent', 'present', 'indeterminate', 'unknown'], while the incoming attribute 'Pleural effusion' has the values ['Present', 'Absent']. Normalizing for case sensitivity, the shared values between the two attributes are ['absent', 'present'], while the existing attribute has unique values of ['indeterminate', 'unknown']. The incoming attribute has no unique values since both values are present in the existing attribute. Therefore, while there are some shared values, each attribute also has unique values. This situation categorizes the relationship as 'needs_review'.

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown

### 2. presence vs Herniation
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The EXISTING attribute contains the values ['absent', 'present', 'indeterminate', 'unknown'], while the INCOMING attribute contains the values ['Present', 'Absent']. After normalizing for case sensitivity, the shared values between the two attributes are ['present', 'absent']. The EXISTING attribute has additional unique values: ['indeterminate', 'unknown'], and the INCOMING attribute has no unique values as both its values are already included in the EXISTING attribute. 

Thus, we have: 
- All incoming values ('present', 'absent') are indeed in existing. 
- Incoming has unique values: [] (no unique values). 
- This situation leads to a 'needs_review' classification because there are shared values, but there are unique values present in the EXISTING attribute and no unique values in the INCOMING attribute.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### 3. change from prior vs Status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute values are: ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller']. The incoming attribute values are: ['Acute', 'Chronic', 'Resolving', 'Newly identified', 'Increased', 'Decreased', 'Resolved', 'Persisting']. Both attributes share the values 'increased', 'decreased', and 'resolved'. However, the existing attribute has unique values such as 'unchanged', 'stable', 'new', 'larger', and 'smaller' that do not appear in the incoming attribute. Likewise, the incoming attribute has unique values like 'Acute', 'Chronic', 'Resolving', 'Newly identified', and 'Persisting' that do not appear in the existing attribute. Therefore, there is some overlap, but each attribute has unique values, leading to the classification of 'needs_review'.

- **Shared values:** increased, decreased, resolved
- **Existing only values:** unchanged, stable, new, larger, smaller
- **Incoming only values:** Acute, Chronic, Resolving, Newly identified, Persisting

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumothorax
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumothorax has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pneumothorax.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of pneumothorax.
- **Values:** Acute, Chronic, Resolving, Newly identified, Increased, Decreased, Resolved, Persisting
- **Max selected:** 1
- **Required:** True

### 3. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Description:** Size of pneumothorax.
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of pneumothorax.
- **Values:** Right, Left, Bilateral
- **Max selected:** 1
- **Required:** True

### 5. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Description:** Distribution of pneumothorax.
- **Values:** Apical, Basilar, Diffuse, Localized
- **Max selected:** 1
- **Required:** True

### 6. Chest tube
- **Name:** Chest tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence of chest tube.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Subcutaneous emphysema
- **Name:** Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Description:** Presence of subcutaneous emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Rib fractures
- **Name:** Rib fractures
- **Type:** AttributeType.CHOICE
- **Description:** Presence of rib fractures.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Pleural effusion
- **Name:** Pleural effusion
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pleural effusion.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Lung collapse
- **Name:** Lung collapse
- **Type:** AttributeType.CHOICE
- **Description:** Presence of lung collapse.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pleural adhesions
- **Name:** Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pleural adhesions.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Mediastinal shift
- **Name:** Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Description:** Presence of mediastinal shift.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 13. Herniation
- **Name:** Herniation
- **Type:** AttributeType.CHOICE
- **Description:** Presence of herniation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (10)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pneumothorax.

#### 2. Chest tube
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of chest tube.

#### 3. Size Finding
- **Type:** AttributeType.CHOICE
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Description:** Size of pneumothorax.

#### 4. Location
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left, Bilateral
- **Description:** Location of pneumothorax.

#### 5. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Apical, Basilar, Diffuse, Localized
- **Description:** Distribution of pneumothorax.

#### 6. Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of subcutaneous emphysema.

#### 7. Rib fractures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of rib fractures.

#### 8. Lung collapse
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of lung collapse.

#### 9. Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of pleural adhesions.

#### 10. Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of mediastinal shift.

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pneumothorax
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pneumothorax has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 3. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pneumothorax.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Chest tube
- **Name:** Chest tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence of chest tube.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Description:** Size of pneumothorax.
- **Values:** Small (<20% lung volume), Medium (20-50% lung volume), Large (>50% lung volume), Tension
- **Max selected:** 1
- **Required:** True

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of pneumothorax.
- **Values:** Right, Left, Bilateral
- **Max selected:** 1
- **Required:** True

### 7. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Description:** Distribution of pneumothorax.
- **Values:** Apical, Basilar, Diffuse, Localized
- **Max selected:** 1
- **Required:** True

### 8. Subcutaneous emphysema
- **Name:** Subcutaneous emphysema
- **Type:** AttributeType.CHOICE
- **Description:** Presence of subcutaneous emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Rib fractures
- **Name:** Rib fractures
- **Type:** AttributeType.CHOICE
- **Description:** Presence of rib fractures.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Lung collapse
- **Name:** Lung collapse
- **Type:** AttributeType.CHOICE
- **Description:** Presence of lung collapse.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pleural adhesions
- **Name:** Pleural adhesions
- **Type:** AttributeType.CHOICE
- **Description:** Presence of pleural adhesions.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Mediastinal shift
- **Name:** Mediastinal shift
- **Type:** AttributeType.CHOICE
- **Description:** Presence of mediastinal shift.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---
