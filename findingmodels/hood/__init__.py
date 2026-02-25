"""Hood pipeline: load, generate, match, merge, format, and extract sub-findings."""

from findingmodels.hood.loaders import (
    should_process_file,
    load_definition,
    SUPPORTED_ENCODINGS,
)
from findingmodels.hood.generators import (
    generate_new_model,
    ensure_required_attributes,
)
from findingmodels.hood.matchers import (
    find_existing_model_with_specificity_check,
)
from findingmodels.hood.mergers import merge_with_existing
from findingmodels.hood.formatters import apply_formatting_guidelines
from findingmodels.hood.subfindings import extract_sub_findings

__all__ = [
    "should_process_file",
    "load_definition",
    "SUPPORTED_ENCODINGS",
    "generate_new_model",
    "ensure_required_attributes",
    "find_existing_model_with_specificity_check",
    "merge_with_existing",
    "apply_formatting_guidelines",
    "extract_sub_findings",
]
