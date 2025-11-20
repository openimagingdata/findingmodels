# Merge Report: Bronchial Plug
**Timestamp:** 2025-11-19 22:13:21

**Existing Model:** mucoid impaction (ID: OIFM_GMTS_015330)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 7
  - Status
  - Location
  - Side Finding
  - Device Type
  - Deployment
  - Complication
  - Airspace consolidation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 9

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mucoid impaction
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mucoid impaction has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence of Bronchial Plug
- **Name:** Presence of Bronchial Plug
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed, Resorbed
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus
- **Max selected:** 1
- **Required:** True

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left
- **Max selected:** 1
- **Required:** True

### 5. Device Type
- **Name:** Device Type
- **Type:** AttributeType.CHOICE
- **Values:** Bioresorbable, Non-bioresorbable
- **Max selected:** 1
- **Required:** True

### 6. Deployment
- **Name:** Deployment
- **Type:** AttributeType.CHOICE
- **Values:** Complete, Partial
- **Max selected:** 1
- **Required:** True

### 7. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion
- **Max selected:** 1
- **Required:** True

### 8. Airspace consolidation
- **Name:** Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Bronchial Plug
- **Relationship:** subset (confidence: 0.95)
- **Recommendation:** no_merge
- **AI Reasoning:** I classified the relationship as 'subset' because all values in the incoming attribute ('present', 'absent') are found in the existing attribute ('absent', 'present', 'indeterminate', 'unknown'). The existing attribute includes additional values ('indeterminate', 'unknown') that are not present in the incoming attribute. This satisfies the criteria for 'subset', where the existing set contains all incoming values plus more. Therefore, all incoming values are in existing, confirming the 'subset' relationship. Incoming has no unique values.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### New Attributes Added (7)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed, Resorbed

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus

#### 3. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left

#### 4. Device Type
- **Type:** AttributeType.CHOICE
- **Values:** Bioresorbable, Non-bioresorbable

#### 5. Deployment
- **Type:** AttributeType.CHOICE
- **Values:** Complete, Partial

#### 6. Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion

#### 7. Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed, Resorbed
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus
- **Max selected:** 1
- **Required:** True

### 3. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left
- **Max selected:** 1
- **Required:** True

### 4. Device Type
- **Name:** Device Type
- **Type:** AttributeType.CHOICE
- **Values:** Bioresorbable, Non-bioresorbable
- **Max selected:** 1
- **Required:** True

### 5. Deployment
- **Name:** Deployment
- **Type:** AttributeType.CHOICE
- **Values:** Complete, Partial
- **Max selected:** 1
- **Required:** True

### 6. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion
- **Max selected:** 1
- **Required:** True

### 7. Airspace consolidation
- **Name:** Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mucoid impaction
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mucoid impaction has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
