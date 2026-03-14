# Gender Bias in Language Models for Mental Health Applications

This repository contains the code and data for a comparative analysis of gender biases in Masked Language Models (MLMs) and Generative Large Language Models (LLMs) applied to the mental health domain. The study evaluates models in both English and Spanish across different clinical phases (based on the HAPA model).

## Directory Structure

### 1. `MLMs bias detection/`

Evaluates gender token probability (mask filling) in general and clinical MLMs (based on BERT, RoBERTa and BETO).

* **`analysis/`**: Notebooks and heatmaps analyzing probability disparities and vocabulary.
* **`proper nouns/`**: Datasets and scripts for gendered proper nouns.
* **`results/`**: CSVs with raw token probabilities.
* **`src/`**: Source code for the MLM pipeline. Run with `python main.py`.

### 2. `LLMs bias detection/`

Evaluates zero-shot responses from LLMs using an LLM-as-a-Judge system.

* **`analysis/`**: Notebooks and heatmaps showing gender disparity.
* **`results/`**: CSVs with raw text and cleaned predictions.
* **`src/`**: Source code for generation and LLM-as-a-Judge classification. Run with `python main.py`.

---

I hope this guide has been helpful!