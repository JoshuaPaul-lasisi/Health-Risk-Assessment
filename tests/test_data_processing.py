import unittest
import pandas as pd
from src.data_processing import load_data, clean_data, feature_engineering

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Sample data to use in tests
        data = {
            'age': [35, 45, 55],
            'education': [1, 2, None],
            'cigsPerDay': [10, None, 20],
            'BPMeds': [None, 0, 1],
            'totChol': [200, None, 180],
            'BMI': [22.0, None, 27.5],
            'heartRate': [72, None, 65],
            'glucose': [85, 105, None]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        df = load_data("../data/raw/framingham.csv")
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        # Check if no missing values are present after cleaning
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_feature_engineering(self):
        engineered_df = feature_engineering(self.df)
        # Check if the age_bins feature has been added
        self.assertIn('age_bins', engineered_df.columns)

if __name__ == "__main__":
    unittest.main()
