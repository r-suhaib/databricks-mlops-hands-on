from mlflow import MlflowClient


def get_champion_run_id(
    model_name: str
):

    client = MlflowClient()

    champion = client.get_model_version_by_alias(
        model_name,
        "Champion"
    )

    return champion.run_id

def get_run_metric(
    run_id: str,
    metric_name: str
):

    client = MlflowClient()

    run = client.get_run(run_id)

    metric =  run.data.metrics.get(
        metric_name
    )

    return metric