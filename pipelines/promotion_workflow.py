from src.evaluation.promotion_executor import (
    execute_promotion
)

MODEL_NAME = (
    "tep_anomaly.served.tep_fault_classifier"
)

CANDIDATE_VERSION = 12

APPROVED = False

result = execute_promotion(
    model_name=MODEL_NAME,
    candidate_version=CANDIDATE_VERSION,
    approved=APPROVED
)

print(result)