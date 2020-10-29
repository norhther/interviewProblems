# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:44:50 2020

@author: norhther
"""


def singleNumber(nums):
    singleNum = nums[0]
    for i in range(1, len(nums)):
        singleNum ^= nums[i]
    return singleNum
     

print(singleNumber([4, 3, 2, 4, 1, 1, 3, 2, 2000]))
