#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def extraLongFactorials(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * extraLongFactorials(n-1)

n = 30
print(extraLongFactorials(n))

n = 25
print(extraLongFactorials(n))

n = 0
print(extraLongFactorials(n))
