"""Transformation steps."""

from typing import Dict
from fragua.core.step_builder import FraguaStepBuilder

from fragua_env.utils.enums import TransfomationFunction

SET_NAME = "transformation"
TransFunc = TransfomationFunction

STRIP_WHITESPACE = FraguaStepBuilder(
    set_name=SET_NAME,
    function=TransFunc.STRIP_WHITESPACE.value,
)

FILL_MISSING_VALUES = FraguaStepBuilder(
    set_name=SET_NAME,
    function=TransFunc.FILL_MISSING_VALUES.value,
)

CREATE_DERIVED_COLUMN = FraguaStepBuilder(
    set_name=SET_NAME,
    function=TransFunc.CREATE_DERIVED_COLUMN.value,
)

CAPITALIZE_STRINGS_COLUMNS = FraguaStepBuilder(
    set_name=SET_NAME,
    function=TransFunc.CAPITALIZE_STRINGS_COLUMNS.value,
)

TRANSFORMATION_STEPS: Dict[str, FraguaStepBuilder] = {
    TransFunc.CREATE_DERIVED_COLUMN.value: CREATE_DERIVED_COLUMN,
    TransFunc.STRIP_WHITESPACE.value: STRIP_WHITESPACE,
    TransFunc.FILL_MISSING_VALUES.value: FILL_MISSING_VALUES,
    TransFunc.CAPITALIZE_STRINGS_COLUMNS.value: CAPITALIZE_STRINGS_COLUMNS,
}
