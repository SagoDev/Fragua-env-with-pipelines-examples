"""Pipeline for extract data from an excel to csv file."""

from typing import Any
from fragua.utils.helpers import get_project_root


# Path created for example use
BASE_DIR = BASE_DIR = get_project_root()
INPUT_FILE = BASE_DIR / "test_files" / "input_files" / "test_data.xlsx"
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"

# -----------------------------------
# Declarative Pipeline Example: excel to csv
# -----------------------------------


# Create declarative pipeline
EXCEL_TO_CSV_DEC_PIP: dict[str, Any] = {
    "name": "excel_cleaning_pipeline",
    "steps": [
        {
            "set": "extraction",
            "function": "extract_from_excel",
            "params": {"path": f"{INPUT_FILE}"},
            "save_as": "raw_df",
        },
        {
            "set": "loading",
            "function": "load_to_csv",
            "params": {"subdir": f"{OUTPUT_FILE}", "filename": "test_data.csv"},
            "use": "raw_df",
            "save_as": "final_df",
        },
    ],
}
