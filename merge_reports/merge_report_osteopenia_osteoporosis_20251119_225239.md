# Merge Report: Osteopenia Osteoporosis
**Timestamp:** 2025-11-19 22:52:39

**Existing Model:** generalized osteoporosis (ID: OIFM_GMTS_010762)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 3
  - presence
  - L1 Hounsfield Unit (at 120 kVp) measurement
  - related entities
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 3
- **Total final attributes:** 5

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of generalized osteoporosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a generalized osteoporosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (3)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether osteoporosis or osteopenia is present or if the mineral density is normal.
- **Values:** Osteoporosis present, Osteopenia present, Normal mineral density
- **Max selected:** 1
- **Required:** True

### 2. L1 Hounsfield Unit (at 120 kVp) measurement
- **Name:** L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.
- **Required:** False

### 3. related entities
- **Name:** related entities
- **Type:** AttributeType.CHOICE
- **Description:** Common entities related to osteopenia and osteoporosis.
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (3)

#### 1. presence
- **Type:** AttributeType.CHOICE
- **Values:** Osteoporosis present, Osteopenia present, Normal mineral density
- **Description:** Indicates whether osteoporosis or osteopenia is present or if the mineral density is normal.

#### 2. L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.

#### 3. related entities
- **Type:** AttributeType.CHOICE
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Description:** Common entities related to osteopenia and osteoporosis.

### Required Attributes Added
None

---

## Final Attributes (5)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether osteoporosis or osteopenia is present or if the mineral density is normal.
- **Values:** Osteoporosis present, Osteopenia present, Normal mineral density
- **Max selected:** 1
- **Required:** True

### 2. L1 Hounsfield Unit (at 120 kVp) measurement
- **Name:** L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.
- **Required:** False

### 3. related entities
- **Name:** related entities
- **Type:** AttributeType.CHOICE
- **Description:** Common entities related to osteopenia and osteoporosis.
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Max selected:** 1
- **Required:** False

### 4. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of generalized osteoporosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 5. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a generalized osteoporosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
