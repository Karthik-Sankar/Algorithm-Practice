# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:47:11 2018

@author: sankarth
"""

#This algorithm is to find gcd using euclid's algorithm
def gcd(m,n):
    while(n!=0):
        r = m%n
        m = n
        n = r
    return m

print(gcd(1701,3768))