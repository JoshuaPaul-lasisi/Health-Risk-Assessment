import pandas as pd
import numpy as np

def load_data(file_path):
    # Load the dataset
    health = pd.read_csv(file_path)
    return health

def clean_data(df):
    # Fill missing values with the mean of each column
    df['education'].fillna(df['education'].mean(), inplace=True)
    df['cigsPerDay'].fillna(df['cigsPerDay'].mean(), inplace=True)
    df['BPMeds'].fillna(df['BPMeds'].mean(), inplace=True)
    df['totChol'].fillna(df['totChol'].mean(), inplace=True)
    df['BMI'].fillna(df['BMI'].mean(), inplace=True)
    df['heartRate'].fillna(df['heartRate'].mean(), inplace=True)
    df['glucose'].fillna(df['glucose'].mean(), inplace=True)
    return df

def feature_engineering(df):
    # Create any new features if necessary
    df['age_bins'] = pd.cut(df['age'], bins=[30, 40, 50, 60, 70], labels=[1, 2, 3, 4])
    return df

def preprocess_data(file_path):
    df = load_data(file_path)
    df_clean = clean_data(df)
    df_final = feature_engineering(df_clean)
    return df_final

if __name__ == "__main__":
    data = preprocess_data("../data/raw/framingham.csv")
    data.to_csv("../data/processed/health_clean.csv", index=False)
