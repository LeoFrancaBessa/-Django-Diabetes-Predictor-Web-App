from django.shortcuts import render


# our home page view
def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    import pickle
    import os
    BASE = os.path.dirname(os.path.abspath(__file__))
    model = pickle.load(open(os.path.join(BASE, "diabetes_voting.sav"), "rb"))
    scaled = pickle.load(open(os.path.join(BASE, "scaler.sav"), "rb"))
    prediction = model.predict(scaled.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]))

    if prediction == 0:
        return "You don't have Diabetes"
    elif prediction == 1:
        return "You have Diabetes"
    else:
        return "error"


# our result page view
def result(request):
    Pregnancies = int(request.GET['Pregnancies'])
    Glucose = int(request.GET['Glucose'])
    BloodPressure = int(request.GET['BloodPressure'])
    SkinThickness = int(request.GET['SkinThickness'])
    Insulin = int(request.GET['Insulin'])
    BMI = float(request.GET['BMI'])
    DiabetesPedigreeFunction = float(request.GET['DiabetesPedigreeFunction'])
    Age = int(request.GET['Age'])

    result = getPredictions(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

    return render(request, 'result.html', {'result': result})