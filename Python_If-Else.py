#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:07:12 2022

@author: m710
"""

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and n in range(2,6):
        print("Not Weird")
    elif n%2 == 0 and n in range(6,21)    :
        print("Weird")
    elif n%2 == 0 and n > 20:
        print("Not Weird")
    