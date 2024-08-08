# Multiple Disease Prediction System - Streamlit Web App

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Streamlit Web App](#streamlit-web-app)
  - [Imports](#imports)
  - [Model and Scaler Loading](#model-and-scaler-loading)
  - [Sidebar Navigation](#sidebar-navigation)

## Project Overview

## Dataset

## Streamlit Web App
### Imports
- **Pickle:** Used to load saved machine learning models and scalers.
- **Streamlit:** Framework for creating the web application.
- **Streamlit_option_menu:** Provides a sidebar menu for navigation between different prediction pages.
- **Numpy:** Used for handling numerical operations and data formatting

### Model and Scaler Loading
Load four pre-trained machine learning models from pickle files:
- **Diabetes Model:** diabetes_model
- **Heart Disease Model:** heart_disease_model
- **Parkinson’s Disease Model:** parkinsons_disease_model
- **Breast Cancer Model:** breast_cancer_model

It also loads corresponding scalers to standardize the input data:
- **Diabetes Scaler:** diabetes_scaler
- **Heart Disease Scaler:** heart_disease_scaler
- **Parkinson’s Disease Scaler:** parkinsons_disease_scaler
- **Breast Cancer Scaler:** breast_cancer_scaler

### Sidebar Navigation
- A sidebar is created using st.sidebar to navigate between four different prediction pages:
- Diabetes Prediction
- Heart Disease Prediction
- Parkinson’s Disease Prediction
- Breast Cancer Prediction

### Diabetes Prediction Page
- **Inputs:** Collects values for features related to diabetes prediction (e.g., number of pregnancies, glucose level, blood pressure).
- **Prediction:** On clicking the "Diabetes Test Result" button, the inputs are scaled and passed to the diabetes model to predict whether the person is diabetic or not.

### Heart Disease Prediction Page
- **Inputs:** Collects values for features related to heart disease prediction (e.g., age, chest pain type, cholesterol levels).
- **Prediction:** On clicking the "Heart Disease Test Result" button, the inputs are scaled and passed to the heart disease model to predict whether the person has heart disease or not.

### Parkinson’s Disease Prediction Page
- **Inputs:** Collects values for features related to Parkinson’s disease prediction (e.g., MDVP - Fo, Jitter percentage).
- **Prediction:** On clicking the "Parkinson’s Test Result" button, the inputs are scaled and passed to the Parkinson’s disease model to predict whether the person has Parkinson’s disease or not.

### Breast Cancer Prediction Page
- **Inputs:** Collects values for features related to breast cancer prediction (e.g., mean radius, worst texture).
- **Prediction:** On clicking the "Breast Cancer Test Result" button, the inputs are scaled and passed to the breast cancer model to predict whether the cancer is malignant or benign.
