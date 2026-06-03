# Review: head CT brain_parenchyma batch 12

10 brain_parenchyma CSV decisions to review: 7 newly created models and 3 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### matched: posterior_reversible_encephalopathy_syndrome -> posterior reversible encephalopathy syndrome
**Source file:** `defs/posterior_reversible_encephalopathy_syndrome.fm.json`  
**ID:** `OIFM_OIDM_755246`  
**Description:** A clinicoradiologic syndrome characterized by typically symmetric, bilateral vasogenic edema predominantly involving the parietal and occipital lobes (often in a posterior circulation distribution), manifesting on head CT as cortical and subcortical hypoattenuation. Commonly associated with acute hypertension, eclampsia, or immunosuppressive therapy, and usually reversible with treatment of the underlying cause.  
**Synonyms:** PRES, reversible posterior leukoencephalopathy syndrome, RPLS  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID1630`; `name=posterior_reversible_encephalopathy_syndrome`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=PRES, reversible posterior leukoencephalopathy syndrome, RPLS`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### pineal cyst
**Source file:** `defs/pineal_cyst.fm.json`  
**ID:** `OIFM_OIDM_273883`  
**Description:** Imaging observation of pineal cyst within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** pineal region cyst  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1635`; `name=pineal_cyst`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=pineal region cyst`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: pineal_lesion -> pineal region lesion
**Source file:** `defs/pineal_region_lesion.fm.json`  
**ID:** `OIFM_GMTS_007385`  
**Description:** Abnormal mass or lesion located near the pineal gland.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1640`; `name=pineal_lesion`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=pineal mass, pineal region mass, pineal region lesion`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps pineal lesion to pineal region lesion. Confirm the region-level scope is acceptable.

**Response:** 

---

### ependymoma
**Source file:** `defs/ependymoma.fm.json`  
**ID:** `OIFM_OIDM_762016`  
**Description:** Diagnosis of ependymoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** ependymal tumor  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1645`; `name=ependymoma`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=ependymal tumor`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### medulloblastoma
**Source file:** `defs/medulloblastoma.fm.json`  
**ID:** `OIFM_OIDM_599986`  
**Description:** Diagnosis of medulloblastoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1650`; `name=medulloblastoma`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: primary_cns_lymphoma -> primary central nervous system lymphoma
**Source file:** `defs/primary_central_nervous_system_lymphoma.fm.json`  
**ID:** `OIFM_OIDM_516995`  
**Description:** Non-Hodgkin lymphoma confined to the brain, spinal cord, leptomeninges, or eyes, typically appearing on CT as one or more hyperdense, homogeneously enhancing masses in periventricular or deep gray matter locations with surrounding vasogenic edema. Lesions are often solitary in immunocompetent patients and multifocal in immunocompromised patients, and necrosis is uncommon except in the setting of HIV.  
**Synonyms:** PCNSL, primary CNS lymphoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved, increased, decreased

**Source CSV:** `id=HID1655`; `name=primary_cns_lymphoma`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=PCNSL, CNS lymphoma, primary brain lymphoma, cerebral lymphoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### pilocytic astrocytoma
**Source file:** `defs/pilocytic_astrocytoma.fm.json`  
**ID:** `OIFM_OIDM_768937`  
**Description:** Diagnosis of pilocytic astrocytoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** JPA, juvenile pilocytic astrocytoma, cystic cerebellar astrocytoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1660`; `name=pilocytic_astrocytoma`; `category=brain_parenchyma`; `parent_id=HID1305`; `synonyms=JPA, juvenile pilocytic astrocytoma, cystic cerebellar astrocytoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### subependymal giant cell astrocytoma
**Source file:** `defs/subependymal_giant_cell_astrocytoma.fm.json`  
**ID:** `OIFM_OIDM_778095`  
**Description:** Diagnosis of subependymal giant cell astrocytoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** SEGA  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1665`; `name=subependymal_giant_cell_astrocytoma`; `category=brain_parenchyma`; `parent_id=HID1305`; `synonyms=SEGA`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### hemangioblastoma
**Source file:** `defs/hemangioblastoma.fm.json`  
**ID:** `OIFM_OIDM_284132`  
**Description:** Diagnosis of hemangioblastoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** cerebellar hemangioblastoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1670`; `name=hemangioblastoma`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=cerebellar hemangioblastoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intracranial germ cell tumor
**Source file:** `defs/intracranial_germ_cell_tumor.fm.json`  
**ID:** `OIFM_OIDM_108949`  
**Description:** Diagnosis of intracranial germ cell tumor, as recognized on head CT or related neuroimaging.  
**Synonyms:** germinoma, intracranial germinoma, CNS germ cell tumor  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1675`; `name=intracranial_germ_cell_tumor`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=germinoma, intracranial germinoma, CNS germ cell tumor`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

