import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('potato_desease.h5')

# Define class labels
class_labels = ['Early', 'Healthy', 'Late']

# Create the Streamlit app
st.title('Potato Disease Classification')

# Display the image below the title
image = Image.open('images.jpg')  # Replace 'images.jpg' with the actual image path
st.image(image, use_container_width=True)

# Allow user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Function to preprocess image
def preprocess_image(image):
    size = (128, 128)  # Resize to match model input
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  # Resize and maintain aspect ratio
    image_array = np.asarray(image)  # Convert to NumPy array
    normalized_image_array = (image_array.astype(np.float32) / 255.0)  # Normalize
    img_array = np.expand_dims(normalized_image_array, axis=0)  # Add batch dimension
    return img_array

# If an image is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)

    # Get predicted class
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_index]

    # Display prediction
    st.write(f"Prediction: **{predicted_class_label}**")