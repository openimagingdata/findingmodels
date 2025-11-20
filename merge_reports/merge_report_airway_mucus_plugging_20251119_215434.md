# Merge Report: Airway Mucus Plugging
**Timestamp:** 2025-11-19 21:54:34

**Existing Model:** mucoid impaction (ID: OIFM_GMTS_015330)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Presence not added)
- **New attributes added:** 6
  - Location
  - Extent
  - Airway Wall Thickening
  - Bronchiectasis
  - Consolidation
  - Ground Glass Opacities
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 7
- **Total final attributes:** 8

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** I chose the relationship type 'needs_review' because there are shared values between the EXISTING and INCOMING attributes, but each attribute also has unique values. The existing attribute has the values: ['absent', 'present', 'indeterminate', 'unknown'], while the incoming attribute has the values: ['Present', 'Absent']. The shared values, after normalizing for case, are: ['present', 'absent']. The existing attribute has additional unique values: ['indeterminate', 'unknown'], and the incoming attribute does not add any new values—neither 'unknown' nor 'indeterminate' is present in the incoming attribute. Hence, while there is overlap, there are also unique values in both, which classifies this relationship as 'needs_review'. All incoming values are in existing. Incoming has no unique values: ['Present', 'Absent'].

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

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

## Incoming Attributes (7)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of mucus plugging
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of mucus plugging
- **Values:** Central airways, Segmental bronchi, Subsegmental bronchi
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** Extent of mucus plugging
- **Values:** Focal, Multifocal, Diffuse
- **Max selected:** 1
- **Required:** True

### 4. Airway Wall Thickening
- **Name:** Airway Wall Thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of airway wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Bronchiectasis
- **Name:** Bronchiectasis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Description:** Presence of consolidation
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Ground Glass Opacities
- **Name:** Ground Glass Opacities
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ground glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (6)

#### 1. Location
- **Type:** AttributeType.CHOICE
- **Values:** Central airways, Segmental bronchi, Subsegmental bronchi
- **Description:** Location of mucus plugging

#### 2. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Focal, Multifocal, Diffuse
- **Description:** Extent of mucus plugging

#### 3. Airway Wall Thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of airway wall thickening

#### 4. Bronchiectasis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of bronchiectasis

#### 5. Consolidation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of consolidation

#### 6. Ground Glass Opacities
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of ground glass opacities

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mucoid impaction
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of mucus plugging
- **Values:** Central airways, Segmental bronchi, Subsegmental bronchi
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** Extent of mucus plugging
- **Values:** Focal, Multifocal, Diffuse
- **Max selected:** 1
- **Required:** True

### 4. Airway Wall Thickening
- **Name:** Airway Wall Thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of airway wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Bronchiectasis
- **Name:** Bronchiectasis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Description:** Presence of consolidation
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Ground Glass Opacities
- **Name:** Ground Glass Opacities
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ground glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mucoid impaction has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
