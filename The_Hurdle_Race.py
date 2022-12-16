#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paco
"""
def hurdleRace(k, height):
    max_=max(height)
    if k < max_:print(max_-k)
    else:print(0)
    return



k=4
height=[1, 6, 3, 5, 2]#2
hurdleRace(k, height)
k=7
height=[2, 5, 4, 5, 2]#0
hurdleRace(k, height)

