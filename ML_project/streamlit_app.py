import streamlit as st
import pandas as pd
import joblib

# Load saved models
cost_model = joblib.load("cost_model.pkl")
delay_model = joblib.load("delay_model.pkl")

st.title("Civil Engineering Design Management Prediction")

st.header("Enter Project Details:")

# User inputs
project_size = st.selectbox("Project Size", ["Small", "Medium", "Large"])
design_duration = st.number_input("Design Duration (weeks)", min_value=1, max_value=52, value=12)
material_type = st.selectbox("Material Type", ["Concrete", "Steel", "Composite"])
design_changes = st.number_input("Number of Design Changes", min_value=0, max_value=10, value=2)
labor_cost = st.number_input("Labor Cost (₦)", min_value=100000, max_value=10000000, value=1000000)
complexity = st.selectbox("Project Complexity", ["Low", "Medium", "High"])

# Create DataFrame for prediction
input_df = pd.DataFrame({
    "Project_Size": [project_size],
    "Design_Duration": [design_duration],
    "Material_Type": [material_type],
    "Design_Changes": [design_changes],
    "Labor_Cost": [labor_cost],
    "Complexity": [complexity]
})

# Encode inputs
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
for col in ["Project_Size", "Material_Type", "Complexity"]:
    input_df[col] = encoder.fit_transform(input_df[col])

# Predict
cost_pred = cost_model.predict(input_df)[0]
delay_pred = delay_model.predict(input_df)[0]

# Show results
st.subheader("Predictions:")
st.write(f"Cost Overrun Risk: {cost_pred}")
st.write(f"Schedule Delay Risk: {delay_pred}")
