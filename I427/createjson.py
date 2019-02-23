# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:31:14 2018

@author: lil_t
"""

import json

userhistory = {}

with open('userhistory.json', 'w', encoding="utf8") as histFile:
    json.dump(userhistory, histFile)
