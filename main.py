"""File Docstring."""

from fragua_env.env_config import ENV
from fragua_env.pipelines.from_excel import EXCEL_TO_CSV_DEC_PIP, EXCEL_TO_TFM_EXCEL_PIP


def main():
    """Main Docstring."""

    ENV.execute_pipeline(EXCEL_TO_CSV_DEC_PIP)
    ENV.execute_pipeline(EXCEL_TO_TFM_EXCEL_PIP)


if __name__ == "__main__":
    main()
