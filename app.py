import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from datetime import datetime
st.set_page_config(
    page_title="Industrial Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)

model = joblib.load("artifacts/model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")
encoder = joblib.load("artifacts/label_encoder.pkl")
st.sidebar.title("⚙️ Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Prediction",
        "Dashboard",
        "About"
    ]
)
if page == "Home":

    st.title("⚙️ Industrial Predictive Maintenance System")

    st.markdown("""
    Predict machine failures before they happen using Machine Learning.
    """)

    st.header("Project Overview")

    st.write("""
    This application helps manufacturing companies identify
    potential machine failures before they occur.
    """)

    st.subheader("Business Problem")

    st.write("""
    Unexpected machine failures result in downtime,
    maintenance costs and production losses.
    """)
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
        machine_type_encoded = encoder.transform(
            [machine_type]
        )[0]
        input_df = pd.DataFrame({
            "Type":[machine_type_encoded],
            "Air_temperature_K":[air_temp],
            "Process_temperature_K":[process_temp],
            "Rotational_speed_rpm":[rotational_speed],
            "Torque_Nm":[torque],
            "Tool_wear_min":[tool_wear]
        })
        scaled_input = scaler.transform(
            input_df
        )
        prediction = model.predict(
            scaled_input
        )
        probability = model.predict_proba(
            scaled_input
        )
        failure_probability = (
            probability[0][1] * 100
        )
        if failure_probability < 30:
            risk = "Low"

        elif failure_probability < 70:
            risk = "Medium"

        else:
            risk = "High"
        if prediction[0] == 0:

            st.success(
                "Machine Healthy ✅"
            )

        else:

            st.error(
                "Maintenance Required ⚠️"
            )

        st.metric(
            "Failure Probability",
            f"{failure_probability:.2f}%"
        )

        st.info(
            f"Risk Level: {risk}"
        )
        if risk == "High":

            st.error("""
            Immediate Inspection Required

            • Check bearings
            • Check lubrication
            • Inspect machine immediately
            """)

        elif risk == "Medium":

            st.warning("""
            Schedule Maintenance Soon
            """)

        else:

            st.success("""
            Continue Normal Operation
            """)
        history = pd.DataFrame({

            "Timestamp":[datetime.now()],

            "Prediction":[prediction[0]],

            "Probability":[failure_probability],

            "Risk":[risk]
        })

        history.to_csv(
            "data/prediction_history.csv",
            mode="a",
            header=False,
            index=False
        )
elif page == "Dashboard":

    st.header("📊 Industrial Analytics Dashboard")

    df = pd.read_csv(
        "data/cleaned_data.csv"
    )
    total_records = len(df)

    total_failures = df[
        "Machine_failure"
    ].sum()

    failure_rate = (
        total_failures /
        total_records
    ) * 100

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Total Machines",
            total_records
        )

    with c2:
        st.metric(
            "Failures",
            total_failures
        )

    with c3:
        st.metric(
            "Failure Rate",
            f"{failure_rate:.2f}%"
        )
    tab1, tab2 = st.tabs(
        ["Analytics", "History"]
    )
    with tab1:
        pie_chart = px.pie(
            df,
            names="Machine_failure",
            title="Failure Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )
        machine_chart = px.histogram(
            df,
            x="Type",
            title="Machine Type Distribution"
        )

        st.plotly_chart(
            machine_chart,
            use_container_width=True
        )
        temp_chart = px.scatter(
            df,
            x="Air_temperature_K",
            y="Process_temperature_K",
            color="Machine_failure",
            title="Temperature Relationship"
        )

        st.plotly_chart(
            temp_chart,
            use_container_width=True
        )

        importance_df = pd.DataFrame({

            "Feature":[
                "Type",
                "Air Temp",
                "Process Temp",
                "RPM",
                "Torque",
                "Tool Wear"
            ],

            "Importance":
            model.feature_importances_
        })

        importance_chart = px.bar(
            importance_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Feature Importance"
        )

        st.plotly_chart(
            importance_chart,
            use_container_width=True
        )
    with tab2:

        st.subheader(
            "Prediction History"
        )

        try:

            history_df = pd.read_csv(
                "data/prediction_history.csv"
            )

            st.dataframe(
                history_df,
                use_container_width=True
            )

        except:

            st.info(
                "No prediction history available."
            )
elif page == "About":

    st.header("About")

    st.write("""
    AI-Powered Industrial Predictive Maintenance System

    Built using:

    • Python
    • Scikit-Learn
    • Streamlit
    • Plotly
    • Pandas
    """)
st.markdown("---")

st.caption(
    "Industrial Predictive Maintenance System | Industry Standard ML Project"
)