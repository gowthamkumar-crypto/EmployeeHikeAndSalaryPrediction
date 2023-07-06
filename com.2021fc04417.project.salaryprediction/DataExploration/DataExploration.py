import os

import pandas as pd
import matplotlib.pyplot as plt

salaryData = pd.read_csv("../resources/SalaryDataset.csv")

#printing top 5 records
print("top 5 records :")
print(salaryData.head(5))

#printing info about data
print("info about columns :")
print(salaryData.info())

