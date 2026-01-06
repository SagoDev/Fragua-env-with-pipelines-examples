"""Pipeline for extract data from an excel to csv file."""

from fragua import FraguaPipeline

from fragua_env.steps import STEP_INDEX
from fragua_env.utils.helpers import get_project_root

# -----------------------------------
# Pipeline Example: excel to csv
# -----------------------------------

# Path created for example use
BASE_DIR = BASE_DIR = get_project_root()
INPUT_FILE = BASE_DIR / "test_files" / "input_files" / "test_data.xlsx"
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"

# Create Empty pipeline
excel_to_csv = FraguaPipeline("excel_to_csv")

# Create first step: extract from excel
extract_from_excel = (
    STEP_INDEX.get("extract_from_excel")
    .with_params(path=INPUT_FILE)
    .with_save_as("excel_to_csv_step_1")
    .build()
)


# Create second step: load to csv
load_to_csv = (
    STEP_INDEX.get("load_to_csv")
    .with_params(filename="excel_to_csv.csv", subdir=OUTPUT_FILE)
    .with_save_as("excel_to_csv_step_2")
    .with_use("excel_to_csv_step_1")
    .build()
)

# Add steps to the pipeline
step_list = [extract_from_excel, load_to_csv]
excel_to_csv.add(step_list)
