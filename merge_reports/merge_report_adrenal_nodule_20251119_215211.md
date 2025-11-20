# Merge Report: Adrenal Nodule
**Timestamp:** 2025-11-19 21:52:11

**Existing Model:** Adrenal Nodule (ID: OIFM_CDE_000003)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - Stability, compared to priors (kept, status not added)
- **New attributes added:** 3
  - size Finding
  - Hounsfield units (HU)
  - enhancement pattern
- **Required attributes added:** 0
- **Total existing attributes:** 10
- **Total incoming attributes:** 6
- **Total final attributes:** 13

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. Stability, compared to priors vs status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'Stability, compared to priors' includes the values: ['no priors', 'stable for a year or longer', 'stable', 'priors less than year ago', 'new', 'enlarging', 'indeterminate']. The incoming attribute 'status' has the values: ['new', 'stable', 'enlarged']. 

1. Shared values between existing and incoming: ['new', 'stable'].
2. Unique values in existing: ['no priors', 'stable for a year or longer', 'priors less than year ago', 'enlarging', 'indeterminate'].
3. Unique values in incoming: ['enlarged'].

All incoming values are not in existing as 'enlarged' is not included in existing attributes. Additionally, 'enlarging' from the existing attribute is different compared to 'enlarged'. 

Since there are shared values and unique values in both attributes, the relationship is classified as 'needs_review'. This indicates that there might be some overlap, but more refinement or analysis is required to understand how these relate contextually.

- **Shared values:** new, stable
- **Existing only values:** no priors, stable for a year or longer, priors less than year ago, enlarging, indeterminate
- **Incoming only values:** enlarged

---

## Existing Attributes (10)

### 1. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Values:** left, right, unknown
- **Max selected:** 1
- **Required:** False

### 2. Unenhanced attenuation
- **Name:** Unenhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained without IV contrast.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 3. Enhanced attenuation
- **Name:** Enhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained during the portovenous phase of enhancement, 60-70s after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 4. Delayed attenuation
- **Name:** Delayed attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained 15 min after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 5. Microscopic fat
- **Name:** Microscopic fat
- **Type:** AttributeType.CHOICE
- **Description:** The adrenal nodule contains macroscopic fat, as evidenced by at least one pixel attenuation value less than -10 HU.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. Lesion composition
- **Name:** Lesion composition
- **Type:** AttributeType.CHOICE
- **Values:** uniformly cystic, non-uniformly cystic, solid, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 7. Lesion size
- **Name:** Lesion size
- **Type:** AttributeType.NUMERIC
- **Description:** The greatest linear dimension of the adrenal lesion.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** False

### 8. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of adrenal nodule.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. Stability, compared to priors
- **Name:** Stability, compared to priors
- **Type:** AttributeType.CHOICE
- **Description:** Current lesion size, compared to previous imaging results.
- **Values:** no priors, stable for a year, or longer, stable, priors less than year ago, new, enlarging, indeterminate
- **Max selected:** 1
- **Required:** False

### 10. Benign features
- **Name:** Benign features
- **Type:** AttributeType.CHOICE
- **Description:** Benign imaging features include homogeneous, low density and smooth margins.
- **Values:** macroscopic fat, density less of equal to 10HU on unenhanced CT, no enhancement or less than 20 HU change, benign calcification, decreased signal on CS-MRI, previously characterized and stable, no benign features, indeterminate, unknown
- **Max selected:** 9
- **Required:** False

---

## Incoming Attributes (6)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Values:** new, stable, enlarged
- **Max selected:** 1
- **Required:** True

### 3. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** True

### 4. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Values:** right, left
- **Max selected:** 1
- **Required:** True

### 5. Hounsfield units (HU)
- **Name:** Hounsfield units (HU)
- **Type:** AttributeType.NUMERIC
- **Description:** Hounsfield units (HU) at non-contrast CT
- **Required:** True

### 6. enhancement pattern
- **Name:** enhancement pattern
- **Type:** AttributeType.CHOICE
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Presence vs presence
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The existing attribute has the values ['absent', 'present', 'indeterminate', 'unknown'], while the incoming attribute has the values ['present', 'absent']. All incoming values ('present' and 'absent') are present in the existing attribute. However, the existing attribute also includes additional values 'indeterminate' and 'unknown', which are not in the incoming attribute. Therefore, the incoming attribute is a subset of the existing attribute. All incoming values are in existing, and incoming has no unique values.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

#### 2. Side vs side Finding
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The existing attribute 'Side' has values ['left', 'right', 'unknown'], while the incoming attribute 'side Finding' has values ['right', 'left']. All incoming values ('right', 'left') are present in the existing values ('left', 'right', 'unknown'), confirming that the incoming values are a subset of the existing values. However, the existing has an additional value 'unknown' which is not in the incoming attribute. Therefore, it confirms the relationship as 'subset'. All incoming values are in existing and existing has additional value: ['unknown']. There are no unique values in the incoming attribute, thus confirming it as a subset.

- **Shared values:** left, right
- **Existing only values:** unknown

### New Attributes Added (3)

#### 1. size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** mm

#### 2. Hounsfield units (HU)
- **Type:** AttributeType.NUMERIC
- **Description:** Hounsfield units (HU) at non-contrast CT

#### 3. enhancement pattern
- **Type:** AttributeType.CHOICE
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out

### Required Attributes Added
None

---

## Final Attributes (13)

### 1. Stability, compared to priors
- **Name:** Stability, compared to priors
- **Type:** AttributeType.CHOICE
- **Description:** Current lesion size, compared to previous imaging results.
- **Values:** no priors, stable for a year, or longer, stable, priors less than year ago, new, enlarging, indeterminate
- **Max selected:** 1
- **Required:** False

### 2. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** True

### 3. Hounsfield units (HU)
- **Name:** Hounsfield units (HU)
- **Type:** AttributeType.NUMERIC
- **Description:** Hounsfield units (HU) at non-contrast CT
- **Required:** True

### 4. enhancement pattern
- **Name:** enhancement pattern
- **Type:** AttributeType.CHOICE
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out
- **Max selected:** 1
- **Required:** True

### 5. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Values:** left, right, unknown
- **Max selected:** 1
- **Required:** False

### 6. Unenhanced attenuation
- **Name:** Unenhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained without IV contrast.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 7. Enhanced attenuation
- **Name:** Enhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained during the portovenous phase of enhancement, 60-70s after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 8. Delayed attenuation
- **Name:** Delayed attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained 15 min after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 9. Microscopic fat
- **Name:** Microscopic fat
- **Type:** AttributeType.CHOICE
- **Description:** The adrenal nodule contains macroscopic fat, as evidenced by at least one pixel attenuation value less than -10 HU.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. Lesion composition
- **Name:** Lesion composition
- **Type:** AttributeType.CHOICE
- **Values:** uniformly cystic, non-uniformly cystic, solid, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 11. Lesion size
- **Name:** Lesion size
- **Type:** AttributeType.NUMERIC
- **Description:** The greatest linear dimension of the adrenal lesion.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** False

### 12. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of adrenal nodule.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 13. Benign features
- **Name:** Benign features
- **Type:** AttributeType.CHOICE
- **Description:** Benign imaging features include homogeneous, low density and smooth margins.
- **Values:** macroscopic fat, density less of equal to 10HU on unenhanced CT, no enhancement or less than 20 HU change, benign calcification, decreased signal on CS-MRI, previously characterized and stable, no benign features, indeterminate, unknown
- **Max selected:** 9
- **Required:** False

---
