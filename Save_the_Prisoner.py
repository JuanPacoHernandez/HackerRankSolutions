#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def saveThePrisoner(n, m, s):
    # print(((s-2+m)%n)+1)
    a = s - 2 + m
    b= a % n
    c= b +1
    print(c)
    return
 

n = 4 # prisioners
m = 6 # candies
s = 2 # start
saveThePrisoner(n,m,s)#3
n = 5 
m = 2 
s = 1
saveThePrisoner(n,m,s)#2
n = 5 
m = 2 
s = 2
saveThePrisoner(n,m,s)#3
n = 7 
m = 19 
s = 2
saveThePrisoner(n,m,s)#6
n = 3 
m = 7 
s = 3
saveThePrisoner(n,m,s)#3