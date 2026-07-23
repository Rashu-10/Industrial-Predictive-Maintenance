# 🏭 Industrial Predictive Maintenance System

## 🔗 Live Application

[Industrial Predictive Maintenance System](https://industrial-predictive-maintenance-system-opjx67kvwfvxeyudd75ev.streamlit.app/?utm_source=chatgpt.com)

---

## 📌 Overview

Industrial equipment failures can cause significant downtime, maintenance costs, and production losses. This project leverages Machine Learning to predict machine failures before they occur, enabling proactive maintenance planning and reducing unexpected breakdowns.

The system analyzes key machine operating parameters such as temperature, rotational speed, torque, and tool wear to determine the likelihood of machine failure and provide actionable maintenance recommendations.

This project demonstrates an end-to-end Machine Learning workflow including data preprocessing, model training, explainable AI, dashboard development, and cloud deployment.

---

## 🎯 Objectives

* Predict machine failures using Machine Learning.
* Provide failure probability and risk assessment.
* Explain predictions using Explainable AI (SHAP).
* Generate maintenance recommendations.
* Visualize operational insights through interactive dashboards.
* Support proactive maintenance decision-making.

---

## 🚀 Features

### 🔮 Machine Failure Prediction

Predict whether a machine is likely to fail based on operational parameters.

### 📊 Interactive Analytics Dashboard

Visualize machine health trends, failure distributions, and operational insights.

### 📈 Explainable AI (SHAP)

Understand which machine parameters contributed most to a prediction.

### ⚠️ Risk Assessment

Classify machine conditions into:

* Low Risk
* Medium Risk
* High Risk

### 🛠 Maintenance Recommendations

Generate intelligent maintenance suggestions based on failure probability.

### 📄 Report Generation

Download machine diagnostics and prediction reports.

### 📥 Prediction History

Track and review previous predictions.

### ☁️ Cloud Deployment

Accessible through a public Streamlit application.

---

## 🧠 Machine Learning Workflow

### Data Collection

AI4I Predictive Maintenance Dataset

### Data Preprocessing

* Missing value analysis
* Feature engineering
* Label encoding
* Feature scaling
* Train-test splitting

### Model Training

Multiple models were evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Extra Trees Classifier

### Model Selection

Random Forest was selected based on overall predictive performance and interpretability. Random Forest models are commonly used in predictive maintenance applications because they effectively capture relationships among operational sensor variables and machine failures.

---

## 📊 Input Parameters

The system accepts the following machine parameters:

| Parameter           | Description                    |
| ------------------- | ------------------------------ |
| Type                | Machine Quality Type (L, M, H) |
| Air Temperature     | Ambient operating temperature  |
| Process Temperature | Internal process temperature   |
| Rotational Speed    | Machine rotational speed (RPM) |
| Torque              | Applied torque (Nm)            |
| Tool Wear           | Tool wear duration (minutes)   |

---

## 🏗 Project Architecture

```text
User Input
      ↓
Data Validation
      ↓
Preprocessing Pipeline
      ↓
Random Forest Model
      ↓
Failure Prediction
      ↓
SHAP Explainability
      ↓
Risk Assessment
      ↓
Maintenance Recommendation
      ↓
Report Generation
```

---

## 🛠 Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* SHAP

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Web Application

* Streamlit

### Model Persistence

* Joblib

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
Industrial-Predictive-Maintenance-System/

│
├── app.py
│
├── artifacts/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── assets/
│   └── style.css
│
├── config/
│   ├── config.py
│   └── constants.py
│
├── data/
│   ├── cleaned_data.csv
│   └── prediction_history.csv
│
├── logs/
│
├── reports/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── pages/
│   ├── explainability.py
│   ├── recommendation_engine.py
│   ├── report_generator.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Industrial-Predictive-Maintenance-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Modules

### 🏠 Home Page
<img width="1276" height="675" alt="image" src="https://github.com/user-attachments/assets/53fbe5e7-3749-43f4-a7d9-cd01c0755f8e" />


Project overview, KPIs, and system introduction.

### 🔮 Prediction Engine
<img width="1271" height="667" alt="image" src="https://github.com/user-attachments/assets/3e5e9767-6836-43a9-acee-308e3898d601" />


Machine failure diagnostics and risk assessment.

### 📊 Dashboard
<img width="1276" height="672" alt="image" src="https://github.com/user-attachments/assets/18a71f00-54ca-4ad4-ba9d-91fdb03d7807" />


Interactive visualizations and operational analytics.

### ℹ️ About
<img width="1268" height="675" alt="image" src="https://github.com/user-attachments/assets/bf113e80-af22-4502-b88d-ca836320bfaf" />


Project information and technology stack.

---

## 💡 Business Impact

Predictive maintenance enables organizations to:

* Reduce unexpected equipment downtime.
* Improve equipment lifespan.
* Lower maintenance costs.
* Increase operational efficiency.
* Improve maintenance planning.
* Support Industry 4.0 initiatives. Predictive maintenance has become a key Industry 4.0 strategy for improving equipment utilization and reducing operational disruptions.

---

## 🔮 Future Enhancements

* Real-time IoT sensor integration
* Remaining Useful Life (RUL) prediction
* Deep Learning models
* API deployment with FastAPI
* Docker containerization
* CI/CD pipeline integration
* Multi-machine monitoring
* Cloud database integration

---

## 👨‍💻 Author

Developed as an end-to-end Machine Learning and Industrial Analytics project demonstrating:

* Data Science
* Machine Learning
* Explainable AI
* Dashboard Development
* Software Engineering
* Cloud Deployment

---

## 📜 License

This project is intended for educational, research, and portfolio purposes.
