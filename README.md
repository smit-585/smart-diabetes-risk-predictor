# 🩺 Smart Diabetes Risk Predictor

A full-stack machine learning web application that predicts the likelihood of diabetes based on patient health parameters. The system uses a trained Random Forest model and provides an intuitive web interface built with Flask.

---

## 🚀 Features

- 🔍 Predicts diabetes risk (High/Low)
- 📊 Displays probability of prediction
- 🌐 User-friendly web interface
- 🧠 Machine Learning model trained on the Pima Indians Diabetes Dataset
- 🧹 Data preprocessing and feature scaling
- 📓 Jupyter Notebook for model development
- 🖥️ Flask-based deployment

---

## 📂 Project Structure
smart-diabetes-risk-predictor/
│
├── app.py # Flask backend
├── diabetes_model.ipynb # Model training notebook
├── diabetes.csv # Dataset
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── models/
│ ├── model.pkl # Trained ML model
│ └── scaler.pkl # Feature scaler
├── templates/
│ └── index.html # Frontend HTML
└── static/
└── style.css # CSS styling


---

## 🧠 Dataset

This project uses the **Pima Indians Diabetes Dataset**, which includes the following features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 🛠️ Tech Stack

| Category | Technology |
|---------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Visualization | Matplotlib |
| Development | Jupyter Notebook |

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-diabetes-risk-predictor.git
cd smart-diabetes-risk-predictor
2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000/
