def passes_promotion_gate(
    metrics: dict,
    minimum_accuracy: float = 0.50
) -> bool:

    return (
        metrics["accuracy"]
        >= minimum_accuracy
    )