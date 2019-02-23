# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:19:57 2018

@author: lil_t
"""

import json, random

username="Jake"

with open('userhistory.json', 'r', encoding="utf8") as histFile:
    histories = json.load(histFile)
    
recommendations = []
    
try:
    for user in histories.keys():
        if user != username:
            userhist = histories[user]
            
            for term in histories[username]:
                if term in userhist:
                    
                    for simterm in userhist:
                        if simterm != term:
                            if simterm not in histories[username]:
                                recommendations.append([user, simterm])
    
    random.shuffle(recommendations)
    try:
        recommend = recommendations[0:4]
    except:
        recommend = recommendations[0:4]
except:
    recommend = ["No user", "No recommendation"]
