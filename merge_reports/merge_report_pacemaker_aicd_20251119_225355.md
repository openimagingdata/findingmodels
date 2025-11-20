# Merge Report: Pacemaker Aicd
**Timestamp:** 2025-11-19 22:53:55

**Existing Model:** chest radiograph-evident hardware (ID: OIFM_MSFT_623632)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 7
  - device_location
  - side_directional_approach
  - vascular_approach
  - device_type
  - components
  - lead_location
  - complication
- **Required attributes added:** 1
- **Total existing attributes:** 1
- **Total incoming attributes:** 7
- **Total final attributes:** 9

---

## Existing Attributes (1)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Whether chest radiograph-evident hardware is visible on the imaging study.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (7)

### 1. device_location
- **Name:** device_location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the pacemaker/AICD device.
- **Values:** ventral chest wall, subcutaneous
- **Max selected:** 1
- **Required:** True

### 2. side_directional_approach
- **Name:** side_directional_approach
- **Type:** AttributeType.CHOICE
- **Description:** The side/directional approach used for the pacemaker/AICD device.
- **Values:** left, right
- **Max selected:** 1
- **Required:** True

### 3. vascular_approach
- **Name:** vascular_approach
- **Type:** AttributeType.CHOICE
- **Description:** The vascular approach used for the pacemaker/AICD device.
- **Values:** subclavian vein, axillary vein
- **Max selected:** 1
- **Required:** True

### 4. device_type
- **Name:** device_type
- **Type:** AttributeType.CHOICE
- **Description:** The type of pacemaker/AICD device.
- **Values:** single chamber, dual chamber, biventricular
- **Max selected:** 1
- **Required:** True

### 5. components
- **Name:** components
- **Type:** AttributeType.CHOICE
- **Description:** The components of the pacemaker/AICD device.
- **Values:** generator, tie-down, lead, manufacturer logo, header, connector, shock coil, ring electrode, tip electrode
- **Max selected:** 1
- **Required:** True

### 6. lead_location
- **Name:** lead_location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the lead in the pacemaker/AICD device.
- **Values:** superior vena cava, right atrial appendage, right atrium, right ventricular apex, interventricular septum, coronary sinus
- **Max selected:** 1
- **Required:** True

### 7. complication
- **Name:** complication
- **Type:** AttributeType.CHOICE
- **Description:** Possible complications associated with the pacemaker/AICD device.
- **Values:** fracture, malposition, disconnection, migration, abandoned
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (7)

#### 1. device_location
- **Type:** AttributeType.CHOICE
- **Values:** ventral chest wall, subcutaneous
- **Description:** The location of the pacemaker/AICD device.

#### 2. side_directional_approach
- **Type:** AttributeType.CHOICE
- **Values:** left, right
- **Description:** The side/directional approach used for the pacemaker/AICD device.

#### 3. vascular_approach
- **Type:** AttributeType.CHOICE
- **Values:** subclavian vein, axillary vein
- **Description:** The vascular approach used for the pacemaker/AICD device.

#### 4. device_type
- **Type:** AttributeType.CHOICE
- **Values:** single chamber, dual chamber, biventricular
- **Description:** The type of pacemaker/AICD device.

#### 5. components
- **Type:** AttributeType.CHOICE
- **Values:** generator, tie-down, lead, manufacturer logo, header, connector, shock coil, ring electrode, tip electrode
- **Description:** The components of the pacemaker/AICD device.

#### 6. lead_location
- **Type:** AttributeType.CHOICE
- **Values:** superior vena cava, right atrial appendage, right atrium, right ventricular apex, interventricular septum, coronary sinus
- **Description:** The location of the lead in the pacemaker/AICD device.

#### 7. complication
- **Type:** AttributeType.CHOICE
- **Values:** fracture, malposition, disconnection, migration, abandoned
- **Description:** Possible complications associated with the pacemaker/AICD device.

### Required Attributes Added (1)

#### change from prior
- **Type:** choice
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

---

## Final Attributes (9)

### 1. device_location
- **Name:** device_location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the pacemaker/AICD device.
- **Values:** ventral chest wall, subcutaneous
- **Max selected:** 1
- **Required:** True

### 2. side_directional_approach
- **Name:** side_directional_approach
- **Type:** AttributeType.CHOICE
- **Description:** The side/directional approach used for the pacemaker/AICD device.
- **Values:** left, right
- **Max selected:** 1
- **Required:** True

### 3. vascular_approach
- **Name:** vascular_approach
- **Type:** AttributeType.CHOICE
- **Description:** The vascular approach used for the pacemaker/AICD device.
- **Values:** subclavian vein, axillary vein
- **Max selected:** 1
- **Required:** True

### 4. device_type
- **Name:** device_type
- **Type:** AttributeType.CHOICE
- **Description:** The type of pacemaker/AICD device.
- **Values:** single chamber, dual chamber, biventricular
- **Max selected:** 1
- **Required:** True

### 5. components
- **Name:** components
- **Type:** AttributeType.CHOICE
- **Description:** The components of the pacemaker/AICD device.
- **Values:** generator, tie-down, lead, manufacturer logo, header, connector, shock coil, ring electrode, tip electrode
- **Max selected:** 1
- **Required:** True

### 6. lead_location
- **Name:** lead_location
- **Type:** AttributeType.CHOICE
- **Description:** The location of the lead in the pacemaker/AICD device.
- **Values:** superior vena cava, right atrial appendage, right atrium, right ventricular apex, interventricular septum, coronary sinus
- **Max selected:** 1
- **Required:** True

### 7. complication
- **Name:** complication
- **Type:** AttributeType.CHOICE
- **Description:** Possible complications associated with the pacemaker/AICD device.
- **Values:** fracture, malposition, disconnection, migration, abandoned
- **Max selected:** 1
- **Required:** True

### 8. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Whether chest radiograph-evident hardware is visible on the imaging study.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. change from prior
- **Name:** change from prior
- **Type:** choice
- **Description:** Whether and how a Pacemaker Aicd has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
