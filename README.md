# 🚀 Customer Churn Prediction & AI Strategic Dashboard
### TechSpire 2025 - Skilio SEA TechSkills Challenge

![Status](https://img.shields.io/badge/Status-Completed-success)
![Achievement](https://img.shields.io/badge/Achievement-TOP%207%20FINALIST-gold)
![Track](https://img.shields.io/badge/Track-AI%20%26%20Data%20Science-blueviolet)
![Stack](https://img.shields.io/badge/Stack-Python%20|%20XGBoost%20|%20LightGBM%20|%20Stacking-2ea44f)

---

## 🌟 Introduction

I am incredibly proud to share that this project helped me secure a spot as a **TOP 7 Finalist** in the AI & Data Science Track of the **TechSpire - Skilio SEA TechSkills Challenge 2025**.

The competition required us to solve a critical business problem: **Customer Churn**. However, looking back at the journey, I realized that winning wasn't just about having the highest accuracy score. It was about telling a story with data and bridging the gap between technical complexity and business strategy.

I created this repository to document that journey. It is organized not just as a "submission file," but as a guide for anyone starting their Machine Learning path. I want to show you how to go from raw, messy data to a high-performance **Stacking Ensemble** model, and finally, how to translate those predictions into actionable business insights.

---

## 💼 The Business Context: SkilioPay

**Scenario:** We are analyzing "SkilioPay," a fast-growing fintech platform in Southeast Asia.
**The Problem:** The platform is experiencing a churn rate of **~25%**. Users are silently leaving, taking their potential revenue with them.
**The Stakes:**
* **Revenue Exposure:** Based on the test data, we identified **SGD 129,311** at immediate risk.
* **The Goal:** Build a predictive system that acts as an "Early Warning System," allowing the Marketing team to intervene *before* the customer leaves.

---

## 🛠️ The Data Science Pipeline

The core logic of this project is broken down into 4 sequential notebooks. You can follow along in the `notebooks/` directory.

### 1. Exploratory Data Analysis (EDA)
*File: `notebooks/01_EDA.ipynb`*

Before modeling, we needed to diagnose the data.
* **Imbalance Check:** We confirmed a **75:25 ratio** (Non-Churn : Churn). This dictated our decision to use **Stratified Splitting** later on.
* **Behavioral Insight:** We discovered that **Inactivity (`days_since_last_order`)** was the "Silent Killer." Users don't just complain and leave; they simply stop buying first.
* **Data Quality:** Financial metrics (GMV) were heavily right-skewed, which required normalization.

### 2. Feature Engineering & Preprocessing
*File: `notebooks/02_FE_and_Preprocessing.ipynb`*

Raw data rarely works well in complex models.
* **Interaction Features:** I engineered features like `satisfaction_x_recency`. Logic: An unhappy user who is also inactive is far more dangerous than just an inactive one.
* **Outlier Handling:** Instead of deleting valuable "whale" customers (high spenders), I used **Winsorizing** (capping at the 99th percentile) to keep the data robust.
* **Smart Encoding:** High-cardinality features like `City` were handled using **Frequency Encoding** to preserve information density without exploding the dataset dimensions.

### 3. Advanced Modeling Strategy (Stacking)
*File: `notebooks/03_Training_and_Evaluation.ipynb`*

I avoided "black box" AutoML solutions and built a **Manual Stacking Ensemble**.
* **Base Learners:** I trained **XGBoost**, **LightGBM**, and **Logistic Regression** independently.
* **Meta-Learner:** Their predictions were fed into a final Logistic Regression model. This allows the system to learn *which model to trust* in different scenarios.
* **Threshold Optimization (Crucial Step):** instead of the default `0.5` threshold, I optimized the decision boundary to **0.62**. This maximizes **Precision**, ensuring we don't waste marketing budget on false alarms.

### 4. Final Evaluation
*File: `notebooks/04_Final_Evaluation.ipynb`*

We unlocked the **Test Set (20%)** to simulate real-world performance.
* **SHAP Analysis:** We used SHAP values to explain the "Why." It confirmed that Recency and Email Engagement are the top drivers of churn.
* **Calibration:** The model's probabilities are trustworthy (e.g., A "90% risk" prediction corresponds to a true 90% churn rate).

---

## 🚀 Going Beyond: The Executive Dashboard (Post-Competition Demo)

*Note: While the modeling notebooks are fully open-source, the Dashboard application (`app.py`) shown below was developed as a post-competition extension. I built this to demonstrate "Product Thinking"—showing how a raw machine learning model is transformed into a business decision support system. The source code for the app is not included in this repo, but the concept is vital for understanding the project's impact.*

A high-accuracy model is useless if it sits in a Jupyter Notebook. To solve the business problem truly, I designed a **Streamlit Dashboard** that translates technical probabilities into financial urgency.

### 🎥 Dashboard Demo

![Demo Preview](assets/demo.gif)

### 🧠 Design Philosophy & Business Features

The dashboard bridges the gap between **Data Science** (What will happen?) and **Business Strategy** (What should we do?).

#### 1. Quantifying Revenue Risk (Not Just Accuracy)
Data Scientists care about *F1-Scores*, but CEOs care about *Cash Flow*.
* **Feature:** The dashboard aggregates the predicted churners and calculates the **Total Revenue Exposure** (SGD 129,311 in the demo).
* **Impact:** This creates immediate urgency. It shifts the conversation from "Our model has 0.99 AUC" to "We are about to lose $129k this month if we don't act."

#### 2. Operational Triage (The Priority List)
Marketing teams cannot call 2,500 at-risk customers manually. They need to know who to save *first*.
* **Feature:** The "Priority Action List" ranks customers not just by Churn Probability (Risk), but effectively prioritizes high-value customers who are on the brink of leaving.
* **Impact:** Enables a **High-Touch Intervention** strategy for the top 20 VIPs, while relegating others to automated email campaigns.

#### 3. AI Chief Strategy Officer (Gemini Integration)
I integrated Google's **Gemini** via API to act as an intelligent logic layer on top of the dashboard data.

* **Context-Aware Analysis:** The AI doesn't just chat; it reads the aggregated metrics (e.g., *Avg Inactivity: 64 days*, *Avg CSAT: 4.3*).
* **Strategic Planning:** It generates structured retention plans. In the demo, the AI proposed a **"Three-Tiered Retention Strategy"**:
    * *Tier 1 (VIP):* Concierge outreach.
    * *Tier 2 (Mass):* Automated "Phoenix" campaign triggering at 58 days of inactivity.
    * *Tier 3 (Prevention):* Micro-surveys for users with dropping CSAT scores.
* **Strict Guardrails:** To ensure professional use, I programmed the System Prompt to **refuse off-topic queries**. If a user asks "What is the weather?", the AI replies: *"I am the SkilioPay Strategy Assistant... My capabilities are limited to analyzing churn data."*

---

## 📊 Key Results (Test Set)

The final Stacking Model achieved results that balance accuracy with business ROI:

| Metric | Score | Business Interpretation |
| :--- | :--- | :--- |
| **ROC AUC** | **0.99** | The model is exceptional at ranking customers from "Safe" to "Risky." |
| **F1-Macro** | **0.92** | Balanced performance across both Churners and Loyal users. |
| **Precision (Churn)**| **0.89** | **High Trust.** When the model flags a risk, it is right 89% of the time. |
| **Recall (Churn)** | **0.88** | **High Safety.** We successfully catch 88% of all potential revenue loss. |

---

## 📂 Project Structure

```bash
├── assets/                # Images & Demo GIF
├── data/                  # Data folder
│   ├── raw/               # Original dataset
│   └── processed/         # Scaled & Encoded artifacts
├── notebooks/             # The Core Logic
│   ├── 01_EDA.ipynb                   # Understanding the data
│   ├── 02_FE_and_Preprocessing.ipynb  # Cleaning & Engineering
│   ├── 03_Training_and_Evaluation.ipynb # Stacking & Tuning
│   └── 04_Final_Evaluation.ipynb      # Testing & Interpretability
├── outputs/               # Saved Models & Figures
│   ├── models/            # .joblib files (Champion Model)
│   └── reports/           # Generated charts
├── src/                   # Helper Scripts
│   ├── config.py          # Global configurations
│   └── feature_engineering.py # Reusable transformation logic
├── requirements.txt       # Dependencies
└── README.md              # Project Documentation
```

---

## ⚙️ How to Reproduce

This repository is designed for you to learn from the notebooks.

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/techspire-churn-prediction.git](https://github.com/yourusername/techspire-churn-prediction.git)
cd techspire-churn-prediction

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Notebooks:**
I recommend running them in order (01 to 04) to see how the data flows through the pipeline.
* Start with `notebooks/01_EDA.ipynb` to see the visualizations.
* Run `notebooks/03_Training_and_Evaluation.ipynb` to see the Stacking Ensemble in action.



---

## ❤️ Final Thoughts

Winning the Top 7 finalist spot was an amazing milestone, but organizing this code for the community is even more rewarding. I believe that a great Data Scientist isn't just a coder—they are a bridge between **Data** and **Decision**.

I hope this repository helps you understand Stacking Ensembles, Data Preprocessing, or simply how to structure a professional DS project.

**If you find this helpful, please give it a ⭐ Star!**

---

*Author: Huy Nguyen*
*TechSpire 2025 Finalist*