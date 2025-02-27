# Over 2.5 Goals Prediction

This repository contains a **machine learning project** that predicts whether the total number of goals in a football match will exceed **2.5 goals** using historical match data and statistical features.

## 📌 Project Overview
The goal of this project is to develop a predictive model that classifies football matches as:
- **Over 2.5 Goals** (total goals > 2.5)
- **Under 2.5 Goals** (total goals ≤ 2.5)

This can be useful for **sports analytics, betting strategies, and match outcome forecasting**.

## 📊 Features
- **Data Scraping & Merging**: Combining multiple datasets into one file
- **Data Processing**: Cleaning and transforming match data
- **Feature Engineering**: Creating statistical features (average goals, categorical encoding, etc.)
- **Model Training**: Using machine learning algorithms to classify matches
- **Performance Evaluation**: Analyzing model accuracy and metrics

## 🛠 Data Scraping & Merging
The dataset was created by merging multiple CSV files using the following approach:
```python
import pandas as pd
import glob

# List of CSV files
csv_files = ["G1 (7).csv", "G1 (6).csv", "G1 (5).csv", "G1 (4).csv",
             "G1 (3).csv", "G1 (2).csv", "G1 (1).csv", "G1.csv"]

# Read and combine all CSVs, keeping all columns
df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True, sort=False)

# Save the final merged file
df.to_csv("merged1.csv", index=False)
```

## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AngelosKontalis/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
1. Open the **Google Colab Notebook**: 
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](LINK_TO_YOUR_NOTEBOOK)
2. Run the notebook step by step to:
   - Load and preprocess data
   - Engineer new features
   - Train machine learning models
   - Evaluate predictions

## 📂 Dataset
- The dataset (`merged1.csv`) contains historical football match results with:
  - **Date** of match
  - **Home/Away Teams** (encoded as categorical variables)
  - **Full-time goals** for home and away teams
  - **Average historical goals per team**
  - **Day of the week** (encoded)
  - **Target variable**: `1` if total goals > 2.5, else `0`

## 📈 Model & Results
The notebook explores different machine learning models, such as:
- Logistic Regression
- Decision Trees
- Random Forest
- XGBoost

The performance is evaluated using **accuracy, precision, recall, and ROC curves**.

## 📜 License
This project is open-source and available under the [MIT License](LICENSE). Contributions and modifications are welcome!

