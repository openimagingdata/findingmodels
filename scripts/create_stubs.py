import asyncio
from pathlib import Path

from loguru import logger
from findingmodel.common import model_file_name
from findingmodel.tools import create_info_from_name, create_model_stub_from_info, add_ids_to_model, add_standard_codes_to_model

FINDING_NAMES = [
    # "abnormal intracranial enhancement",
    # "basal cistern effacement",
    # "bone island",
    # "bladder abnormality",
    # "upper extremity fracture",
    # "bowel inflammatory signs",
    # "skull abnormality",
    "clavicle fracture",
    "cerebral volume loss",
    "Chiari malformation",
    "diffuse idiopathic skeletal hyperostosis",
    "thoracic spine degenerative changes",
    "lumbar spine degenerative changes",
    "colonic diverticulosis",
    "colornic diverticulitis",
    "hepatic lesion",
    "IVC thrombosis",
    "soft tissue mass",
    "hydronephrosis",
    "intracranial mass",
    "loss of gray-white differentiation",
    "mitral annular calcification",
    "orbital mass",
    "mastoid air cell fluid",
    "pancreatic lesion",
    "peripancreatic fluid",
    "parapelvic renal cyst",
    "prostatic abnormality",
    "pulmonary opacity",
    "pulmonary scarring",
    "intracranial vascular abnormality",
    "soft tissue mass",
    "small vessel ischemic disease"
]

output_dir = Path("defs/ipl_defs")
names_ids: dict[str, tuple[str, str]] = {}

async def main() -> None:
    # for name in FINDING_NAMES:
    for name in ["seminal vesicle abnormality"]:
        logger.info(f"Processing finding: {name}")
        info = await create_info_from_name(name)
        base_stub = create_model_stub_from_info(info)
        stub = add_ids_to_model(base_stub, source="OIDM")
        add_standard_codes_to_model(stub)

        output_path = output_dir / model_file_name(stub.name)

        logger.info(f"Writing stub to: {output_path}")
        output_path.write_text(stub.model_dump_json(indent=2, exclude_none=True))
        names_ids[name] = (stub.oifm_id, stub.attributes[0].oifma_id)

    for name, ids in names_ids.items():
        print(f"{name} {ids[0]} {ids[1]}")
if __name__ == "__main__":

    asyncio.run(main())