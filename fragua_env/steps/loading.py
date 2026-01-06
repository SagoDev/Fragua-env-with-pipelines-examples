"""FraguaStepBuilders for load functions."""

from typing import Dict
from fragua.core.step_builder import FraguaStepBuilder
from fragua_sets.utils.enums.functions import LoadFunction
from fragua_sets.utils.enums.sets import Sets

SET_NAME = Sets.LOADING.value
LoadFunc = LoadFunction

LOAD_TO_CSV = FraguaStepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_CSV.value,
)

LOAD_TO_EXCEL = FraguaStepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_EXCEL.value,
)

LOAD_TO_API = FraguaStepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_API.value,
)

LOAD_TO_BD = FraguaStepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_DB.value,
)

LOADING_STEPS: Dict[str, FraguaStepBuilder] = {
    LoadFunc.LOAD_TO_API.value: LOAD_TO_API,
    LoadFunc.LOAD_TO_DB.value: LOAD_TO_BD,
    LoadFunc.LOAD_TO_CSV.value: LOAD_TO_CSV,
    LoadFunc.LOAD_TO_EXCEL.value: LOAD_TO_EXCEL,
}
