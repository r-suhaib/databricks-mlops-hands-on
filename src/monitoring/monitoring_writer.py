from pyspark.sql import Row
from datetime import datetime


def write_feature_statistics(
    spark,
    statistics,
    table_name
):

    rows = []

    from datetime import datetime

    now = datetime.utcnow()

    for feature, values in statistics.items():

        rows.append(
            Row(
                monitoring_timestamp=now,
                feature_name=feature,
                mean_value=values["mean"],
                stddev_value=values["stddev"],
                min_value=values["min"],
                max_value=values["max"]
            )
        )

    (
        spark
        .createDataFrame(rows)
        .write
        .mode("append")
        .saveAsTable(table_name)
    )