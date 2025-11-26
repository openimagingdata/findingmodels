# Merge Report: Bronchial Plug
**Timestamp:** 2025-11-25 23:39:38

**Existing Model:** mucoid impaction (ID: OIFM_GMTS_015330)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Location
  - Side Finding
  - Device Type
  - Deployment
  - Complication
  - Airspace consolidation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of mucoid impaction
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a mucoid impaction has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence of Bronchial Plug
- **Name:** Presence of Bronchial Plug
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New placement, Unchanged, Complication, Removed, Resorbed
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus
- **Max selected:** 1
- **Required:** True

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Right, Left
- **Max selected:** 1
- **Required:** True

### 5. Device Type
- **Name:** Device Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Bioresorbable, Non-bioresorbable
- **Max selected:** 1
- **Required:** True

### 6. Deployment
- **Name:** Deployment
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Complete, Partial
- **Max selected:** 1
- **Required:** True

### 7. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion
- **Max selected:** 1
- **Required:** True

### 8. Airspace consolidation
- **Name:** Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Bronchial Plug
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Bronchial Plug' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. change from prior vs Status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** New placement, Unchanged, Complication, Removed, Resorbed

### New Attributes Added (6)

#### 1. Location
- **Type:** AttributeType.CHOICE
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus

#### 2. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left

#### 3. Device Type
- **Type:** AttributeType.CHOICE
- **Values:** Bioresorbable, Non-bioresorbable

#### 4. Deployment
- **Type:** AttributeType.CHOICE
- **Values:** Complete, Partial

#### 5. Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion

#### 6. Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Main bronchus, Lobar bronchus, Segmental bronchus
- **Max selected:** 1
- **Required:** True

### 2. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Right, Left
- **Max selected:** 1
- **Required:** True

### 3. Device Type
- **Name:** Device Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Bioresorbable, Non-bioresorbable
- **Max selected:** 1
- **Required:** True

### 4. Deployment
- **Name:** Deployment
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Complete, Partial
- **Max selected:** 1
- **Required:** True

### 5. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Mucosal erosion, Perforation, Migration, Stenosis, Occlusion
- **Max selected:** 1
- **Required:** True

### 6. Airspace consolidation
- **Name:** Airspace consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mucoid impaction
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mucoid impaction has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
