import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

def load_clean_data(file_path):
    # Load the preprocessed data
    data = pd.read_csv(file_path)
    return data

def train_model(df):
    # Select features and target
    X = df.drop(columns=['TenYearCHD', 'age_bins'])
    y = df['TenYearCHD']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Gradient Boosting Classifier
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    
    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Save the trained model
    with open("../models/health_risk_model.pkl", "wb") as file:
        pickle.dump(model, file)
    
    print(f"Model trained with accuracy: {accuracy:.2f}")
    return model

if __name__ == "__main__":
    data = load_clean_data("../data/processed/health_clean.csv")
    train_model(data)
