import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder
import joblib
    
def perform_feature_engineering(df):
    # Copy the DataFrame to retain the original columns
    df_processed = df.copy()

    # Initialize encoders
    ordinal_enc = OrdinalEncoder()

    # Ordinal Encoding for 'Buying_Price' and 'Maintenance_Price' columns
    df_processed['Buying_Price_Encoded'] = ordinal_enc.fit_transform(df_processed[['Buying_Price']])
    df_processed['Maintenance_Price_Encoded'] = ordinal_enc.fit_transform(df_processed[['Maintenance_Price']])

    # Create binary columns based on 'Safety' and 'Size_of_Luggage'
    df_processed['Safety_low'] = (df_processed['Safety'] == 'low').astype(int)
    df_processed['Safety_med'] = (df_processed['Safety'] == 'med').astype(int)
    df_processed['Size_of_Luggage_med'] = (df_processed['Size_of_Luggage'] == 'med').astype(int)
    df_processed['Size_of_Luggage_small'] = (df_processed['Size_of_Luggage'] == 'small').astype(int)

    # Mapping categorical values to numeric values for 'No_of_Doors'
    door_mapping = {'2': 2, '3': 3, '4': 4, '5more': 5}
    df_processed['No_of_Doors_Numeric'] = df_processed['No_of_Doors'].map(door_mapping)

    # Mapping categorical values to numeric values for 'Person_Capacity'
    person_mapping = {'2': 2, '4': 4, 'more': 6}  # Assuming 'more' refers to more than 4
    df_processed['Person_Capacity_Numeric'] = df_processed['Person_Capacity'].map(person_mapping)

    # Rearrange columns to match the model's order
    df_processed = df_processed[['Buying_Price_Encoded', 'Maintenance_Price_Encoded', 'Size_of_Luggage_med', 'Size_of_Luggage_small', 'Safety_low', 'Safety_med', 'No_of_Doors_Numeric', 'Person_Capacity_Numeric']]

    return df_processed

    
def predict_car_acceptability(input_df, model):
    try:
        # Perform feature engineering on user input
        input_df_processed = perform_feature_engineering(input_df)

        # Make prediction
        prediction = model.predict(input_df_processed)

        # Decode prediction label
        label_mapping = {0: 'Acceptable', 1: 'Good', 2: 'Unacceptable', 3: 'Very good'}
        predicted_label = label_mapping[prediction[0]]

        return predicted_label
    except Exception as e:
        return f"Prediction Error: {e}"