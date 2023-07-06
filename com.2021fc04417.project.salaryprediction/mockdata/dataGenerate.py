import csv
import random
import math

import pandas as pd


def getExp(l):
    if(l==1):
        return "{0:.1f}".format(random.uniform(0,4))
    elif(l==2):
        return "{0:.1f}".format(random.uniform(5, 7.5))
    else:
        return "{0:.1f}".format(random.uniform(7, 11))

def getExp2(l):
    if(l==1):
        return "{0:.1f}".format(random.uniform(5,8))
    elif(l==2):
        return "{0:.1f}".format(random.uniform(8.5, 15))
    else:
        return "{0:.1f}".format(random.uniform(13, 24))

def getAge(exp):
    return math.ceil(exp) + random.randrange(0, 4)

def getEdu(age,exp):
    if(age-exp-22==0):
        return 'Bachelor\'s'
    elif(age-exp-22>0 and age-exp-22<=2):
        return 'Masters\'s'
    else:
        return 'Phd'

def getSal(l):
    sal = 0
    if (l == 1):
        sal = ((math.floor(random.randrange(650000, 900000) / 1000))*1000)
    elif (l == 2):
        sal = ((math.floor(random.randrange(1000000, 1800000) / 1000)) * 1000)
    else:
        sal = ((math.floor(random.randrange(2000000, 3000000) / 1000)) * 1000)
    return sal



data = []
header = ["Age","Education Level","Job Title","Level","Years of Experience","Salary"]
for i in range(0,1000):
    level = random.randrange(1, 3)
    exp = float(getExp(level))
    age = getAge(exp)+22
    education = getEdu(age, exp)
    job_title = "Data Scientist"
    salary = getSal(level)
    data.append([age,education,job_title,level,exp,salary])

df = pd.DataFrame(data, columns=["Age","Education Level","Job Title","Level","Years of Experience","Salary"])
df.to_csv('resources/sn15_data.csv')

# with open('resources/data.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#
#     # write the header
#     writer.writerow(header)
#
#     # write the data
#     writer.writerow(data)