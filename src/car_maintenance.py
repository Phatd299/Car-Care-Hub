import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler  

# Load the pre-trained model
model = joblib.load('models\car_maintenance.joblib')

# Function for preprocessing user input
import pandas as pd

def perform_feature_engineering(df):
    processed_data = df.copy()

    # Mapping checkbox values to 1s and 0s
    checkbox_columns = [
        'oil_filter', 'engine_oil', 'washer_plug_drain', 'dust_and_pollen_filter',
        'whell_alignment_and_balancing', 'air_clean_filter', 'fuel_filter',
        'spark_plug', 'brake_fluid', 'brake_and_clutch_oil', 'transmission_fluid',
        'brake_pads', 'clutch', 'coolant'
    ]

    for col in checkbox_columns:
        processed_data[col] = processed_data[col].apply(lambda x: 1 if x else 0)
        processed_data[f'{col}_percentage'] = processed_data[col] / processed_data['mileage']

    # Add 'current_year' and 'age_of_vehicle'
    processed_data['make_year'] = processed_data['make_year'].astype(int)
    processed_data['current_year'] = pd.Timestamp.now().year
    processed_data['age_of_vehicle'] = processed_data['current_year'] - processed_data['make_year']

    # Calculate maintenance percentages
    maintenance_cols = checkbox_columns
    for col in maintenance_cols:
        processed_data[f'{col}_percentage'] = processed_data[col] / processed_data['mileage']

    # One-hot encoding for categorical variables
    categorical_cols = ['brand', 'model', 'engine_type', 'make_year']
    processed_data = pd.get_dummies(processed_data, columns=categorical_cols, drop_first=True)

    # Define expected columns order
    expected_columns_order = [
    'mileage_range', 'mileage', 'oil_filter', 'engine_oil',
    'washer_plug_drain', 'dust_and_pollen_filter',
    'whell_alignment_and_balancing', 'air_clean_filter', 'fuel_filter',
    'spark_plug', 'brake_fluid', 'brake_and_clutch_oil',
    'transmission_fluid', 'brake_pads', 'clutch', 'coolant',
    'current_year', 'age_of_vehicle', 'oil_filter_percentage',
    'engine_oil_percentage', 'washer_plug_drain_percentage',
    'dust_and_pollen_filter_percentage',
    'whell_alignment_and_balancing_percentage',
    'air_clean_filter_percentage', 'fuel_filter_percentage',
    'spark_plug_percentage', 'brake_fluid_percentage',
    'brake_and_clutch_oil_percentage', 'transmission_fluid_percentage',
    'brake_pads_percentage', 'clutch_percentage', 'coolant_percentage',
    'brand_toyota', 'model_city', 'model_fortuner', 'model_jazz',
    'engine_type_petrol', 'make_year_2017', 'make_year_2018'
    ]

    # Add missing columns with default values
    missing_cols = set(expected_columns_order) - set(processed_data.columns)
    for col in missing_cols:
        processed_data[col] = 0  # You might adjust default values based on data type or context

    # Reorder columns to match expected order
    processed_data = processed_data.reindex(columns=expected_columns_order, fill_value=0)

    print(processed_data.columns)  # Optional: Print column names for verification

    return processed_data


def predict_maintenance_cost(user_input, model):
    try:
        # Assuming perform_feature_engineering is replaced with preprocess_input
        input_preprocessed_data = perform_feature_engineering(user_input)

        # Assuming model is a trained model and can directly predict
        predicted_cost = model.predict(input_preprocessed_data)

        return predicted_cost

    except Exception as e:
        return f"Prediction Error: {e}"
