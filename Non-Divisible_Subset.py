#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""

def nonDivisibleSubset(k, s):
    count_arr = [0] * k
    for i in s:
        count_arr[i%k] += 1
    if k % 2 != 0:
        res = 
    return


s = [1, 2, 3, 4, 5, 6]
k = 3
nonDivisibleSubset(k,s) 

s = [19, 10, 12, 10, 24, 25, 22]
k = 4
# nonDivisibleSubset(k,s) # 3

s = [1, 7, 2, 4]
k = 3
# nonDivisibleSubset(k,s) # 3

s = [3, 7, 2, 9, 1]        
k = 3
# nonDivisibleSubset(k,s) # 3

s = [3, 17, 12, 9, 11, 15]
k = 5
# nonDivisibleSubset(k,s) # 4  




