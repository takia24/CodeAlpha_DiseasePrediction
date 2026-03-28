import streamlit as st
import pickle
import numpy as np

# Load models
diabetes_model = pickle.load(open("model.pkl", "rb"))
heart_model = pickle.load(open("heart_model.pkl", "rb"))
cancer_model = pickle.load(open("cancer_model.pkl", "rb"))

st.set_page_config(page_title="Multi Disease Prediction", layout="wide")

st.title("🩺 Multi Disease Prediction System")

# Sidebar
disease = st.sidebar.radio(
    "Select Disease",
    ["Diabetes", "Heart Disease", "Breast Cancer"]
)

# ---------------- DIABETES ----------------
if disease == "Diabetes":
    st.header("🧪 Diabetes Prediction")

    preg = st.number_input("Pregnancies", min_value=0.0)
    glucose = st.number_input("Glucose", min_value=0.0)
    bp = st.number_input("Blood Pressure", min_value=0.0)
    skin = st.number_input("Skin Thickness", min_value=0.0)
    insulin = st.number_input("Insulin", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0.0)

    if st.button("Predict Diabetes"):
        data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
        result = diabetes_model.predict(data)

        if result[0] == 1:
            st.error("⚠️ Diabetes Detected")
        else:
            st.success("✅ No Diabetes")

# ---------------- HEART ----------------
elif disease == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")

    age = st.number_input("Age", min_value=0.0)
    sex = st.number_input("Sex (1=Male, 0=Female)", min_value=0.0, max_value=1.0)
    cp = st.number_input("Chest Pain Type (0-3)", min_value=0.0, max_value=3.0)
    trestbps = st.number_input("Resting BP", min_value=0.0)
    chol = st.number_input("Cholesterol", min_value=0.0)
    fbs = st.number_input("Fasting Blood Sugar", min_value=0.0, max_value=1.0)
    restecg = st.number_input("Rest ECG (0-2)", min_value=0.0, max_value=2.0)
    thalach = st.number_input("Max Heart Rate", min_value=0.0)
    exang = st.number_input("Exercise Induced Angina (1=Yes,0=No)", min_value=0.0, max_value=1.0)
    oldpeak = st.number_input("Oldpeak", min_value=0.0)
    slope = st.number_input("Slope (0-2)", min_value=0.0, max_value=2.0)
    ca = st.number_input("Number of vessels (0-4)", min_value=0.0, max_value=4.0)
    thal = st.number_input("Thal (1-3)", min_value=0.0, max_value=3.0)

    if st.button("Predict Heart Disease"):

        # Correct order
        data = np.array([[
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak,
            slope, ca, thal
        ]])

        result = heart_model.predict(data)
        proba = heart_model.predict_proba(data)

        # Show debug
        st.write("📊 Probability:", proba)

        # Rule-based score
        risk_score = 0
        if trestbps > 140: risk_score += 1
        if chol > 240: risk_score += 1
        if oldpeak > 2: risk_score += 1
        if ca >= 2: risk_score += 1
        if thal == 3: risk_score += 1

        # Final decision
        if proba[0][1] > 0.3 or risk_score >= 2:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ No Heart Disease")

# ---------------- CANCER ----------------
elif disease == "Breast Cancer":
    st.header("🎗️ Breast Cancer Prediction")

    radius = st.number_input("Radius Mean", min_value=0.0)
    texture = st.number_input("Texture Mean", min_value=0.0)
    perimeter = st.number_input("Perimeter Mean", min_value=0.0)
    area = st.number_input("Area Mean", min_value=0.0)
    smoothness = st.number_input("Smoothness Mean", min_value=0.0)
    compactness = st.number_input("Compactness Mean", min_value=0.0)

    if st.button("Predict Cancer"):
        data = np.array([[radius, texture, perimeter, area, smoothness, compactness]])
        result = cancer_model.predict(data)

        if result[0] == 1:
            st.error("⚠️ Malignant (Cancer Detected)")
        else:
            st.success("✅ Benign (No Cancer)")