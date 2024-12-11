import pickle
import pandas as pd
import streamlit as st

# Load the trained model
model_file = '../models/model.pkl'

with open(model_file, 'rb') as input_file:
    model = pickle.load(input_file)

# Dictionary for translating predictions
class_dict = {
    0: 'Not diabetic',
    1: 'Diabetic'
}

# Page Configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# App Title and Description
st.title("Diabetes Prediction Web Application")
st.markdown(
    """
    ### Welcome! 🩺
    This app predicts whether a person is diabetic or not based on input data. 
    Please provide the necessary information below.
    """
)

# Sidebar Styling and Input Section
st.sidebar.header("Input Features")
st.sidebar.markdown("### Provide your health data:")

# Input Fields
glucose = st.sidebar.number_input(
    'Glucose Level (mg/dL)', min_value=0, max_value=300, step=1, value=100, help="Enter glucose level."
)
insulin = st.sidebar.number_input(
    'Insulin Level (μIU/mL)', min_value=0, max_value=1000, step=1, value=50, help="Enter insulin level."
)
bmi = st.sidebar.number_input(
    'Body Mass Index (BMI)', min_value=0.0, max_value=70.0, step=0.1, value=25.0, help="Enter BMI value."
)
age = st.sidebar.number_input(
    'Age (years)', min_value=0, max_value=120, step=1, value=30, help="Enter your age."
)

# Input Data Frame
input_data = pd.DataFrame({
    'Glucose': [glucose],
    'Insulin': [insulin],
    'BMI': [bmi],
    'Age': [age]
})

# Prediction Button
st.markdown("---")
if st.button("Predict"):
    try:
        # Prediction logic
        prediction = model.predict(input_data)[0]
        predicted_class = class_dict[prediction]

        # Display Results
        st.success(f"Prediction: {predicted_class}")
        if prediction == 1:
            st.warning("Consult a healthcare professional for further evaluation.")
        else:
            st.info("Maintain a healthy lifestyle to reduce risks.")
    except Exception as e:
        st.error(f"An error occurred while predicting: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    ### Notes:
    - Model trained with health-related data.
    - Ensure input values are within reasonable ranges.
    - Consult a healthcare provider for clinical advice.
    """
)

# Styling with external CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)