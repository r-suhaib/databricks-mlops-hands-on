from src.utils.config_loader import (
    load_config
)


def load_environment(
    environment_name
):

    return load_config(
        f"conf/environments/{environment_name}.yml"
    )