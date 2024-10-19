import pickle
import pandas as pd
from sklearn.metrics import classification_report

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def evaluate_model(model, df):
    X = df.drop(columns=['TenYearCHD', 'age_bins'])
    y = df['TenYearCHD']
    
    y_pred = model.predict(X)
    report = classification_report(y, y_pred)
    print(report)
    return report

if __name__ == "__main__":
    model = load_model("../models/health_risk_model.pkl")
    data = pd.read_csv("../data/processed/health_clean.csv")
    evaluate_model(model, data)
