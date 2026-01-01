import streamlit as st
import pandas as pd
import joblib

# 1. Load your saved pipeline
model = joblib.load('house_predicition_model.pkl')

st.title("King County House Price Predictor")
st.markdown("Enter basic property details to get an instant valuation.")

# --- USER INPUT SECTION (Left Column for UI) ---
col1, col2 = st.columns(2)

with col1:
    sqft_living = st.number_input("Total Square Footage", min_value=300, max_value=15000, value=2000)
    grade = st.slider("Construction Grade (1-13)", 1, 13, 7)
    lat = st.number_input("Latitude (King County: 47.1 to 47.7)", min_value=47.1, max_value=47.7, value=47.5600, format="%.4f")

with col2:
    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Bathrooms", 1.0, 8.0, 1.0, step=0.5)
    is_waterfront = st.checkbox("Waterfront Property?")

# --- SMART DEFAULTS LOGIC ---
# These are the variables the user doesn't see, but the model needs.
floors = 1.0
view = 0
sqft_basement = 0 # Assume no basement for a quick estimate
sqft_above = sqft_living - sqft_basement # Logic-based default
sqft_living15 = sqft_living # Assume current house is similar to neighbors
waterfront_val = 1 if is_waterfront else 0

# --- PREDICTION ---
if st.button("Calculate Market Value"):
    # THE ORDER MUST MATCH YOUR LIST EXACTLY
    # features = ['floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement', 
    #             'view', 'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living']
    
    input_data = pd.DataFrame([[
        floors, 
        waterfront_val, 
        lat, 
        bedrooms, 
        sqft_basement, 
        view, 
        bathrooms, 
        sqft_living15, 
        sqft_above, 
        grade, 
        sqft_living
    ]], columns=['floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement', 
                 'view', 'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living'])

    prediction = model.predict(input_data)
    
    st.divider()
    st.subheader(f"Estimated Price: ${prediction[0]:,.2f}")
    st.info("Note: This estimate is based on the Ridge Regression model built in the Valuation Project.")