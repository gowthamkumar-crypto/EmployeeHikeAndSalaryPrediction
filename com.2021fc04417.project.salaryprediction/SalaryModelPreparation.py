from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pickle

random_forest_reg = RandomForestRegressor(random_state=0)

def model(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
    random_forest_reg.fit(X_train, y_train)
    y_pred = random_forest_reg.predict(X_test)
    score = r2_score(y_pred, y_test)
    print(score)
    dumpModel()

def dumpModel():
    fileName = 'pickles/random_forest_reg_model.pkl'
    pickle.dump(random_forest_reg, open(fileName, 'wb'))

