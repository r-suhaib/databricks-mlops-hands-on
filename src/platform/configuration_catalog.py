from pyspark.sql import Row


def create_configuration_record():

    return [
        Row(
            model_name="tep_fault_classifier",
            config_file="conf/models/tep_fault_classifier.yml",
            source_table="tep_anomaly.served.training_base",
            registry_model="tep_anomaly.served.tep_fault_classifier",
            environment="dev",
            schedule="Daily",
            active_flag=True
        )
    ]