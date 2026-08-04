from mlflow import MlflowClient


def assign_alias(
    model_name,
    alias,
    version
):

    client = MlflowClient()

    client.set_registered_model_alias(
        name=model_name,
        alias=alias,
        version=str(version)
    )