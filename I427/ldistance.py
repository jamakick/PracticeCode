# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy

def get_smallest_neighbor(i,j):
    u = matrix[i-1][j]
    l = matrix[i][j-1]
    lu = matrix[i-1][j-1]
    smallest = u
    if l < smallest:
        smallest = 1
    if lu < smallest:
        smallest = lu
    return smallest

term1 = "LOUISIANA"

term2 = "INDIANA"

len1 = len(term1) + 1
len2 = len(term2) + 1

matrix = numpy.zeros((len1, len2))

for i in range(len2):
    matrix[0][i] = i
    
for i in range(len1):
    matrix[i][0] = i

for i in range(1, len1):
    for j in range(1, len2):
        if term1[i-1] == term2[j-1]:
            matrix[i][j] = 0 + get_smallest_neighbor(i,j)
        else:
            matrix[i][j] = 1 + get_smallest_neighbor(i,j)
            
print(matrix)