#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paco
"""
# k: WHAT ANNA DOES NOT EAT
# b: AMOUNT OF MONEY THAT ANNA CONTRIBUTED TO THE BILL

def bonAppetit(bill, k, b):
    bill.pop(k)
    anna=int(sum(bill)/2)
    if b == anna:print('Bon Appetit')
    else: print(b-anna) 
    return
    
    

bonAppetit([3,10,2,9],1,12)#5
bonAppetit([3,10,2,9],1,7)#Bon appetit
bonAppetit([72,53,60,66,90,62,12,31,36,94],6,288)#6

