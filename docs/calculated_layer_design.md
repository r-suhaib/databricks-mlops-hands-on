# Calculated Layer Design

## Purpose

Store reusable intermediate datasets derived from Source tables.

Calculated datasets support feature engineering and downstream model workflows.

---

# Table: sensor_statistics

Purpose:

Store rolling and aggregated sensor statistics.

Examples:

- rolling mean
- rolling standard deviation
- rolling minimum
- rolling maximum

Input:

source tables

Consumers:

feature_generation_base

---

# Table: feature_generation_base

Purpose:

Store reusable engineered features.

Examples:

- lag features
- rolling features
- rate of change features

Input:

sensor_statistics

Consumers:

training datasets
inference datasets

---

# Design Principles

- Rebuildable from Source
- Reusable across workflows
- No model-specific logic
- No training labels
- No prediction outputs

---

# Data Flow

Source
    ↓
sensor_statistics
    ↓
feature_generation_base
    ↓
Served