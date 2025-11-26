# Merge Report: Tunneled Port Catheter
**Timestamp:** 2025-11-26 00:33:34

**Existing Model:** chest radiograph-evident hardware (ID: OIFM_MSFT_623632)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 9
  - Status
  - Appropriate location
  - Side Finding
  - Number of Lumens
  - Vein approach
  - Course
  - Distal tip location
  - Port location
  - Complications
- **Required attributes added:** 0
- **Total existing attributes:** 1
- **Total incoming attributes:** 10
- **Total final attributes:** 10

---

## Existing Attributes (1)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Whether chest radiograph-evident hardware is visible on the imaging study.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence of Tunneled Port Catheter
- **Name:** Presence of Tunneled Port Catheter
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether a tunneled port catheter is present or not.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Indicates the status of the tunneled port catheter.
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 3. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether the tunneled port catheter is in an appropriate location.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the side of the body where the tunneled port catheter is located.
- **Values:** Left, Right
- **Max selected:** 1
- **Required:** True

### 5. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of lumens (channels) in the tunneled port catheter.
- **Values:** Single, Double
- **Max selected:** 1
- **Required:** True

### 6. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the vein approach used for inserting the tunneled port catheter.
- **Values:** Internal jugular, Subclavian
- **Max selected:** 1
- **Required:** True

### 7. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the course of the tunneled port catheter.
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** True

### 8. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the distal tip of the tunneled port catheter.
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Max selected:** 1
- **Required:** True

### 9. Port location
- **Name:** Port location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the port of the tunneled port catheter.
- **Values:** Pectoral, Abdominal
- **Max selected:** 1
- **Required:** True

### 10. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the complications associated with the tunneled port catheter.
- **Values:** None, Occlusion, Catheter fracture, Port displacement, Thrombosis (fibrin sheath), Tip migration
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Tunneled Port Catheter
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Tunneled Port Catheter' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (9)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed
- **Description:** Indicates the status of the tunneled port catheter.

#### 2. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates whether the tunneled port catheter is in an appropriate location.

#### 3. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right
- **Description:** Indicates the side of the body where the tunneled port catheter is located.

#### 4. Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double
- **Description:** Indicates the number of lumens (channels) in the tunneled port catheter.

#### 5. Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian
- **Description:** Indicates the vein approach used for inserting the tunneled port catheter.

#### 6. Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling
- **Description:** Indicates the course of the tunneled port catheter.

#### 7. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Description:** Indicates the location of the distal tip of the tunneled port catheter.

#### 8. Port location
- **Type:** AttributeType.CHOICE
- **Values:** Pectoral, Abdominal
- **Description:** Indicates the location of the port of the tunneled port catheter.

#### 9. Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Catheter fracture, Port displacement, Thrombosis (fibrin sheath), Tip migration
- **Description:** Indicates the complications associated with the tunneled port catheter.

### Required Attributes Added
None

---

## Final Attributes (10)

### 1. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Indicates the status of the tunneled port catheter.
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 2. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates whether the tunneled port catheter is in an appropriate location.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the side of the body where the tunneled port catheter is located.
- **Values:** Left, Right
- **Max selected:** 1
- **Required:** True

### 4. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of lumens (channels) in the tunneled port catheter.
- **Values:** Single, Double
- **Max selected:** 1
- **Required:** True

### 5. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the vein approach used for inserting the tunneled port catheter.
- **Values:** Internal jugular, Subclavian
- **Max selected:** 1
- **Required:** True

### 6. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the course of the tunneled port catheter.
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** True

### 7. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the distal tip of the tunneled port catheter.
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Max selected:** 1
- **Required:** True

### 8. Port location
- **Name:** Port location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the port of the tunneled port catheter.
- **Values:** Pectoral, Abdominal
- **Max selected:** 1
- **Required:** True

### 9. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the complications associated with the tunneled port catheter.
- **Values:** None, Occlusion, Catheter fracture, Port displacement, Thrombosis (fibrin sheath), Tip migration
- **Max selected:** 1
- **Required:** True

### 10. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Whether chest radiograph-evident hardware is visible on the imaging study.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
