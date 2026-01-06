"""Enums File"""

from enum import Enum


# -------------------
# Pipelines
# -------------------
class Pipelines(str, Enum):
    """Pipelines"""

    EXCEL_TO_CSV = "excel_to_csv"
    API_TO_EXCEL = "api_to_excel"


# ------------------------
# Transforamtion Functions
# ------------------------


class TransfomationFunction(str, Enum):
    """Transformation functions."""

    STRIP_WHITESPACE = "strip_whitespace"
    FILL_MISSING_VALUES = "fill_missing_values"
    CREATE_DERIVED_COLUMN = "create_derived_column"
    CAPITALIZE_STRINGS_COLUMNS = "capitalize_string_columns"
