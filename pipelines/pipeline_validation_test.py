from mlflow import MlflowClient

client = MlflowClient()

champion = client.get_model_version_by_alias(
    "tep_anomaly.served.tep_fault_classifier",
    "Champion"
)

print(champion.version)