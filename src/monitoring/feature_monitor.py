from pyspark.sql import functions as F


def calculate_feature_statistics(
    df,
    feature_columns
):

    results = {}

    for feature in feature_columns:

        stats = (
            df
            .agg(
                F.mean(feature).alias("mean"),
                F.stddev(feature).alias("stddev"),
                F.min(feature).alias("min"),
                F.max(feature).alias("max")
            )
            .collect()[0]
        )

        results[feature] = {
            "mean": stats["mean"],
            "stddev": stats["stddev"],
            "min": stats["min"],
            "max": stats["max"]
        }

    return results