import streamlit as st
import pandas as pd
import joblib

#load model and preprocessor 
model = joblib.load("model/Classification_model.pkl")
preprocessor = joblib.load("model/preprocessor.pkl")
# Define the Streamlit app
def predict_heart_disease():
    st.title('Heart Disease Prediction')
    
    # Create input form
    age = st.slider('Age', min_value=1, max_value=100, value=30)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
    trestbps = st.slider('Resting Blood Pressure', min_value=50, max_value=250, value=120)
    chol = st.slider('Cholesterol Level', min_value=50, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar', ['absence', 'presence'])
    restecg = st.selectbox('Resting ECG', ['normal', 'abnormal'])
    thalach = st.slider('Maximum Heart Rate Achieved', min_value=50, max_value=250, value=150)
    exang = st.selectbox('Exercise Induced Angina', ['absence', 'presence'])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['upsloping', 'flat', 'downsloping'])
    ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['no major vessel', '1 major vessel', '2 major vessels', '3 major vessels'])
    thal = st.selectbox('Thalassemia', ['normal', 'fixed defect', 'reversable defect'])
    
    # Create prediction button
    if st.button('Predict'):
        new_user_data = pd.DataFrame(data={
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        })
        
        transform_data = preprocessor.transform(new_user_data)
        prediction = model.predict(transform_data)
        
        if prediction[0] == 1:
            st.markdown('### Diagnosis: Heart Disease Detected')
        else:
            st.markdown('### Diagnosis: No Heart Disease Detected')

# Run the Streamlit app
if __name__ == '__main__':
    predict_heart_disease()
