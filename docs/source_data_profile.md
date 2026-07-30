# Source Data Profile

## Source Tables

- faultfree_training
- faultfree_testing
- faulty_training
- faulty_testing

## Dataset Volumes

Fault Free Training: 250,000

Fault Free Testing: 480,000

Faulty Training: 5,000,000

Faulty Testing: 9,600,000

## Metadata Columns

- faultNumber
- simulationRun
- sample

## Process Measurements

41 columns:

xmeas_1 ... xmeas_41

## Manipulated Variables

11 columns:

xmv_1 ... xmv_11

## Key Findings

### Dataset Structure

- 500 simulation runs per dataset
- Training datasets contain 500 samples per simulation run
- Process data is ordered by sample number

### Fault Structure

- faultNumber = 0 represents normal operation
- faultNumber 1-20 represent fault conditions
- Fault datasets are balanced

### Time-Series Characteristics

simulationRun behaves as a process execution identifier.

sample behaves as an ordered time sequence within a simulation run.

This enables:

- lag features
- rolling statistics
- rate-of-change features

for downstream feature engineering.

### Initial Architecture Implication

Window-based feature engineering should occur in the Calculated layer rather than Source.