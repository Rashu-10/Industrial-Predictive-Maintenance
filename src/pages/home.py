import os
import streamlit as st

def show_home():
    # Banner Image
    if os.path.exists("images/banner.png"):
        st.image("images/banner.png", use_container_width=True)
    
    # Hero Title and Subtitle
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
            <h1 class="hero-title">PredictiveAI 🏭</h1>
            <p class="hero-subtitle">Next-Generation Industrial Failure Forecasting</p>
            <p style="font-size: 1.15rem; max-width: 800px; margin: 0 auto 30px auto; color: #94A3B8; line-height: 1.6;">
                Harness machine learning trained on <strong>10,000 real industrial machine records</strong> 
                across 3 categories — predicting machinery failure from climate, speed, torque, and tool wear inputs 
                with <strong>98.0% F1-score accuracy</strong>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Platform Overview Section
    st.markdown(
        """
        <div style="margin-top: 40px; margin-bottom: 20px;">
            <p style="color: #00F2FE; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; margin-bottom: 5px;">
                Platform Overview
            </p>
            <h2 style="color: white; font-weight: 700; font-size: 1.8rem; margin-top: 0; margin-bottom: 10px;">
                Trained on Real Industrial Telemetry Data
            </h2>
            <p style="color: #94A3B8; margin-bottom: 30px;">
                Built from standard industrial datasets containing multisensor telemetry and tool wear logs.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # KPI Cards in HTML row style
    st.markdown(
        """
        <div class="kpi-container">
            <div class="kpi-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">📊</div>
                <div class="kpi-value">10,000</div>
                <div class="kpi-label">Telemetry Records</div>
            </div>
            <div class="kpi-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">⚙️</div>
                <div class="kpi-value">3</div>
                <div class="kpi-label">Machine Types (L/M/H)</div>
            </div>
            <div style="position: relative;" class="kpi-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">⏱️</div>
                <div class="kpi-value">6</div>
                <div class="kpi-label">Sensors Monitored</div>
            </div>
            <div class="kpi-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">🎯</div>
                <div class="kpi-value">98.0%</div>
                <div class="kpi-label">F1-Score Accuracy</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Key Benefits / Platform Features in glassmorphism cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color: #00F2FE; margin-top: 0;">⚡ Real-time Prediction Engine</h3>
                <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.5;">
                    Input current telemetry reading (ambient temperatures, rotational speed, torque, and wear time) 
                    and receive instantaneous risk predictions with detailed failure probabilities.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color: #00F2FE; margin-top: 0;">🔮 Explainable AI (SHAP)</h3>
                <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.5;">
                    Understand exactly why a machine is predicted to fail. Our built-in SHAP (Shapley Additive exPlanations) 
                    explainer visualizes the precise feature contributions driving the risk score.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
