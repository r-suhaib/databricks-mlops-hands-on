import mlflow
import mlflow.spark

from mlflow.models.signature import infer_signature

from src.training.train_fault_classifier import (
    prepare_training_data,
    train_model, 
    feature_columns
)

SOURCE_TABLE = (
    "tep_anomaly.served.training_base"
)

MLFLOW_TMP_DIR = (
    "/Volumes/tep_anomaly/served/mlflow_artifacts"
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

    signature_input = (
        source_df
        .select(*feature_columns)
        .limit(10)
        .toPandas()
    )

    prediction_df = (
        model.transform(prepared_df)
        .select("prediction")
        .limit(10)
        .toPandas()
    )

    signature = infer_signature(
        signature_input,
        prediction_df
    )

    mlflow.spark.log_model(
        spark_model=model,
        artifact_path="model",
        dfs_tmpdir=MLFLOW_TMP_DIR,
        signature=signature,
        input_example=signature_input
    )

    run_id = mlflow.active_run().info.run_id

    model_uri = (
        f"runs:/{run_id}/model"
    )

    registration = mlflow.register_model(
        model_uri=model_uri,
        name="tep_anomaly.served.tep_fault_classifier"
    )

    print(
        f"Registered model version: "
        f"{registration.version}"
    )

    print(
        "Model successfully logged to MLflow."
    )

