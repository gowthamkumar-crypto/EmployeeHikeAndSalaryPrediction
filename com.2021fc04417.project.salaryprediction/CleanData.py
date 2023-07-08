
def removeNull(data):
    data = data.dropna()
    return data

def printNullCount(data):
    for col in data.columns:
        print(col +":"+str(data[col].isna().sum()))