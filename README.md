# SkilioPay User Churn Prediction 

## 1. Project Overview

This project aims to predict customer churn for SkilioPay, an e-commerce platform. The goal is to build a robust and production-lean machine learning model that can accurately identify users at high risk of churning. By doing so, SkilioPay can implement targeted retention strategies to improve customer loyalty and maximize ROI. This solution was developed for the Techspire AI & Data Science Competition (Round 2).

**Key Achievements:**
*   **Final Model:** Stacking Ensemble (LightGBM, XGBoost, Logistic Regression)
*   **Test Set ROC AUC:** `[Điền kết quả cuối cùng, ví dụ: 0.985]`
*   **Test Set F1-Score (Macro):** `[Điền kết quả cuối cùng, ví dụ: 0.921]`

---

## 2. Project Structure

The project is organized into a modular structure to ensure clarity, reproducibility, and ease of maintenance.

```
.
├── data/
│   ├── raw/
│   │   └── dataset.csv       # Original, immutable data
│   └── processed/            # Processed data ready for modeling
├── notebooks/                # Jupyter notebooks for EDA and step-by-step execution
├── outputs/
│   ├── models/               # Trained models and evaluation metrics
│   └── reports/
│       └── figures/          # Generated plots and visualizations
├── src/
│   ├── config.py             # Central configuration file
│   └── feature_engineering.py# Reusable functions for feature creation
├── .gitignore
├── README.md                 # Project documentation (You are here)
└── requirements.txt          # Project dependencies
```

---

## 3. Reproduction Guide

To reproduce the results, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Set Up the Environment:** It is highly recommended to use a virtual environment to avoid conflicts with other projects.
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate

    # Install the required packages
    pip install -r requirements.txt
    ```

3.  **Run the Notebooks:** Execute the Jupyter notebooks in the `/notebooks` directory in the following order:
    *   `01_EDA.ipynb`: (Optional) For a detailed review of the exploratory data analysis.
    *   `02_FE_and_Preprocessing.ipynb`: Runs the feature engineering and data splitting pipeline. This will generate the necessary processed data in `data/processed/`.
    *   `03_Training_and_Evaluation.ipynb`: Trains the base models, performs hyperparameter tuning, builds the stacking ensemble, and saves the final champion model.
    *   `04_Final_Evaluation.ipynb`: Loads the champion model and generates the final evaluation metrics and artifacts on the hold-out test set. All outputs will be saved in the `outputs/` directory.

---

## 4. Data Leakage Prevention Strategy

To ensure the integrity and reliability of the model's performance, a strict data leakage prevention strategy was implemented:

-   **Train-Validation-Test Split:** The dataset is first split into a training/validation pool (80%) and a hold-out test set (20%). The test set is completely isolated and is only used for the final performance report. The 80% pool is then further split into a dedicated training set (~65%) and a validation set (~15%).

-   **Fit on Train, Transform on All:** All preprocessing steps (e.g., `StandardScaler`, frequency encoding maps) are **fit exclusively on the training set (~65%)**. The learned transformations are then consistently applied to the validation and test sets. This methodology simulates a real-world scenario where the model encounters new, unseen data.

-   **Purpose-Driven Data Sets:**
    -   **Training Set (~65%):** Used for training base models and performing hyperparameter search via cross-validation.
    -   **Validation Set (~15%):** Used for "meta" decisions that do not involve direct model training, such as selecting the optimal probability threshold and building the stacking ensemble's meta-learner.
    -   **Test Set (20%):** Used only once at the very end to provide an unbiased evaluation of the final, chosen model after it has been retrained on the full 80% training/validation pool.