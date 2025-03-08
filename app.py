import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from chatbot_logic import predict_lung_cancer, analyze_chat

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.title("🩺 Risk Assessment")
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.slider("Age", 10, 100, 30)
    smoking = st.radio("Do you smoke?", ["Yes", "No"])
    yellow_fingers = st.radio("Yellow fingers?", ["Yes", "No"])
    anxiety = st.radio("Anxiety?", ["Yes", "No"])
    peer_pressure = st.radio("Peer pressure?", ["Yes", "No"])
    chronic_disease = st.radio("Chronic disease?", ["Yes", "No"])
    fatigue = st.radio("Fatigue?", ["Yes", "No"])
    allergy = st.radio("Allergies?", ["Yes", "No"])
    wheezing = st.radio("Wheezing?", ["Yes", "No"])
    alcohol = st.radio("Alcohol?", ["Yes", "No"])
    coughing = st.radio("Coughing?", ["Yes", "No"])
    shortness_of_breath = st.radio("Shortness of breath?", ["Yes", "No"])
    swallowing_difficulty = st.radio("Swallowing difficulty?", ["Yes", "No"])
    chest_pain = st.radio("Chest pain?", ["Yes", "No"])

    def encode_input(value):
        return 1 if value == "Yes" else 0

    inputs = [
        1 if gender == "Male" else 0,
        age,
        encode_input(smoking),
        encode_input(yellow_fingers),
        encode_input(anxiety),
        encode_input(peer_pressure),
        encode_input(chronic_disease),
        encode_input(fatigue),
        encode_input(allergy),
        encode_input(wheezing),
        encode_input(alcohol),
        encode_input(coughing),
        encode_input(shortness_of_breath),
        encode_input(swallowing_difficulty),
        encode_input(chest_pain),
    ]

    if st.button("Check Risk"):
        result = predict_lung_cancer(inputs)
        st.success(result)

with col2:
    st.title("💬 Chat Assistant")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about lung cancer..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = analyze_chat(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})