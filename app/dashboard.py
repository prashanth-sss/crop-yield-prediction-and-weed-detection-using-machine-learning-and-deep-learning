import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model (example path)
# model = joblib.load('../models/crop_yield_model.pkl')

st.title("Crop Yield Prediction Dashboard")

# Input fields
crop = st.selectbox("Crop Type", ["Wheat", "Rice", "Maize"])
state = st.selectbox("Region", ["Punjab", "Maharashtra", "Tamil Nadu"])
season = st.selectbox("Season", ["Rabi", "Kharif", "Zaid"])
rainfall = st.slider("Rainfall (mm)", 0, 500, 100)
cost = st.number_input("Cost of Cultivation", 1000, 100000)

# Dummy model prediction for UI
if st.button("Predict Yield"):
    prediction = np.random.uniform(1.0, 5.0)  # Replace with model.predict()
    st.success(f"Estimated Yield: {prediction:.2f} tons/ha")