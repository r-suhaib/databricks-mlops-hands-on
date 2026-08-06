from src.evaluation.alias_management import (
    assign_alias
)


def execute_promotion(
    model_name,
    candidate_version,
    approved
):

    if not approved:

        return (
            "PROMOTION_SKIPPED"
        )

    assign_alias(
        model_name=model_name,
        alias="Champion",
        version=candidate_version
    )

    return (
        "PROMOTION_EXECUTED"
    )