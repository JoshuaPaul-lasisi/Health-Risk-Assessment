import unittest
import pandas as pd
from src.model_training import load_clean_data, train_model
from sklearn.ensemble import GradientBoostingClassifier

class TestModelTraining(unittest.TestCase):

    def setUp(self):
        # Sample cleaned data for testing
        data = {
            'age': [35, 45, 55],
            'education': [1, 2, 3],
            'cigsPerDay': [10, 15, 20],
            'BPMeds': [0, 0, 1],
            'totChol': [200, 240, 180],
            'BMI': [22.0, 24.5, 27.5],
            'heartRate': [72, 80, 65],
            'glucose': [85, 105, 95],
            'prevalentHyp': [1, 0, 1],
            'prevalentStroke': [0, 0, 0],
            'diabetes': [0, 1, 0],
            'sysBP': [120, 130, 140],
            'diaBP': [80, 85, 90],
            'male': [1, 0, 1],
            'TenYearCHD': [0, 1, 1]
        }
        self.df = pd.DataFrame(data)

    def test_load_clean_data(self):
        df = load_clean_data("../data/processed/health_clean.csv")
        self.assertIsInstance(df, pd.DataFrame)

    def test_train_model(self):
        model = train_model(self.df)
        # Check if the model is an instance of GradientBoostingClassifier
        self.assertIsInstance(model, GradientBoostingClassifier)

if __name__ == "__main__":
    unittest.main()