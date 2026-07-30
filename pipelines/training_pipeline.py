import mlflow

from src.training.train_fault_classifier import (
    prepare_training_data,
    train_model
)

SOURCE_TABLE = (
    "tep_anomaly.served.training_base"
)

source_df = spark.table(
    SOURCE_TABLE
)

row_count = source_df.count()

prepared_df = prepare_training_data(
    source_df
)

with mlflow.start_run(
    run_name="rf_baseline_fault_classifier"
):

    mlflow.log_param(
        "source_table",
        SOURCE_TABLE
    )

    mlflow.log_param(
        "catalog",
        "tep_anomaly"
    )

    mlflow.log_param(
        "source_schema",
        "served"
    )

    mlflow.log_param(
        "algorithm",
        "RandomForestClassifier"
    )

    mlflow.log_param(
        "numTrees",
        20
    )

    mlflow.log_param(
        "maxDepth",
        5
    )

    mlflow.log_param(
        "seed",
        42
    )

    mlflow.log_metric(
        "training_rows",
        row_count
    )

    model = train_model(
        prepared_df
    )