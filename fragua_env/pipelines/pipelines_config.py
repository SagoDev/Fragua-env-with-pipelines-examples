"""Pipelines config."""

from typing import List

from fragua import FraguaPipeline, FraguaRegistry, FraguaSet

from .from_excel.excel_to_csv import excel_to_csv


PIPELINES_FUNCTIONS: List[FraguaPipeline] = [
    excel_to_csv,
]


def add_pipelines_set_to_registry(registry: FraguaRegistry) -> None:
    """Add pipelines set to an given registry."""

    pipelines_set = registry.get_set("pipelines")

    if pipelines_set is None:
        pipelines_set = FraguaSet("pipelines")
        registry.add_set(pipelines_set)

    for pipeline in PIPELINES_FUNCTIONS:
        pipelines_set.register(pipeline.name, pipeline)
