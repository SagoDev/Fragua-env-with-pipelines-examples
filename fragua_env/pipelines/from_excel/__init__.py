"""Pipelines for data extraction from an excel file to other destination type."""

from .excel_to_csv import EXCEL_TO_CSV_DEC_PIP
from .excel_to_transformed_excel import EXCEL_TO_TFM_EXCEL_PIP

__all__ = ["EXCEL_TO_CSV_DEC_PIP", "EXCEL_TO_TFM_EXCEL_PIP"]
