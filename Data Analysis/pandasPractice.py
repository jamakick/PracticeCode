import pandas as pd

nba = pd.read_csv("NBA_Eastern_Conf.csv")

#print(nba)

print(nba[["Team", "PCT"]].sort_values(by="PCT", ascending = False))
