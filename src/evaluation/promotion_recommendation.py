def get_promotion_recommendation(
    challenger_better: bool
):

    if challenger_better:

        return "PROMOTE"

    return "RETAIN_CHAMPION"