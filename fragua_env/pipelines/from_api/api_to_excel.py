"""Pipeline for extract data from an API to a excel file."""

from typing import Any

from fragua.utils.helpers import get_project_root


# -----------------------------------
# Pipeline Example: api to excel
# -----------------------------------

# Path created for example use
BASE_DIR = get_project_root()
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"
URL = "https://jsonplaceholder.typicode.com/posts"


API_TO_EXCEL: dict[str, Any] = {
    "name": "from_api_excel",
    "steps": [
        {
            "set": "extraction",
            "function": "extract_from_api",
            "params": {"url": f"{URL}"},
            "save_as": "raw_df",
        },
        {
            "set": "loading",
            "function": "load_to_excel",
            "params": {
                "subdir": f"{OUTPUT_FILE}",
                "filename": "test_api_to_excel.xlsx",
            },
            "use": "raw_df",
            "save_as": "final_df",
        },
    ],
}
