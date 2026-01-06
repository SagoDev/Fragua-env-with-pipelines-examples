"""File Docstring."""

from fragua_env.env_config import ENV
from fragua_env.utils.enums import Pipelines


def main():
    """Main Docstring."""

    # [Optional]: Enums to validate pipelines names
    api_to_excel = Pipelines.API_TO_EXCEL.value
    excel_to_csv = Pipelines.EXCEL_TO_CSV.value

    # Execute pipelines
    ENV.run(api_to_excel)
    ENV.run(excel_to_csv)


if __name__ == "__main__":
    main()
