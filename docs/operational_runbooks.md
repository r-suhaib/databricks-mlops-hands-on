## Training Failure Runbook

Symptoms:
Training workflow fails

Checks:
1. Training dataset exists
2. Contract validation passed
3. MLflow experiment available
4. Volume accessible

Recovery:
Re-run workflow after correction

## Promotion Failure Runbook

Symptoms:
Promotion workflow fails

Checks:
1. Recommendation exists
2. Approval exists
3. Registry accessible
4. Model version exists

Recovery:
Retry promotion workflow

## Rollback Failure Runbook

Symptoms:
Rollback workflow fails

Checks:
1. Rollback version exists
2. Alias permissions exist
3. Registry available

Recovery:
Manually update Champion alias

## Drift Alert Runbook

Symptoms:
Data drift alert

Checks:
1. Source data changes
2. Feature distribution changes
3. Upstream system changes

Recovery:
Investigate
Validate
Retrain if required