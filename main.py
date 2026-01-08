"""File Docstring."""

from fragua_env.env_config import ENV
from fragua_env.pipelines import (
    EXCEL_TO_CSV,
    EXCEL_TO_TFM_EXCEL,
    API_TO_EXCEL,
)


def main():
    """Main Docstring."""

    ENV.execute_pipeline(EXCEL_TO_CSV)
    ENV.execute_pipeline(EXCEL_TO_TFM_EXCEL)
    ENV.execute_pipeline(API_TO_EXCEL)


if __name__ == "__main__":
    main()
