from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd
import ControllerService as cs


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/predict/salary", methods=['POST'])
def getSalaryPrediction():
    request.json['Age']=relativedelta(date.today(), datetime.strptime(request.json['Age'], '%Y-%m-%d').date()).years
    preddata = np.array([request.json['Age'], request.json['Education_Level'], request.json['Job_Title'], request.json['Level'],
                          request.json['Years_of_Experience'], request.json['gender'], request.json['Location'], request.json['Prev_Salary'],
                         request.json['first_name'], request.json['last_name'], request.json['email']])
    columns = ['Age', 'Education Level', 'Job Title', 'Level', 'Years of Experience', 'gender', 'Location',
               'Prev Salary','First Name','Last Name','Email']
    predRec = pd.Series(preddata, index=columns)
    return cs.getSalaryPrediction(predRec,columns)

@app.route("/roles", methods=['GET'])
def getRoles():
    return jsonify({'roles': cs.getRoles()})

@app.route("/sprint/review", methods=['POST'])
def sprintReview():
    return jsonify(request.json)

@app.route("/login")
def login():
  return jsonify({'success': 'ok'})


app.run(debug=True)