# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:04:07 2018

@author: lil_t
"""

import json

with open('pageranks.json', 'r', encoding="utf8") as rankFile:
    pageRanks = json.load(rankFile)
    
    
print(pageRanks)