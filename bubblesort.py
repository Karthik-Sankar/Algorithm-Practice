# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:06:37 2018

@author: Karthikeyan Sankar
"""
#Algorithm Practice - BubbleSort
x = list(map(int,input().split()))
n = len(x)

#Swapping Function
def swap(l,a,b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

switch = True # To make the algorithm run for the first time
i = 0
while(i<=n-1 and switch==True):
    switch = False #Initially we dont know wether the bubble pass result in swap
    for j in range(n-1-i):#n-i because we dont have to consider already sorted ones
        if(x[j] > x[j+1]):
            swap(x,j,j+1)
            switch = True
print(x)
