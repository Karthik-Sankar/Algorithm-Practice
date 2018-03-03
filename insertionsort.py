# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:50:11 2018

@author: sankarth
"""

#Algorithm Practice - InsertionSort
x = list(map(int,input().split()))
n = len(x)

for j in range(1,n):#Starting from element 2
    key = x[j]
    i = j-1
    while(i>=0 and x[i]>key):
        x[i+1] = x[i]
        i -= 1
    x[i+1] = key
print(x)