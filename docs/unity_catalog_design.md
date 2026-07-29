# Unity Catalog Design

## Catalog

tep_anomaly

Purpose:

Contains all data assets for the TEP anomaly detection platform.

---

## Schemas

### source

Stores raw immutable datasets.

Tables:

- raw_sensor_telemetry
- raw_fault_events
- raw_dataset_metadata

---

### calculated

Stores intermediate transformations.

Tables:

- sensor_statistics
- feature_generation_base
- anomaly_feature_dataset

---

### served

Stores trusted datasets used by ML workflows.

Tables:

- training_dataset
- batch_inference_dataset
- anomaly_predictions
- model_monitoring_metrics

---

## Naming Standards

Table names must:

- Use snake_case
- Be descriptive
- Represent business meaning
- Avoid abbreviations where possible

---

## Ownership

Catalog Owner:
TEP Platform Team

Data Owner:
TEP ML Team

Pipeline Owner:
TEP ML Team

---

## Future Environments

- dev
- test
- prod