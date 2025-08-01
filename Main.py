import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#load the the saved models
with open(r'C:\Users\vinay\OneDrive\Desktop\MDP\saved models\diabetes_model.sav', 'rb') as file:
    diabetes_model = pickle.load(file)
with open(r'C:\Users\vinay\OneDrive\Desktop\MDP\saved models\heart_disease_model.sav', 'rb') as file:
    heart_disease_model = pickle.load(file)
with open(r'C:\Users\vinay\OneDrive\Desktop\MDP\saved models\parkinsons_model.sav', 'rb') as file:
    parkinsons_model = pickle.load(file)

# sidebar
with st.sidebar:
    selected = option_menu(
        "Health Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=['activity', 'heart', 'person'],
        default_index=0
        )
# diabetes prediction
if selected == "Diabetes Prediction":

    #page title
    st.title("Diabetes Prediction using ML")

    # getting the input data from the user
    #colmns for input
    col1, col2, col3 = st.columns(3)
    with col1:
        Pragnencies = st.text_input("Number of Pragnencies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age of the Person")
    


    # code for prediction
    diab_dignosis = ''

    # button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pragnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_dignosis = 'The person is diabetic'
        else:
            diab_dignosis = 'The person is not diabetic'
    st.success(diab_dignosis)

# Heart disease prediction
elif selected == "Heart Disease Prediction":

    #page title
    st.title("Heart Disease Prediction using ML")
    # getting the input data from the user
    #colmns for input
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results (0-2)")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina (1 = yes; 0 = no)")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise Relative to Rest")
    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")
    with col3:
        ca = st.text_input("Number of Major Vessels (0-3) Colored by Fluoroscopy")
    with col1:
        thal = st.text_input("Thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect)")
    with col2:
        target = st.text_input("Heart Disease (1 = presence; 0 = absence)")
    
    # code for prediction
    heart_disease_diagnosis = ''

    # button for prediction
    if st.button("Heart Disease Test Result"):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_disease_prediction[0] == 1:
            heart_disease_diagnosis = 'The person has heart disease'
        else:
            heart_disease_diagnosis = 'The person does not have heart disease'
    st.success(heart_disease_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
