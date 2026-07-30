# Data Contracts

## Purpose

Define the minimum quality, schema, and governance expectations for data entering the platform.

The Source layer acts as the system of record and preserves original dataset lineage.

---

# Source Layer

The Tennessee Eastman Process dataset is onboarded as four independent source assets.

These assets are preserved separately to maintain lineage and traceability back to the original dataset distribution.

---

## Table

faultfree_training

### Purpose

Store fault-free training telemetry from the original source dataset.

### Required Columns

- faultNumber
- simulationRun
- sample

### Sensor Measurements

- xmeas_1 ... xmeas_41

### Manipulated Variables

- xmv_1 ... xmv_11

### Expected Rules

- faultNumber must not be null
- simulationRun must not be null
- sample must not be null

### Data Owner

TEP ML Platform Team

---

## Table

faultfree_testing

### Purpose

Store fault-free testing telemetry from the original source dataset.

### Required Columns

- faultNumber
- simulationRun
- sample

### Sensor Measurements

- xmeas_1 ... xmeas_41

### Manipulated Variables

- xmv_1 ... xmv_11

### Expected Rules

- faultNumber must not be null
- simulationRun must not be null
- sample must not be null

### Data Owner

TEP ML Platform Team

---

## Table

faulty_training

### Purpose

Store faulty training telemetry from the original source dataset.

### Required Columns

- faultNumber
- simulationRun
- sample

### Sensor Measurements

- xmeas_1 ... xmeas_41

### Manipulated Variables

- xmv_1 ... xmv_11

### Expected Rules

- faultNumber must not be null
- simulationRun must not be null
- sample must not be null

### Data Owner

TEP ML Platform Team

---

## Table

faulty_testing

### Purpose

Store faulty testing telemetry from the original source dataset.

### Required Columns

- faultNumber
- simulationRun
- sample

### Sensor Measurements

- xmeas_1 ... xmeas_41

### Manipulated Variables

- xmv_1 ... xmv_11

### Expected Rules

- faultNumber must not be null
- simulationRun must not be null
- sample must not be null

### Data Owner

TEP ML Platform Team

---

# Common Dataset Schema

## Metadata Columns

### faultNumber

Represents the process fault identifier.

### simulationRun

Represents the simulation execution identifier.

### sample

Represents the sample sequence number within a simulation run.

---

## Process Measurements

41 continuous process measurements.

Columns:

- xmeas_1
- xmeas_2
- ...
- xmeas_41

---

## Manipulated Variables

11 control variables.

Columns:

- xmv_1
- xmv_2
- ...
- xmv_11

---

# Data Quality Principles

All Source datasets must satisfy:

- Required columns present
- Expected schema maintained
- Column types remain consistent
- Source lineage preserved
- Raw values remain unmodified
- Ingestion is reproducible

---

# Pipeline Failure Conditions

Source ingestion must fail when:

- Required columns are missing
- Schema changes unexpectedly
- Critical identifier fields are null
- Dataset cannot be traced back to an original source asset

---

# Lineage Principles

Original source assets must remain independently identifiable.

The following lineage must be preserved:

faultfree_training
    ↓
calculated datasets
    ↓
served datasets

faultfree_testing
    ↓
calculated datasets
    ↓
served datasets

faulty_training
    ↓
calculated datasets
    ↓
served datasets

faulty_testing
    ↓
calculated datasets
    ↓
served datasets

Source assets must never be merged directly during ingestion.
Any consolidation occurs in downstream Calculated layer transformations.