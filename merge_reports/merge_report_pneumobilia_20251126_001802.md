# Merge Report: Pneumobilia
**Timestamp:** 2025-11-26 00:18:02

**Existing Model:** gas in gallbladder or biliary tract (ID: OIFM_GMTS_005685)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 9
  - Extent
  - Location
  - Associated bile duct dilation
  - Cholecystitis
  - Choledocholithiasis
  - Biliary stent
  - Acute pancreatitis
  - Periportal edema
  - Portal vein gas
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 11

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of gas in gallbladder or biliary tract
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a gas in gallbladder or biliary tract has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Whether pneumobilia is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The extent of pneumobilia.
- **Values:** Limited, Extensive
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of pneumobilia.
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Max selected:** 1
- **Required:** True

### 4. Associated bile duct dilation
- **Name:** Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether there is associated bile duct dilation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Cholecystitis
- **Name:** Cholecystitis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether cholecystitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Choledocholithiasis
- **Name:** Choledocholithiasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether choledocholithiasis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Biliary stent
- **Name:** Biliary stent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether a biliary stent is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Acute pancreatitis
- **Name:** Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether acute pancreatitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Periportal edema
- **Name:** Periportal edema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether periportal edema is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Portal vein gas
- **Name:** Portal vein gas
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether portal vein gas is present.
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

### New Attributes Added (9)

#### 1. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Limited, Extensive
- **Description:** The extent of pneumobilia.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Description:** The location of pneumobilia.

#### 3. Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether there is associated bile duct dilation.

#### 4. Cholecystitis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether cholecystitis is present.

#### 5. Choledocholithiasis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether choledocholithiasis is present.

#### 6. Biliary stent
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether a biliary stent is present.

#### 7. Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether acute pancreatitis is present.

#### 8. Periportal edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether periportal edema is present.

#### 9. Portal vein gas
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether portal vein gas is present.

### Required Attributes Added
None

---

## Final Attributes (11)

### 1. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The extent of pneumobilia.
- **Values:** Limited, Extensive
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of pneumobilia.
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Max selected:** 1
- **Required:** True

### 3. Associated bile duct dilation
- **Name:** Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether there is associated bile duct dilation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Cholecystitis
- **Name:** Cholecystitis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether cholecystitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Choledocholithiasis
- **Name:** Choledocholithiasis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether choledocholithiasis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Biliary stent
- **Name:** Biliary stent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether a biliary stent is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Acute pancreatitis
- **Name:** Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether acute pancreatitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Periportal edema
- **Name:** Periportal edema
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether periportal edema is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Portal vein gas
- **Name:** Portal vein gas
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether portal vein gas is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gas in gallbladder or biliary tract
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 11. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gas in gallbladder or biliary tract has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
