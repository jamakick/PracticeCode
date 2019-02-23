import pandas as pd

contents = pd.read_csv("LaqnData.csv")

beforeDupes = len(contents)

#drops 60 duplicates found in the csv file
contents = contents.drop_duplicates()

afterDupes = len(contents)

print(str(int(beforeDupes) - int(afterDupes)) + " Duplicate rows were found.")

numCol = len(contents.columns)

contents = contents.dropna(thresh = numCol - 2)

afterDrops = len(contents)

print(str(int(afterDupes) - int(afterDrops)) + " records missing 2 or more columns of data were found.")

print(contents["Provisional or Ratified"].value_counts())


