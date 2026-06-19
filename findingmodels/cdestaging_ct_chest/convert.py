"""Convert CDEStaging CT chest definitions to validated finding models."""

import logging
from dataclasses import dataclass
from pathlib import Path

from findingmodel import FindingModelFull
from findingmodel.common import model_file_name
from findingmodel.tools import add_standard_codes_to_model
from pydantic import ValidationError

from findingmodels.cdestaging_ct_chest.json_adapter import CDEStagingCtChestJsonAdapter
from findingmodels.cdestaging_ct_chest.loaders import load_definition
from findingmodels.cdestaging_ct_chest.markdown_adapter import CDEStagingCtChestMarkdownAdapter
from findingmodels.cdestaging_ct_chest.normalize_output import normalize_for_validation
from findingmodels.cdestaging_ct_chest.postprocess import enrich_model

logger = logging.getLogger(__name__)


@dataclass
class ConversionResult:
    source_path: Path
    source_type: str
    status: str
    output_path: Path | None
    oifm_id: str | None
    finding_name: str | None
    error: str | None


def _raw_name_from_source(
    file_path: Path,
    file_type: str,
    data: dict | None,
) -> str:
    if file_type == "json" and data:
        return data.get("finding_name") or data.get("name") or file_path.stem
    return file_path.stem.replace("-", " ").replace("_", " ")


async def convert_definition(
    file_path: Path,
    *,
    output_dir: Path,
    write: bool = True,
    output_claims: dict[str, Path] | None = None,
    enrich_metadata: bool = False,
    enrich_locations: bool = False,
) -> ConversionResult:
    """Convert one CDEStaging CT chest definition file to a validated finding model."""
    try:
        data, markdown_content, file_type = await load_definition(file_path)
        raw_name = _raw_name_from_source(file_path, file_type, data)

        if file_type == "json":
            model = await CDEStagingCtChestJsonAdapter.adapt_cdestaging_ct_chest_json(
                data, file_path.name
            )
        else:
            model = await CDEStagingCtChestMarkdownAdapter.adapt_cdestaging_ct_chest_markdown(
                markdown_content, file_path.stem
            )

        model = await enrich_model(
            model,
            source_type=file_type,
            raw_name=raw_name,
            enrich_metadata=enrich_metadata and file_type == "json",
            enrich_locations=enrich_locations,
        )
        add_standard_codes_to_model(model)
        model_dict = normalize_for_validation(model.model_dump())
        validated = FindingModelFull.model_validate(model_dict)

        output_filename = model_file_name(validated.name)
        if output_claims is not None:
            prior = output_claims.get(output_filename)
            if prior is not None and prior != file_path:
                raise ValueError(
                    f"Output filename collision: {prior.name} and {file_path.name} "
                    f"both map to {output_filename}"
                )
            output_claims[output_filename] = file_path

        output_path = None
        if write:
            output_path = output_dir / output_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(
                validated.model_dump_json(indent=2, exclude_none=True),
                encoding="utf-8",
            )

        return ConversionResult(
            source_path=file_path,
            source_type=file_type,
            status="success",
            output_path=output_path,
            oifm_id=validated.oifm_id,
            finding_name=validated.name,
            error=None,
        )
    except ValidationError as e:
        logger.error("Validation failed for %s: %s", file_path.name, e)
        return ConversionResult(
            source_path=file_path,
            source_type=file_path.suffix.lstrip("."),
            status="error",
            output_path=None,
            oifm_id=None,
            finding_name=None,
            error=str(e),
        )
    except Exception as e:
        logger.exception("Failed to convert %s", file_path.name)
        return ConversionResult(
            source_path=file_path,
            source_type=file_path.suffix.lstrip("."),
            status="error",
            output_path=None,
            oifm_id=None,
            finding_name=None,
            error=str(e),
        )
