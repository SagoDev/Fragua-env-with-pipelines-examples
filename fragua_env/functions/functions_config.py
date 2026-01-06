"""Function configurations."""

from fragua import FraguaRegistry, FraguaSet
from .functions import TRANSFORMATION_FUNCTIONS


def add_transformation_set_to_registry(registry: FraguaRegistry) -> None:
    """Add functions set to an given registry."""
    transformation_set = FraguaSet("transformation")

    if transformation_set is None:
        transformation_set = FraguaSet("transformation")
        registry.add_set(transformation_set)

    for function in TRANSFORMATION_FUNCTIONS:
        transformation_set.register(function.__name__, function)
