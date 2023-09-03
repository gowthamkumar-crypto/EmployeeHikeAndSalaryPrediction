import pickle
import pandas as pd
import SprintReview as sr


def getHikePrediction(inputData,empId):
    data = pd.DataFrame(inputData,index=[0])
    data['Sprint review'] = sr.getEmployeeReview(empId)
    model = pickle.load(open("pickles/hike_model.pkl", "rb"))
    en = pickle.load(open("pickles/hike_encoder.pkl", "rb"))
    sc = pickle.load(open("pickles/hike_scaler.pkl", "rb"))

    data['EmpDepartment'] = en.transform(data['EmpDepartment'])
    predValues = sc.transform(data)
    hikeCategory = model.predict(predValues)

    hikePrecentage = ''
    if(hikeCategory<=1):
        hikePrecentage = '1-2%'
    elif(hikeCategory>1 and hikeCategory<=2):
        hikePrecentage = '5%'
    elif(hikeCategory>2 and hikeCategory<=3):
        hikePrecentage = '7%'
    elif(hikeCategory>3 and hikeCategory<=4):
        hikePrecentage = '10%'
    elif(hikeCategory>4 and hikeCategory<=5):
        hikePrecentage = '15%'

    response = {'hikePercentage':hikePrecentage}

    return response
