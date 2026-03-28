# 🩺 Multi Disease Prediction System

A Machine Learning-based web application that predicts the likelihood of multiple diseases using patient medical data.

---

## 🚀 Project Overview

This project is developed as part of the **CodeAlpha Machine Learning Internship (Task 4)**.

The system predicts:

* ✅ Diabetes
* ❤️ Heart Disease
* 🎗 Breast Cancer

using trained ML models and a user-friendly web interface built with Streamlit.

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle (for model saving)

---

## 📊 Machine Learning Models

* Random Forest Classifier (for all diseases)
* Trained on medical datasets
* Achieved high accuracy:

  * Diabetes: ~88%
  * Heart Disease: ~94%
  * Breast Cancer: ~96%

---

## 🧾 Features

* Predict multiple diseases from one platform
* Simple and interactive UI
* Real-time prediction
* Displays probability of disease
* Clean and responsive design

---

## 📂 Project Structure

```
CodeAlpha_DiseasePrediction/
│── app.py
│── model.pkl
│── heart_model.pkl
│── cancer_model.pkl
│── README.md
│── .gitignore
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/takia24/CodeAlpha_DiseasePrediction.git
```

2. Navigate to the project folder:

```
cd CodeAlpha_DiseasePrediction
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## 🎯 How It Works

* User inputs medical data
* Data is passed to trained ML model
* Model predicts disease (0 or 1)
* Result is shown with probability

---

## ⚠️ Disclaimer

This project is for educational purposes only.
It is not a substitute for professional medical advice.

---

## 👩‍💻 Author

**Takia Yasmin**
Machine Learning Intern @ CodeAlpha

---

## 🌟 Future Improvements

* Add more diseases
* Improve UI design
* Deploy on cloud (Streamlit Cloud / Render)
* Add user authentication

---

## ⭐ If you like this project, give it a star!
