# Merge Report: Pneumobilia
**Timestamp:** 2025-11-19 22:57:49

**Existing Model:** gas in gallbladder or biliary tract (ID: OIFM_GMTS_005685)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Choledocholithiasis not added)
- **New attributes added:** 8
  - Presence
  - Extent
  - Location
  - Associated bile duct dilation
  - Biliary stent
  - Acute pancreatitis
  - Periportal edema
  - Portal vein gas
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 10

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Choledocholithiasis
- **Relationship:** needs_review (confidence: 0.95)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute has the values: ['Present', 'Absent']. When normalized for case, the shared values are: ['present', 'absent']. The existing attribute has additional unique values: ['indeterminate', 'unknown'] that are not present in the incoming attribute. Conversely, the incoming attribute has no unique values. Therefore, all incoming values are in existing, making it not 'enhanced'. Since there are shared values with unique values on either side, the relationship is classified as 'needs_review'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gas in gallbladder or biliary tract
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gas in gallbladder or biliary tract has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Whether pneumobilia is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** The extent of pneumobilia.
- **Values:** Limited, Extensive
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of pneumobilia.
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Max selected:** 1
- **Required:** True

### 4. Associated bile duct dilation
- **Name:** Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Description:** Whether there is associated bile duct dilation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Cholecystitis
- **Name:** Cholecystitis
- **Type:** AttributeType.CHOICE
- **Description:** Whether cholecystitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Choledocholithiasis
- **Name:** Choledocholithiasis
- **Type:** AttributeType.CHOICE
- **Description:** Whether choledocholithiasis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Biliary stent
- **Name:** Biliary stent
- **Type:** AttributeType.CHOICE
- **Description:** Whether a biliary stent is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Acute pancreatitis
- **Name:** Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Description:** Whether acute pancreatitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Periportal edema
- **Name:** Periportal edema
- **Type:** AttributeType.CHOICE
- **Description:** Whether periportal edema is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Portal vein gas
- **Name:** Portal vein gas
- **Type:** AttributeType.CHOICE
- **Description:** Whether portal vein gas is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Cholecystitis
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The EXISTING attribute has the values ['absent', 'present', 'indeterminate', 'unknown'], while the INCOMING attribute has the values ['Present', 'Absent']. When comparing these values, all incoming values are found in the existing attribute when case is normalized (i.e., 'Present' is considered the same as 'present' and 'Absent' is the same as 'absent'). The EXISTING attribute has additional values 'indeterminate' and 'unknown', which are not present in the INCOMING attribute. Therefore, this clearly indicates that all incoming values are in existing and existing has additional unique values. This makes it a subset.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### New Attributes Added (8)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether pneumobilia is present or absent.

#### 2. Extent
- **Type:** AttributeType.CHOICE
- **Values:** Limited, Extensive
- **Description:** The extent of pneumobilia.

#### 3. Location
- **Type:** AttributeType.CHOICE
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Description:** The location of pneumobilia.

#### 4. Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether there is associated bile duct dilation.

#### 5. Biliary stent
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether a biliary stent is present.

#### 6. Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether acute pancreatitis is present.

#### 7. Periportal edema
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether periportal edema is present.

#### 8. Portal vein gas
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether portal vein gas is present.

### Required Attributes Added
None

---

## Final Attributes (10)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gas in gallbladder or biliary tract
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Whether pneumobilia is present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Extent
- **Name:** Extent
- **Type:** AttributeType.CHOICE
- **Description:** The extent of pneumobilia.
- **Values:** Limited, Extensive
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of pneumobilia.
- **Values:** Intrahepatic ducts, Common bile duct, Both
- **Max selected:** 1
- **Required:** True

### 5. Associated bile duct dilation
- **Name:** Associated bile duct dilation
- **Type:** AttributeType.CHOICE
- **Description:** Whether there is associated bile duct dilation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 6. Biliary stent
- **Name:** Biliary stent
- **Type:** AttributeType.CHOICE
- **Description:** Whether a biliary stent is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Acute pancreatitis
- **Name:** Acute pancreatitis
- **Type:** AttributeType.CHOICE
- **Description:** Whether acute pancreatitis is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Periportal edema
- **Name:** Periportal edema
- **Type:** AttributeType.CHOICE
- **Description:** Whether periportal edema is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Portal vein gas
- **Name:** Portal vein gas
- **Type:** AttributeType.CHOICE
- **Description:** Whether portal vein gas is present.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gas in gallbladder or biliary tract has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
