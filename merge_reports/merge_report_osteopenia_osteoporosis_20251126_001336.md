# Merge Report: Osteopenia Osteoporosis
**Timestamp:** 2025-11-26 00:13:36

**Existing Model:** generalized osteoporosis (ID: OIFM_GMTS_010762)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 2
  - L1 Hounsfield Unit (at 120 kVp) measurement
  - related entities
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 3
- **Total final attributes:** 4

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of generalized osteoporosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a generalized osteoporosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (3)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether osteoporosis or osteopenia is present or if the mineral density is normal.
- **Values:** Osteoporosis present, Osteopenia present, Normal mineral density
- **Max selected:** 1
- **Required:** True

### 2. L1 Hounsfield Unit (at 120 kVp) measurement
- **Name:** L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.
- **Required:** False

### 3. related entities
- **Name:** related entities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Common entities related to osteopenia and osteoporosis.
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Osteoporosis present, Osteopenia present, Normal mineral density

### New Attributes Added (2)

#### 1. L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.

#### 2. related entities
- **Type:** AttributeType.CHOICE
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Description:** Common entities related to osteopenia and osteoporosis.

### Required Attributes Added
None

---

## Final Attributes (4)

### 1. L1 Hounsfield Unit (at 120 kVp) measurement
- **Name:** L1 Hounsfield Unit (at 120 kVp) measurement
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Measurement of Hounsfield units at the L1 region of the spine using a 120 kVp imaging protocol.
- **Required:** False

### 2. related entities
- **Name:** related entities
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Common entities related to osteopenia and osteoporosis.
- **Values:** vertebral fracture, multilevel vertebral body height loss, cement augmentation of vertebral body, rib fracture, sacral fracture
- **Max selected:** 1
- **Required:** False

### 3. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of generalized osteoporosis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 4. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a generalized osteoporosis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
