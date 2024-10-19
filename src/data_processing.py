# Imports
import pandas as pd
import numpy as np

# Set pandas options to manage future warnings about downcasting
pd.set_option('future.no_silent_downcasting', True)

# Loading the data
health = pd.read_csv('../data/raw/framingham.csv')
health.head()

# Express the missing values as percentages
missing_values = health.isna().mean() *100

# Reduce it to only columns with missing values
missing_values = missing_values[missing_values > 0]
missing_values

# List of columns to impute with the median
median_columns = ['cigsPerDay', 'totChol', 'BMI', 'heartRate', 'glucose']

# Impute missing values with the median for each column
for column in median_columns:
    health[column] = health[column].fillna(health[column].median())

# List of columns to impute with the median
mode_columns = ['education', 'BPMeds']

# Impute missing values with the median for each column
for column in mode_columns:
    health[column] = health[column].fillna(health[column].mode()[0])

# Check if any missing values are left
remaining_missing_values = health.isna().sum()
print("Remaining missing values after imputation:", remaining_missing_values[remaining_missing_values > 0])

# Save the processed data to the ../data/processed folder
processed_file_path = '../data/processed/framingham_processed.csv'
health.to_csv(processed_file_path, index=False)

print(f"Processed data saved to {processed_file_path}")