import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="Concrete Strength Predictor",
    page_icon="🏗️",
    layout="centered"
)

# Load the saved model
@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "concrete_strength_model.joblib"
    return joblib.load(model_path)

try:
    saved_data = load_model()
    model = saved_data["model"]
    feature_names = saved_data["feature_names"]
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()

# Application title
st.title("🏗️ Concrete Strength Predictor")

st.write(
    "This application uses machine learning to predict "
    "concrete compressive strength based on mixture "
    "ingredients and curing age."
)

st.subheader("Enter Concrete Mixture Values")

# Input fields
with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        cement = st.number_input(
            "Cement (kg/m³)", min_value=0.0, value=300.0
        )
        slag = st.number_input(
            "Slag (kg/m³)", min_value=0.0, value=100.0
        )
        fly_ash = st.number_input(
            "Fly Ash (kg/m³)", min_value=0.0, value=0.0
        )
        water = st.number_input(
            "Water (kg/m³)", min_value=0.0, value=180.0
        )

    with col2:
        superplasticizer = st.number_input(
            "Superplasticizer (kg/m³)",
            min_value=0.0, value=8.0
        )
        coarse = st.number_input(
            "Coarse Aggregate (kg/m³)",
            min_value=0.0, value=950.0
        )
        fine = st.number_input(
            "Fine Aggregate (kg/m³)",
            min_value=0.0, value=760.0
        )
        age = st.number_input(
            "Curing Age (days)", min_value=1, value=28
        )

    submitted = st.form_submit_button(
        "Predict Concrete Strength",
        use_container_width=True
    )

# Generate prediction
if submitted:

    if cement == 0 or water == 0:
        st.warning("Please enter positive cement and water values.")
    else:
        values = {
            "Cement": cement,
            "Slag": slag,
            "Fly Ash": fly_ash,
            "Water": water,
            "Superplasticizer": superplasticizer,
            "Coarse Aggregate": coarse,
            "Fine Aggregate": fine,
            "Age": age
        }

        input_data = pd.DataFrame(
            [values], columns=feature_names
        )

        prediction = model.predict(input_data)[0]

        st.success("Prediction completed!")

        st.metric(
            label="Predicted Compressive Strength",
            value=f"{prediction:.2f} MPa"
        )

        st.info(
            "This result is a machine learning estimate "
            "and should not replace laboratory testing."
        )

# Project information
st.divider()
st.subheader("About This Project")

st.write(
    "This project compares Linear Regression and "
    "Random Forest models using the UCI Concrete "
    "Compressive Strength dataset."
)

st.write(
    "**Final Random Forest Test R²:** 0.851"
)

st.caption(
    "Advanced Artificial Intelligence Final Project | "
    "Maha Matalkeh | Virginia State University"
)
