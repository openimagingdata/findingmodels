import logging
from typing import List

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from dotenv import load_dotenv
from findingmodel import FindingModelFull, FindingInfo
from findingmodel.contributor import Person, Organization
from findingmodel.tools import add_ids_to_model
from findingmodel_ai.authoring import create_model_from_markdown

load_dotenv()

logger = logging.getLogger(__name__)


class CDEStagingCtChestMarkdownAdapter:
    @staticmethod
    def _create_oidm_organization() -> Organization:
        return Organization(
            name="Open Imaging Data Model",
            code="OIDM",
            url="https://openimagingdata.org",
        )

    @staticmethod
    def _create_person() -> Person:
        return Person(
            github_username="hoodcm",
            email="chood@mgh.harvard.edu",
            name="C. Michael Hood, MD",
            organization_code="MGB",
        )

    @staticmethod
    def _create_default_contributors() -> List:
        return [
            CDEStagingCtChestMarkdownAdapter._create_oidm_organization(),
            CDEStagingCtChestMarkdownAdapter._create_person(),
        ]

    @staticmethod
    async def adapt_cdestaging_ct_chest_markdown(
        markdown_content: str,
        filename_stem: str,
    ) -> FindingModelFull:
        finding_name = filename_stem.replace("-", " ").replace("_", " ").title()
        logger.debug("Adapting markdown definition for '%s'", finding_name)

        finding_info = FindingInfo(name=finding_name.lower(), description="")
        model = await create_model_from_markdown(
            finding_info,
            markdown_text=markdown_content,
        )

        full_model = add_ids_to_model(model, source="MGB")
        full_model.contributors = CDEStagingCtChestMarkdownAdapter._create_default_contributors()
        return FindingModelFull(**full_model.model_dump())
