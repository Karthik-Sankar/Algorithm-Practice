# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:59:05 2018

@author: sankarth
"""

#Algorithm Practice - MergeSort
x = list(map(int,input().split()))
n = len(x)

def merge(l,r,a):
    nl = len(l)
    nr = len(r)
    i = 0 #Pointer for l
    j = 0 #Pointer for r
    k = 0 #Pointer for a
    while(i<nl and j<nr):
        if(l[i]<r[j]):
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while(i<nl):
        a[k] = l[i]
        i += 1
        k += 1
    while(j<nl):
        a[k] = r[j]
        j += 1
        k += 1
        
def merge_sort(a):
    n = len(a)
    if(n == 1):
        return
    mid = n//2
    # Copying left array
    left = [a[i] for i in range(0,mid)]
    # Copying right array
    right = [a[i] for i in range(mid,n)]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,a)
    
merge_sort(x)
print(x)