#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paco
"""
def pickingNumbers(a):
    from collections import Counter
    # CONVERT DE COUNTER OF OCURRENCES IN A DICTIONARY
    dicc=dict(Counter(a))
    # CHECK IF THERE IS A UNIQUE KEY IN DICTIONARY, THEN OUTPUT THE LENGTH
    # OF THE LIST AS A MAXIMUM LENGTH OF SUB ARRAY
    if len(dicc)==1:
        print(len(a))
        return
    # LIST COUNT OF ELEMENTS IN LIST, TO KNOW THE LENGTHS OF SUBARRAYS
    not_sorted_keys=list(dicc.keys())
    # LIST NEEDS TO BE SORTED TO GO THROUGH THE LIST AND FIND CONSECUTIVE
    keys=sorted(not_sorted_keys)
    # LIST COMPRHENSION THAT GO THROUGH LIST OF KEYS, FIND CONSECUTIVE AND 
    # WITH THAT KEYS FIND THE VALUE OF OCURRENCES IN COUNTER DICT
    c=[dicc[keys[i]] + dicc[keys[i+1]] for i in range(len(keys)-1) if abs(keys[i]-keys[i+1]) == 1]
    # 
    # THIS IS THE EQUIVALENT FOR LIST COMPREHENSION
    # for i in range(len(keys)-1):
    #     if abs(keys[i]-keys[i+1]) == 1:
    #         c.append(Counter(a)[keys[i]] + Counter(a)[keys[i+1]])
    # 
    # AT THE END THERE IS A LIST OF NUMBER OF OCURRENCES BY CONSECUTIVE,
    # THEN PICK THE HIGHEST, THE LONGEST SUBARRAY  
    if max(list(dicc.values())) > max(c):
        print(max(list(dicc.values())))
    else:    
        print(max(c))
    return

    
    
    
a=[1,1,2,2,4,4,5,5,5]#5
pickingNumbers(a)
a=[4,6,5,3,3,1]#3
pickingNumbers(a)
a=[1,2,2,3,1,2]#5
pickingNumbers(a)
a=[4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
pickingNumbers(a)#50
a=[66]*100
pickingNumbers(a)#100



