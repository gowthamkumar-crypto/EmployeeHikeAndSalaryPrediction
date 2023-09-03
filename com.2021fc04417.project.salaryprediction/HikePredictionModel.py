import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV



def model(X_train, X_test, y_train, y_test):
    classifier_rfg = RandomForestClassifier(random_state=33, n_estimators=23)
    parameters = [{'min_samples_split': [2, 3, 4, 5], 'criterion': ['gini', 'entropy'], 'min_samples_leaf': [1, 2, 3]}]
    model_gridrf = GridSearchCV(estimator=classifier_rfg, param_grid=parameters, scoring='accuracy', cv=10)
    model_gridrf.fit(X_train, y_train)
    y_predict_rf = model_gridrf.predict(X_test)
    print('accuracy score:')
    print(accuracy_score(y_test, y_predict_rf))
    print('classification report:')
    print(classification_report(y_test, y_predict_rf))
    fileName = 'pickles/hike_model.pkl'
    pickle.dump(model_gridrf, open(fileName, 'wb'))
