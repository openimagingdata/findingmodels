# Merge Report: Adrenal Nodule
**Timestamp:** 2025-11-24 17:34:34

**Existing Model:** Adrenal Nodule (ID: OIFM_CDE_000003)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - Stability, compared to priors (kept, status not added)
- **New attributes added:** 2
  - size Finding
  - enhancement pattern
- **Required attributes added:** 0
- **Total existing attributes:** 10
- **Total incoming attributes:** 6
- **Total final attributes:** 12

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. Stability, compared to priors vs status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The EXISTING attribute (Values: ['no priors', 'stable for a year or longer', 'stable', 'priors less than year ago', 'new', 'enlarging', 'indeterminate']) and the INCOMING attribute (Values: ['new', 'stable', 'enlarged']) share two values: 'new' and 'stable'. 

However, the EXISTING attribute has unique values that are not present in the INCOMING attribute, including: 'no priors', 'stable for a year or longer', 'priors less than year ago', 'enlarging', and 'indeterminate'. The INCOMING attribute has one unique value, 'enlarged', which is not present in the EXISTING attribute. 

Therefore, while there are shared values, each attribute also has unique values. 

This results in the relationship being classified as 'needs_review'.

- **Shared values:** new, stable
- **Existing only values:** no priors, stable for a year or longer, priors less than year ago, enlarging, indeterminate
- **Incoming only values:** enlarged

---

## Existing Attributes (10)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of adrenal nodule.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Stability, compared to priors
- **Name:** Stability, compared to priors
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Current lesion size, compared to previous imaging results.
- **Values:** no priors, stable for a year, or longer, stable, priors less than year ago, new, enlarging, indeterminate
- **Max selected:** 1
- **Required:** False

### 3. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** left, right, unknown
- **Max selected:** 1
- **Required:** False

### 4. Unenhanced attenuation
- **Name:** Unenhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained without IV contrast.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 5. Enhanced attenuation
- **Name:** Enhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained during the portovenous phase of enhancement, 60-70s after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 6. Delayed attenuation
- **Name:** Delayed attenuation
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained 15 min after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 7. Microscopic fat
- **Name:** Microscopic fat
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The adrenal nodule contains macroscopic fat, as evidenced by at least one pixel attenuation value less than -10 HU.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. Lesion composition
- **Name:** Lesion composition
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** uniformly cystic, non-uniformly cystic, solid, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. Lesion size
- **Name:** Lesion size
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The greatest linear dimension of the adrenal lesion.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** False

### 10. Benign features
- **Name:** Benign features
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Benign imaging features include homogeneous, low density and smooth margins.
- **Values:** macroscopic fat, density less of equal to 10HU on unenhanced CT, no enhancement or less than 20 HU change, benign calcification, decreased signal on CS-MRI, previously characterized and stable, no benign features, indeterminate, unknown
- **Max selected:** 9
- **Required:** False

---

## Incoming Attributes (6)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** new, stable, enlarged
- **Max selected:** 1
- **Required:** True

### 3. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** True

### 4. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** right, left
- **Max selected:** 1
- **Required:** True

### 5. Hounsfield units (HU)
- **Name:** Hounsfield units (HU)
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Hounsfield units (HU) at non-contrast CT
- **Required:** True

### 6. enhancement pattern
- **Name:** enhancement pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (3)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** present, absent

#### 2. Side vs side Finding
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The existing attribute 'Side' contains the values ['left', 'right', 'unknown'], while the incoming attribute 'side Finding' includes ['right', 'left']. All values from the incoming attribute are present in the existing attribute, and the existing attribute has the additional value 'unknown'. This meets the criteria for a 'subset', where incoming values are entirely contained within existing values, but existing has one or more unique values. Therefore, all incoming values are in existing. Incoming has unique values: ['unknown']. The relationship is classified as 'subset'.

- **Shared values:** right, left
- **Existing only values:** unknown

#### 3. Delayed attenuation vs Hounsfield units (HU)
- **Relationship:** identical (confidence: 0.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Both attributes are numeric types, but they have no values at all. Since both attributes have no values, we can say they are effectively identical in terms of having no data to compare. However, there is no content to substantiate an identical relationship with values, hence the low confidence level. All incoming values are in existing because there are literally no values present in either. Incoming has no unique values: [] and existing has no unique values: []. This leads to the relationship being classified as "identical" due to the absence of data. Additionally, uniqueness cannot be evaluated because there are no entries in either attribute.

### New Attributes Added (2)

#### 1. size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** mm

#### 2. enhancement pattern
- **Type:** AttributeType.CHOICE
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out

### Required Attributes Added
None

---

## Final Attributes (12)

### 1. Stability, compared to priors
- **Name:** Stability, compared to priors
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Current lesion size, compared to previous imaging results.
- **Values:** no priors, stable for a year, or longer, stable, priors less than year ago, new, enlarging, indeterminate
- **Max selected:** 1
- **Required:** False

### 2. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** True

### 3. enhancement pattern
- **Name:** enhancement pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** nonenhancing, enhancing, rapid wash-in and wash-out, delayed wash-out
- **Max selected:** 1
- **Required:** True

### 4. Side
- **Name:** Side
- **Type:** AttributeType.CHOICE
- **Values:** left, right, unknown
- **Max selected:** 1
- **Required:** False

### 5. Unenhanced attenuation
- **Name:** Unenhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained without IV contrast.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 6. Enhanced attenuation
- **Name:** Enhanced attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained during the portovenous phase of enhancement, 60-70s after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 7. Delayed attenuation
- **Name:** Delayed attenuation
- **Type:** AttributeType.NUMERIC
- **Description:** Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained 15 min after IV contrast administration.
- **Unit:** HU
- **Range:** -1024 - 1024
- **Required:** False

### 8. Microscopic fat
- **Name:** Microscopic fat
- **Type:** AttributeType.CHOICE
- **Description:** The adrenal nodule contains macroscopic fat, as evidenced by at least one pixel attenuation value less than -10 HU.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. Lesion composition
- **Name:** Lesion composition
- **Type:** AttributeType.CHOICE
- **Values:** uniformly cystic, non-uniformly cystic, solid, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. Lesion size
- **Name:** Lesion size
- **Type:** AttributeType.NUMERIC
- **Description:** The greatest linear dimension of the adrenal lesion.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** False

### 11. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of adrenal nodule.
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 12. Benign features
- **Name:** Benign features
- **Type:** AttributeType.CHOICE
- **Description:** Benign imaging features include homogeneous, low density and smooth margins.
- **Values:** macroscopic fat, density less of equal to 10HU on unenhanced CT, no enhancement or less than 20 HU change, benign calcification, decreased signal on CS-MRI, previously characterized and stable, no benign features, indeterminate, unknown
- **Max selected:** 9
- **Required:** False

---
