"""Pipeline for extract data from an API to a excel file."""

from fragua import FraguaPipeline

from fragua_env.steps import STEP_INDEX
from fragua_env.utils.helpers import get_project_root

# -----------------------------------
# Pipeline Example: api to excel
# -----------------------------------

# Path created for example use
BASE_DIR = get_project_root()
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"
URL = "https://jsonplaceholder.typicode.com/posts"

# Create Empty pipeline
api_to_excel = FraguaPipeline("api_to_excel")

# Create first step: extract from api
extract_from_api = (
    STEP_INDEX.get("extract_from_api")
    .with_params(url=URL)
    .with_save_as("api_to_excel_step_1")
    .build()
)

# Create second step: load to excel
load_to_excel = (
    STEP_INDEX.get("load_to_excel")
    .with_params(filename="api_to_excel.xlsx", subdir=OUTPUT_FILE)
    .with_use("api_to_excel_step_1")
    .build()
)


# Add steps to the pipeline
step_list = [extract_from_api, load_to_excel]
api_to_excel.add(step_list)
