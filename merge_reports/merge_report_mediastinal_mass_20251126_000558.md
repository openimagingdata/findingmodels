# Merge Report: Mediastinal Mass
**Timestamp:** 2025-11-26 00:05:58

**Existing Model:** soft-tissue mediastinal mass (ID: OIFM_GMTS_015538)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 8
  - Anatomical Location
  - Size Finding
  - Density
  - Borders
  - Effects on Surrounding Structures
  - Lymphadenopathy
  - Calcifications
  - Signs of Invasion
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 9
- **Total final attributes:** 10

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of soft-tissue mediastinal mass
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a soft-tissue mediastinal mass has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (9)

### 1. Presence of Mediastinal Mass
- **Name:** Presence of Mediastinal Mass
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether a mediastinal mass is present or not.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Anatomical Location
- **Name:** Anatomical Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The anatomical location of the mediastinal mass.
- **Values:** Anterior Mediastinum, Middle Mediastinum, Posterior Mediastinum
- **Max selected:** 1
- **Required:** True

### 3. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The size of the mediastinal mass.
- **Values:** Small, Medium, Large
- **Max selected:** 1
- **Required:** True

### 4. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The density of the mediastinal mass.
- **Values:** Solid, Cystic, Mixed
- **Max selected:** 1
- **Required:** True

### 5. Borders
- **Name:** Borders
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The borders of the mediastinal mass.
- **Values:** Well-defined, Poorly defined
- **Max selected:** 1
- **Required:** True

### 6. Effects on Surrounding Structures
- **Name:** Effects on Surrounding Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The effects of the mediastinal mass on the surrounding structures.
- **Values:** Compression, Displacement, None
- **Max selected:** 1
- **Required:** True

### 7. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether lymphadenopathy, or enlarged lymph nodes, is present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Calcifications
- **Name:** Calcifications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether calcifications are present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Signs of Invasion
- **Name:** Signs of Invasion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether signs of invasion, such as infiltration into surrounding tissue, are present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Mediastinal Mass
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Mediastinal Mass' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

### New Attributes Added (8)

#### 1. Anatomical Location
- **Type:** AttributeType.CHOICE
- **Values:** Anterior Mediastinum, Middle Mediastinum, Posterior Mediastinum
- **Description:** The anatomical location of the mediastinal mass.

#### 2. Size Finding
- **Type:** AttributeType.CHOICE
- **Values:** Small, Medium, Large
- **Description:** The size of the mediastinal mass.

#### 3. Density
- **Type:** AttributeType.CHOICE
- **Values:** Solid, Cystic, Mixed
- **Description:** The density of the mediastinal mass.

#### 4. Borders
- **Type:** AttributeType.CHOICE
- **Values:** Well-defined, Poorly defined
- **Description:** The borders of the mediastinal mass.

#### 5. Effects on Surrounding Structures
- **Type:** AttributeType.CHOICE
- **Values:** Compression, Displacement, None
- **Description:** The effects of the mediastinal mass on the surrounding structures.

#### 6. Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether lymphadenopathy, or enlarged lymph nodes, is present or not.

#### 7. Calcifications
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether calcifications are present or not.

#### 8. Signs of Invasion
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether signs of invasion, such as infiltration into surrounding tissue, are present or not.

### Required Attributes Added
None

---

## Final Attributes (10)

### 1. Anatomical Location
- **Name:** Anatomical Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The anatomical location of the mediastinal mass.
- **Values:** Anterior Mediastinum, Middle Mediastinum, Posterior Mediastinum
- **Max selected:** 1
- **Required:** True

### 2. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The size of the mediastinal mass.
- **Values:** Small, Medium, Large
- **Max selected:** 1
- **Required:** True

### 3. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The density of the mediastinal mass.
- **Values:** Solid, Cystic, Mixed
- **Max selected:** 1
- **Required:** True

### 4. Borders
- **Name:** Borders
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The borders of the mediastinal mass.
- **Values:** Well-defined, Poorly defined
- **Max selected:** 1
- **Required:** True

### 5. Effects on Surrounding Structures
- **Name:** Effects on Surrounding Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The effects of the mediastinal mass on the surrounding structures.
- **Values:** Compression, Displacement, None
- **Max selected:** 1
- **Required:** True

### 6. Lymphadenopathy
- **Name:** Lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether lymphadenopathy, or enlarged lymph nodes, is present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Calcifications
- **Name:** Calcifications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether calcifications are present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Signs of Invasion
- **Name:** Signs of Invasion
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether signs of invasion, such as infiltration into surrounding tissue, are present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of soft-tissue mediastinal mass
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a soft-tissue mediastinal mass has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
