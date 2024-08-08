# Multiple Disease Prediction System - Streamlit Web App
This project is a web application for predicting various medical conditions using machine learning models. Built with Streamlit, the application allows users to input health-related data and receive predictions for four conditions: diabetes, heart disease, Parkinson's disease, and breast cancer. 
The application utilizes pre-trained models and corresponding scalers to process and analyze user input, providing instant, actionable insights about the likelihood of each condition based on the data provided. The user-friendly interface includes a sidebar for easy navigation between different prediction pages, making it accessible and straightforward for users seeking health predictions.
![image](https://github.com/user-attachments/assets/60861c68-639a-4c13-a0ba-705b706e1ce1)

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Streamlit Web App](#streamlit-web-app)
  - [Imports](#imports)
  - [Model and Scaler Loading](#model-and-scaler-loading)
  - [Sidebar Navigation](#sidebar-navigation)
  - [Diabetes Prediction Page](#diabetes-prediction-page)
  - [Heart Disease Prediction Page](#heart-disease-prediction-page)
  - [Parkinsons Disease Prediction Page](#parkinsons-disease-prediction-page)
  - [Breast Cancer Prediction Page](#breast-cancer-prediction-page)

## Project Overview
The web app is built using Streamlit, which offers an intuitive and interactive interface for users to interact with the system.

**Goals:**
- **Develop a User-Friendly Interface:** Create an accessible web application where users can easily input their health data and navigate between different disease prediction pages.
- **Implement Predictive Models:** Utilize pre-trained machine learning models to analyze user data and provide accurate predictions for diabetes, heart disease, Parkinson’s disease, and breast cancer.
- **Ensure Data Processing Accuracy:** Integrate data scaling and transformation processes to ensure that user inputs are accurately processed by the models for reliable predictions.
- **Provide Instant Feedback:** Offer immediate, clear, and actionable predictions based on the input data, enabling users to understand their health risk status quickly.

**Objectives:**
- **Build the Web Application:**
  - Develop a Streamlit application with a sidebar menu for navigation between disease prediction pages.
  - Design input forms for each health condition to collect relevant data from users.
- **Load and Utilize Pre-Trained Models:**
  - Implement the functionality to load and apply machine learning models and scalers for each condition.
  - Ensure that the models are accurately applied to user input data for generating predictions.
- **Enhance User Experience:**
  - Design the interface to be intuitive and user-friendly, allowing users to enter data and receive predictions with minimal effort.
  - Display prediction results in a clear and understandable format.
- **Test and Validate the Application:**
  - Conduct thorough testing to ensure the accuracy and reliability of predictions.
  - Validate the user interface and functionality to ensure a seamless user experience.

## Dataset
The datasets are structured with a range of features specific to each condition, providing a detailed basis for training machine learning models to predict disease presence or risk. They include both numerical measurements and categorical indicators, which are used to build and validate predictive models for accurate health risk assessment.

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

![image](https://github.com/user-attachments/assets/2ef2ca5f-72e0-4bde-b05e-bbdd04416109)

### Diabetes Prediction Page
- **Inputs:** Collects values for features related to diabetes prediction (e.g., number of pregnancies, glucose level, blood pressure).
- **Prediction:** On clicking the "Diabetes Test Result" button, the inputs are scaled and passed to the diabetes model to predict whether the person is diabetic or not.
![image](https://github.com/user-attachments/assets/8cb9b011-ddf9-4888-83d6-a21a2ab1fe41)

### Heart Disease Prediction Page
- **Inputs:** Collects values for features related to heart disease prediction (e.g., age, chest pain type, cholesterol levels).
- **Prediction:** On clicking the "Heart Disease Test Result" button, the inputs are scaled and passed to the heart disease model to predict whether the person has heart disease or not.
![image](https://github.com/user-attachments/assets/975e4c46-17d6-4f56-8d46-c792837da164)

### Parkinsons Disease Prediction Page
- **Inputs:** Collects values for features related to Parkinson’s disease prediction (e.g., MDVP - Fo, Jitter percentage).
- **Prediction:** On clicking the "Parkinson’s Test Result" button, the inputs are scaled and passed to the Parkinson’s disease model to predict whether the person has Parkinson’s disease or not.
![image](https://github.com/user-attachments/assets/af4c09b5-bbbc-4210-a968-3b5d425e9025)

### Breast Cancer Prediction Page
- **Inputs:** Collects values for features related to breast cancer prediction (e.g., mean radius, worst texture).
- **Prediction:** On clicking the "Breast Cancer Test Result" button, the inputs are scaled and passed to the breast cancer model to predict whether the cancer is malignant or benign.
![image](https://github.com/user-attachments/assets/25a35a22-14cf-457e-ae7d-3fc3af62ad5c)

The web app is designed to provide users with a simple web interface to input their health data and receive predictions on the likelihood of having certain diseases based on pre-trained machine learning models. The inputs are processed, scaled, and then used to generate predictions, which are displayed as text results on the web page.
