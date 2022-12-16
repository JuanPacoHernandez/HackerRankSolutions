#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:33:29 2022

@author: m710
"""

def equalizeArray(arr):
    from collections import Counter
    freq = Counter(arr)
    residuals = [len(arr)-freq[i] for i in freq]
    return min(residuals)
    
    
a = [1, 2, 2, 3]
print(equalizeArray(a)) #2

a = [3, 3, 2, 1, 3]
print(equalizeArray(a)) #2
