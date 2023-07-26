import pickle
import DataProcessor as dp
import numpy as np
import pandas as pd
import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.simplefilter("error", InconsistentVersionWarning)
import DBConnection as db
import json


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

    emp_id = db.saveEmployee(saveRec,role_id,level_id,predictedSalary)
    emp_name = saveRec["First Name"] +' '+saveRec["Last Name"]
    dataObj = {'Employee_id': str(emp_id),'Employee_name': emp_name, 'Employee_role': str(predRec["Job Title"]), 'Level': str(predRec["Level"]),"Predicted Salary":predictedSalary}
    resObj = {'Status': 'Employee saved successfully','Employee Data':dataObj}
    response = json.dumps(resObj, indent=4)
    return str(response)