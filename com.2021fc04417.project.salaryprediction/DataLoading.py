import pandas as pd
import constants as const
import DataProcessor as dp

salaryData = pd.read_csv(const.DataSetLocation)
print(type(salaryData))
dp.dataProcessor(salaryData)