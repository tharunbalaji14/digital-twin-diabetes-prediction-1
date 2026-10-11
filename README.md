# 🩺 Digital Twin for Type 2 Diabetes

## 📌 Project Overview

This project develops a Proof-of-Concept (PoC) Digital Twin for Type 2 Diabetes.

The system combines historical Electronic Health Record (EHR) data with dynamic wearable and sensor data to create a virtual representation of a patient's health state.

The primary goal is to predict the risk of a glucose spike up to 2 hours in advance, enabling a shift from reactive healthcare toward proactive and personalized healthcare.

---

## 🎯 Problem Statement

Patients with Type 2 Diabetes experience fluctuations in blood glucose levels influenced by factors such as physical activity, sleep, heart rate, lifestyle patterns, and previous glucose measurements.

Traditional monitoring primarily identifies abnormal glucose levels after they occur.

Our Digital Twin aims to continuously analyse patient-specific historical and time-series data to estimate the risk of an upcoming glucose spike before it occurs.

---

## 💡 Proposed Solution

The Digital Twin combines two major data streams:

### 1. Static / Historical EHR Data
- Age
- Demographic information
- Previous diagnoses
- HbA1c
- Historical glucose measurements
- Relevant medical history

### 2. Dynamic / Wearable Data
- Continuous glucose measurements
- Heart rate
- Step count
- Sleep duration
- Physical activity

These data streams are processed and fused before being provided to a machine-learning model.

The final system will generate a prediction such as:

> **Low / Moderate / High risk of a glucose spike within the next 2 hours**

---

## 🧠 Digital Twin Workflow

Patient Data  
↓  
EHR Data + Wearable/Sensor Data  
↓  
Data Preprocessing  
↓  
Feature Engineering & Data Fusion  
↓  
AI/ML Prediction Model  
↓  
Glucose Spike Risk Prediction  
↓  
Digital Twin Dashboard

---

## 🤖 AI / Machine Learning

The project will evaluate suitable machine-learning approaches for short-term glucose risk prediction.

The final model and evaluation metrics will be documented after model training and validation.

---

## 🖥️ Doctor Dashboard

The conceptual dashboard will allow healthcare professionals to:

- View the patient's Digital Twin
- Monitor glucose trends
- Monitor wearable health parameters
- View historical health information
- View predicted glucose-spike risk
- Understand important factors influencing the prediction

---

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Plotly / Matplotlib
- Git & GitHub

---

## 📂 Planned Repository Structure

    digital-twin-diabetes-prediction/
    │
    ├── data/
    ├── notebooks/
    ├── src/
    ├── models/
    ├── dashboard/
    ├── docs/
    ├── README.md
    ├── requirements.txt
    └── LICENSE

---

## 🔒 Data Privacy

This Proof-of-Concept will use only synthetic, anonymized, or permitted open-source datasets.

No personally identifiable patient information is intended to be used in this project.

---

## ⚠️ Medical Disclaimer

This project is an educational and research Proof-of-Concept.

It is not a medical device and must not be used for clinical diagnosis, treatment, or medical decision-making.

---

## 🚧 Project Status

🟡 **Currently Under Development**

Current development stages:

- [x] Problem selection
- [x] GitHub repository creation
- [ ] Dataset preparation
- [ ] Data preprocessing
- [ ] Feature engineering
- [ ] Model development
- [ ] Model evaluation
- [ ] Digital Twin dashboard
- [ ] Architecture diagram
- [ ] Final presentation
- [ ] Prototype demonstration video

---

## 👥 Team
TYST  
St.Joseph's college of engineering

### Team Members
- Team Leader — SUDHAKAR T K
- Member 2 — THARUN B
- Member 3 — Thilakan S
- Member 4 — Yogavel D

---

## 📜 License

Open-source license information will be updated before the final submission.
