"""
Compatibility shim for findingmodel-ai with findingmodel 1.x.

findingmodel-ai 0.2.1 expects DuckDBIndex in findingmodel.index, but
findingmodel 1.0.3 renamed it to FindingModelIndex. This module patches
the alias so findingmodel-ai can import successfully.

Import this module before any findingmodel_ai import.
"""


def _patch_findingmodel_for_ai():
    """Add DuckDBIndex alias for FindingModelIndex in findingmodel.index."""
    import findingmodel.index as _fi

    if not hasattr(_fi, "DuckDBIndex"):
        _fi.DuckDBIndex = _fi.FindingModelIndex


# Run patch on module load
_patch_findingmodel_for_ai()
