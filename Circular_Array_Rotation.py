#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def circularArrayRotation(a, k, q):    
    import collections
    lst = collections.deque(a)
    for i in range(k):
        lst.rotate(1)
    _lst=list(lst)    
    print([_lst[i] for i in q])
    return



a=[1,2,3]
k=2
q=[0,1,2]
circularArrayRotation(a,k,q) # 2, 3, 1

