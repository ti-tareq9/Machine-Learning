# ML Prerequisites and Algorithms

Author: **Tohidul Islam Tareq**

This repository contains clean, runnable Jupyter notebooks for machine learning prerequisites and classical ML algorithms. The notebooks are organized for CV/GitHub portfolio use.

## Repository Structure

```text
ml-prerequisites-and-algorithms/
├── notebooks/
│   ├── 01_prerequisites/
│   └── 02_ml_algorithms/
├── src/
│   └── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Notebook Topics

### Prerequisites
- Activation functions
- Loss functions
- Bias-variance tradeoff
- Training vs test error
- Imputing missing values
- Outlier handling
- Imbalanced data
- ROC curve

### ML Algorithms
- Binary classification with breast cancer data
- K-Means clustering with Iris data
- KNN classification with Iris data
- L1 and L2 regression
- LDA and QDA
- Linear and logistic regression introduction
- Logistic regression
- Multiclass classification
- Multiclass logistic regression
- Polynomial regression

## How to Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open any notebook from the `notebooks/` folder and run all cells.

## Notes

- All notebooks include the author name: **Tohidul Islam Tareq**.
- External missing file dependencies were removed.
- The examples use built-in or generated datasets so they can run reliably.
