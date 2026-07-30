from pyspark.sql import DataFrame


def validate_required_columns(
    df: DataFrame,
    required_columns: list[str]
) -> None:
    """
    Validate that required columns exist.
    """

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def validate_row_count(
    df: DataFrame
) -> None:
    """
    Ensure dataset contains records.
    """

    if df.count() == 0:
        raise ValueError(
            "Dataset contains no records."
        )