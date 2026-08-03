def compare_to_champion(
    challenger_accuracy: float,
    champion_accuracy: float | None
):

    if champion_accuracy is None:

        return {
            "champion_accuracy": None,
            "challenger_accuracy":
                challenger_accuracy,
            "challenger_better": None
        }

    return {
        "champion_accuracy":
            champion_accuracy,

        "challenger_accuracy":
            challenger_accuracy,

        "challenger_better":
            challenger_accuracy > champion_accuracy
    }