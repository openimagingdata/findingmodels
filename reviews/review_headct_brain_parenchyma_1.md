# Review: head CT brain_parenchyma batch 1

10 brain_parenchyma CSV decisions to review: 7 newly created models and 3 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### brain parenchymal abnormality
**Source file:** `defs/brain_parenchymal_abnormality.fm.json`  
**ID:** `OIFM_OIDM_063972`  
**Description:** Broad grouping for brain parenchymal abnormality findings within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0200`; `name=brain_parenchymal_abnormality`; `category=brain_parenchyma`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### hypoattenuation
**Source file:** `defs/hypoattenuation.fm.json`  
**ID:** `OIFM_OIDM_381117`  
**Description:** Imaging observation of hypoattenuation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** hypodensity, low attenuation, decreased attenuation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0205`; `name=hypoattenuation`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=hypodensity, low attenuation, decreased attenuation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### hyperattenuation
**Source file:** `defs/hyperattenuation.fm.json`  
**ID:** `OIFM_OIDM_485183`  
**Description:** Imaging observation of hyperattenuation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** hyperdensity, high attenuation, increased attenuation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0210`; `name=hyperattenuation`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=hyperdensity, high attenuation, increased attenuation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### early infarct sign
**Source file:** `defs/early_infarct_sign.fm.json`  
**ID:** `OIFM_OIDM_813192`  
**Description:** Imaging observation of early infarct sign within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0250`; `name=early_infarct_sign`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=(blank)`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### insular ribbon sign
**Source file:** `defs/insular_ribbon_sign.fm.json`  
**ID:** `OIFM_OIDM_802330`  
**Description:** Imaging observation of insular ribbon sign within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** loss of insular ribbon  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0255`; `name=insular_ribbon_sign`; `category=brain_parenchyma`; `parent_id=HID0250`; `synonyms=loss of insular ribbon`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: gray_white_matter_indistinction -> loss of gray-white differentiation
**Source file:** `defs/loss_of_gray_white_differentiation.fm.json`  
**ID:** `OIFM_OIDM_786838`  
**Description:** Diminished distinction between cortical gray matter and underlying white matter on CT or MRI, most commonly reflecting cerebral edema or acute ischemia. A marker of early or evolving brain injury.  
**Synonyms:** loss of gray-white matter differentiation, gray-white matter indistinction  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID0260`; `name=gray_white_matter_indistinction`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=loss of gray-white differentiation, loss of gray-white junction`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### mass effect
**Source file:** `defs/mass_effect.fm.json`  
**ID:** `OIFM_OIDM_113253`  
**Description:** Imaging observation of mass effect within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0300`; `name=mass_effect`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=(blank)`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: midline_shift -> midline shift
**Source file:** `defs/midline_shift.fm.json`  
**ID:** `OIFM_OIDM_618974`  
**Description:** Lateral displacement of normally midline intracranial structures (such as the septum pellucidum, third ventricle, or falx) across the anatomic midline, typically quantified in millimeters on axial imaging. It is a key sign of asymmetric mass effect and often reflects underlying hemispheric pathology such as hemorrhage, infarct, edema, or mass.  
**Synonyms:** midline deviation, shift of midline structures  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved, increased, decreased

**Source CSV:** `id=HID0305`; `name=midline_shift`; `category=brain_parenchyma`; `parent_id=HID0300`; `synonyms=midline deviation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### sulcal effacement
**Source file:** `defs/sulcal_effacement.fm.json`  
**ID:** `OIFM_OIDM_392893`  
**Description:** Imaging observation of sulcal effacement within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** effaced sulci, sulcal crowding  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0310`; `name=sulcal_effacement`; `category=brain_parenchyma`; `parent_id=HID0300`; `synonyms=effaced sulci, sulcal crowding`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: effacement_of_basal_cisterns -> basal cistern effacement
**Source file:** `defs/basal_cistern_effacement.fm.json`  
**ID:** `OIFM_OIDM_267712`  
**Description:** Loss, narrowing, or obliteration of the cerebrospinal fluid–filled basal (perimesencephalic) cisterns on CT or MRI due to mass effect from edema, hemorrhage, or a space-occupying lesion. This finding commonly reflects elevated intracranial pressure and may indicate increased risk of transtentorial herniation; the original phrasing 'basal cistern effacement' is an example of this imaging appearance.  
**Synonyms:** effacement of basal cisterns, basilar cistern effacement, cisternal effacement, perimesencephalic cistern effacement, basal cistern obliteration, basal cistern effacement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0315`; `name=effacement_of_basal_cisterns`; `category=brain_parenchyma`; `parent_id=HID0300`; `synonyms=compressed cisterns`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

