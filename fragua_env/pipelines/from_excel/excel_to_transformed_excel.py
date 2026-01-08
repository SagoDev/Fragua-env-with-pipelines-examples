"""Pipeline to apply extraction, transformations to data from excel and to load in other excel."""

from typing import Any, Dict
from fragua.utils.helpers import get_project_root

# --------------------------------------------
# Pipeline Declarative Example: excel to transformed excel
# --------------------------------------------

# Path created for example use
BASE_DIR = BASE_DIR = get_project_root()
INPUT_FILE = BASE_DIR / "test_files" / "input_files" / "test_data.xlsx"
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"


# Create declarative pipeline
EXCEL_TO_TFM_EXCEL_PIP: Dict[str, Any] = {
    "name": "excel_to_transformed_excel",
    "steps": [
        {
            "set": "extraction",
            "function": "extract_from_excel",
            "params": {"path": f"{INPUT_FILE}"},
            "save_as": "raw_df",
        },
        {
            "macro": "transform_chain",
            "start_from": "raw_df",
            "save_as": "transformed_df",
            "steps": [
                {
                    "function": "strip_whitespace",
                },
                {
                    "function": "fill_missing_values",
                },
                {
                    "function": "create_derived_column",
                    "params": {
                        "col_a": "price",
                        "col_b": "quantity",
                    },
                },
                {
                    "function": "capitalize_string_columns",
                },
            ],
            "step_prefix": "transform_chain_step",
        },
        {
            "set": "loading",
            "function": "load_to_excel",
            "params": {
                "subdir": f"{OUTPUT_FILE}",
                "filename": "excel_to_excel.xlsx",
            },
            "use": "transformed_df",
            "save_as": "loaded_df",
        },
    ],
}
