"""File Docstring."""

from typing import Any, Dict
from fragua import FraguaPipeline, get_project_root
from fragua_env.env_config import ENV


BASE_DIR = BASE_DIR = get_project_root()
INPUT_FILE = BASE_DIR / "test_files" / "input_files" / "test_data.xlsx"
OUTPUT_FILE = BASE_DIR / "test_files" / "output_files"
URL = "https://jsonplaceholder.typicode.com/posts"


def main():
    """Main Docstring."""

    # The 3 ways to execute a pipeline in Fragua

    # 1- Execute registered declarative pipelines (str)
    ENV.execute_pipeline("excel_to_csv")

    # 2- Execute directly declarative pipelines (dict[str,Any])

    # 2.1- Create declarative pipeline
    # Here you must use functions previusly registered in sets.
    # In this case I'm want to use an transform pipeline.
    # This type of pipelines represent an sequence of steps(registered functions)
    # that can have params or not.
    # It's very useful beacuse I don't need to create an enterly step for each functions.

    excel_to_excel_with_data_transformed: Dict[str, Any] = {
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
                "set": "transformation",
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
                        "function": "add_total_price_derived_column",
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
                    "filename": "test_excel_to_excel_with_data_transformed.xlsx",
                },
                "use": "transformed_df",
                "save_as": "loaded_df",
            },
        ],
    }
    # 2.1- Execute pipeline
    ENV.execute_pipeline(excel_to_excel_with_data_transformed)

    # 3- Execute directly an FraguaPipeline (FraguaPipeline object)

    # 3.1- Create an FraguaPipeline
    api_to_excel = FraguaPipeline("api_to_excel")

    # 3.2- Create steps
    extract_from_api_step = (
        ENV.step_index.get("extract_from_api")
        .with_params(url=URL)
        .with_save_as("api_to_excel_step_1")
        .build()
    )

    load_to_excel_step = (
        ENV.step_index.get("load_to_excel")
        .with_params(filename="test_api_to_excel.xslx", subdir=OUTPUT_FILE)
        .with_save_as("excel_to_csv_step_2")
        .with_use("excel_to_csv_step_1")
        .build()
    )

    # 3.3- Add step to created FraguaPipeline
    step_list = [extract_from_api_step, load_to_excel_step]
    api_to_excel.add(step_list)

    # 3.4-Execute pipeline
    ENV.execute_pipeline(api_to_excel)


if __name__ == "__main__":
    main()
