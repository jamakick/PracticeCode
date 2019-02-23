import pandas as pd, matplotlib.pyplot as plt

contents = pd.read_csv("countries.csv")

#contents.plot(x="Agriculture", y="Literacy", kind='scatter',
#              title="Agriculture/Literacy", grid=True, xlim = [0,1], ylim = [0,1])

contents.plot(y="Population", kind='kde',
              title="Agriculture/Literacy", grid=True)



