# Aberrant Subclavian Artery: Single-Agent vs Multi-Agent Output Comparison

**Date:** 2025-02-25  
**Input:** aberrant-subclavian-artery.md  
**Outputs compared:** `defs/single_agent_output/` vs `defs/pipeline_multiagent_output/`

---

## Summary Table

| Aspect | Single-agent | Multi-agent |
|--------|--------------|-------------|
| **oifm_id** | OIFM_MGB_846464 | OIFM_MGB_174876 (different; new IDs each run) |
| **name** | aberrant subclavian artery | aberrant subclavian artery ✓ |
| **description** | Shorter, generic | Longer, more specific (retroesophageal, compressive symptoms, aneurysmal change) |
| **synonyms** | 4 (aberrant right/left, arteria lusoria, aortic arch anomaly) | 4 (arteria lusoria, aberrant right/left, arteria lusoria syndrome) |
| **tags** | vascular, aortic arch, congenital, thorax | ct, chest, vascular, aortic arch, congenital anomaly, subclavian artery |
| **anatomic_locations** | ✓ Present (subclavian artery, aortic arch) | ✓ Present (aorta, arterial system, anterior spinal artery) |
| **contributors** | ✓ Present (MGB) | ✓ Present (MGB) |
| **presence / change_from_prior** | ✓ First two attributes | ✓ First two attributes |
| **Attribute count** | 8 attributes | 4 attributes |

---

## Attributes

### Single-agent (8 attributes)

1. presence
2. change_from_prior
3. side of origin
4. course
5. **compression** (esophagus/trachea)
6. **atherosclerosis**
7. **aneurysmal dilation**
8. **aneurysm diameter** (numeric)
9. **other arterial anomalies**

### Multi-agent (4 attributes)

1. presence
2. change_from_prior
3. side_of_origin (with value descriptions: classic arteria lusoria, right-sided aortic arch)
4. course (retroesophageal, intertracheoesophageal, pretracheal, other, unknown — with descriptions)

---

## Findings

- **Multi-agent** has richer description and more detailed attribute value descriptions (e.g., course values explain retroesophageal, intertracheoesophageal).
- **Single-agent** has more attributes (compression, atherosclerosis, aneurysmal dilation, aneurysm diameter, other arterial anomalies).
- **anatomic_locations** and **contributors** now present in both outputs (pipeline fix applied).
- **anatomic_locations** differ: single-agent uses subclavian artery + aortic arch; multi-agent uses aorta, arterial system, anterior spinal artery (from `find_anatomic_locations`; anterior spinal artery may be a suboptimal match).
- Both correctly put `presence` and `change_from_prior` first as required.
