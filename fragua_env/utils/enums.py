"""Enums File"""

from enum import Enum


# -------------------
# Pipelines
# -------------------
class Pipelines(str, Enum):
    """Pipelines"""

    EXCEL_TO_CSV = "excel_to_csv"
    API_TO_EXCEL = "api_to_excel"
    EXCEL_TO_TFM_EXCEL = "excel_to_tfm_excel"
