from pyspark.sql import functions as F


def calculate_prediction_distribution(
    predictions_df
):

    results = (
        predictions_df
        .groupBy("prediction")
        .count()
        .orderBy("prediction")
    )

    return results