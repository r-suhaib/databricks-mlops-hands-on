# Data Architecture

## Catalog

tep_anomaly

---

## Schemas

### source

Purpose:

Store raw immutable datasets.

Candidate Tables:

- faultfree_training
- faultfree_testing
- faulty_training
- faulty_testing

---

### calculated

Purpose:

Store intermediate transformed datasets.

Candidate Tables:

- sensor_windows
- sensor_statistics
- feature_generation_base
- anomaly_feature_dataset

---

### served

Purpose:

Store trusted business-ready datasets.

Candidate Tables:

- training_dataset
- batch_inference_dataset
- anomaly_predictions
- model_monitoring_metrics

---

## Data Flow

source
    ↓
calculated
    ↓
served
    ↓
training
    ↓
inference
    ↓
monitoring