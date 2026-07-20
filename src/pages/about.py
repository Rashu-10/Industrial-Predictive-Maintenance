import streamlit as st


def show_about():
    st.markdown(
        """
        <div style="margin-bottom: 25px;">
            <p style="color: #00F2FE; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; margin-bottom: 5px;">
                Information Hub
            </p>
            <h2 style="color: white; font-weight: 700; font-size: 1.8rem; margin-top: 0;">
                ⚙️ Technical Specifications & Architecture
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass-card">
            <h3 style="color: #00F2FE; margin-top: 0; font-size: 1.3rem;">🏭 Industrial Predictive Maintenance System</h3>
            <p style="color: #CBD5E1; line-height: 1.6; font-size: 0.95rem;">
                This software is designed to predict failure events in industrial milling machinery using multivariate sensor data inputs. 
                By forecasting equipment failures, the system aids in preventing costly factory downtime, planning maintenance slots 
                efficiently, and preserving equipment health.
            </p>
        </div>

        <div class="glass-card">
            <h3 style="color: #00F2FE; margin-top: 0; font-size: 1.3rem;">🛠️ Technology Stack & Libraries</h3>
            <ul style="color: #CBD5E1; line-height: 1.8; font-size: 0.95rem; padding-left: 20px;">
                <li><strong>Streamlit</strong>: Application interface, dynamic forms, and presentation layer.</li>
                <li><strong>Scikit-Learn</strong>: ML pipeline, scaling, encoding, and the Random Forest classifier model.</li>
                <li><strong>Plotly</strong>: Reactive dashboard charts and interactive data visualization.</li>
                <li><strong>SHAP (Shapley Additive exPlanations)</strong>: Local model explainability and feature contribution analysis.</li>
                <li><strong>Pandas & NumPy</strong>: Mathematical data structures and feature manipulation.</li>
                <li><strong>Joblib</strong>: Serialization and loading of model binaries and preprocessors.</li>
            </ul>
        </div>

        <div class="glass-card">
            <h3 style="color: #00F2FE; margin-top: 0; font-size: 1.3rem;">🧠 ML Pipeline Workflow</h3>
            <ol style="color: #CBD5E1; line-height: 1.8; font-size: 0.95rem; padding-left: 20px;">
                <li><strong>Ingestion & Validation</strong>: Validate inputs from telemetry sensors to prevent model execution with out-of-bound variables.</li>
                <li><strong>Categorical Encoding</strong>: Categorize machine classifications using fit encoders.</li>
                <li><strong>Feature Scaling</strong>: Standardize features using the training set fit standard scaler.</li>
                <li><strong>Model Inference</strong>: Predict binary machine failure outcomes (failed vs healthy) and failure probability distributions.</li>
                <li><strong>Local Explainability</strong>: Generate SHAP tree values to outline individual feature contributions for transparency.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )