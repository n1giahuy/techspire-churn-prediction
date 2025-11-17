# SkilioPay User Churn Prediction - Project Submission

## 1. Project Overview

This project tackles the critical business challenge of customer churn for SkilioPay, an e-commerce platform. The core objective was to develop a robust, production-lean machine learning model capable of accurately identifying users at high risk of churning. By leveraging data-driven insights, this model serves as the foundation for targeted retention strategies, aiming to enhance customer loyalty and maximize business ROI.

This repository contains the complete solution developed for the Techspire AI & Data Science Competition (Round 1).

### Key Achievements

*   **Final Model:** A Stacking Ensemble model, intelligently combining the strengths of LightGBM, XGBoost, and Logistic Regression.
*   **ROC AUC (Test Set):** **0.986** — Demonstrating outstanding capability in distinguishing between churning and non-churning users.
*   **F1-Score (Macro, Test Set):** **0.922** — Highlighting a strong, balanced performance in identifying both user classes, which is crucial for the imbalanced nature of the dataset.

---

## 2. Project Structure

The project follows a modular and organized structure to ensure clarity, reproducibility, and ease of maintenance, adhering to best practices in data science project management.

```
.
├── data/
│   ├── raw/
│   │   └── dataset.csv       # Original, immutable data provided for the competition.
│   └── processed/            # Cleaned, transformed, and feature-engineered data ready for modeling.
├── notebooks/                # Jupyter Notebooks that walk through the entire process.
│   ├── 01_EDA.ipynb
│   ├── 02_FE_and_Preprocessing.ipynb
│   ├── 03_Training_and_Evaluation.ipynb
│   └── 04_Final_Evaluation.ipynb
├── outputs/
│   ├── models/               # Contains the final trained model artifact ('champion_model.joblib').
│   └── reports/
│       └── figures/          # All generated plots and visualizations from the analysis.
├── src/
│   ├── config.py             # A centralized configuration file for all paths, parameters, and settings.
│   └── feature_engineering.py# A module with reusable functions for all feature creation steps.
├── .gitignore
├── README.md                 # Project documentation (this file).
└── requirements.txt          # A list of all project dependencies for easy environment recreation.
```

---

## 3. How to Reproduce the Results

To replicate the project and its results, please follow the steps below.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/n1giahuy/Vietnam_NguyenLamGiaHuy_ADS.git
    cd Vietnam_NguyenLamGiaHuy_ADS
    ```

2.  **Set Up the Python Environment:** Using a virtual environment is strongly recommended.
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate

    # Install all required libraries
    pip install -r requirements.txt
    ```

3.  **Run the Jupyter Notebooks:** For a complete walkthrough and to regenerate all artifacts, execute the notebooks located in the `/notebooks` directory in sequential order:
    *   **`01_EDA.ipynb`**: (Optional) Provides a comprehensive exploratory data analysis of the raw dataset.
    *   **`02_FE_and_Preprocessing.ipynb`**: The core data pipeline. It handles feature engineering, data splitting, and preprocessing, saving the final datasets to `data/processed/`.
    *   **`03_Training_and_Evaluation.ipynb`**: This notebook trains the base models, performs hyperparameter tuning, builds the champion Stacking ensemble, and finds the optimal decision threshold.
    *   **`04_Final_Evaluation.ipynb`**: Loads the champion model, retrains it on the full training data, and generates the final, unbiased performance evaluation on the hold-out test set.

---

## 4. Methodological Rigor: Data Leakage Prevention

To ensure the model's evaluation is unbiased and reflects real-world performance, a strict methodology was employed to prevent data leakage at every stage.

-   **Dedicated Data Sets:** The data was rigorously split into three distinct sets: a **Training Set (~65%)**, a **Validation Set (~15%)**, and a **Test Set (20%)**. The Test Set was completely isolated and was only accessed a single time for the final report.

-   **Correct Preprocessing Sequence:** All preprocessing objects (like `StandardScaler` for scaling or frequency maps for encoding) were **fit exclusively on the Training Set**. These trained objects were then used to **transform** the Training, Validation, and Test sets consistently. This approach correctly simulates a production environment where the model must process new, unseen data.

-   **Purpose-Driven Workflow:**
    -   The **Training Set** was used to train the base models and perform hyperparameter tuning via cross-validation.
    -   The **Validation Set** served as an independent "playground" for meta-decisions, including building the Stacking model's meta-learner and, crucially, determining the optimal probability threshold to maximize the F1-score.
    -   The **Test Set** was the final, untouched benchmark to provide an honest evaluation of the fully-trained champion model.