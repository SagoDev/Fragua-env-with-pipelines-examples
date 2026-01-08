"""Pipelines for data extraction from an excel file to other destination type."""

from .excel_to_csv import EXCEL_TO_CSV
from .excel_to_transformed_excel import EXCEL_TO_TFM_EXCEL

__all__ = ["EXCEL_TO_CSV", "EXCEL_TO_TFM_EXCEL"]
