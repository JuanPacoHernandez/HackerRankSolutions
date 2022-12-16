#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def jumpingOnClouds(c):
    jump, i = 0, 0
    while i < len(c)-1:
        if c[i+1] == 1:
            jump += 1
            i += 2
        elif (i+2) > (len(c)-1):
            jump += 1
            i += 1
        elif c[i+2] == 1:
            jump += 1
            i += 1
        else:
            jump += 1
            i += 2
    return jump
    
    
c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c)) #3    



c = [0, 1, 0, 0, 0, 1, 0]
print(jumpingOnClouds(c)) #3

c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c)) #4

c = [0, 0, 0, 0, 1, 0]
print(jumpingOnClouds(c)) #3

