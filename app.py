from flask import Flask, render_template, request
#from flask_cors import cross_origin
#import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('SVM_model.pkl', 'rb'))


@app.route('/')

def Home():
    return render_template('index.html')


@app.route("/predict", methods=["GET", "POST"])

def predict():
    churn = 0
    if request.method == 'POST':
        # Gender
        # AIR ASIA = 0 (not in column)
        gender = request.form['gender']
        if gender == 'Male':
            male = 1
            female = 0

        elif gender == 'Female':
            male = 0
            female = 1

        # Partner
        # AIR ASIA = 0 (not in column)
        partner = request.form['partner']
        if partner == 'Yes':
            yes = 1
            no = 0

        elif partner == 'No':
            yes = 0
            no = 1

        # Dependents
        dependents = request.form['dependents']
        if dependents == 'Yes':
            yes = 1
            no = 0

        elif dependents == 'No':
            yes = 0
            no = 1

        # Phone Service
        phone_service = request.form['phone_service']
        if phone_service == 'Yes':
            yes = 1
            no = 0

        elif phone_service == 'No':
            yes = 0
            no = 1

        # MultipleLines
        multipleLines = request.form['multipleLines']
        if multipleLines == 'Yes':
            yes = 1
            no = 0
            no_phone_service = 0

        elif multipleLines == 'No':
            yes = 0
            no = 1
            no_phone_service = 0

        else:
            yes = 0
            no = 0
            no_phone_service = 1

        # InternetService
        internetService = request.form['internetService']
        if internetService == 'DSL':
            dSL = 1
            no = 0
            fiber_optic = 0

        elif internetService == 'Fiber optic':
            dSL = 0
            fiber_optic = 1
            no = 0

        else:
            dSL = 0
            no = 1
            fiber_optic = 0

        # OnlineSecurity
        onlineSecurity = request.form['onlineSecurity']
        if onlineSecurity == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif onlineSecurity == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # OnlineBackup
        onlineBackup = request.form['onlineBackup']
        if onlineBackup == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif onlineBackup == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # DeviceProtection
        deviceProtection = request.form['DeviceProtection']
        if deviceProtection == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif deviceProtection == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # TechSupport
        techSupport = request.form['techSupport']
        if techSupport == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif techSupport == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # StreamingTV
        streamingTV = request.form['StreamingTV']
        if streamingTV == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif streamingTV == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # StreamingMovies
        streamingMovies = request.form['StreamingMovies']
        if streamingMovies == 'Yes':
            yes = 1
            no = 0
            no_internet_service = 0

        elif streamingMovies == 'No':
            yes = 0
            no_internet_service = 0
            no = 1

        else:
            yes = 0
            no = 0
            no_internet_service = 1

        # PaperlessBilling
        paperlessBilling = request.form['PaperlessBilling']
        if paperlessBilling == 'Yes':
            yes = 1
            no = 0

        elif paperlessBilling == 'No':
            yes = 0
            no = 1

        # PaymentMethod
        paymentMethod = request.form['paymentMethod']
        if paymentMethod == 'Bank transfer (automatic)':
            bank_transfer_automatic = 1
            credit_card_automatic = 0
            electronic_check = 0
            mailed_check = 0

        elif paymentMethod == 'Credit card (automatic)':
            bank_transfer_automatic = 0
            credit_card_automatic = 1
            electronic_check = 0
            mailed_check = 0

        elif paymentMethod == 'Electronic check':
            bank_transfer_automatic = 0
            credit_card_automatic = 0
            electronic_check = 1
            mailed_check = 0

        elif paymentMethod == 'Mailed check':
            bank_transfer_automatic = 0
            credit_card_automatic = 0
            electronic_check = 0
            mailed_check = 1

        # Contract
        contract = request.form['contract']
        if contract == 'Month-to-month':
            month_to_month = 1
            one_year = 0
            two_year = 0

        elif contract == 'One year':
            month_to_month = 0
            two_year = 0
            one_year = 1

        else:
            month_to_month = 0
            one_year = 0
            two_year = 1

        # SeniorCitizen
        seniorCitizen = int(request.form['SeniorCitizen'])

        # tenure
        tenure = int(request.form['tenure'])

        # MonthlyCharges
        monthlyCharges = float(request.form['MonthlyCharges'])

        # TotalCharges
        totalCharges = float(request.form['TotalCharges'])

        prediction = model.predict([[gender, partner, dependents, phone_service, multipleLines, internetService,
                                     onlineSecurity, onlineBackup, deviceProtection, techSupport,
                                     streamingTV, streamingMovies, paperlessBilling, paymentMethod, contract,
                                     seniorCitizen, tenure, monthlyCharges, totalCharges]])

        return render_template('index.html', prediction_text=" Your Customer Churn is {}".format(prediction))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)