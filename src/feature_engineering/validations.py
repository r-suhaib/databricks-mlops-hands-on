from pyspark.sql import DataFrame


def validate_temporal_feature_inputs(
    df: DataFrame
) -> None:

    required_columns = [
        "simulationRun",
        "sample",
        "xmeas_1",
        "xmeas_2",
        "xmeas_3"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )