import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Industrial Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Industrial Predictive Maintenance System")
st.write("Predict machine failures before they occur.")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Home", "Prediction", "About"]
)

# Load saved artifacts
model = joblib.load("artifacts/model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")
encoder = joblib.load("artifacts/label_encoder.pkl")

# Home Page
if page == "Home":

    st.header("Project Overview")

    st.write("""
    This application predicts machine failures using operational machine parameters.
    """)

    st.subheader("Business Problem")

    st.write("""
    Unexpected machine failures cause downtime and financial losses.
    """)

# About Page
elif page == "About":

    st.header("About")

    st.write("""
    Developed using:

    - Python
    - Scikit-Learn
    - Streamlit
    - Plotly
    """)

# Prediction Page
elif page == "Prediction":

    st.header("Machine Failure Prediction")

    col1, col2 = st.columns(2)

    with col1:
        machine_type = st.selectbox(
            "Machine Type",
            ["L", "M", "H"]
        )

        air_temp = st.number_input(
            "Air Temperature (K)",
            value=298.0
        )

        process_temp = st.number_input(
            "Process Temperature (K)",
            value=308.0
        )

    with col2:
        rotational_speed = st.number_input(
            "Rotational Speed (RPM)",
            value=1500
        )

        torque = st.number_input(
            "Torque (Nm)",
            value=40.0
        )

        tool_wear = st.number_input(
            "Tool Wear (min)",
            value=100
        )

    predict_btn = st.button("Predict Failure")

    if predict_btn:

      machine_type_encoded = encoder.transform([machine_type])[0]

      input_df = pd.DataFrame({
      "Type": [machine_type_encoded],
      "Air_temperature_K": [air_temp],
      "Process_temperature_K": [process_temp],
      "Rotational_speed_rpm": [rotational_speed],
      "Torque_Nm": [torque],
      "Tool_wear_min": [tool_wear]
      })

      scaled_input = scaler.transform(input_df)

      prediction = model.predict(scaled_input)
      probability = model.predict_proba(scaled_input)

      failure_probability = probability[0][1] * 100

      if prediction[0] == 0:
          st.success("Machine is Healthy ✅")
      else:
          st.error("Maintenance Required ⚠️")

      st.metric(
          "Failure Probability",
          f"{failure_probability:.2f}%"
      )
      if failure_probability<30:
          risk="Low"
      elif failure_probability<70:
          risk="Medium"
      else:
          risk="High"
      st.info(f"Risk Level:  {risk}") 
      if risk == "High":

        recommendation = """Inspect machine immediately.Check bearings and lubrication."""

      elif risk == "Medium":
        recommendation = """Schedule maintenance soon."""

      else:
        recommendation ="""Continue normal operation."""
      st.write(recommendation)
st.markdown("---")

st.caption(
    "Industrial Predictive Maintenance System | ML Project"
)
