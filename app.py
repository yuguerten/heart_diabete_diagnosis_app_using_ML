import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

#loading the models {'diabests_disease' , 'heart_disease'}

diabets_model = pickle.load(open('diabets_disease_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))

#sidebar for navigation : 

with st.sidebar:
    selected = option_menu('Disease Prediction System ' ,['Diabests Disease Prediction' ,'Heart Disease Prediction'],
                           menu_icon = 'hospital-fill' , icons = ['activity', 'heart' , 'person'] ,
                           default_index = 0)

    
if selected == 'Diabests Disease Prediction':
    #page title 
    st.title("Diabets Prediction using Machine Learning ")

    #define columns names for user input data

    col1 , col2 , col3 = st.columns(3)

    with col1:
        Pregnanacies = st.text_input('Number of Pragrancies')

    with col2 :
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure level')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    # creating a button so lunch the prediction system

    if st.button('Diabetes Test Result :)'):
        user_input = [Pregnanacies , Glucose , BloodPressure ,SkinThickness,Insulin , BMI ,DiabetesPedigreeFunction , Age ]
        user_as_np = np.asarray(user_input)
        input_data_reshaped = user_as_np.reshape(1,-1)
        diab_prediction = diabets_model.predict(input_data_reshaped.astype(float))

        if diab_prediction == 0 :
            diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis,icon="✅")
        else:
            diab_diagnosis = 'The perosn is diabatic'
            st.error(diab_diagnosis , icon="🚨")
if selected == 'Heart Disease Prediction' :

    st.title('Heart Disease Prediction using Machine Learning')

    col1 , col2 , col3 = st.columns(3)

    with col1 :
        Age = st.text_input("Age of the Person")
    
    with col2 :
        Sex = st.text_input("Gender of the person")
    
    with col3 :
        RestingBP = st.text_input("Resting Blood Pressure value")
    
    with col1 :
        Cholesterol = st.text_input("Cholesterol value")
    
    with col2 :
        FastingBS = st.text_input("Fasting Blood Sugar value")
    
    with col3 :
        MaxHR = st.text_input("Maximum Heart Rate")
    
    with col1 :
        OldPeak = st.text_input("ST depression induced by exercise")
    
    heart_diagnosis = ''

    if st.button('heart test result'):
        if Sex == 'Male':
            Sex = 1
        else:
            Sex = 0
        user_input = [Age ,Sex ,  RestingBP , Cholesterol , FastingBS , MaxHR , OldPeak]
        user_as_np = np.asarray(user_input)
        input_data_reshaped = user_as_np.reshape(1,-1)
        heart_prediction = heart_model.predict(input_data_reshaped.astype(float))
        
        if heart_prediction == 0 :
                heart_diagnosis = 'The person does not have any heart disease'
                st.success(heart_diagnosis,icon="✅")
        else:
                heart_diagnosis = 'The person is having heart disease'
                st.error(heart_diagnosis , icon="🚨")

    






