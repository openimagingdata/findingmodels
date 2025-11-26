# Merge Report: Ventricular Shunt Catheter
**Timestamp:** 2025-11-26 00:35:37

**Existing Model:** Ventriculoperitoneal Shunt Assessment (ID: OIFM_CDE_000118)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 8
  - Status
  - Shunt Type
  - Appropriate location
  - Proximal tip location
  - Distal tip location
  - Valve Type
  - Valve Setting (if programmable)
  - Complications
- **Required attributes added:** 0
- **Total existing attributes:** 4
- **Total incoming attributes:** 9
- **Total final attributes:** 12

---

## Existing Attributes (4)

### 1. Abandoned shunt catheters
- **Name:** Abandoned shunt catheters
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 3. Programmable valve setting
- **Name:** Programmable valve setting
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** setting of the programmable valve
- **Unit:** cm H2O
- **Range:** 0 - 100
- **Required:** False

### 4. Shunt catheter status
- **Name:** Shunt catheter status
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** status of the VP shunt
- **Values:** intact, discontinuous, kinked, discontinuous and kinked, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (9)

### 1. Presence of Ventricular Shunt Catheter
- **Name:** Presence of Ventricular Shunt Catheter
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether a ventricular shunt catheter is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** The status of the ventricular shunt catheter.
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 3. Shunt Type
- **Name:** Shunt Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The type of ventricular shunt.
- **Values:** Ventriculoperitoneal (VP), Ventriculoatrial (VA), Ventriculopleural
- **Max selected:** 1
- **Required:** True

### 4. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether the ventricular shunt catheter is in an appropriate location.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Proximal tip location
- **Name:** Proximal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the proximal tip of the ventricular shunt catheter.
- **Values:** Right lateral ventricle, Left lateral ventricle, Third ventricle, Not identified
- **Max selected:** 1
- **Required:** True

### 6. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the distal tip of the ventricular shunt catheter.
- **Values:** Peritoneal cavity, Right atrium, Pleural cavity
- **Max selected:** 1
- **Required:** True

### 7. Valve Type
- **Name:** Valve Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The type of valve used in the ventricular shunt catheter.
- **Values:** Programmable, Fixed pressure
- **Max selected:** 1
- **Required:** True

### 8. Valve Setting (if programmable)
- **Name:** Valve Setting (if programmable)
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The setting of the programmable valve used in the ventricular shunt catheter.
- **Values:** Specify setting, Not applicable
- **Max selected:** 1
- **Required:** False

### 9. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Any complications associated with the ventricular shunt catheter.
- **Values:** None, Catheter fracture, Tip migration
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Abandoned shunt catheters vs Presence of Ventricular Shunt Catheter
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Ventricular Shunt Catheter' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (8)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed
- **Description:** The status of the ventricular shunt catheter.

#### 2. Shunt Type
- **Type:** AttributeType.CHOICE
- **Values:** Ventriculoperitoneal (VP), Ventriculoatrial (VA), Ventriculopleural
- **Description:** The type of ventricular shunt.

#### 3. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates whether the ventricular shunt catheter is in an appropriate location.

#### 4. Proximal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Right lateral ventricle, Left lateral ventricle, Third ventricle, Not identified
- **Description:** The location of the proximal tip of the ventricular shunt catheter.

#### 5. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Peritoneal cavity, Right atrium, Pleural cavity
- **Description:** The location of the distal tip of the ventricular shunt catheter.

#### 6. Valve Type
- **Type:** AttributeType.CHOICE
- **Values:** Programmable, Fixed pressure
- **Description:** The type of valve used in the ventricular shunt catheter.

#### 7. Valve Setting (if programmable)
- **Type:** AttributeType.CHOICE
- **Values:** Specify setting, Not applicable
- **Description:** The setting of the programmable valve used in the ventricular shunt catheter.

#### 8. Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Catheter fracture, Tip migration
- **Description:** Any complications associated with the ventricular shunt catheter.

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** The status of the ventricular shunt catheter.
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 2. Shunt Type
- **Name:** Shunt Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The type of ventricular shunt.
- **Values:** Ventriculoperitoneal (VP), Ventriculoatrial (VA), Ventriculopleural
- **Max selected:** 1
- **Required:** True

### 3. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether the ventricular shunt catheter is in an appropriate location.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Proximal tip location
- **Name:** Proximal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the proximal tip of the ventricular shunt catheter.
- **Values:** Right lateral ventricle, Left lateral ventricle, Third ventricle, Not identified
- **Max selected:** 1
- **Required:** True

### 5. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the distal tip of the ventricular shunt catheter.
- **Values:** Peritoneal cavity, Right atrium, Pleural cavity
- **Max selected:** 1
- **Required:** True

### 6. Valve Type
- **Name:** Valve Type
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The type of valve used in the ventricular shunt catheter.
- **Values:** Programmable, Fixed pressure
- **Max selected:** 1
- **Required:** True

### 7. Valve Setting (if programmable)
- **Name:** Valve Setting (if programmable)
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The setting of the programmable valve used in the ventricular shunt catheter.
- **Values:** Specify setting, Not applicable
- **Max selected:** 1
- **Required:** False

### 8. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Any complications associated with the ventricular shunt catheter.
- **Values:** None, Catheter fracture, Tip migration
- **Max selected:** 1
- **Required:** True

### 9. Programmable valve setting
- **Name:** Programmable valve setting
- **Type:** AttributeType.NUMERIC
- **Description:** setting of the programmable valve
- **Unit:** cm H2O
- **Range:** 0 - 100
- **Required:** False

### 10. Shunt catheter status
- **Name:** Shunt catheter status
- **Type:** AttributeType.CHOICE
- **Description:** status of the VP shunt
- **Values:** intact, discontinuous, kinked, discontinuous and kinked, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 11. Abandoned shunt catheters
- **Name:** Abandoned shunt catheters
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 12. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
