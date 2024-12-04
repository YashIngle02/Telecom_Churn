#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    form_data = request.form
    
    # Extract input values from the form
    
    senior_citizen = int(form_data['SeniorCitizen'])
    partner = 1 if form_data['Partner'] == 'Yes' else 0
    dependents = 1 if form_data['Dependents'] == 'Yes' else 0
    tenure = float(form_data['tenure'])
    
    multiple_lines = 1 if form_data['MultipleLines'] == 'Yes' else 0
    internet_service = int(form_data['InternetService'])
    online_security = 1 if form_data['OnlineSecurity'] == 'Yes' else 0
    online_backup = 1 if form_data['OnlineBackup'] == 'Yes' else 0
    device_protection = 1 if form_data['DeviceProtection'] == 'Yes' else 0
    tech_support = 1 if form_data['TechSupport'] == 'Yes' else 0
    streaming_tv = 1 if form_data['StreamingTV'] == 'Yes' else 0
    streaming_movies = 1 if form_data['StreamingMovies'] == 'Yes' else 0
    contract = int(form_data['Contract'])
    paperless_billing = 1 if form_data['PaperlessBilling'] == 'Yes' else 0
    payment_method = int(form_data['PaymentMethod'])
    monthly_charges = float(form_data['MonthlyCharges'])
    total_charges = float(form_data['TotalCharges'])
    Avg_monthly_Charges = float(form_data['Avg_monthly_Charges'])

    # Create a feature vector for prediction
    features = np.array([[
        senior_citizen, partner, dependents, tenure,
        multiple_lines, internet_service, online_security, online_backup,
        device_protection, tech_support, streaming_tv, streaming_movies,
        contract, paperless_billing, payment_method, monthly_charges, total_charges,Avg_monthly_Charges
    ]])
    
    # Make prediction
    prediction = model.predict(features)
    output = "Yes" if prediction[0] == 1 else "No"

    return render_template('index.html', prediction_text=f'Churn Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




