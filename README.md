# Over 2.5 Goals Prediction

This repository contains a **machine learning project** that predicts whether the total number of goals in a football match will exceed **2.5 goals** using historical match data and statistical features.

## 📌 Project Overview
The goal of this project is to develop a predictive model that classifies football matches as:
- **Over 2.5 Goals** (total goals > 2.5)
- **Under 2.5 Goals** (total goals ≤ 2.5)

This can be useful for **sports analytics, betting strategies, and match outcome forecasting**.

## 📊 Features
- **Data Scraping**: Scraping soccer data from the web
- **Data Processing**: Cleaning and transforming match data
- **Feature Engineering**: Creating statistical features (average goals, categorical encoding, etc.)
- **Model Training**: Using machine learning algorithms to classify matches
- **Performance Evaluation**: Analyzing model accuracy and metrics

## 🛠 Data Scraping & Merging

The Python program uses Selenium to scrape data from a webpage containing information about football matches in the Super League Greece. The goal is to extract match details (e.g., week, date, time, home team, score, and away team) and save the data into a CSV file for further analysis. Throughout the execution, the program prints status messages indicating whether the page loaded successfully, how many tables were found, whether the correct table was located, and if the CSV file was saved successfully.

## 🛠 Installation
1. Clone the repository:

   git clone https://github.com/AngelosKontalis/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME

## 🚀 Usage
1. Open the **Google Colab Notebook**: 
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]
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
This project is open-source and available under the [MIT License]. Contributions and modifications are welcome!

