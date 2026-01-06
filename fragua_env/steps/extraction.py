"""FraguaStepBuilders for extraction functions."""

from typing import Dict
from fragua.core.step_builder import FraguaStepBuilder
from fragua_sets.utils.enums.functions import ExtractionFunction
from fragua_sets.utils.enums.sets import Sets

SET_NAME = Sets.EXTRACTION.value
ExtFunc = ExtractionFunction

EXTRACT_FROM_CSV = FraguaStepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_CSV.value,
)

EXTRACT_FROM_EXCEL = FraguaStepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_EXCEL.value,
)

EXTRACT_FROM_API = FraguaStepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_API.value,
)

EXTRACT_FROM_BD = FraguaStepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_DB.value,
)

EXTRACTION_STEPS: Dict[str, FraguaStepBuilder] = {
    ExtFunc.EXTRACT_FROM_API.value: EXTRACT_FROM_API,
    ExtFunc.EXTRACT_FROM_DB.value: EXTRACT_FROM_BD,
    ExtFunc.EXTRACT_FROM_CSV.value: EXTRACT_FROM_CSV,
    ExtFunc.EXTRACT_FROM_EXCEL.value: EXTRACT_FROM_EXCEL,
}
