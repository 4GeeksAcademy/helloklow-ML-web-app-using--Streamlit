import pickle
import pandas as pd
from flask import Flask, request, render_template

# Load the model
model_file='models/model.pkl'

with open(model_file, 'rb') as input_file:
    model=pickle.load(input_file)

# Define the flask application
app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':

        Glucose = float(request.form["Glucose"])
        Insulin = float(request.form["Insulin"])
        BMI = float(request.form["BMI"])
        Age = float(request.form["Age"])
        
        data = pd.DataFrame([[Glucose, Insulin, BMI, Age]], columns= ['Glucose', 'Insulin', 'BMI', 'Age'])

        prediction = model.predict(data)[0]

        pred_class = "Diabetic" if prediction == 1 else "non-diabetic"
    else:
        pred_class = None

    # Return the result to flask
    return render_template('index.html', prediction=pred_class)