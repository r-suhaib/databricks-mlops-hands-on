def compare_to_champion(
    challenger_accuracy: float,
    champion_accuracy: float
):

    return {
        "champion_accuracy": champion_accuracy,
        "challenger_accuracy": challenger_accuracy,
        "challenger_better":
            challenger_accuracy > champion_accuracy
    }