#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    # DT2 IS DUE TIME
    from datetime import datetime
    dt1 = datetime(year = y1, month = m1, day = d1)
    dt2 = datetime(year = y2, month = m2, day = d2)
    if dt1 <= dt2:
        fine = 0
    elif dt1 > dt2 and dt1.month == dt2.month and dt1.year == dt2.year:
        fine = (dt1.day - dt2.day) * 15
    elif dt1 > dt2 and dt1.month > dt2.month and dt1.year == dt2.year:
        fine = (dt1.month - dt2.month) * 500
    elif dt1 > dt2 and dt1.year > dt2.year:
        fine = 10000
    print(fine)
    return
    
    
    
d1 = 9 
m1 = 6 
y1 = 2015
d2 = 6 
m2 = 6 
y2 = 2015
libraryFine(d1, m1, y1, d2, m2, y2)

d1 = 14
m1 = 7
y1 = 2018
d2 = 5 
m2 = 7 
y2 = 2018
libraryFine(d1, m1, y1, d2, m2, y2)

d1 = 1
m1 = 1
y1 = 2000
d2 = 1
m2 = 1 
y2 = 2000
libraryFine(d1, m1, y1, d2, m2, y2)







"""
class Date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    
def leapyear(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def difference(dt1,dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0,dt1.m - 1):
        n1 += monthDays[i]
    n1 += leapyear(dt1)
    n2 = dt2.y * 365 +dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += leapyear(dt2)
    return n2 - n1
    
dt1 = Date(6, 6, 2015)
dt2 = Date(9, 6, 2015)
print(difference(dt1,dt2),'days')
"""