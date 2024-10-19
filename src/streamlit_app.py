import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("../models/health_risk_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Health Risk Assessment")

# Input fields for user data
age = st.slider("Age", 30, 70)
sex = st.radio("Gender", options=["Male", "Female"])
education = st.selectbox("Education Level", [1, 2, 3, 4])
smoker = st.radio("Are you a current smoker?", options=["Yes", "No"])
cigs_per_day = st.number_input("Cigarettes per Day", min_value=0, max_value=70, value=0)
bpmeds = st.radio("On Blood Pressure Medication?", options=["Yes", "No"])
stroke = st.radio("Have you had a stroke?", options=["Yes", "No"])
hypertension = st.radio("Do you have Hypertension?", options=["Yes", "No"])
diabetes = st.radio("Do you have Diabetes?", options=["Yes", "No"])
cholesterol = st.number_input("Total Cholesterol", min_value=100, max_value=700, value=200)
sysbp = st.number_input("Systolic BP", min_value=80, max_value=300, value=120)
diabp = st.number_input("Diastolic BP", min_value=50, max_value=150, value=80)
bmi = st.number_input("BMI", min_value=15.0, max_value=60.0, value=25.0)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=150, value=70)
glucose = st.number_input("Glucose Level", min_value=40, max_value=400, value=80)

# Map input values to the model's format
input_data = {
    "male": 1 if sex == "Male" else 0,
    "age": age,
    "education": education,
    "currentSmoker": 1 if smoker == "Yes" else 0,
    "cigsPerDay": cigs_per_day,
    "BPMeds": 1 if bpmeds == "Yes" else 0,
    "prevalentStroke": 1 if stroke == "Yes" else 0,
    "prevalentHyp": 1 if hypertension == "Yes" else 0,
    "diabetes": 1 if diabetes == "Yes" else 0,
    "totChol": cholesterol,
    "sysBP": sysbp,
    "diaBP": diabp,
    "BMI": bmi,
    "heartRate": heart_rate,
    "glucose": glucose
}

# Convert to DataFrame for model input
df = pd.DataFrame([input_data])

# Predict the risk
if st.button("Predict"):
    prediction = model.predict(df)
    risk = "high" if prediction[0] == 1 else "low"
    st.write(f"Your risk of developing heart disease in 10 years is: {risk}")