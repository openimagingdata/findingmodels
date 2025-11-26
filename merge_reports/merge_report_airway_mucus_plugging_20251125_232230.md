# Merge Report: Airway Mucus Plugging
**Timestamp:** 2025-11-25 23:22:30

**Existing Model:** mucoid impaction (ID: OIFM_GMTS_015330)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
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

## Incoming Attributes (7)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of mucus plugging
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of mucus plugging
- **Values:** Central airways, Segmental bronchi, Subsegmental bronchi
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Extent of mucus plugging
- **Values:** Focal, Multifocal, Diffuse
- **Max selected:** 1
- **Required:** True

### 4. Airway Wall Thickening
- **Name:** Airway Wall Thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of airway wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Bronchiectasis
- **Name:** Bronchiectasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of consolidation
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Ground Glass Opacities
- **Name:** Ground Glass Opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ground glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

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

### 1. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of mucus plugging
- **Values:** Central airways, Segmental bronchi, Subsegmental bronchi
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Extent of mucus plugging
- **Values:** Focal, Multifocal, Diffuse
- **Max selected:** 1
- **Required:** True

### 3. Airway Wall Thickening
- **Name:** Airway Wall Thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of airway wall thickening
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Bronchiectasis
- **Name:** Bronchiectasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of bronchiectasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Consolidation
- **Name:** Consolidation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of consolidation
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Ground Glass Opacities
- **Name:** Ground Glass Opacities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ground glass opacities
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

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
