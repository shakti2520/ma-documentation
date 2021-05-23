from logging import error
from flask import Flask, request, render_template
import json
import numpy as np
import requests


app = Flask(__name__)


BASE = "https://ma-api-call.herokuapp.com/"

####################################### Home screen ##########################
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/ApiCall')
def apiCall():
    return render_template('ApiCall.html')


@app.route('/objectModel')
def objectModel():
    return render_template('objectModel.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    details = request.form
    response = requests.get(BASE+"predict", {"sex": details["sex"],
                                             "age": details["age"],
                                             "education": details["education"],
                                             "currentSmoker": details["currentSmoker"],
                                             "cigsPerDay": details["cigsPerDay"],
                                             "BPMeds": details["BPMeds"],
                                             "prevalentStroke": details["prevalentStroke"],
                                             "prevalentHyp": details["prevalentHyp"],
                                             "diabetes": details["diabetes"],
                                             "sysBP": details["sysBP"],
                                             "diaBP": details["diaBP"],
                                             "BMI": details["BMI"],
                                             "heartRate": details["heartRate"],
                                             "glucose": details["glucose"]})
    return response.json()



if __name__ == "__main__":
    app.run(debug=True)
