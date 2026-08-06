from src.evaluation.rollback_executor import (
    execute_rollback
)

MODEL_NAME = (
    "tep_anomaly.served.tep_fault_classifier"
)

ROLLBACK_VERSION = 11

result = execute_rollback(
    model_name=MODEL_NAME,
    rollback_version=ROLLBACK_VERSION
)

print(result)