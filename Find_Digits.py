#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def findDigits(n):
    gen = (int(i) for i in str(n))
    c = 0
    for i in gen:
        if i != 0 and n % i == 0:
            c += 1
    print(c)    
    return

n = 124
findDigits(n) # 3

n = 111
findDigits(n) # 3

n = 10 # 1
findDigits(n)

n = 12
findDigits(n) # 2

n = 1012
findDigits(n) # 3



