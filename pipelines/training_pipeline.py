import mlflow
import mlflow.spark

from mlflow.models.signature import infer_signature

from src.utils.config_loader import (
    load_config
)

from src.training.train_fault_classifier import (
    prepare_training_data,
    train_model,
    feature_columns
)

from src.training.training_validations import (
    validate_training_input
)

from src.utils.delta_utils import (
    get_latest_delta_version
)

from src.evaluation.model_evaluation import (
    evaluate_model
)

from src.evaluation.promotion_gate import (
    passes_promotion_gate
)

from src.evaluation.champion_comparision import (
    compare_to_champion
)

from src.utils.environment_config import (
    load_environment
)

from src.utils.runtime_config import (
    get_runtime_parameters
)

from src.evaluation.registry_utils import (
    get_champion_run_id,
    get_run_metric
)

from src.evaluation.promotion_recommendation import (
    get_promotion_recommendation
)

from src.evaluation.promotion_approval import (
    is_approved_for_promotion
)

# runtime parameters

runtime_parameters = (
    get_runtime_parameters()
)

# environment type

environment = load_environment(
    runtime_parameters[
        "environment"
    ]
)

# MLflow Experiment

mlflow.set_experiment(
    "/Users/rsuhaib678@gmail.com/databricks-mlops-hands-on/pipelines/training_pipeline.py"
)

# Load Configuration

config = load_config(
    f"../conf/models/"
    f"{runtime_parameters['model_config']}.yml"
)

SOURCE_TABLE = (
    f"{config['catalog']}."
    f"{config['schema']}."
    f"{config['source_table']}"
)

MODEL_NAME = (
    config["full_model_name"]
)

MLFLOW_TMP_DIR = (
    config["mlflow_volume"]
)

# Read Source Dataset

source_df = spark.table(
    SOURCE_TABLE
)

validate_training_input(
    source_df
)

delta_version = (
    get_latest_delta_version(
        spark,
        SOURCE_TABLE
    )
)

row_count = source_df.count()

prepared_df = prepare_training_data(
    source_df
)

# MLflow Run

with mlflow.start_run(
    run_name="rf_challenger_candidate"
):

    # Metadata

    mlflow.log_param(
        "environment",
        environment["environment"]
    )

    mlflow.log_param(
        "model_suffix",
        environment["model_suffix"]
    )

    mlflow.log_param(
        "runtime_model_config",
        runtime_parameters["model_config"]
    )

    mlflow.log_param(
        "model_role",
        "challenger_candidate"
    )

    mlflow.log_param(
        "source_table",
        SOURCE_TABLE
    )

    mlflow.log_param(
        "delta_version",
        delta_version
    )

    mlflow.log_param(
        "catalog",
        config["catalog"]
    )

    mlflow.log_param(
        "source_schema",
        config["schema"]
    )

    mlflow.log_param(
        "repository",
        "databricks-mlops-hands-on"
    )

    mlflow.log_param(
        "branch",
        "main"
    )

    mlflow.log_param(
        "algorithm",
        config["algorithm"]
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

    # Train

    model = train_model(
        prepared_df
    )

    predictions_df = (
        model.transform(
            prepared_df
        )
    )

    # Evaluate

    evaluation_metrics = (
        evaluate_model(
            predictions_df
        )
    )

    champion_run_id = (
        get_champion_run_id(
            MODEL_NAME
        )
    )

    champion_accuracy = (
        get_run_metric(
            champion_run_id,
            "accuracy"
        )
    )

    champion_comparison = (
        compare_to_champion(
            challenger_accuracy=
                evaluation_metrics["accuracy"],
            champion_accuracy=
                champion_accuracy
        )
    )

    promotion_recommendation = (
        get_promotion_recommendation(
            champion_comparison[
                "challenger_better"
            ]
        )
    )

    approval_status = (
        is_approved_for_promotion(
            promotion_recommendation
        )
    )

    promotion_passed = (
        passes_promotion_gate(
            evaluation_metrics
        )
    )

    mlflow.log_metric(
        "accuracy",
        evaluation_metrics["accuracy"]
    )

    mlflow.log_metric(
        "f1",
        evaluation_metrics["f1"]
    )

    mlflow.log_metric(
        "weighted_precision",
        evaluation_metrics[
            "weighted_precision"
        ]
    )

    mlflow.log_metric(
        "weighted_recall",
        evaluation_metrics[
            "weighted_recall"
        ]
    )

    mlflow.log_param(
        "promotion_recommendation",
        promotion_recommendation
    )

    mlflow.log_param(
        "promotion_passed",
        promotion_passed
    )

    mlflow.log_param(
        "champion_run_id",
        champion_run_id
    )

    mlflow.log_metric(
        "retrieved_champion_accuracy",
        champion_accuracy
    )

    mlflow.log_metric(
        "champion_accuracy",
        champion_comparison[
            "champion_accuracy"
        ]
    )

    mlflow.log_metric(
        "challenger_accuracy",
        champion_comparison[
            "challenger_accuracy"
        ]
    )

    mlflow.log_param(
        "challenger_better",
        champion_comparison[
            "challenger_better"
        ]
    )

    mlflow.log_param(
        "promotion_approved",
        approval_status
    )

    # Model Signature

    signature_input = (
        source_df
        .select(*feature_columns)
        .limit(10)
        .toPandas()
    )

    prediction_df = (
        predictions_df
        .select("prediction")
        .limit(10)
        .toPandas()
    )

    signature = infer_signature(
        signature_input,
        prediction_df
    )

    # Log Model

    mlflow.spark.log_model(
        spark_model=model,
        artifact_path="model",
        dfs_tmpdir=MLFLOW_TMP_DIR,
        signature=signature,
        input_example=signature_input
    )

    # Register Model

    run_id = mlflow.active_run().info.run_id

    model_uri = (
        f"runs:/{run_id}/model"
    )

    registration = mlflow.register_model(
        model_uri=model_uri,
        name=MODEL_NAME
    )

    print(
        f"Registered model version: "
        f"{registration.version}"
    )

    print(
        "Model successfully logged to MLflow."
    )