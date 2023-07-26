
from flask import Flask, request
import numpy as np
import pandas as pd
import ControllerService as cs


app = Flask(__name__)

@app.route("/predict/salary", methods=['POST'])
def getSalaryPrediction():
    preddata = np.array([request.json['Age'], request.json['Education_Level'], request.json['Job_Title'], request.json['Level'],
                          request.json['Years_of_Experience'], request.json['gender'], request.json['Location'], request.json['Prev_Salary'],
                         request.json['first_name'], request.json['last_name'], request.json['email']])
    columns = ['Age', 'Education Level', 'Job Title', 'Level', 'Years of Experience', 'gender', 'Location',
               'Prev Salary','First Name','Last Name','Email']
    predRec = pd.Series(preddata, index=columns)
    return cs.getSalaryPrediction(predRec,columns)


app.run(debug=True)