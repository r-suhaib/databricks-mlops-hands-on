from pyspark.sql import Row


def create_ownership_record():

    return [
        Row(
            model_name="tep_fault_classifier",
            technical_owner="Suhaibur Rehman",
            business_owner="Operations",
            platform_owner="MLOps Platform Team",
            support_group="Process Monitoring",
            escalation_contact="operations@company.com",
            active_flag=True
        )
    ]