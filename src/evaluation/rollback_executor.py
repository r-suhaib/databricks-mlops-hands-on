from src.evaluation.alias_management import (
    assign_alias
)


def execute_rollback(
    model_name,
    rollback_version
):

    assign_alias(
        model_name=model_name,
        alias="Champion",
        version=rollback_version
    )

    return "ROLLBACK_EXECUTED"