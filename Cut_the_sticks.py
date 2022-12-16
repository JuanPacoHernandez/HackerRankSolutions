#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def cutTheSticks(arr):
    # VERSION USING NUMPY
    import numpy as np
    sticks = np.array(arr)
    sticks_left =[]
    while np.size(sticks):
        length_of_cut = np.min(sticks)
        sticks_to_cut = np.size(sticks)
        sticks = sticks - length_of_cut
        sticks = sticks[sticks > 0]
        sticks_left.append(sticks_to_cut)
    print(sticks_left)    
    return

def cutTheSticks(arr):
    #VERSION USING LISTS
    sticks_left =[]
    while len(arr):
        length_of_cut = min(arr)
        sticks_to_cut = len(arr)
        arr = [i - length_of_cut for i in arr]
        arr = [i for i in arr if i > 0]
        sticks_left.append(sticks_to_cut)
    print(sticks_left)    
    return

n = [5, 4, 4, 2, 2, 8]
cutTheSticks(n) # [6, 4, 2 ,1]

n = [1, 2, 3, 4, 3, 3, 2, 1]
cutTheSticks(n) # [8, 6, 4, 1]
