import streamlit as st
import pandas as pd
import joblib
from src.car_acceptability_testing import predict_car_acceptability

MODEL_PATH = 'models\car_accept.joblib'  # Adjust the path as needed

def run_module2_app():
    st.title('Module 2: Car Acceptability Prediction')
    st.write('Enter car details to predict acceptability')

    # User input for car details
    buying_price = st.selectbox('Buying Price', ['vhigh', 'high', 'med', 'low'])
    maintenance_price = st.selectbox('Maintenance Price', ['vhigh', 'high', 'med', 'low'])
    doors = st.selectbox('Number of Doors', ['2', '3', '4', '5more'])
    capacity = st.selectbox('Person Capacity', ['2', '4', 'more'])
    luggage_size = st.selectbox('Size of Luggage', ['med', 'small'])
    safety = st.selectbox('Safety Level', ['med', 'low'])

    input_data = {
        'Buying_Price': [buying_price],
        'Maintenance_Price': [maintenance_price],
        'No_of_Doors': [doors],
        'Person_Capacity': [capacity],
        'Size_of_Luggage': [luggage_size],
        'Safety': [safety]
    }

    # Convert input to DataFrame
    input_df = pd.DataFrame(input_data)

    # Load the trained model
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model file path is correct.")
        return
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Create a predict button
    if st.button('Predict'):
        # Check if model is loaded
        if model:
            # Perform prediction
            predicted_label = predict_car_acceptability(input_df, model)
            st.write(f"Predicted Car Acceptability: {predicted_label}")
        else:
            st.error("Error: Model loading failed. Please check the model file.")