# Source Ingestion Strategy

## Physical Storage

Catalog:
tep_anomaly

Schema:
source

Volume:
raw_files

Purpose:

Store raw source files exactly as received from the source system.

---

## Source Files

- TEP_FaultFree_Training.RData
- TEP_FaultFree_Testing.RData
- TEP_Faulty_Training.RData
- TEP_Faulty_Testing.RData

---

## Ingestion Principles

- Preserve original files
- Preserve source lineage
- No transformations during storage
- No feature engineering during ingestion

---

## Target Source Tables

- faultfree_training
- faultfree_testing
- faulty_training
- faulty_testing

---

## Data Flow

Raw Files
    ↓
Volume Storage
    ↓
Source Tables
    ↓
Calculated Layer
    ↓
Served Layer