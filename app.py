import streamlit as st
import pandas as pd
import joblib


model = joblib.load('gym_model.pkl')


st.set_page_config(page_title="Gym Calories Predictor", page_icon="🏋️‍♂️")
st.title("🏋️‍♂️ Gym Calories Burned Predictor")
st.write("กรอกข้อมูลการออกกำลังกายเพื่อทำนายปริมาณแคลอรี่ที่เผาผลาญ")


col1, col2 = st.columns(2)


with col1:
    age = st.number_input("อายุ (Age)", min_value=18, max_value=100, value=25)
    gender = st.selectbox("เพศ (Gender)", ["Male", "Female"])
   
    membership = st.selectbox("ประเภทสมาชิก", ["Annual", "Quarterly", "Monthly"])

with col2:
   
    workout_type = st.selectbox("ประเภทการเล่น", ["HIIT", "Strength Training", "Cardio", "CrossFit", "Yoga"])
    duration = st.slider("ระยะเวลา (นาที)", 10, 120, 45)



if st.button("Predict Calories"):
  
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'membership_type': [membership],
        'workout_type': [workout_type],
        'workout_duration_minutes': [duration]
    })
    

    prediction = model.predict(input_data)[0]
    

    st.success(f"🔥 คาดว่าคุณจะเผาผลาญได้ประมาณ: **{prediction:.2f} แคลอรี่**")
    st.balloons()
