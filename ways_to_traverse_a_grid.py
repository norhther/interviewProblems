# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:32:21 2020

@author: norhther

Hi, here's your problem today. This problem was recently asked by Microsoft:

You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

"""

import scipy.special 

def num_ways(n, m):
    num_steps = n + m - 2
    #how many norths I have to take? n
    return int(scipy.special.binom(num_steps,n - 1))


print (num_ways(40000, 100))

