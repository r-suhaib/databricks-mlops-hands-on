from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from src.feature_engineering.validations import (
    validate_temporal_feature_inputs
)


def create_temporal_features(df: DataFrame) -> DataFrame:

    validate_temporal_feature_inputs(df)

    window_spec = (
        Window
        .partitionBy("simulationRun")
        .orderBy("sample")
    )

    sensors = [
        "xmeas_1",
        "xmeas_2",
        "xmeas_3"
    ]

    result = df

    for sensor in sensors:

        lag_col = F.lag(sensor, 1).over(window_spec)

        result = (
            result
            .withColumn(f"{sensor}_lag1", lag_col)
            .withColumn(
                f"{sensor}_delta1",
                F.col(sensor) - lag_col
            )
        )

    return result