#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def viralAdvertising(n):
    cumulative = 0
    shared = 5
    for i in range(n):
        liked = shared//2
        shared = liked * 3
        cumulative += liked
    print(cumulative)    
    return


viralAdvertising(5)
viralAdvertising(3)
