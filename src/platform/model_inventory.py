from pyspark.sql import Row


def create_inventory_record():

    return [
        Row(
            model_name="tep_fault_classifier",
            business_domain="Process Monitoring",
            technical_owner="Suhaibur Rehman",
            business_owner="Operations",
            model_tier="Tier 2",
            source_table="tep_anomaly.served.training_base",
            registry_model="tep_anomaly.served.tep_fault_classifier",
            schedule="Daily",
            active_flag=True
        )
    ]