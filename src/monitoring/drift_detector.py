def calculate_percentage_change(
    baseline_value,
    current_value
):

    if baseline_value == 0:
        return 0

    return (
        abs(
            current_value - baseline_value
        )
        / abs(baseline_value)
    ) * 100

def detect_mean_drift(
    baseline_stats,
    current_stats,
    threshold=20
):

    drift_results = {}

    for feature in baseline_stats:

        baseline_mean = (
            baseline_stats[feature]["mean"]
        )

        current_mean = (
            current_stats[feature]["mean"]
        )

        drift_pct = (
            calculate_percentage_change(
                baseline_mean,
                current_mean
            )
        )

        drift_results[feature] = {
            "drift_percent":
                drift_pct,
            "drift_detected":
                drift_pct > threshold
        }

    return drift_results