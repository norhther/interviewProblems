# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:02:00 2020

@author: norhther
"""


def two_sum(l, k):
    value_search = set()
    for elem in l:
        value_needed = k - elem
        if value_needed in value_search:
            return True
        else:
            value_search.add(elem)
    return False
        
        
print (two_sum([4,7,1,-3,2], 5))
# True