import mlflow

# import classifier model
from src.training.train_fault_classifier import (
    prepare_training_data,
    train_model
)

# utilised served table for training not calculated
source_df = spark.table(
    "tep_anomaly.served.training_base"
)

# apply tranformation
prepared_df = prepare_training_data(
    source_df
)

# log trainig with MLflow
with mlflow.start_run():

    mlflow.log_param(
        "source_table",
        "tep_anomaly.served.training_base"
    )

    model = train_model(
        prepared_df
    )

    mlflow.log_param(
        "algorithm",
        "logistic_regression"
    )

    mlflow.log_param(
    "catalog",
    "tep_anomaly"
    )

    mlflow.log_param(
    "source_schema",
    "served"
    )

    row_count = source_df.count()

    mlflow.log_metric(
    "training_rows",
    row_count
    )