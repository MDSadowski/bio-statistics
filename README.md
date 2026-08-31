# bio-statistics

**Descriptive and clinical statistics for small biological datasets.**  

Desktop Python and Casio fx-CG50 MicroPython.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Casio](https://img.shields.io/badge/Casio-fx--CG50-black)](https://github.com/MDSadowski/bio-statistics)
[![Deps](https://img.shields.io/badge/dependencies-none-success)](requirements.txt)

A compact toolkit for checking biological measurements by hand: sample summaries, two-group comparisons, paired differences, proportions, diagnostic 2×2 measures, and cutoff checks. The same menu style runs on a PC and on a graphing calculator.

This project is training material for statistics and bioinformatics, written to support work in environmental health, endocrine-disrupting chemicals, and reproducible quantitative research.

---

**## Contents**

- [Why this exists](#why-this-exists)
- [Programs](#programs)
- [Repository layout](#repository-layout)
- [Interface](#interface)
- [Statistics provided](#statistics-provided)
- [Run on Windows](#run-on-windows)
- [Run on Casio fx-CG50](#run-on-casio-fx-cg50)
- [Installation](#installation)
- [Limits](#limits)
- [Example uses](#example-uses)
- [Author](#author)

---

**## Why this exists**

Research analysis starts with small, inspectable numbers: how many observations, where the centre sits, how wide the spread is, and whether two groups differ. These programs make those checks available without libraries, notebooks, or a lab PC.

The Casio versions keep every on-screen line to **21 characters**, so results remain readable on the fx-CG50.

---

**## Programs**

| File | Role | Modes |
|---|---|---|
| `biostats.py` | Version 1. Core summaries | One-sample stats, two-sample mean difference, help |
| `biostat2.py` | Clinical extras | Descriptive, group compare, paired difference, proportion, 2×2 test, cutoff, help |

`biostats.py` is the finished starter tool.  
`biostat2.py` is the wider clinical set.

---


**## Installation**

**Run on Windows**

No packages to install.
PowerShellCopypy Desktop\biostats.py
py Desktop\biostat2.py
If python is not recognised, use py.

**Run on Casio fx-CG50**

Connect the calculator by USB and choose USB Flash.
Copy the Casio script into the calculator root.
Name the file without a hyphen:
biostats.py
biostat2.py

Eject the drive on Windows before unplugging.
Open Python → FILES and press EXE.

Official Casio Python cannot bind raw keys such as EXIT. The scripts therefore read the characters produced by -, +, *, /, and a blank EXE.


**## Limits**

A summary is refused when fewer than two values are entered, except cutoff check.
These programs do not compute p-values.
Wald intervals are a teaching approximation and are weak for small n or extreme proportions.
Two-sample t assumes equal variances.
If a 2×2 denominator is 0, that measure is reported as 0.
This is a field-check and training tool, not a substitute for a full analysis in R, Python scientific stacks, or validated clinical software.


## Example uses

Summarise a short list of metabolite or hormone values
Compare two small exposure or control groups
Enter before/after differences
Check a positivity rate and a rough confidence interval
Convert a 2×2 table into sensitivity, specificity, PPV and NPV
Count how many measurements exceed a reference cutoff

For file-based analysis with public datasets, plots, and a written methods note, use a separate repository. This repo is the calculator-and-desktop toolkit.


## Author

**Michael D. Sadowski**.
Independent researcher, applied statistics, bioinformatics, public-health data.

GitHub: [**MDSadowski**](https://github.com/MDSadowski/)
ORCID: [**0009-0008-2316-3300**](https://orcid.org/0009-0008-2316-3300/)
Site: [**sadowski.ju.mp**](https://sadowski.ju.mp/)

License: [**CC0 1.0**](https://creativecommons.org/publicdomain/zero/1.0/)
