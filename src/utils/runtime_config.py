import os


def get_runtime_parameters():

    return {
        "environment":
            os.getenv(
                "ENVIRONMENT",
                "dev"
            ),

        "model_config":
            os.getenv(
                "MODEL_CONFIG",
                "tep_fault_classifier"
            )
    }