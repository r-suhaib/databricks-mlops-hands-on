from pyspark.sql import Row
from datetime import datetime


def build_kpi_records(
    total_models,
    active_models,
    monitoring_alerts
):

    now = datetime.utcnow()

    return [

        Row(
            kpi_timestamp=now,
            metric_name="total_models",
            metric_value=float(total_models)
        ),

        Row(
            kpi_timestamp=now,
            metric_name="active_models",
            metric_value=float(active_models)
        ),

        Row(
            kpi_timestamp=now,
            metric_name="monitoring_alerts",
            metric_value=float(monitoring_alerts)
        )
    ]
