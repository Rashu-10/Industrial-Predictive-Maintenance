import os
import streamlit as st

from src.pages.home import show_home
from src.pages.prediction import show_prediction
from src.pages.dashboard import show_dashboard
from src.pages.about import show_about
from src.ui.styles import load_css

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Industrial Predictive Maintenance System",
    page_icon="⚙️",
    layout="wide"
)

# ---------------------------
# Load Custom CSS
# ---------------------------
st.markdown(load_css(), unsafe_allow_html=True)

# ---------------------------
# Sidebar Branding
# ---------------------------
if os.path.exists("images/logo.png"):
    st.sidebar.image(
        "images/logo.png",
        use_container_width=True
    )
    st.sidebar.markdown(
        """
        <div style="text-align: center; color: #94A3B8; margin-top: 10px;">
            <h4 style="color: #00F2FE; margin-bottom: 0;">PredictiveAI 🏭</h4>
            <p style="font-size: 0.85rem; margin-top: 5px;">AI-Powered Failure Forecasting</p>
            <hr style="border: 0; border-top: 1px solid rgba(0, 242, 254, 0.15); margin: 15px 0;" />
            <p style="font-size: 0.8rem; line-height: 1.4;">
                Active Model: <strong>Random Forest</strong><br/>
                F1 Score: <strong>98.0%</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.sidebar.title("🏭 Predictive Maintenance")

st.sidebar.markdown("---")
st.sidebar.caption("System Telemetry Diagnostics © 2026")

# ---------------------------
# Navigation Tabs
# ---------------------------
tab_home, tab_predict, tab_dash, tab_about = st.tabs(
    [
        "🏠 Home Overview",
        "🔮 Health Diagnostics",
        "📊 Analytics Dashboard",
        "⚙️ Technical Specs"
    ]
)

with tab_home:
    show_home()

with tab_predict:
    show_prediction()

with tab_dash:
    show_dashboard()

with tab_about:
    show_about()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption(
    "Industrial Predictive Maintenance System | Built with Streamlit, Scikit-Learn, Plotly & SHAP"
)