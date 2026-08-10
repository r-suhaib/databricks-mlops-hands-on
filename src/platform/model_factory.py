from pathlib import Path


def discover_model_configs():

    config_dir = Path(
        "conf/models"
    )

    return sorted(
        [
            file.name
            for file in config_dir.glob(
                "*.yml"
            )
        ]
    )