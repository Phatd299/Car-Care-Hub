# car_engine_app.py
import streamlit as st
import pandas as pd
import joblib
from src.car_engine import predict_engine_condition

MODEL_PATH = 'models\car_engine.joblib'  # Adjust the path as needed

def run_module3_app():
    st.write('Enter engine details to predict maintenance needs')

    rpm = st.slider("Engine RPM", min_value=50, max_value=2000, value=1000)
    oil_pressure = st.slider("Lub Oil Pressure", min_value=0.0, max_value=10.0, value=5.0)
    fuel_pressure = st.slider("Fuel Pressure", min_value=0.0, max_value=20.0, value=10.0)
    coolant_pressure = st.slider("Coolant Pressure", min_value=0.0, max_value=8.0, value=2.5)
    oil_temp = st.slider("Lub Oil Temperature", min_value=50.0, max_value=100.0, value=50.0)
    coolant_temp = st.slider("Coolant Temperature", min_value=50.0, max_value=200.0, value=50.0)

    # Create a dictionary with lists for each value
    engine_data = {
        'Engine rpm': [rpm],
        'Lub oil pressure': [oil_pressure],
        'Fuel pressure': [fuel_pressure],
        'Coolant pressure': [coolant_pressure],
        'lub oil temp': [oil_temp],
        'Coolant temp': [coolant_temp]
    }
    
    # Convert input to DataFrame
    input_df = pd.DataFrame(engine_data)
    
    # Load the trained model
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model file path is correct.")
        return
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return
    
    if st.button('Predict Engine Condition'):
        if model:
            # Perform prediction
            predicted_condition = predict_engine_condition(input_df, model)
            st.write(f"Predicted Engine Condition: {predicted_condition}")
        else:
            st.error("Error: Model loading failed. Please check the model file.")
