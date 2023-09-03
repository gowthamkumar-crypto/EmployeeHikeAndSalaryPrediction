import os
import pickle
import DataProcessor as dp
import numpy as np
import pandas as pd
import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.simplefilter("error", InconsistentVersionWarning)
import sys
import json
import DBConnection as db



def getSalaryPrediction(predRec,columns):
    predValue = 0
    role_id = db.getRoleIdByRoleName(predRec["Job Title"])
    level_id = db.getLevelIdByRoleNameAndLevel(role_id,predRec["Level"])
    saveRec = predRec


    predRec = predRec.drop(['First Name','Last Name','Email'])
    columns = columns[:8]
    try:
        model = pickle.load(open("pickles/random_forest_reg_model.pkl", "rb"))
        encoder_edu = pickle.load(open("pickles/encoder_edu.pkl", "rb"))
        encoder_gender = pickle.load(open("pickles/encoder_gender.pkl", "rb"))
        encoder_job = pickle.load(open("pickles/encoder_job.pkl", "rb"))
        encoder_level = pickle.load(open("pickles/encoder_level.pkl", "rb"))
        encoder_loc = pickle.load(open("pickles/encoder_loc.pkl", "rb"))
        scaler = pickle.load(open("pickles/scaler.pkl", "rb"))

        predRec['Education Level'] = encoder_edu.transform(pd.Series(predRec['Education Level']))[0]
        predRec['Job Title'] = encoder_job.transform(pd.Series(predRec['Job Title']))[0]
        predRec['Level'] = encoder_level.transform(pd.Series(predRec['Level']))[0]
        predRec['gender'] = encoder_gender.transform(pd.Series(predRec['gender']))[0]
        predRec['Location'] = encoder_loc.transform(pd.Series(predRec['Location']))[0]
        rec = dp.normalizeRecord(predRec, scaler.data_min_, scaler.data_max_, columns)
        rec = np.asarray(rec, dtype=np.float32)
        data = rec.reshape(1, -1)

        predictedSalary = model.predict(data)[0]
    except InconsistentVersionWarning as w:
        print(w.original_sklearn_version)

    emp_id = db.saveCandiate(saveRec, role_id, level_id, predictedSalary)

    message = ''
    if(float(saveRec["Prev Salary"])>predictedSalary):
        message = 'Candiate experience does not balance with the level of the role and salary'
    elif(abs(float(saveRec["Prev Salary"])-predictedSalary)<100000):
        message = 'Candiate just fits into the level of the role'
    else:
        message = 'Great Match'



    emp_name = saveRec["First Name"] +' '+saveRec["Last Name"]
    dataObj = {'employeeId': str(emp_id),'employeeName': emp_name, 'employeeRole': str(predRec["Job Title"]), 'level': str(predRec["Level"]),"predictedSalary":predictedSalary,
               'message':message}
    resObj = {'Status': 'Employee saved successfully','employeeData':dataObj}
    response = json.dumps(resObj, indent=4)
    return response

def getRoles():
    return db.getRoles()
