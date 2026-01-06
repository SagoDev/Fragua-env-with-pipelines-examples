"""Configuration for creation of FraguaStep."""

from fragua.core.step_index import FraguaStepIndex
from fragua_env.steps.extraction import EXTRACTION_STEPS
from fragua_env.steps.loading import LOADING_STEPS

DICTS_LIST = [EXTRACTION_STEPS, LOADING_STEPS]


def create_step_index() -> FraguaStepIndex:
    """Create fragua-sets step index."""
    step_index = FraguaStepIndex()

    for step_dict in DICTS_LIST:
        for name, step in step_dict.items():
            step_index.register(name=name, builder=step)

    return step_index


STEP_INDEX = create_step_index()
