# Data Contracts

## Source Layer

### Table

raw_sensor_telemetry

### Purpose

Store raw immutable sensor telemetry records.

### Contract

Required Columns:

- timestamp
- sensor_id
- sensor_value

Expected Rules:

- timestamp must not be null
- sensor_id must not be null
- sensor_value must not be null

Accepted Behaviour:

- duplicate records allowed for investigation
- no feature engineering applied

Data Owner:

TEP ML Team

---

### Table

raw_fault_events

### Purpose

Store known fault and event information.

### Contract

Required Columns:

- event_id
- event_timestamp

Expected Rules:

- event_id must not be null
- event_timestamp must not be null

Data Owner:

TEP ML Team

---

## Data Quality Principles

All source data should satisfy:

- Required fields populated
- Schema consistency
- Type consistency
- Ingestion traceability
- Reproducibility

---

## Pipeline Failure Conditions

Source ingestion should fail when:

- Required columns are missing
- Critical fields contain null values
- Schema changes unexpectedly