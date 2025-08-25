# Left ventricle macros—`OIFM_CDE_000035`

This module describes the common data elements for left ventricle volume use case.

**Codes:** RADELEMENT RDES35 left ventricle macros; RADLEX RID1392 left ventricle

## Attributes

### End diastolic volume—`OIFMA_CDE_000218`

Measure LV end-diastolic volume   
Mininum: 0  
Maximum: 100  
Unit: ml

### End systolic volume—`OIFMA_CDE_000219`

Measure LV end-systolic volume  
Mininum: 0  
Maximum: 100  
Unit: ml

### Ejection fraction—`OIFMA_CDE_000220`

LV ejection fraction, calculated dividing stroke volume by the end-diastolic volume. The stroke volume is calculated subtracting LV ESV from LV EDV (EDV-ESV)  
Mininum: 0  
Maximum: 1  
Unit: percent

### Indexed end diastolic volume—`OIFMA_CDE_000221`

LV end-diastolic volume indexed to body surface area   
Mininum: 0  
Maximum: 100  
Unit: mL/m2

### Indexed end systolic volume—`OIFMA_CDE_000222`

LV end-systolic volume indexed to body surface area  
Mininum: 0  
Maximum: 100  
Unit: mL/m2

### Cardiothoracic ratio—`OIFMA_CDE_001735`

Cardiac size expressed as cardiothoracic ratio. Value step: 0.1  
Mininum: 0  
Maximum: 100  
Unit: unit

### Cardiomegaly—`OIFMA_CDE_001736`

*(Select one)*

- **absent**  
- **present**  
- **indeterminate**  
- **unknown**  

### Carina angle—`OIFMA_CDE_001737`

Value step: 0.1  
Mininum: 0  
Maximum: 100  
Unit: degrees

### Left atrial enlargement—`OIFMA_CDE_001738`

Presence of left atrial enlargement If the cardiothoracic ratio is greater than 05 and the carina angle is greater than 100 degrees then suggest left atrial enlargement.  
*(Select one)*

- **absent**  
- **present**  
- **indeterminate**  
- **unknown**  

### Cardiac output—`OIFMA_CDE_001739`

Calculated multiplying LV stroke volume by the heart rate. Value step:0.1.  
Mininum: 0  
Maximum: 100  
Unit: L/min

---

**Contributors**

- [ACR/RSNA Common Data Elements Project](https://radelement.org/) (CDE)