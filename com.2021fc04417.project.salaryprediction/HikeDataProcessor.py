import pickle

import pandas as pd
import sys

from sklearn.model_selection import train_test_split

sys.path.append('/')
import constants as const
import HikePredictionModel as hikeModel
from sklearn.preprocessing import LabelEncoder, StandardScaler


hikeData = pd.read_csv(const.hikeDataSetLocation)

enc = LabelEncoder()
for i in (2,3,4,6,7,16,26,5):
    hikeData.iloc[:,i] = enc.fit_transform(hikeData.iloc[:,i])

hikeData.drop(['EmpNumber'],inplace=True,axis=1)

y = hikeData.PerformanceRating
X = hikeData.iloc[:,[4,5,9,16,20,21,22,23,24,26]]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
hikeModel.model(X_train, X_test, y_train, y_test)

# encoderFileName = '../pickles/hike_encoder.pkl'
# pickle.dump(enc, open(encoderFileName, 'wb'))
#
# scalerFileName = '../pickles/hike_scaler.pkl'
# pickle.dump(sc, open(scalerFileName, 'wb'))