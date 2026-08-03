## Configuration File:
conf/training_config.yml

## Consumed By:
training_pipeline.py

## Parameters:

catalog
schema
source_table
model_name
full_model_name
mlflow_volume

## Purpose:

Decouple model-specific values
from reusable pipeline logic.