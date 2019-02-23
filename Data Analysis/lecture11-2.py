# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:36:14 2019

@author: jamakick
"""

import pandas as pd

#contents = pd.read_csv("tips.csv")
#
#
#contents['tip_pct'] = contents['tip'] / contents['total_bill']
#
#
#print(contents)
#
##for item in contents.columns:
##        print(contents.groupby(item)[item].count())
#
#for item in contents.columns:
#    print(contents.groupby(item)['tip_pct'].mean())

contents = pd.read_csv("debt.csv", index_col = "year")

print(contents)

def decades(year):
    year = str(year)
    decade = year[0:3]
    return decade

print(decades(1985))
            
#print(contents.groupby(decades)["year"].agg(['mean', 'std', 'count']))