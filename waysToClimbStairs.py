# -*- coding: utf-8 -*-
"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
  
print staircase(4)
# 5
print staircase(5)
# 8
Can you find a solution in O(n) time?

"""

def staircase(n):
    res = 0
    a = 0
    b = 1
    for i in range(0,n):
        res = a + b
        a = b
        b = res
    return res

print(staircase(3))