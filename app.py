# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("./models/best_random_forest_model.pkl")

# Define expected feature columns based on the training set
expected_columns = [
    "Age", "Biomass_Fuel_Exposure", "Occupational_Exposure", "Family_History_COPD",
    "BMI", "Air_Pollution_Level", "Respiratory_Infections_Childhood", "Pollution_Risk_Score",
    "Smoking_Status_encoded", "Gender_", "Smoking_Pollution_Interaction",
    "Location_Biratnagar", "Location_Butwal", "Location_Chitwan", "Location_Dharan",
    "Location_Hetauda", "Location_Kathmandu", "Location_Lalitpur", "Location_Nepalgunj",
    "Location_Pokhara"
]

st.title("COPD Prediction Application")
st.write("Enter the input values to predict COPD Diagnosis")

# Collect user input for each feature
age = st.number_input("Age", min_value=0, max_value=120, value=30)
biomass_fuel_exposure = st.selectbox("Biomass Fuel Exposure", [0, 1])
occupational_exposure = st.selectbox("Occupational Exposure", [0, 1])
family_history_copd = st.selectbox("Family History of COPD", [0, 1])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
air_pollution_level = st.number_input(
    "Air Pollution Level", min_value=0, max_value=500, value=100)
respiratory_infections_childhood = st.selectbox(
    "Respiratory Infections in Childhood", [0, 1])
pollution_risk_score = st.number_input(
    "Pollution Risk Score", min_value=0.0, max_value=100.0, value=0.0)
smoking_status_encoded = st.slider(
    "Smoking Status (0 = Non-smoker, 1 = Smoker)", 0.0, 1.0, 0.5)
gender_ = st.selectbox("Gender (0 = Male, 1 = Female)", [0, 1])
smoking_pollution_interaction = st.number_input(
    "Smoking Pollution Interaction", min_value=0.0, max_value=500.0, value=0.0)

# Categorical Location Input
location = st.selectbox(
    "Location",
    ["Biratnagar", "Butwal", "Chitwan", "Dharan", "Hetauda", "Kathmandu",
     "Lalitpur", "Nepalgunj", "Pokhara"]
)

# Create a DataFrame with the input values
input_data = pd.DataFrame([{
    "Age": age,
    "Biomass_Fuel_Exposure": biomass_fuel_exposure,
    "Occupational_Exposure": occupational_exposure,
    "Family_History_COPD": family_history_copd,
    "BMI": bmi,
    "Air_Pollution_Level": air_pollution_level,
    "Respiratory_Infections_Childhood": respiratory_infections_childhood,
    "Pollution_Risk_Score": pollution_risk_score,
    "Smoking_Status_encoded": smoking_status_encoded,
    "Gender_": gender_,
    "Smoking_Pollution_Interaction": smoking_pollution_interaction,
    "Location_Biratnagar": location == "Biratnagar",
    "Location_Butwal": location == "Butwal",
    "Location_Chitwan": location == "Chitwan",
    "Location_Dharan": location == "Dharan",
    "Location_Hetauda": location == "Hetauda",
    "Location_Kathmandu": location == "Kathmandu",
    "Location_Lalitpur": location == "Lalitpur",
    "Location_Nepalgunj": location == "Nepalgunj",
    "Location_Pokhara": location == "Pokhara"
}])

# Align input DataFrame with expected columns
input_data = input_data.reindex(columns=expected_columns, fill_value=0)

# Predict using the loaded model
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(
        f"Predicted COPD Diagnosis: {'Positive' if prediction[0] == 1 else 'Negative'}")
