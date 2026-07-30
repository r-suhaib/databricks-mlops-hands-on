from pyspark.sql import DataFrame


def create_training_base(
    df: DataFrame
) -> DataFrame:

    selected_columns = [
        "faultNumber",
        "simulationRun",
        "sample",

        "xmeas_1",
        "xmeas_2",
        "xmeas_3",

        "xmeas_1_lag1",
        "xmeas_1_delta1",

        "xmeas_2_lag1",
        "xmeas_2_delta1",

        "xmeas_3_lag1",
        "xmeas_3_delta1"
    ]

    return df.select(*selected_columns)