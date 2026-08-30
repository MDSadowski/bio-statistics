# bio-statistics

Small statistical tools for biological datasets, written to run on
**desktop Python** and a **Casio fx-CG50**.

This repository is part of training in statistics and bioinformatics
for environmental-health research, including work on endocrine-disrupting
chemicals and reproductive-health outcomes.

## Why this exists

Research work starts with very small, checkable calculations:
sample size, range, mean, and spread. This program practises those
operations in a form that can be used at a desk or on a calculator.

## Features

- Interactive menu
- One-sample descriptive statistics
- Two-sample comparison, including mean difference
- Value-by-value entry, with back and forward editing
- Results stay on screen until EXE / Enter

Statistics reported:

- n
- min
- max
- mean
- sample standard deviation

The Casio version also prints variance in spirit through SD;
the current script reports n, min, max, mean, and SD.

## Repository layout

```text
bio-statistics/
├── Casio/biostats.py      # MicroPython for fx-CG50
├── Desktop/biostats.py    # desktop Python
├── README.md
├── requirements.txt
└── LICENSE