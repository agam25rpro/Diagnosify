from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load models
diabetes_model = pickle.load(open("trained_model.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    diagnosis = ''
    if request.method == 'POST':
        try:
            # Get values from the form
            user_input = [
                float(request.form['pregnancies']),
                float(request.form['glucose']),
                float(request.form['bloodpressure']),
                float(request.form['skinthickness']),
                float(request.form['insulin']),
                float(request.form['bmi']),
                float(request.form['diabetespedigree']),
                float(request.form['age'])
            ]
            
            # Make prediction
            prediction = diabetes_model.predict([user_input])
            diagnosis = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
            
        except ValueError:
            diagnosis = 'Please enter valid numerical values'
            
    return render_template('diabetes.html', diagnosis=diagnosis)

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    diagnosis = ''
    if request.method == 'POST':
        try:
            # Get values from the form
            user_input = [
                float(request.form['age']),
                float(request.form['sex']),
                float(request.form['cp']),
                float(request.form['trestbps']),
                float(request.form['chol']),
                float(request.form['fbs']),
                float(request.form['restecg']),
                float(request.form['thalach']),
                float(request.form['exang']),
                float(request.form['oldpeak']),
                float(request.form['slope']),
                float(request.form['ca']),
                float(request.form['thal'])
            ]
            
            # Make prediction
            prediction = heart_disease_model.predict([user_input])
            diagnosis = 'The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease'
            
        except ValueError:
            diagnosis = 'Please enter valid numerical values'
            
    return render_template('heart.html', diagnosis=diagnosis)

@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    diagnosis = ''
    if request.method == 'POST':
        try:
            # Get values from the form
            user_input = [
                float(request.form['fo']),
                float(request.form['fhi']),
                float(request.form['flo']),
                float(request.form['jitter_percent']),
                float(request.form['jitter_abs']),
                float(request.form['rap']),
                float(request.form['ppq']),
                float(request.form['ddp']),
                float(request.form['shimmer']),
                float(request.form['shimmer_db']),
                float(request.form['apq3']),
                float(request.form['apq5']),
                float(request.form['apq']),
                float(request.form['dda']),
                float(request.form['nhr']),
                float(request.form['hnr']),
                float(request.form['rpde']),
                float(request.form['dfa']),
                float(request.form['spread1']),
                float(request.form['spread2']),
                float(request.form['d2']),
                float(request.form['ppe'])
            ]
            
            # Make prediction
            prediction = parkinsons_model.predict([user_input])
            diagnosis = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
            
        except ValueError:
            diagnosis = 'Please enter valid numerical values'
            
    return render_template('parkinsons.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)