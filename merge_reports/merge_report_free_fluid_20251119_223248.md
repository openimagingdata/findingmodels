# Merge Report: Free Fluid
**Timestamp:** 2025-11-19 22:32:48

**Existing Model:** ascites (ID: OIFM_GMTS_000480)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 3
- **Review decisions made:** 3
  - Keep existing: 3
    - presence (kept, Presence not added)
    - presence (kept, Hemoperitoneum not added)
    - presence (kept, Organ Injury not added)
- **New attributes added:** 4
  - Volume
  - Location
  - Attenuation
  - Pneumoperitoneum
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 7
- **Total final attributes:** 6

---

## ⚠️ Attributes Needing Review (3)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values ['absent', 'present', 'indeterminate', 'unknown'] while the incoming attribute has the values ['Present', 'Absent']. The values 'Present' and 'Absent' from the incoming attribute match with 'present' and 'absent' in the existing attribute when considering case insensitivity. Thus, the shared values are ['Present', 'Absent']. However, the incoming attribute does not incorporate the values 'indeterminate' and 'unknown' that are present in the existing attribute. Therefore, while there are shared values, both attributes also have unique values not found in the other, which is why this classification is 'needs_review'. Incoming has unique values: ['Present', 'Absent'], and all incoming values are in existing. Hence it falls into needs_review.

- **Shared values:** Present, Absent
- **Existing only values:** indeterminate, unknown

### 2. presence vs Hemoperitoneum
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute 'Hemoperitoneum' has values: ['Present', 'Absent']. Comparing these values, the shared values are ['Present', 'Absent'] (ignoring case for comparison), and both attributes contain unique values that are not in the other. Specifically, 'indeterminate' and 'unknown' are in the existing attribute but not in the incoming attribute, and the exact values of 'absent' and 'present' in the existing attribute do not match exactly due to case sensitivity. 

Since there are shared values, but there are also unique values not found in the other attribute, the relationship is classified as 'needs_review'. Hence, not all incoming values are in existing, and there are incoming values (also case insensitive) that belong to 'existing'. The incoming attribute has unique values: [] (none).

- **Shared values:** Present, Absent
- **Existing only values:** indeterminate, unknown

### 3. presence vs Organ Injury
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute 'Organ Injury' has values: ['Present', 'Absent']. Normalizing for case, we can see that the shared values between the existing and incoming attributes are: ['present', 'absent']. The existing attribute has additional unique values: ['indeterminate', 'unknown']. The incoming attribute only has one unique value which is 'present' and does not have 'indeterminate' and 'unknown'. This means not all incoming values are in existing, and not all existing values are in incoming. Therefore, there is some overlap (the shared values) and unique values in both attributes. Thus, the relationship is classified as 'needs_review'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown
- **Incoming only values:** present, absent

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of ascites
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a ascites has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (7)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Volume
- **Name:** Volume
- **Type:** AttributeType.CHOICE
- **Values:** Small, Moderate, Large
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic
- **Max selected:** 1
- **Required:** True

### 4. Attenuation
- **Name:** Attenuation
- **Type:** AttributeType.CHOICE
- **Values:** Simple, Complex
- **Max selected:** 1
- **Required:** True

### 5. Hemoperitoneum
- **Name:** Hemoperitoneum
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Organ Injury
- **Name:** Organ Injury
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Pneumoperitoneum
- **Name:** Pneumoperitoneum
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (4)

#### 1. Volume
- **Type:** AttributeType.CHOICE
- **Values:** Small, Moderate, Large

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic

#### 3. Attenuation
- **Type:** AttributeType.CHOICE
- **Values:** Simple, Complex

#### 4. Pneumoperitoneum
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of ascites
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Volume
- **Name:** Volume
- **Type:** AttributeType.CHOICE
- **Values:** Small, Moderate, Large
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic
- **Max selected:** 1
- **Required:** True

### 4. Attenuation
- **Name:** Attenuation
- **Type:** AttributeType.CHOICE
- **Values:** Simple, Complex
- **Max selected:** 1
- **Required:** True

### 5. Pneumoperitoneum
- **Name:** Pneumoperitoneum
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a ascites has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
