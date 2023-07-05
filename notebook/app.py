import streamlit as st 
import joblib 
import pandas as pd 


# load model and feature engineering pipeline
model = joblib.load("pipeline/Our_Final_Model.pkl")
preprocessor = joblib.load("pipeline/preprocessor.pkl")

def predict_heart_disease():
    st.title("Heart Disease Prediction")
    age = st.slider("Age",min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex",['Male','Female',])
    cp = st.selectbox("Chest Pain Type",['typical angina','atypical angina','non-angina pain','asymptomatic'])
    trestbps = st.slider("Resting Blood Pressure",min_value=50, max_value=250, value=120)
    chol = st.slider("Cholesterol Level",min_value=50,max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar",['presence','absence'])
    restecg = st.selectbox("Resting ECG", ['abnormal','normal'])
    thalach = st.slider("Maximum Heart Rate Achieved",min_value=50, max_value=250,value=150)
    exang = st.selectbox("Exercise Induced Angina", ['presence','absence'])
    oldpeak = st.slider("ST Depression Induced Angina",min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment",['upsloping','flat','downsloping'])
    ca = st.selectbox("Number of major Vessels",['no major vessel','1 major vessel','2 major vessels','3 major vessels'])
    thal = st.selectbox("Thalassemia",['normal','fixed defect','reversable defect'])
    
    if st.button("Predict"):
        user_data = pd.DataFrame(data={
            'age': age ,
    'sex': sex,
    'cp': cp,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg': restecg,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope': slope,
    'ca': ca,
    'thal': thal
        }, index =[0])
        
        
        transformed_data = preprocessor.transform(user_data)
        prediction = model.predict(transformed_data)
        
        if prediction[0] ==1:
            st.markdown("Patient is suffering from heart disease")
        else:
            st.markdown("Patient is not suffering from heart disease")
    
    
if __name__ == "__main__":
    predict_heart_disease()