# 🏥 Early Disease Prediction System Using AI & ML

An intelligent healthcare application that leverages Machine Learning to predict the risk of three major lifestyle diseases: **Diabetes**, **Heart Disease**, and **Hypertension** at an early stage, enabling timely medical intervention and preventive care.

---

## 📋 Project Overview

The **Early Disease Prediction System** is a web-based application designed to help users assess their risk of developing chronic diseases before symptoms become severe. By analyzing health parameters such as glucose levels, blood pressure, cholesterol, BMI, and lifestyle factors, the system uses trained Machine Learning models to provide accurate risk assessments.

### Problem Statement
Millions of people worldwide are diagnosed with lifestyle diseases at advanced stages due to lack of early detection and awareness. This project aims to bridge that gap by providing an accessible, AI-powered tool for early risk prediction.

### Objectives
- Develop accurate ML models for predicting Diabetes, Heart Disease, and Hypertension.
- Create a user-friendly web interface for easy health data input.
- Provide personalized health recommendations based on risk levels.
- Enable users to track their health history over time.

---

## ✨ Features

- **AI-Powered Predictions:** Analyzes user health data to predict disease risks.
- **Multi-Disease Support:** Evaluates risks for Diabetes, Heart Disease, and Hypertension.
- **Risk Classification:** Categorizes results into Low, Medium, and High risk levels.
- **Personalized Recommendations:** Provides health tips based on the prediction results.
- **Secure Data Storage:** Stores user data and prediction history in a secure database.
- **User-Friendly Interface:** Easy-to-use web interface for data input and result viewing.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, Joblib |
| **Database** | SQLite |

---

## 📁 Project Structure

```text
Early-Disease-Prediction-System-/
│
├── backend/
│   ├── app.py                 # Main Flask application and API routes
│   ├── train_models.py        # Script to train ML models
│   ├── requirements.txt       # Python dependencies
│   └── trained_models/        # Saved .pkl model files
│
├── frontend/
│   ├── login.html             # User login page
│   ├── dashboard.html         # User dashboard
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
│
├── datasets/
│   ├── diabetes.csv           # Dataset for Diabetes
│   ├── heart_disease.csv      # Dataset for Heart Disease
│   └── hypertension.csv       # Dataset for Hypertension
│
└── README.md
