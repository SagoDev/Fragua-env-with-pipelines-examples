"""Fragua Environment Configuration."""

import fragua as fg
import fragua_sets as fs
from .pipelines import EXCEL_TO_CSV, EXCEL_TO_TFD_EXCEL, API_TO_EXCEL

# Create fragua environment
env = fg.FraguaEnvironment("env-example")

# Add pre-configurated sets from fragua-sets
pre_fg_sets = fs.FRAGUA_SETS
env.add_sets(*pre_fg_sets)

# Add pre-configurated declarative pipelines
pipelines = [EXCEL_TO_TFD_EXCEL, EXCEL_TO_CSV, API_TO_EXCEL]
env.add_pipelines(*pipelines)

ENV = env
