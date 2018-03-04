# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:08:02 2018

@author: sankarth
"""

#Algorithm Practice - Quick Sort

x = list(map(int,input().split()))
n = len(x)

def swap(a,m,n):
    temp = a[m]
    a[m] = a[n]
    a[n] = temp

def partition(a,start,end):
    pivot = a[end]
    pindex = start
    for i in range(start,end):
        if(a[i]<=pivot):
            swap(a,i,pindex)
            pindex += 1
    swap(a,pindex,end)
    return pindex

def quicksort(a,start,end):
    if(start<end):
        pid = partition(a,start,end)
        quicksort(a,start,pid-1)
        quicksort(a,pid+1,end)

quicksort(x,0,n-1)
print(x)        