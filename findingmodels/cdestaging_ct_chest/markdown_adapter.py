import logging

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from findingmodel import FindingInfo, FindingModelFull
from findingmodel.tools import add_ids_to_model
from findingmodel_ai.authoring import create_model_from_markdown

logger = logging.getLogger(__name__)


class CDEStagingCtChestMarkdownAdapter:
    @staticmethod
    async def adapt_cdestaging_ct_chest_markdown(
        markdown_content: str,
        filename_stem: str,
    ) -> FindingModelFull:
        finding_name = filename_stem.replace("-", " ").replace("_", " ").lower()
        logger.debug("Adapting markdown definition for '%s'", finding_name)

        finding_info = FindingInfo(name=finding_name, description="")
        model = await create_model_from_markdown(
            finding_info,
            markdown_text=markdown_content,
        )

        return add_ids_to_model(model, source="MGB")
