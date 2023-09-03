from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import SalaryModelPreparation as mp
import pickle

encoder_edu = LabelEncoder()
encoder_job = LabelEncoder()
encoder_level = LabelEncoder()
encoder_gender = LabelEncoder()
encoder_loc = LabelEncoder()
scaler = MinMaxScaler()
experience_mean = 0
salary_mean = 0
prevSalary_mean = 0

def oneHotEncoderFit(data):
    encoder_edu.fit(data['Education Level'])
    encoder_job.fit(data['Job Title'])
    encoder_level.fit(data['Level'])
    encoder_gender.fit(data['gender'])
    encoder_loc.fit(data['Location'])

def oneHotEncoderTransform(data):
    data['Education Level'] = encoder_edu.transform(data['Education Level'])
    data['Job Title'] = encoder_job.transform(data['Job Title'])
    data['Level'] = encoder_level.transform(data['Level'])
    data['gender'] = encoder_gender.transform(data['gender'])
    data['Location'] = encoder_loc.transform(data['Location'])
    return data

def normalizeRecord(record,minVals,maxVals,columns):
  normalizedValue = []
  i=0
  for col in columns:
      normalizedValue.append((float(record[col])-minVals[i])/(maxVals[i]-minVals[i]))
      i=i+1
  return normalizedValue

def dataProcessor(data):
    dataNullDrop = data.dropna()
    print(type(dataNullDrop))
    oneHotEncoderFit(dataNullDrop)
    dataEncoded = oneHotEncoderTransform(dataNullDrop)
    processedData = dataEncoded.drop(['Employee_id', 'first_name', 'last_name', 'email'], axis=1)
    columns = ['Age', 'Education Level', 'Job Title', 'Level', 'Years of Experience', 'Salary', 'gender', 'Location',
               'Prev Salary']

    experience_mean = processedData['Years of Experience'].mean()
    salary_mean = processedData['Salary'].mean()
    prevSalary_mean = processedData['Prev Salary'].mean()

    y = processedData['Salary']
    X = processedData.drop(['Salary'], axis=1)

    X = scaler.fit_transform(X)

    print('Saving the transformers ...')
    f = open('pickles/scaler.pkl', 'wb')
    pickle.dump(scaler, f)
    f.close()

    print('Saving the encoding ...')
    f = open('pickles/encoder_edu.pkl', 'wb')
    pickle.dump(encoder_edu, f)
    f.close()

    print('Saving the encoding ...')
    f = open('pickles/encoder_job.pkl', 'wb')
    pickle.dump(encoder_job, f)
    f.close()

    print('Saving the encoding ...')
    f = open('pickles/encoder_level.pkl', 'wb')
    pickle.dump(encoder_level, f)
    f.close()

    print('Saving the encoding ...')
    f = open('pickles/encoder_gender.pkl', 'wb')
    pickle.dump(encoder_gender, f)
    f.close()

    print('Saving the encoding ...')
    f = open('pickles/encoder_loc.pkl', 'wb')
    pickle.dump(encoder_loc, f)
    f.close()

    mp.model(X,y)
