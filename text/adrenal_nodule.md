# Adrenal nodule—`OIFM_CDE_000003`

Detection and characterization of an adrenal nodule.

**Codes:** RADELEMENT RDES3 adrenal nodule; RADLEX RID88 adrenal gland

## Attributes

### Side—`OIFMA_CDE_000042`

*(Select one)*

- **left**  
- **right**  
- **unknown**  

### Unenhanced attenuation—`OIFMA_CDE_000043`

Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained without IV contrast.  
**Codes**: RADLEX RID28662 attenuation; RADLEX RID11086 unenhanced phase  
Mininum: -1024  
Maximum: 1024  
Unit: HU

### Enhanced attenuation—`OIFMA_CDE_000044`

Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained during the portovenous phase of enhancement, 60-70s after IV contrast administration.  
Mininum: -1024  
Maximum: 1024  
Unit: HU

### Delayed attenuation—`OIFMA_CDE_000045`

Mean attenuation in Hounsfield units (HU) of the region of interest on CT images obtained 15 min after IV contrast administration.  
Mininum: -1024  
Maximum: 1024  
Unit: HU

### Microscopic fat—`OIFMA_CDE_001695`

The adrenal nodule contains macroscopic fat, as evidenced by at least one pixel attenuation value less than -10 HU.  
*(Select one)*

- **absent**  
- **present**  
- **indeterminate**  
- **unknown**  

### Lesion composition—`OIFMA_CDE_001985`

*(Select one)*

- **uniformly cystic**  
- **non-uniformly cystic**  
- **solid**  
- **indeterminate**  
- **unknown**  

### Lesion size—`OIFMA_CDE_001986`

The greatest linear dimension of the adrenal lesion.  
Mininum: 0  
Maximum: 100  
Unit: mm

### Presence—`OIFMA_CDE_001987`

Presence of adrenal nodule.  
*(Select one)*

- **absent**  
- **present**  
- **indeterminate**  
- **unknown**  

### Stability, compared to priors—`OIFMA_CDE_001988`

Current lesion size, compared to previous imaging results.  
*(Select one)*

- **no priors**: No prior imaging was done  
- **stable for a year, or longer**  
- **stable, priors less than year ago**  
- **new**  
- **enlarging**  
- **indeterminate**  

### Benign features—`OIFMA_CDE_001989`

Benign imaging features include homogeneous, low density and smooth margins.  
*(Select up to 9)*
- **macroscopic fat**  
- **density less of equal to 10HU on unenhanced CT**  
- **no enhancement or less than 20 HU change**  
- **benign calcification**: Benign calcification (old hematoma or granuloma)  
- **decreased signal on CS-MRI**  
- **previously characterized and stable**  
- **no benign features**  
- **indeterminate**  
- **unknown**  

---

**Contributors**

- [ACR/RSNA Common Data Elements Project](https://radelement.org/) (CDE)