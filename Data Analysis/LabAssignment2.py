import numpy as np

contents = np.loadtxt("salaries.csv",dtype=str, delimiter=",")

#print(contents)

names = []

salaries = []

for item in contents:
    names.append(item[0])
    salaries.append(item[1])
    
names = np.array(names)

salaries = np.array(salaries, float)

names = np.where(names=='ï»¿TD-DEPARTMENT OF TRANSPORTATION', 'TD-DEPARTMENT OF TRANSPORTATION', names)

#print(names)

nameBools = names == "HS-DEPARTMENT OF HOMELAND SECURITY"

#print(nameBools)

homelandAvg = round(np.mean(salaries[nameBools]), 2)




allAvg = []

for name in np.unique(names):
    newBools = names == name
    newAvg = round(np.mean(salaries[newBools]), 2)
    allAvg.append([name, newAvg])
    
avgArray = np.array(allAvg)

np.savetxt("agencyAverageSalaries.csv", avgArray, fmt="%s", delimiter=",")