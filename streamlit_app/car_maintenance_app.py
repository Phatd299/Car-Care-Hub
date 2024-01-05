import streamlit as st
import pandas as pd
import joblib
from src.car_maintenance import predict_maintenance_cost

MODEL_PATH = 'models\car_maintenance.joblib'

def run_module4_app():
    st.write('Enter vehicle details to predict maintenance costs')

    # User input for vehicle details
    brand = st.selectbox('Select Vehicle Brand', ['honda', 'toyota'])
    model = st.selectbox('Select Vehicle Model',['jazz', 'amaze', 'city', 'fortuner'])
    engine_type = st.selectbox('Select Engine Type', ['petrol', 'diesel'])
    make_year = st.selectbox('Select Year Car Made', ['2016', '2017','2018'])
    mileage_range = st.slider('Mileage Range', min_value=10000, max_value=100000, value=1000)
    mileage = st.slider('Mileage', min_value=9000, max_value=140000, value=100)
    oil_filter = st.checkbox('Oil Filter')
    engine_oil = st.checkbox('Engine Oil')
    washer_plug_drain = st.checkbox('Washer Plug Drain')
    dust_and_pollen_filter = st.checkbox('Dust and Pollen Filter')
    whell_alignment_and_balancing = st.checkbox('Wheel Alignment and Balancing')
    air_clean_filter = st.checkbox('Air Clean Filter')
    fuel_filter = st.checkbox('Fuel Filter')
    spark_plug = st.checkbox('Spark Plug')
    brake_fluid = st.checkbox('Brake Fluid')
    brake_and_clutch_oil = st.checkbox('Brake and Clutch Oil')
    transmission_fluid = st.checkbox('Transmission Fluid')
    brake_pads = st.checkbox('Brake Pads')
    clutch = st.checkbox('Clutch')
    coolant = st.checkbox('Coolant')

    # Example of how you can retrieve user inputs into a dictionary
    user_input = {
        'brand': brand,
        'model': model,
        'engine_type': engine_type,
        'make_year': make_year,
        'mileage_range': mileage_range,
        'mileage': mileage,
        'oil_filter': oil_filter,
        'engine_oil': engine_oil,
        'washer_plug_drain': washer_plug_drain,
        'dust_and_pollen_filter': dust_and_pollen_filter,
        'whell_alignment_and_balancing': whell_alignment_and_balancing,
        'air_clean_filter': air_clean_filter,
        'fuel_filter': fuel_filter,
        'spark_plug': spark_plug,
        'brake_fluid': brake_fluid,
        'brake_and_clutch_oil': brake_and_clutch_oil,
        'transmission_fluid': transmission_fluid,
        'brake_pads': brake_pads,
        'clutch': clutch,
        'coolant': coolant
    }

    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Load the trained model
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model file path is correct.")
        return
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return
    
    if st.button('Predict Maintenance Cost'):
            if model:
                # Perform prediction
                predicted_cost = predict_maintenance_cost(input_df, model)
                predicted_cost = predicted_cost[0]  # Extract the value from the list

                st.markdown(f"**Predicted Maintenance Cost:** ${predicted_cost:.2f}")  # Emphasize and format the cost
            else:
                st.error("Error: Model loading failed. Please check the model file.")


