# Databricks MLOps Architecture Mapping

## Project Overview

### Project Name

Databricks MLOps: TEP Industrial Process Anomaly Detection Platform

### Objective

Build an enterprise-grade machine learning platform for industrial process anomaly detection using the Tennessee Eastman Process (TEP) dataset.

The primary objective is to implement modern Databricks MLOps best practices, including data governance, feature management, experiment tracking, automated workflows, deployment automation, monitoring, and retraining.

### Business Problem

Detect abnormal process behaviour from industrial sensor telemetry.

The platform should support:

- Reproducible model training
- Automated batch inference
- Monitoring and observability
- Controlled model lifecycle management
- Automated retraining
- End-to-end deployment automation

---

# Architecture Principles

## Principle 1: Data as a Product

Data assets are treated as governed products with clear ownership, lineage, and quality standards.

## Principle 2: Reproducibility

Every model must be reproducible from source data, code, configuration, and workflow definitions.

## Principle 3: Automation First

Training, validation, deployment, monitoring, and retraining should be automated wherever possible.

## Principle 4: Code Promotion

Environments are promoted through version-controlled code and configuration rather than manually moving artifacts.

## Principle 5: Observability

Data pipelines, models, features, and inference processes must be observable and measurable.

---

# Data Architecture

## Source Layer

### Purpose

Store raw, immutable datasets.

### Contents

- Raw TEP sensor telemetry
- Raw fault event information
- Raw metadata files

### Characteristics

- No feature engineering
- No business logic
- Immutable history
- Acts as system of record

---

## Calculated Layer

### Purpose

Store intermediate transformed datasets.

### Contents

- Rolling window calculations
- Aggregated metrics
- Time-series transformations
- Lag features
- Derived statistical features

### Characteristics

- Rebuildable from Source
- Intermediate processing layer
- Supports downstream feature engineering

---

## Served Layer

### Purpose

Store business-ready and ML-ready datasets.

### Contents

- Training datasets
- Inference datasets
- Prediction outputs
- Monitoring datasets

### Characteristics

- Stable interfaces
- Trusted data products
- Consumed by ML workflows

---

# Catalog Strategy

## Catalog

tep_anomaly

## Schemas

### source

Stores raw data assets.

### calculated

Stores transformed and intermediate datasets.

### served

Stores curated datasets used by training, inference, and monitoring processes.

---

# Feature Strategy

## Feature Objectives

Features should be:

- Reusable
- Versioned
- Traceable
- Reproducible

## Candidate Features

- Rolling mean
- Rolling standard deviation
- Rolling minimum
- Rolling maximum
- Rate of change
- Lag features
- Delta from baseline
- Window statistics

## Feature Ownership

Features are owned by the project and managed through version-controlled pipelines.

---

# Model Lifecycle

## Training Workflow

1. Validate input data
2. Generate features
3. Build training dataset
4. Train model
5. Evaluate model
6. Register model
7. Store model artifacts

## Initial Model

Isolation Forest

The model is intentionally simple so that effort remains focused on MLOps architecture rather than model optimisation.

---

# Batch Inference Workflow

1. Load latest served data
2. Generate feature set
3. Load registered model
4. Generate anomaly predictions
5. Store predictions
6. Publish monitoring metrics

---

# Monitoring Strategy

## Data Monitoring

Monitor:

- Missing values
- Schema changes
- Volume changes
- Distribution drift

## Feature Monitoring

Monitor:

- Feature drift
- Feature statistics
- Null rates

## Model Monitoring

Monitor:

- Prediction distributions
- Anomaly rate trends
- Training performance
- Inference performance

## Operational Monitoring

Monitor:

- Job failures
- Workflow execution times
- Pipeline health
- Deployment status

---

# Retraining Strategy

Retraining may be triggered by:

- Scheduled retraining windows
- Significant data drift
- Significant feature drift
- Performance degradation

Retraining workflows should be fully automated and reproducible.

---

# CI/CD Strategy

## Source Control

GitHub

## Development Workflow

Feature Branch
→ Pull Request
→ Automated Validation
→ Merge
→ Deployment

## Deployment Strategy

Deploy through version-controlled configuration and infrastructure definitions.

---

# Environments

## Development

Used for experimentation and feature development.

## Test

Used for validation and integration testing.

## Production

Used for approved and monitored operational workloads.

Each environment should be independently deployable from source-controlled assets.

---

# Success Criteria

The project demonstrates:

- Governed data architecture
- Reproducible training workflows
- Automated deployment workflows
- Model lifecycle management
- Monitoring and observability
- Retraining capability
- Enterprise-grade MLOps practices using Databricks