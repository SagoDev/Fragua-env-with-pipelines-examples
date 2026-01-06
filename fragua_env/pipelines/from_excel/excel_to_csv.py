"""Pipeline for convert data from an excel into csv."""

from pathlib import Path
from fragua import FraguaPipeline

from fragua_env.steps import STEP_INDEX

BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "test_files" / "input_files" / "test_data.xlsx"

excel_to_csv = FraguaPipeline("excel_to_csv")

extract_from_excel = (
    STEP_INDEX.get("extract_from_excel")
    .with_params(path=INPUT_FILE)
    .with_save_as("excel_to_csv_step_1")
    .build()
)


load_to_csv = (
    STEP_INDEX.get("load_to_csv")
    .with_params(filename="excel_to_csv.csv")
    .with_save_as("excel_to_csv_step_2")
    .with_use("excel_to_csv_step_1")
    .build()
)


step_list = [extract_from_excel, load_to_csv]

excel_to_csv.add(step_list)
