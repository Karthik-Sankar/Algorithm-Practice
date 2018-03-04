# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:25:42 2018

@author: sankarth
"""

#binary to decimal
x = input()
length = len(x)
dec = 0
oc = 0
for i in range(length):
    temp = int(x[i])
    dec += temp*(2**(length-i-1))
print(dec)