# CDEStaging CT Chest Batch Progress

Alphabetical deduped sources from `../CDEStaging/definitions/hood_CT_chest`.
Total sources: **205**. Chunk size: **10**. Chunks: **21**.

## Chunk status

| Chunk | Offset | Limit | Sources | Triage | Convert | Lint | Review file | TUI |
|-------|--------|-------|---------|--------|---------|------|-------------|-----|
| 1 | 0 | 10 | aberrant-subclavian-artery.md … aortic-measurements.json | done (4 matched / 6 convert / 0 ambiguous / 0 skipped) | done (6 new / 4 matched) | passed | ready | pending_tui |
| 2 | 10 | 10 | aortic-valve-replacement.json … breast-implant.json | pending | pending | pending | pending | pending |
| 3 | 20 | 10 | breast-mass.json … bronchiectasis.json | pending | pending | pending | pending | pending |
| 4 | 30 | 10 | bronchiolectasis.json … chest_tube.json | pending | pending | pending | pending | pending |
| 5 | 40 | 10 | cholelithiasis.json … elastofibroma.md | pending | pending | pending | pending | pending |
| 6 | 50 | 10 | emphysema.json … esophageal-stricture.json | pending | pending | pending | pending | pending |
| 7 | 60 | 10 | esophageal-varices.md … gastrostomy-tube.md | pending | pending | pending | pending | pending |
| 8 | 70 | 10 | glenohumeral-joint-degenerative-changes.md … hepatic-steatosis.json | pending | pending | pending | pending | pending |
| 9 | 80 | 10 | hiatal-hernia.json … laminectomy.md | pending | pending | pending | pending | pending |
| 10 | 90 | 10 | latarjet-procedure.md … lipoma.json | pending | pending | pending | pending | pending |
| 11 | 100 | 10 | lipomatous-atrial-septal-hypertrophy.md … mediastinal-fat-stranding.json | pending | pending | pending | pending | pending |
| 12 | 110 | 10 | mediastinal-fluid-collection.json … orif-ribs.md | pending | pending | pending | pending | pending |
| 13 | 120 | 10 | osteonecrosis-humeral-head.md … percutaneous-drainage-catheter.json | pending | pending | pending | pending | pending |
| 14 | 130 | 10 | pericardial-cyst.md … pleural-thickening.md | pending | pending | pending | pending | pending |
| 15 | 140 | 10 | pneumobilia.json … pulmonary-emboli.json | pending | pending | pending | pending | pending |
| 16 | 150 | 10 | pulmonary-hamartoma.md … rib-fracture.json | pending | pending | pending | pending | pending |
| 17 | 160 | 10 | ribs-bifid.md … sclerotic-lesion.json | pending | pending | pending | pending | pending |
| 18 | 170 | 10 | spinal-canal-narrowing.md … thyroid-goiter.md | pending | pending | pending | pending | pending |
| 19 | 180 | 10 | thyroid_nodule.json … tracheal-secretions.md | pending | pending | pending | pending | pending |
| 20 | 190 | 10 | tracheal-stenosis.md … tunneled-CVC.json | pending | pending | pending | pending | pending |
| 21 | 200 | 5 | tunneled-port-catheter.json … wedge-resection.json | pending | pending | pending | pending | pending |

## TUI outcome rules

- Chunk **done** when every entry has `**Response:**` = `ok` or blank, after fix rounds, and lint is clean.
- Specific feedback → `needs_fix`; questions → `in_progress`; never opened → `pending_tui`.

## Triage

- Run before convert per chunk: `scripts/triage_cdestaging_sources.py --offset N --limit M --output reviews/triage_cdestaging_chunk_<N>.json`
- Triage JSON records per-source `decision`: `exact_match`, `no_match`, `ambiguous`, `convert`, `user_skip`
- Convert uses `--triage-file` to skip `exact_match` and `user_skip` stems
- Update per-chunk tallies after triage: `matched / converted / ambiguous / skipped` (in progress notes or triage JSON `summary`)

## Source index (alphabetical)

- [1] `aberrant_subclavian_artery` ← `aberrant-subclavian-artery.md`
- [1] `acromioclavicular_joint_degenerative_changes` ← `acromioclavicular-joint-degenerative-changes.md`
- [1] `adrenal_nodule` ← `adrenal-nodule.json`
- [1] `adrenal_thickening` ← `adrenal-thickening.json`
- [1] `airway_mucus_plugging` ← `airway-mucus-plugging.json`
- [1] `annular_calcifications` ← `annular-calcifications.json`
- [1] `anterolisthesis` ← `anterolisthesis.md`
- [1] `aortic_atherosclerosis` ← `aortic-atherosclerosis.json`
- [1] `aortic_dissection` ← `aortic-dissection.md`
- [1] `aortic_measurements` ← `aortic-measurements.json`
- [2] `aortic_valve_replacement` ← `aortic-valve-replacement.json`
- [2] `apical_scarring` ← `apical-scarring.md`
- [2] `arterial_stent` ← `arterial-stent.json`
- [2] `ascending_aortic_repair` ← `ascending-aortic-repair.json`
- [2] `atrial_septal_defect_asd` ← `atrial-septal-defect-asd.md`
- [2] `axillary_nodal_dissection` ← `axillary-nodal-dissection.json`
- [2] `azygos_fissure` ← `azygos-fissure.md`
- [2] `bochdalek_hernia` ← `bochdalek-hernia.json`
- [2] `breast_calcification` ← `breast-calcification.json`
- [2] `breast_implant` ← `breast-implant.json`
- [3] `breast_mass` ← `breast-mass.json`
- [3] `breast_skin_thickening` ← `breast-skin-thickening.json`
- [3] `bronchial_atresia` ← `bronchial-atresia.md`
- [3] `bronchial_occlusion` ← `bronchial-occlusion.md`
- [3] `bronchial_plug` ← `bronchial-plug.json`
- [3] `bronchial_secretions` ← `bronchial-secretions.md`
- [3] `bronchial_stenosis` ← `bronchial-stenosis.md`
- [3] `bronchial_stent` ← `bronchial-stent.json`
- [3] `bronchial_wall_thickening` ← `bronchial-wall-thickening.json`
- [3] `bronchiectasis` ← `bronchiectasis.json`
- [4] `bronchiolectasis` ← `bronchiolectasis.json`
- [4] `cabg` ← `cabg.json`
- [4] `calcified_granuloma` ← `calcified-granuloma.json`
- [4] `calcified_ligamentum_arteriosum` ← `calcified-ligamentum-arteriosum.md`
- [4] `cardiac_thrombus` ← `cardiac-thrombus.md`
- [4] `cardiac_transplant` ← `cardiac-transplant.md`
- [4] `cardiomems_device` ← `cardiomems-device.md`
- [4] `chest_wall_edema` ← `chest-wall-edema.md`
- [4] `chest_wall_fluid_collection` ← `chest-wall-fluid-collection.md`
- [4] `chest_tube` ← `chest_tube.json`
- [5] `cholelithiasis` ← `cholelithiasis.json`
- [5] `clavicle_fracture` ← `clavicle-fracture.md`
- [5] `compression_fracture` ← `compression-fracture.json`
- [5] `coronary_stent` ← `coronary-stent.json`
- [5] `cutaneous_cardiac_rhythm_monitor_zio_patch` ← `cutaneous-cardiac-rhythm-monitor-zio-patch.json`
- [5] `diaphragmatic_lymph_node` ← `diaphragmatic-lymph-node.md`
- [5] `diffuse_idiopathic_skeletal_hyperostosis_dish` ← `diffuse-idiopathic-skeletal-hyperostosis-dish.md`
- [5] `distal_clavicular_resection` ← `distal-clavicular-resection.md`
- [5] `ecmo_cannula` ← `ECMO-cannula.json`
- [5] `elastofibroma` ← `elastofibroma.md`
- [6] `emphysema` ← `emphysema.json`
- [6] `endobronchial_mass` ← `endobronchial-mass.json`
- [6] `endobronchial_valve` ← `endobronchial-valve.md`
- [6] `epidermal_inclusion_cyst` ← `epidermal-inclusion-cyst.json`
- [6] `esophageal_dilation` ← `esophageal-dilation.md`
- [6] `esophageal_diverticulum` ← `esophageal-diverticulum.md`
- [6] `esophageal_fluid` ← `esophageal-fluid.md`
- [6] `esophageal_mass` ← `esophageal-mass.md`
- [6] `esophageal_stent` ← `esophageal-stent.json`
- [6] `esophageal_stricture` ← `esophageal-stricture.json`
- [7] `esophageal_varices` ← `esophageal-varices.md`
- [7] `esophageal_wall_calcification` ← `esophageal-wall-calcification.md`
- [7] `esophageal_wall_thickening` ← `esophageal-wall-thickening.json`
- [7] `esophagectomy` ← `esophagectomy.md`
- [7] `extrapleural_fat_deposition` ← `extrapleural-fat-deposition.md`
- [7] `fibroelastoma` ← `fibroelastoma.md`
- [7] `fibrous_dysplasia_of_ribs` ← `fibrous-dysplasia-of-ribs.md`
- [7] `free_fluid` ← `free-fluid.json`
- [7] `gastric_tube` ← `gastric-tube.md`
- [7] `gastrostomy_tube` ← `gastrostomy-tube.md`
- [8] `glenohumeral_joint_degenerative_changes` ← `glenohumeral-joint-degenerative-changes.md`
- [8] `glenohumeral_joint_dislocation` ← `glenohumeral-joint-dislocation.md`
- [8] `glenohumeral_joint_effusion` ← `glenohumeral-joint-effusion.md`
- [8] `glenohumeral_joint` ← `glenohumeral-joint.json`
- [8] `glenoid_fracture` ← `glenoid-fracture.md`
- [8] `gynecomastia` ← `gynecomastia.json`
- [8] `healed_rib_fracture` ← `healed-rib-fracture.json`
- [8] `hepatic_cyst` ← `hepatic-cyst.json`
- [8] `hepatic_hemangioma` ← `hepatic-hemangioma.json`
- [8] `hepatic_steatosis` ← `hepatic-steatosis.json`
- [9] `hiatal_hernia` ← `hiatal-hernia.json`
- [9] `hill_sachs_fracture` ← `hill-sachs-fracture.md`
- [9] `humeral_resurfacing_arthroplasty` ← `humeral-resurfacing-arthroplasty.md`
- [9] `impella` ← `impella.md`
- [9] `interlobular_septal_thickening` ← `interlobular-septal-thickening.json`
- [9] `internal_mammary_lymph_node` ← `internal-mammary-lymph-node.md`
- [9] `intraparenchymal_lymph_node` ← `intraparenchymal-lymph-node.json`
- [9] `ipmn` ← `ipmn.json`
- [9] `ivc_filter` ← `ivc-filter.json`
- [9] `laminectomy` ← `laminectomy.md`
- [10] `latarjet_procedure` ← `latarjet-procedure.md`
- [10] `leadless_pacemaker` ← `leadless-pacemaker.md`
- [10] `left_atrial_appendage_closure_device` ← `left-atrial-appendage-closure-device.md`
- [10] `left_atrial_appendage_occlusion_device` ← `left-atrial-appendage-occlusion-device.json`
- [10] `left_atrial_enlargement` ← `left-atrial-enlargement.md`
- [10] `left_ventricular_aneurysm` ← `left-ventricular-aneurysm.md`
- [10] `left_ventricular_assist_device_lvad` ← `left-ventricular-assist-device-lvad.json`
- [10] `left_ventricular_enlargement` ← `left-ventricular-enlargement.md`
- [10] `left_ventricular_hypertrophy` ← `left-ventricular-hypertrophy.md`
- [10] `lipoma` ← `lipoma.json`
- [11] `lipomatous_atrial_septal_hypertrophy` ← `lipomatous-atrial-septal-hypertrophy.md`
- [11] `lobectomy` ← `lobectomy.json`
- [11] `loop_recorder` ← `loop-recorder.json`
- [11] `lymphangioma` ← `lymphangioma.md`
- [11] `lytic_lesion` ← `lytic-lesion.json`
- [11] `mastectomy_breast_implant` ← `mastectomy-breast-implant.json`
- [11] `mastectomy` ← `mastectomy.json`
- [11] `median_sternotomy` ← `median-sternotomy.json`
- [11] `mediastinal_cyst` ← `mediastinal-cyst.md`
- [11] `mediastinal_fat_stranding` ← `mediastinal-fat-stranding.json`
- [12] `mediastinal_fluid_collection` ← `mediastinal-fluid-collection.json`
- [12] `mediastinal_lymph_nodes` ← `mediastinal-lymph-nodes.json`
- [12] `mediastinal_mass` ← `mediastinal-mass.json`
- [12] `mitral_valve_replacement` ← `mitral-valve-replacement.md`
- [12] `morgagni_hernia` ← `morgagni-hernia.json`
- [12] `nephrolithiasis` ← `nephrolithiasis.json`
- [12] `neurostimulator_device` ← `neurostimulator-device.json`
- [12] `nontunneled_cvc` ← `nontunneled-CVC.json`
- [12] `orif_clavicle` ← `orif-clavicle.md`
- [12] `orif_ribs` ← `orif-ribs.md`
- [13] `osteonecrosis_humeral_head` ← `osteonecrosis-humeral-head.md`
- [13] `osteopenia_osteoporosis` ← `osteopenia-osteoporosis.json`
- [13] `pacemaker_aicd` ← `pacemaker-aicd.json`
- [13] `papillary_muscle_calcification` ← `papillary-muscle-calcification.md`
- [13] `partial_rib_resection` ← `partial-rib-resection.md`
- [13] `patent_ductus_arteriosus` ← `patent-ductus-arteriosus.md`
- [13] `patent_foramen_ovale_pfo` ← `patent-foramen-ovale-pfo.md`
- [13] `pectus_carinatum` ← `pectus-carinatum.md`
- [13] `pectus_excavatum` ← `pectus-excavatum.md`
- [13] `percutaneous_drainage_catheter` ← `percutaneous-drainage-catheter.json`
- [14] `pericardial_cyst` ← `pericardial-cyst.md`
- [14] `pericardial_effusion` ← `pericardial-effusion.json`
- [14] `pericardial_mass` ← `pericardial-mass.md`
- [14] `peripherally_inserted_central_catheter_picc` ← `peripherally_inserted_central_catheter_picc.json`
- [14] `pfo_closure_device` ← `pfo-closure-device.json`
- [14] `physiologic_wedging_lower_thoracic_vertebrae` ← `physiologic-wedging-lower-thoracic-vertebrae.md`
- [14] `picc` ← `PICC.json`
- [14] `pleural_effusion` ← `pleural-effusion.json`
- [14] `pleural_mass` ← `pleural-mass.md`
- [14] `pleural_thickening` ← `pleural-thickening.md`
- [15] `pneumobilia` ← `pneumobilia.json`
- [15] `pneumomediastinum` ← `pneumomediastinum.json`
- [15] `pneumothorax` ← `pneumothorax.json`
- [15] `posterior_rod_screw_fixation` ← `posterior-rod-screw-fixation.md`
- [15] `postsurgical_changes_thoracotomy` ← `postsurgical-changes-thoracotomy.md`
- [15] `postsurgical_changes_vats` ← `postsurgical-changes-vats.md`
- [15] `proximal_humerus_fracture` ← `proximal-humerus-fracture.md`
- [15] `pulmonary_artery_catheter` ← `pulmonary-artery-catheter.json`
- [15] `pulmonary_artery_dilation` ← `pulmonary-artery-dilation.json`
- [15] `pulmonary_emboli` ← `pulmonary-emboli.json`
- [16] `pulmonary_hamartoma` ← `pulmonary-hamartoma.md`
- [16] `pulmonary_nodule_harmonized` ← `pulmonary-nodule-harmonized.md`
- [16] `pulmonary_nodule` ← `pulmonary-nodule.json`
- [16] `pulmonary_thrombus` ← `pulmonary-thrombus.md`
- [16] `pulmonary_valve_replacement` ← `pulmonary-valve-replacement.md`
- [16] `radiation_fibrosis` ← `radiation-fibrosis.json`
- [16] `replaced_cardiac_valve` ← `replaced-cardiac-valve.json`
- [16] `retrolisthesis` ← `retrolisthesis.md`
- [16] `rib_cervical` ← `rib-cervical.md`
- [16] `rib_fracture` ← `rib-fracture.json`
- [17] `ribs_bifid` ← `ribs-bifid.md`
- [17] `ribs_congenital_fusion` ← `ribs-congenital-fusion.md`
- [17] `ribs_osseous_bridging` ← `ribs-osseous-bridging.md`
- [17] `right_atrial_enlargement` ← `right-atrial-enlargement.md`
- [17] `right_heart_strain` ← `right-heart-strain.json`
- [17] `right_ventricular_enlargement` ← `right-ventricular-enlargement.md`
- [17] `rotator_cuff_calcification` ← `rotator-cuff-calcification.md`
- [17] `saber_sheath_trachea` ← `saber-sheath-trachea.json`
- [17] `scapular_fracture` ← `scapular-fracture.md`
- [17] `sclerotic_lesion` ← `sclerotic-lesion.json`
- [18] `spinal_canal_narrowing` ← `spinal-canal-narrowing.md`
- [18] `sternal_fracture` ← `sternal-fracture.json`
- [18] `sternoclavicular_joint_degenerative_changes` ← `sternoclavicular-joint-degenerative-changes.md`
- [18] `subcutaneous_emphysema` ← `subcutaneous-emphysema.md`
- [18] `subendocardial_fatty_metaplasia` ← `subendocardial-fatty-metaplasia.md`
- [18] `subpleural_reticular_opacities` ← `subpleural-reticular-opacities.json`
- [18] `thoracic_spine_endplate_degenerative_changes` ← `thoracic-spine-endplate-degenerative-changes.md`
- [18] `thymus` ← `thymus.json`
- [18] `thyroid_atrophy` ← `thyroid-atrophy.md`
- [18] `thyroid_goiter` ← `thyroid-goiter.md`
- [19] `thyroid_nodule` ← `thyroid_nodule.json`
- [19] `thyroidectomy` ← `thyroidectomy.json`
- [19] `total_shoulder_arthroplasty` ← `total-shoulder-arthroplasty.md`
- [19] `tracheal_bronchus` ← `tracheal-bronchus.md`
- [19] `tracheal_calcification` ← `tracheal-calcification.md`
- [19] `tracheal_deviation` ← `tracheal-deviation.md`
- [19] `tracheal_dilation` ← `tracheal-dilation.md`
- [19] `tracheal_diverticulum` ← `tracheal-diverticulum.md`
- [19] `tracheal_mass` ← `tracheal-mass.md`
- [19] `tracheal_secretions` ← `tracheal-secretions.md`
- [20] `tracheal_stenosis` ← `tracheal-stenosis.md`
- [20] `tracheal_stent` ← `tracheal-stent.json`
- [20] `tracheal_thickening` ← `tracheal-thickening.md`
- [20] `tracheomalacia` ← `tracheomalacia.json`
- [20] `tracheostomy_tube` ← `tracheostomy-tube.json`
- [20] `traction_bronchiectasis` ← `traction-bronchiectasis.md`
- [20] `tree_in_bud` ← `tree-in-bud.json`
- [20] `tricuspid_valve_replacement` ← `tricuspid-valve-replacement.md`
- [20] `tumoral_calcinosis_shoulder` ← `tumoral-calcinosis-shoulder.md`
- [20] `tunneled_cvc` ← `tunneled-CVC.json`
- [21] `tunneled_port_catheter` ← `tunneled-port-catheter.json`
- [21] `usual_interstitial_pneumonia_uip` ← `usual-interstitial-pneumonia-uip.json`
- [21] `ventricular_septal_defect` ← `ventricular-septal-defect.md`
- [21] `ventricular_shunt_catheter` ← `ventricular-shunt-catheter.json`
- [21] `wedge_resection` ← `wedge-resection.json`
