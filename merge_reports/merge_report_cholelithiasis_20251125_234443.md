# Merge Report: Cholelithiasis
**Timestamp:** 2025-11-25 23:44:43

**Existing Model:** gallstone (ID: OIFM_GMTS_022482)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Number of stones
  - Stone size
  - Location
  - Gallbladder wall thickening
  - Pericholecystic fluid
  - Biliary dilatation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of gallstone
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a gallstone has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates the presence or absence of cholelithiasis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Signs of acute cholecystitis
- **Name:** Signs of acute cholecystitis
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates the presence or absence of signs of acute cholecystitis.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. Number of stones
- **Name:** Number of stones
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of stones present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 4. Stone size
- **Name:** Stone size
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Indicates the size of the stones.
- **Unit:** mm
- **Required:** True

### 5. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the stones.
- **Values:** Gallbladder lumen, Bile ducts
- **Max selected:** 1
- **Required:** True

### 6. Gallbladder wall thickening
- **Name:** Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of gallbladder wall thickening.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. Pericholecystic fluid
- **Name:** Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of pericholecystic fluid.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 8. Biliary dilatation
- **Name:** Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of biliary dilatation.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Signs of acute cholecystitis
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Signs of acute cholecystitis' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

### New Attributes Added (6)

#### 1. Number of stones
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Indicates the number of stones present.

#### 2. Stone size
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Description:** Indicates the size of the stones.

#### 3. Location
- **Type:** AttributeType.CHOICE
- **Values:** Gallbladder lumen, Bile ducts
- **Description:** Indicates the location of the stones.

#### 4. Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of gallbladder wall thickening.

#### 5. Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pericholecystic fluid.

#### 6. Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of biliary dilatation.

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Number of stones
- **Name:** Number of stones
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of stones present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 2. Stone size
- **Name:** Stone size
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Indicates the size of the stones.
- **Unit:** mm
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the stones.
- **Values:** Gallbladder lumen, Bile ducts
- **Max selected:** 1
- **Required:** True

### 4. Gallbladder wall thickening
- **Name:** Gallbladder wall thickening
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of gallbladder wall thickening.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Pericholecystic fluid
- **Name:** Pericholecystic fluid
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of pericholecystic fluid.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 6. Biliary dilatation
- **Name:** Biliary dilatation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of biliary dilatation.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of gallstone
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a gallstone has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
