import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# Load the saved models
diabetes_model = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/heart_disease_model.sav', 'rb'))

parkinsons_disease_model = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/parkinsons_disease_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/breast_cancer_model.sav', 'rb'))

# Load the scaler
diabetes_scaler = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/diabetes_scaler.sav', 'rb'))
heart_disease_scaler = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/heart_disease_scaler.sav', 'rb'))
parkinsons_disease_scaler = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/parkinsons_disease_scaler.sav', 'rb'))
breast_cancer_scaler = pickle.load(open('I:/Work/Data Science/Multiple Disease Prediction System using Machine Learning in Python -  Streamlit Web App - Deployment/Models/breast_cancer_scaler.sav', 'rb'))


# Creating sidebar/navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Breast Cancer Prediction'],
                            
                            icons =['heart-pulse',
                                    'heart',
                                    'activity',
                                    'h-square'],
                            
                            default_index = 0)
    
# Diabetes prediction page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using Machine Learning')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age = st.text_input('Age of the person')
    

    # making predictions
    diab_diagnosis = ''

    # create a button for making prediction
    if st.button('Diabetes Test Result'):
        input_data = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
        input_data = diabetes_scaler.transform(input_data)

        diab_prediction = diabetes_model.predict(input_data)
    
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'This person is Diabetic'
        else:
            diab_diagnosis = 'This person is not diabetic'
    st.success(diab_diagnosis)





# Heart Disease Prediction page
if (selected == 'Heart Disease Prediction'):

    #page title
    st.title('Heart Disease Prediction using Machine Learning')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    
    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('cp: Chest Pain Type(1,2,3 or 4)')
    
    with col1:
        trestbps = st.text_input('trestbps: Resting Blood Pressure')

    with col2:
        chol = st.text_input('chol: Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('fbs: Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('restecg: Resting Electrocardiographic Results (values 0,1,2)')

    with col2:
        thalach = st.text_input('thalach: Maximum Heart Rate Achieved')
    
    with col3:
        exang = st.text_input('exang: exercise induced angina')
    
    with col1:
        oldpeak = st.text_input('Oldpeak: ST Depression Induced by Exercise Relative To Rest')
    
    with col2:
        slope = st.text_input('slope: The Slope Of The Peak Exercise ST Segment')
    
    with col3:
        ca = st.text_input('ca: Number Of Major Vessels (0-3) Colored By Flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversable Defect')
    

    # making predictions
    diab_diagnosis = ''

    # create a button for making prediction
    if st.button('Heart Disease Test Result'):
        input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
        input_data = heart_disease_scaler.transform(input_data)

        diab_prediction = heart_disease_model.predict(input_data)
    
        if (diab_prediction[0] == 0):
            diab_diagnosis = 'The person does not have a heart disease'
        else:
            diab_diagnosis = 'The person has heart disease'
    st.success(diab_diagnosis)





# Parkinsons Disease Prediction page
if (selected == 'Parkinsons Disease Prediction'):

    #page title
    st.title('Parkinsons Disease Prediction using Machine Learning')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Fo = st.text_input('MDVP - Fo(Hz)')
    
    with col2:
        Fhi = st.text_input('MDVP - Fhi(Hz)')

    with col3:
        Flo = st.text_input('MDVP - Flo(Hz)')
    
    with col1:
        Jitter_percentage = st.text_input('MDVP - Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP - Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP - RAP')

    with col1:
        PPQ = st.text_input('MDVP - PPQ')

    with col2:
        DDP = st.text_input('Jitter - DDP')
    
    with col3:
        Shimmer = st.text_input('MDVP - Shimmer')
    
    with col1:
        Shimmer_dB = st.text_input('MDVP - Shimmer(dB)')
    
    with col2:
        APQ3 = st.text_input('Shimmer - APQ3')
    
    with col3:
        APQ5 = st.text_input('Shimmer - APQ5')

    with col1:
        APQ = st.text_input('MDVP - APQ')

    with col2:
        DDA = st.text_input('Shimmer - DDA')
    
    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')
    
    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('Spread 1')

    with col2:
        spread2 = st.text_input('Spread 2')
    
    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

       

    # making predictions
    diab_diagnosis = ''

    # create a button for making prediction
    if st.button('Parkinsons Test Result'):
        input_data = np.array([Fo, Fhi, Flo, Jitter_percentage, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]).reshape(1, -1)
        input_data = parkinsons_disease_scaler.transform(input_data)

        diab_prediction = parkinsons_disease_model.predict(input_data)
    
        if (diab_prediction[0] == 0):
            diab_diagnosis = 'This person does not have Parkinsons Disease'
        else:
            diab_diagnosis = 'This person has Parkinsons Disease'
    st.success(diab_diagnosis)

    


# Breast Cancer Prediction Prediction page
if (selected == 'Breast Cancer Prediction'):

    #page title
    st.title('Breast Cancer Prediction using Machine Learning')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('mean radius')
    
    with col2:
        mean_texture = st.text_input('mean texture')

    with col3:
        mean_perimeter = st.text_input('mean perimeter')
    
    with col1:
        mean_area = st.text_input('mean area')

    with col2:
        mean_smoothness = st.text_input('mean smoothness')

    with col3:
        mean_compactness = st.text_input('mean compactness')

    with col1:
        mean_concavity = st.text_input('mean concavity')

    with col2:
        mean_concave_points = st.text_input('mean concave points')
    
    with col3:
        mean_symmetry = st.text_input('mean symmetry')
    
    with col1:
        mean_fractal_dimension = st.text_input('mean fractal dimension')
    
    with col2:
        radius_error = st.text_input('radius error')
    
    with col3:
        texture_error = st.text_input('texture error')

    with col1:
        perimeter_error = st.text_input('perimeter error')

    with col2:
        area_error = st.text_input('area error')
    
    with col3:
        smoothness_error = st.text_input('smoothness error')

    with col1:
        compactness_error = st.text_input('compactness error')

    with col2:
        concavity_error = st.text_input('concavity error')
    
    with col3:
        concave_points_error = st.text_input('concave points error')

    with col1:
        symmetry_error = st.text_input('symmetry error')

    with col2:
        fractal_dimension_error = st.text_input('fractal dimension error')
    
    with col3:
        worst_radius = st.text_input('worst radius')

    with col1:
        worst_texture = st.text_input('worst texture')

    with col2:
        worst_perimeter = st.text_input('worst perimeter')
    
    with col3:
        worst_area = st.text_input('worst area')

    with col1:
        worst_smoothness = st.text_input('worst smoothness')

    with col2:
        worst_compactness = st.text_input('worst compactness')
    
    with col3:
        worst_concavity = st.text_input('worst concavity')

    with col1:
        worst_concave_points = st.text_input('worst concave points')

    with col2:
        worst_symmetry = st.text_input('worst symmetry')
    
    with col3:
        worst_fractal_dimension = st.text_input('worst fractal dimension')
    

    # making predictions
    diab_diagnosis = ''

    # create a button for making prediction
    if st.button('Breast Cancer Test Result'):
        input_data = np.array([mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, 
                               texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, 
                               worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]).reshape(1, -1)
        input_data = breast_cancer_scaler.transform(input_data)

        diab_prediction = breast_cancer_model.predict(input_data)
    
        if (diab_prediction[0] == 0):
            diab_diagnosis = 'The breast cancer is Malignant'
        else:
            diab_diagnosis = 'The breast cancer is Benign'
    st.success(diab_diagnosis)
