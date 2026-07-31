from pyspark.sql import DataFrame


REQUIRED_COLUMNS = [
    "faultNumber",
    "xmeas_1",
    "xmeas_2",
    "xmeas_3",
    "xmeas_1_delta1",
    "xmeas_2_delta1",
    "xmeas_3_delta1"
]


def validate_training_input(
    df: DataFrame
) -> None:

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    row_count = df.count()

    if row_count == 0:
        raise ValueError(
            "Training dataset is empty."
        )

    print(
        f"Training validation passed. "
        f"Rows: {row_count:,}"
    )