import streamlit as st
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Define the mapping of car brand indices to their names
car_brands = {
    0: 'Aston Martin', 1: 'Mercedes-Benz', 2: 'Mini', 3: 'Tesla', 4: 'GMC', 5: 'Alfa Romeo',
    6: 'Studebaker', 7: 'Suzuki', 8: 'Peugeot', 9: 'Genesis', 10: 'BMW', 11: 'Honda', 12: 'Chrysler',
    13: 'Mazda', 14: 'Infiniti', 15: 'Land Rover', 16: 'Dodge', 17: 'Fiat', 18: 'Maserati', 19: 'Saab',
    20: 'Nissan', 21: 'Hudson', 22: 'Lincoln', 23: 'Volvo', 24: 'Mitsubishi', 25: 'Oldsmobile', 26: 'Lexus',
    27: 'Buick', 28: 'Jaguar', 29: 'Toyota', 30: 'Volkswagen', 31: 'Renault', 32: 'Citroen', 33: 'Audi',
    34: 'Subaru', 35: 'Cadillac', 36: 'Pontiac', 37: 'Porsche', 38: 'Daewoo', 39: 'Bugatti', 40: 'Jeep',
    41: 'Ram Trucks', 42: 'Chevrolet', 43: 'MG', 44: 'Hyundai', 45: 'Ferrari', 46: 'Acura', 47: 'Kia',
    48: 'Bentley', 49: 'Ford'
}

# Load the model directly
processor = AutoImageProcessor.from_pretrained("dima806/car_brand_image_detection")
model = AutoModelForImageClassification.from_pretrained("dima806/car_brand_image_detection")

def run_module1_app():
    st.write('Upload an image to predict the car brand')

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Read the uploaded file
            img = Image.open(uploaded_file).convert("RGB")
            st.image(img, caption='Uploaded Image', use_column_width=True)

            # Perform classification when the user clicks the button
            if st.button('Predict'):
                # Preprocess the image
                inputs = processor(img, return_tensors="pt")

                # Perform prediction
                outputs = model(**inputs)
                predicted_class_idx = outputs.logits.argmax().item()

                # Map the predicted index to car brand name
                predicted_brand = car_brands.get(predicted_class_idx, "Unknown")
                st.write(f'Predicted Car Brand: {predicted_brand}')
        except Exception as e:
            st.error(f"Error processing image: {e}")
