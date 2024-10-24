import unittest
import json
from src.flask_app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Test the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Health Risk Assessment API is running!", response.data)

    def test_predict(self):
        # Test the predict endpoint with valid data
        sample_data = {
            "male": 1,
            "age": 50,
            "education": 2,
            "currentSmoker": 0,
            "cigsPerDay": 0,
            "BPMeds": 0,
            "prevalentStroke": 0,
            "prevalentHyp": 1,
            "diabetes": 0,
            "totChol": 250,
            "sysBP": 120,
            "diaBP": 80,
            "BMI": 25.0,
            "heartRate": 70,
            "glucose": 85
        }
        response = self.app.post('/predict', 
                                 data=json.dumps(sample_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"prediction", response.data)

if __name__ == "__main__":
    unittest.main()
