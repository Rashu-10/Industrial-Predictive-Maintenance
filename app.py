import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from src.logger import logging

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
    st.markdown("""
<div style="
background: linear-gradient(
90deg,
#1565C0,
#42A5F5
);
padding:25px;
border-radius:15px;
color:white;
text-align:center;
">

<h1>
⚙️ Industrial Predictive Maintenance
</h1>

<p>
AI-powered Machine Health Monitoring Platform
</p>

</div>
""",
unsafe_allow_html=True)

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
        health_score = 100 - failure_probability

        if failure_probability < 30:
            risk = "Low"
        elif failure_probability < 70:
            risk = "Medium"
        else:
            risk = "High"

        if prediction[0] == 0:
            st.success("Machine Healthy ✅")
        else:
            st.error("Maintenance Required ⚠️")

        c1, c2 = st.columns([1.2, 0.8])
        with c1:
            st.markdown(f"""
            <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
                <h3>Failure Probability</h3>
                <h2>{failure_probability:.2f}%</h2>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
                <h3>Health Score</h3>
                <h2>{health_score:.2f}%</h2>
            </div>
            """, unsafe_allow_html=True)
            st.progress(int(health_score))
            st.caption(f"Risk Level: {risk}")

        with c2:
            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=health_score,
                    title={"text": "Machine Health"}
                )
            )
            st.plotly_chart(fig, use_container_width=True)

        if risk == "High":
            st.markdown("""
            <div style="padding:20px;border-radius:10px;border:1px solid #d0d7de;">
                <h4>Maintenance Recommendation</h4>
                <p>Immediate inspection is recommended. Check bearings, lubrication, and machine operating conditions.</p>
            </div>
            """, unsafe_allow_html=True)
        elif risk == "Medium":
            st.markdown("""
            <div style="padding:20px;border-radius:10px;border:1px solid #d0d7de;">
                <h4>Maintenance Recommendation</h4>
                <p>Schedule preventive maintenance soon to avoid unexpected downtime.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="padding:20px;border-radius:10px;border:1px solid #d0d7de;">
                <h4>Maintenance Recommendation</h4>
                <p>Continue normal monitoring and follow the standard inspection routine.</p>
            </div>
            """, unsafe_allow_html=True)

        logging.info(
            f"Prediction={prediction[0]}, Probability={failure_probability:.2f}"
        )
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

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
            <h3>Total Machines</h3>
            <h2>{total_records}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
            <h3>Failures</h3>
            <h2>{total_failures}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
            <h3>Failure Rate</h3>
            <h2>{failure_rate:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        try:
            history_df = pd.read_csv("data/prediction_history.csv")
            predictions_made = len(history_df)
        except FileNotFoundError:
            predictions_made = 0
        st.markdown(f"""
        <div style="padding:18px;border-radius:12px;text-align:center;border:1px solid #d0d7de;">
            <h3>Predictions Made</h3>
            <h2>{predictions_made}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("System Statistics")
    stat1, stat2, stat3 = st.columns(3)
    with stat1:
        st.markdown(f"""
        <div style="padding:16px;border-radius:10px;text-align:center;border:1px solid #d0d7de;">
            <h4>Average Torque</h4>
            <p>{df['Torque_Nm'].mean():.2f} Nm</p>
        </div>
        """, unsafe_allow_html=True)
    with stat2:
        st.markdown(f"""
        <div style="padding:16px;border-radius:10px;text-align:center;border:1px solid #d0d7de;">
            <h4>Average RPM</h4>
            <p>{df['Rotational_speed_rpm'].mean():.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    with stat3:
        st.markdown(f"""
        <div style="padding:16px;border-radius:10px;text-align:center;border:1px solid #d0d7de;">
            <h4>Average Tool Wear</h4>
            <p>{df['Tool_wear_min'].mean():.2f} min</p>
        </div>
        """, unsafe_allow_html=True)
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
            risk_filter = st.selectbox(
                "Filter Risk",
                ["All", "Low", "Medium", "High"]
            )
            if risk_filter != "All":
                history_df = history_df[history_df["Risk"] == risk_filter]

            st.dataframe(
                history_df,
                use_container_width=True
            )
            csv = history_df.to_csv(index=False)
            st.download_button(
                "Download History",
                csv,
                "history.csv",
                "text/csv"
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