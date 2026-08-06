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


def get_model_version(
    model_name,
    alias
):

    client = MlflowClient()

    model = client.get_model_version_by_alias(
        model_name,
        alias
    )

    return model.version
