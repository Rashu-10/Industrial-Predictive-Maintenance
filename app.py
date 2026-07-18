import streamlit as st
from src.components import data_validation
import joblib
from config.config import *
import pandas as pd
import plotly.express as px
from datetime import datetime
from src.logger import logging
from utils import model_exists
st.set_page_config(page_title="Industrial Predictive Maintenance",page_icon="⚙️",layout="wide")

st.title("⚙️ Industrial Predictive Maintenance System")
st.markdown("""Predict machine failures before they happen using Machine Learning.""")
st.sidebar.title("Navigation")

page = st.sidebar.radio("Navigation", ["Home", "Prediction", "Dashboard", "About"])
if page == "Home":
  st.header("Project Overview")
  st.write("""This application predicts machine failures using operational machine parameters.""")
  st.subheader("Business Problem")
  st.write("""Unexpected machine failures cause downtimeand financial losses.""")
if page == "About":
  st.header("About")
  st.write("""Developed using •Python •Scikit-Learn •Streamlit •Plotly""")
if page == "Prediction":
  if not model_exists():
    st.error("Model file missing")
    st.stop()
  try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    encoder = joblib.load(ENCODER_PATH)

  except Exception as e:
    logging.error(str(e))
    st.error("Unable to load model artifacts.")
    st.stop()
  
  col1, col2 = st.columns(2)
  with col1:
    machine_type = st.selectbox("Machine Type",["L", "M", "H"])
    air_temp=st.number_input("Air Temperature (K)",value=298.0)
    process_temp=st.number_input("Process Temperature (K)",value=308.0)
  with col2:
    rotational_speed = st.number_input("Rotational Speed (RPM)", value=1500)
    torque = st.number_input("Torque (Nm)", value=40.0)
    tool_wear = st.number_input("Tool Wear (min)", value=100)
  predict_btn = st.button("Predict Failure")
  if predict_btn:
    logging.info("Prediction request received")
    is_valid=data_validation.DataValidator.validate_input(air_temp,process_temp,rotational_speed,torque,tool_wear)
    if not is_valid:
      st.error("Invalid Input Values")
      logging.warning("Invalid input received")
      st.stop()

    machine_type_encoded = encoder.transform([machine_type])[0]
    input_df = pd.DataFrame({"Type":[machine_type_encoded], "Air_temperature_K":[air_temp], "Process_temperature_K":[process_temp], "Rotational_speed_rpm":[rotational_speed], "Torque_Nm":[torque], "Tool_wear_min":[tool_wear]})
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)
    probability = model.predict_proba(scaled_input)
    logging.info(f"Prediction Generated: {prediction[0]}")
    failure_probability = probability[0][1] * 100
    st.metric("Failure Probability", f"{failure_probability:.2f}%")
    if failure_probability < 30:
      risk = "Low"
    elif failure_probability < 70:
      risk = "Medium"
    else:
      risk = "High"
    if risk=="Low":
      st.success("Machine Healthy ✅")
    elif risk == "Medium":
      st.warning("Maintenance Recommended ⚠️")
    else:
      st.error("Immediate Inspection Required 🚨")
    st.info(f"Risk Level: {risk}")
    if risk == "High":
      st.error("Immediate Inspection Required 🚨")
      recommendation = "Inspect machine immediately. Check bearings and lubrication. Review operating conditions."

    elif risk == "Medium":
      st.warning("Maintenance Recommended ⚠️")
      recommendation = "Schedule maintenance soon. Monitor machine performance. Check wear components."

    else:
      st.success("Machine Healthy ✅")
      recommendation = "Continue normal operation. Follow routine maintenance schedule."

    st.info(recommendation)
      
    history = pd.DataFrame({"Timestamp":[datetime.now()], "Prediction":[prediction[0]], "Probability":[failure_probability], "Risk":[risk]})
    history.to_csv("data/prediction_history.csv", mode="a", header=False, index=False)
  
if page == "Dashboard":
  st.header("📊 Industrial Analytics Dashboard")
  df=pd.read_csv("data/cleaned_data.csv")
  total_records = len(df)
  total_failures = df["Machine_failure"].sum()
  failure_rate=(total_failures/total_records)*100
  col1,col2,col3 = st.columns(3)
  with col1: 
    st.metric("Total Machines", total_records)
  with col2: 
    st.metric("Failures", total_failures)
  with col3: 
    st.metric("Failure Rate", f"{failure_rate:.2f}%")
  tab1, tab2 = st.tabs(["Analytics", "History"])

  with tab1:
    failure_chart = px.pie(df, names="Machine_failure", title="Failure Distribution")
    st.plotly_chart(failure_chart, use_container_width=True)
    machine_chart = px.histogram(df, x="Type", title="Machine Type Distribution")
    st.plotly_chart(machine_chart, use_container_width=True)
    temp_chart = px.scatter(df, x="Air_temperature_K", y="Process_temperature_K", color="Machine_failure", title="Temperature Relationship")
    st.plotly_chart(temp_chart,use_container_width=True)
    model=joblib.load("artifacts/model.pkl")
    importance_df = pd.DataFrame({"Feature":["Type","Air Temp","Process Temp","RPM","Torque","Tool Wear"], "Importance": model.feature_importances_})
    importance_chart = px.bar(importance_df, x="Importance", y="Feature", orientation="h", title="Feature Importance")
    st.plotly_chart(importance_chart, use_container_width=True)
  with tab2:
    history_df = pd.read_csv(
      "data/prediction_history.csv",
      names=["Timestamp", "Prediction", "Probability", "Risk"],
      on_bad_lines="skip"
    )
    st.dataframe(history_df, use_container_width=True)






st.markdown("---")

st.caption("Industrial Predictive Maintenance System | ML Project")