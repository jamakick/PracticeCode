import pandas as pd

tobacco = pd.read_csv("tobacco.csv")

#print(tobacco)

print(tobacco.dtypes)
print(tobacco.shape)

tobacco_in = tobacco[tobacco['LocationAbbr'] == "IN"]

#print(tobacco_in)

#print(tobacco_in[['YEAR', "Gender", "Age", "Data_Value", "Sample_Size"]])

indexedTobacco = tobacco[tobacco["LocationAbbr"] == "IN"][['YEAR', "Gender", "Age", "Data_Value", "Sample_Size"]]

#print(indexedTobacco)

#del tobacco_in['DisplayOrder']
#del tobacco_in['SubMeasureID']
#del tobacco_in['StratificationID4']
#del tobacco_in['StratificationID3']
#del tobacco_in['StratificationID2']
#del tobacco_in['StratificationID1']

columns = tobacco_in.columns

for i in range(1,7):
    del tobacco_in[columns[-i]]

print(tobacco_in)
#
tobaccoFiltered = tobacco[tobacco["Age"] == "Age 20 and Older"][tobacco['LocationAbbr'] == "IN"][tobacco["YEAR"] == "2016"]

tobaccoFiltered = tobaccoFiltered[["YEAR", "LocationDesc", "TopicDesc", "MeasureDesc", "Data_Value", "Education"]]

print(tobaccoFiltered)