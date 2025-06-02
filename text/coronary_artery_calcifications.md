# Coronary artery calcifications—`OIFM_MSFT_430810`

**Synonyms:** Coronary Calcification, CAC, Coronary Atherosclerosis

Atherosclerotic calcifications of the coronary arteries

## Attributes

### Presence—`OIFMA_MSFT_286425`

Indicates whether calcification is present in the coronary arteries.  
**Codes**: SNOMED 705057003 Presence (property) (qualifier value)  
*(Select one)*

- **absent**: No coronary artery calcification detected.  
_RADLEX RID28473 absent; SNOMED 2667000 Absent (qualifier value)_
- **present**: Coronary artery calcification is present.  
_RADLEX RID28472 present; SNOMED 52101004 Present (qualifier value)_
- **indeterminate**: Presence of coronary artery calcification cannot be determined.  
_RADLEX RID39110 indeterminate; SNOMED 82334004 Indeterminate (qualifier value)_
- **unknown**: Presence of coronary artery calcification is unknown.  
_RADLEX RID5655 unknown; SNOMED 261665006 Unknown (qualifier value)_

### Cac severity category—`OIFMA_MSFT_976443`

Categorizes coronary artery calcification based on the total Agatston score.  
*(Select one)*

- **none**: No coronary calcification (Agatston score = 0).  
- **mild**: Mild coronary calcification (Agatston score 1–99).  
_RADLEX RID5671 mild; SNOMED 255604002 Mild (qualifier value)_
- **moderate**: Moderate coronary calcification (Agatston score 100–399).  
_RADLEX RID5672 moderate; SNOMED 1255665007 Moderate (qualifier value)_
- **severe**: Severe coronary calcification (Agatston score ≥ 400).  
_RADLEX RID5673 severe; SNOMED 24484000 Severe (severity modifier) (qualifier value)_

### Location—`OIFMA_MSFT_472379`

Identifies which coronary arteries are involved in the calcification.  
**Codes**: RADLEX RID39038 location; SNOMED 758637006 Anatomic location (property) (qualifier value)  
*(Select up to 4)*
- **left main coronary artery**: Calcification present in the left main coronary artery.  
- **left circumflex artery**: Calcification present in the left circumflex artery.  
- **left anterior descending artery**: Calcification present in the left anterior descending artery.  
- **right coronary artery**: Calcification present in the right coronary artery.  

### Agatston score—`OIFMA_MSFT_161908`

Agatston score for coronary artery calcification, used to quantify severity.  
Mininum: 0  
Maximum: 10000  
Unit: score

### Arterial age—`OIFMA_MSFT_429306`

Numeric value calculated from the Agatston score, providing an estimation of arterial age.  
Mininum: 39  
Unit: years

---

**Contributors**

- Heather Chase (MSFT) — [Email](mailto:heatherchase@microsoft.com) — [Link](https://www.linkedin.com/in/heatherwalkerchase/)