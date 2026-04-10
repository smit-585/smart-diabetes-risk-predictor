from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('models/model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bp = float(request.form['bp'])
        skin = float(request.form['skin'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = float(request.form['age'])

        # Prepare input data
        input_data = np.array([[pregnancies, glucose, bp, skin,
                                insulin, bmi, dpf, age]])

        # Scale the input
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        return render_template(
            'index.html',
            result=int(prediction),
            prob=round(probability * 100, 2)
        )

    except Exception as e:
        return render_template(
            'index.html',
            error=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)