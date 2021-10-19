import pandas as pd

data = pd.read_csv('https://drive.google.com/uc?id=1JY8l5nSu9O4GtMDpaOfH2Oowlpza3U-c')
print(data.info())
print('-' * 20)
print(data['Age'].value_counts())
dataMale = data.query("Gender == 'M' & Age == '26-35'")['User_ID'].count()
dataFemale = data.query("Gender == 'F' & Age > '35'")['User_ID'].count()
print(dataMale)
print(dataFemale)
count = round((dataMale + dataFemale) / len(data), 4)
print('-' * 20)
print(count)
# dataGA = data.query("Gender == 'F' & Age == '46-50'")
# dataGAP = dataGA[dataGA['Purchase'] > 20000]
# print(len(dataGAP))
# print(data["Product_Category_3"].isna().sum())
