# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 03:04:04 2020

@author: norhther
"""


def move(a,b):
    print("Move {} to {}!".format(a,b))
    
def hanoi(n,f,t,h):
    if n != 0:
        hanoi(n-1,f,h,t)
        move(f,t)
        hanoi(n-1,h,t,f)

hanoi(4,"A","C","B")