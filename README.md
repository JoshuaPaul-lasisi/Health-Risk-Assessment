# Health Risk Assessment Project

## Overview

This project predicts the 10-year risk of developing coronary heart disease (CHD) using demographic, lifestyle, and medical data. It involves data cleaning, exploratory data analysis, feature scaling, and evaluating various classification models. The Gradient Boosting Classifier was identified as the optimal model based on performance metrics.

## Features

- **Age**: The age of the individual.
- **Gender**: Gender of the individual.
- **BMI**: Body Mass Index.
- **Smoking Status**: Cigarettes per day.
- **Blood Pressure**: Systolic and Diastolic Blood Pressure.
- **Cholesterol Levels**: Total cholesterol levels.
- **Heart Rate**: Resting heart rate.
- **Glucose**: Blood glucose levels.
- **Education**: Level of education.
- **BPMeds**: Use of blood pressure medication.
- **TenYearCHD**: Target variable indicating whether the individual has a 10-year risk of CHD.

## Key Steps

1. **Data Cleaning**: Handling missing data and imputation.
2. **EDA**: Analyzing distributions, correlations, and feature relationships.
3. **Modeling**: Training and evaluating multiple classifiers.
4. **Model Comparison**: Visualizing performance metrics and selecting the best model.

## Results

The Gradient Boosting Classifier provided the best performance, with a high ROC AUC score, making it the most suitable model for predicting CHD risk.

## Installation

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/health-risk-assessment.git
cd health-risk-assessment
```

### 2. On your terminal

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

# Install deoendencies
pip install -r requirements.txt

# Run in this manner
python src/data_processing.py

python src/model_training.py

python src/flask_app.py

streamlit run src/streamlit_app.py
```