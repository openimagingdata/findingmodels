# Merge Report: Cholelithiasis
**Timestamp:** 2025-11-19 22:19:13

**Existing Model:** gallstone (ID: OIFM_GMTS_022482)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Presence not added)
- **New attributes added:** 7
  - Signs of acute cholecystitis
  - Number of stones
  - Stone size
  - Location
  - Gallbladder wall thickening
  - Pericholecystic fluid
  - Biliary dilatation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 9

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values ['absent', 'present', 'indeterminate', 'unknown'], while the incoming attribute contains ['Present', 'Absent']. When comparing these values case insensitively, we can see that there are shared values: 'present' (from existing) and 'absent' (from existing) which correspond to 'Present' and 'Absent' in incoming. However, the existing attribute has additional unique values 'indeterminate' and 'unknown'. The incoming attribute does not provide any unique values beyond the shared ones. Therefore, while there is an overlap with some shared values, the existence of unique values in the existing attribute means the relationship type is 'needs_review'.  Furthermore, "All incoming values are in existing" is true, but "Incoming has unique values: []" is false since there are no values unique to the incoming attribute as both incoming values are included in existing. This makes the relationship 'needs_review', as there are shared values but also unique ones that are only present in the existing attribute.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gallstone
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gallstone has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of cholelithiasis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Number of stones
- **Name:** Number of stones
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of stones present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 3. Stone size
- **Name:** Stone size
- **Type:** AttributeType.NUMERIC
- **Description:** Indicates the size of the stones.
- **Unit:** mm
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the stones.
- **Values:** Gallbladder lumen, Bile ducts
- **Max selected:** 1
- **Required:** True

### 5. Gallbladder wall thickening
- **Name:** Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of gallbladder wall thickening.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 6. Pericholecystic fluid
- **Name:** Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pericholecystic fluid.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. Biliary dilatation
- **Name:** Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of biliary dilatation.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 8. Signs of acute cholecystitis
- **Name:** Signs of acute cholecystitis
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of signs of acute cholecystitis.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (7)

#### 1. Signs of acute cholecystitis
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of signs of acute cholecystitis.

#### 2. Number of stones
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Indicates the number of stones present.

#### 3. Stone size
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Description:** Indicates the size of the stones.

#### 4. Location
- **Type:** AttributeType.CHOICE
- **Values:** Gallbladder lumen, Bile ducts
- **Description:** Indicates the location of the stones.

#### 5. Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of gallbladder wall thickening.

#### 6. Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pericholecystic fluid.

#### 7. Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of biliary dilatation.

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gallstone
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Signs of acute cholecystitis
- **Name:** Signs of acute cholecystitis
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of signs of acute cholecystitis.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. Number of stones
- **Name:** Number of stones
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of stones present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 4. Stone size
- **Name:** Stone size
- **Type:** AttributeType.NUMERIC
- **Description:** Indicates the size of the stones.
- **Unit:** mm
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the stones.
- **Values:** Gallbladder lumen, Bile ducts
- **Max selected:** 1
- **Required:** True

### 6. Gallbladder wall thickening
- **Name:** Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of gallbladder wall thickening.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. Pericholecystic fluid
- **Name:** Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pericholecystic fluid.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 8. Biliary dilatation
- **Name:** Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of biliary dilatation.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gallstone has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
