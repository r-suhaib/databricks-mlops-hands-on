from pyspark.ml.evaluation import MulticlassClassificationEvaluator


def evaluate_model(
    predictions_df
):

    metrics = {}

    evaluator = MulticlassClassificationEvaluator(
        labelCol="faultNumber",
        predictionCol="prediction"
    )

    metrics["accuracy"] = evaluator.evaluate(
        predictions_df,
        {
            evaluator.metricName: "accuracy"
        }
    )

    metrics["f1"] = evaluator.evaluate(
        predictions_df,
        {
            evaluator.metricName: "f1"
        }
    )

    metrics["weighted_precision"] = (
        evaluator.evaluate(
            predictions_df,
            {
                evaluator.metricName:
                "weightedPrecision"
            }
        )
    )

    metrics["weighted_recall"] = (
        evaluator.evaluate(
            predictions_df,
            {
                evaluator.metricName:
                "weightedRecall"
            }
        )
    )

    return metrics