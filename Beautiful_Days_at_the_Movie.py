#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def beautifulDays(i, j, k):
    n=0
    for m in range(i,j+1):
        if abs(m-int(str(m)[::-1])) % k == 0:
            n += 1
    print(n)
    return

i=20
j=23
k=6
beautifulDays(i,j,k)
i=13
j=45
k=3
beautifulDays(i,j,k)
    
    
    
    

    
    
    
    

