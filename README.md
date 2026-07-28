# databricks-mlops-hands-on
Enterprise MLOps project implementing the Databricks best-practices for MLOps using the Tennessee Eastman Process dataset.

# Databricks MLOps Hands-On

Enterprise MLOps project implementing modern Databricks best practices using the Tennessee Eastman Process (TEP) dataset.

---

## Project Goal

The purpose of this repository is to build an end-to-end machine learning platform that demonstrates:

- Data governance
- Reproducible model training
- Automated workflows
- Model lifecycle management
- CI/CD for machine learning
- Monitoring and observability
- Automated retraining

The focus of this project is MLOps architecture and operationalisation rather than model optimisation.

---

## Business Problem

The project uses industrial process telemetry from the Tennessee Eastman Process (TEP) dataset to build an anomaly detection platform.

The solution aims to support:

- Batch training
- Batch inference
- Monitoring
- Drift detection
- Retraining workflows
- Deployment automation

---

## High-Level Architecture

```text
Raw Sensor Data
        │
        ▼
     Source
        │
        ▼
   Calculated
        │
        ▼
     Served
        │
        ▼
 Training Workflow
        │
        ▼
      MLflow
        │
        ▼
 Model Registry
        │
        ▼
 Batch Inference
        │
        ▼
    Monitoring
        │
        ▼
   Retraining
```

---

## Repository Structure

```text
databricks-mlops-hands-on/
│
├── docs/
├── src/
├── tests/
├── pipelines/
├── conf/
├── databricks/
├── README.md
└── .gitignore
```

---

## Data Architecture

The project follows a layered data architecture:

### Source

Stores raw and immutable datasets.

Examples:

- Raw sensor telemetry
- Raw event information

### Calculated

Stores intermediate transformations and engineered features.

Examples:

- Rolling statistics
- Time-window aggregations
- Lag features

### Served

Stores curated datasets ready for training, inference, and monitoring.

Examples:

- Training datasets
- Prediction datasets
- Monitoring datasets

---

## Technology Stack

- Databricks
- Unity Catalog
- Delta Lake
- MLflow
- Databricks Workflows
- Databricks Asset Bundles
- GitHub
- GitHub Actions
- Python

---

## Current Status

### Phase 1: Architecture & Design

- [x] Repository created
- [x] Initial project structure created
- [x] Architecture mapping created
- [ ] Unity Catalog design
- [ ] Dataset onboarding
- [ ] Data quality framework
- [ ] Feature engineering pipeline
- [ ] Training workflow
- [ ] Model registry integration
- [ ] Monitoring framework
- [ ] Retraining workflow
- [ ] CI/CD implementation

---

## Learning Objective

By completing this project, the goal is to gain practical experience designing, implementing, deploying, monitoring, and maintaining enterprise machine learning systems using Databricks.