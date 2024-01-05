import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
import joblib

# Load the trained model
model = joblib.load('models/car_engine.joblib')

def perform_feature_engineering(df):

    X = df.copy()

    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Interaction Terms
    poly = PolynomialFeatures(interaction_only=True, include_bias=False)
    X_poly = poly.fit_transform(X_scaled)

    # Combine the scaled features and interaction terms
    preprocessed_data = np.concatenate((X_scaled, X_poly), axis=1)

    return preprocessed_data


def predict_engine_condition(input_df, model):
    try:

        input_preprocessed_data = perform_feature_engineering(input_df)
        predicted_condition = model.predict(input_preprocessed_data)

        # Decode prediction label
        label_mapping = {0: 'Normal', 1: 'Requires Maintenance'}
        predicted_label = label_mapping[predicted_condition[0]]

        return predicted_label

    except Exception as e:
        return f"Prediction Error: {e}"
