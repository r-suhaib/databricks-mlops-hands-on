from datetime import datetime


def generate_alerts(
    drift_results
):

    alerts = []

    for feature, result in drift_results.items():

        if result["drift_detected"]:

            alerts.append(
                {
                    "alert_timestamp":
                        datetime.utcnow(),
                    "feature_name":
                        feature,
                    "drift_percent":
                        result["drift_percent"],
                    "alert_type":
                        "DATA_DRIFT",
                    "alert_message":
                        f"Drift detected for "
                        f"{feature}"
                }
            )

    return alerts