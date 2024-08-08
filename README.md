# Multiple Disease Prediction System - Streamlit Web App

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Streamlit Web App](#streamlit-web-app)
  - [Imports](#imports)
  - [Model and Scaler Loading](#model-and-scaler-loading)

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
