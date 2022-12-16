#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paco
"""
def dayOfProgrammer(year):
    # 1918 WAS NOT A LEAP YEAR SO BY DEFAULT PRINT OUT STRIGHTFORWARD
    if year == 1918: print('26.09.1918')
    
    # IF YEAR WAS IN JULIAN CALENDAR TIME, DO THIS:
    elif 1700 <= year <= 1917:
        # TO DETERMINE IF A YEAR IS A LEAP YEAR OR NOT
        if year % 4 == 0: 
            print('12.09.'+str(year))
        else: 
            print('13.09.'+str(year))
            
    # BUT IF WAS GREGORIAN CALENDAR TIME, DO THIS:        
    elif 1919 <= year <= 2700:   
        # TO DETERMINE IF A YEAR IS A LEAP YEAR OR NOT
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print('12.09.'+str(year))
        else: 
            print('13.09.'+str(year))
    # WHEN YEAR IS NOT BETWEEN 1700 TO 2700    
    else:
        print('Year out of boundaries!')
    return


dayOfProgrammer(2016)
dayOfProgrammer(2017)
dayOfProgrammer(1800)
dayOfProgrammer(1917)
dayOfProgrammer(1918)