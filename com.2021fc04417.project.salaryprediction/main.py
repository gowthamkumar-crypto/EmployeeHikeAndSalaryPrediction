import pandas as pd
import matplotlib.pyplot as plt

rawData = pd.read_csv("resources/SalaryDataset.csv")
print(rawData.head())

# printing info of the data
print("Info of the dataset:")
print(rawData.info)
# df = rawData.sample(frac=1)
# df.to_csv('resources/Salary Data.csv')
# print(df.head())

# exp_role_sal = rawData.filter(["Age","Education Level","Job Title","Years of Experience","Salary"])
# print(exp_role_sal.describe())