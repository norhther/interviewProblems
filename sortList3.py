# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:20:33 2020

@author: norhther
"""

def sortList(l):
    domain = list(set(l))
    domain.sort()
    ##Now it's the national dutch flag problem...
    i = 0
    j = 0   
    k = len(l)
    mid = domain[1]
    
    while j < k:
        if l[j] < mid:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1
        elif l[j] > mid:
            k -= 1
            l[j], l[k] = l[k], l[j]
        else:
            j = j + 1
    return l

    
            
    
    
print(sortList([1,2,2,4,4,1,2,1,1,1,1,1,1,2,4,4,4,4,4]))
