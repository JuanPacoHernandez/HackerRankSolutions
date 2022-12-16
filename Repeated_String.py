#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:07:26 2022

@author: m710
"""

def repeatedString(s, n):
    # Import Counter function that returns frequency of elements from a list
    from collections import Counter
    # Floor to get the floor integer from a decimal number
    from math import floor    
    
    # factor represents the number of times that the string fits on the infinite string
    factor = floor(n/len(s))    
    
    # residual is the residual from the factor 
    residual = (n/len(s))%1
    
    # residual_slicer is the integer that will slice the original string based on the 
    # residual
    residual_slicer = round(residual*len(s))
    
    # frequencies of the letter 'a' in the string
    freq_a = s.count('a')
    
    # test if there is no 'a' in the string
    if freq_a == None:
        return 0
    
    # number_a is the frequency of letter 'a' in the original string
    number_a = freq_a*factor
    
    # if there is a residual, we only need to count from the start of the original
    # string up to the string sliced by residual
    if residual != 0:
        # freq of letters from residual string
        freq_a_residuals = s[:residual_slicer].count('a')
        # test if there is no 'a' in the residual string
        if freq_a_residuals == None:
            return number_a
        # if there are 'a' in residual string sum to the a's in the original string
        else:
            number_a = number_a + freq_a_residuals
        return number_a
    # if the string fits enterely in the infinte string, then won't be residual and 
    # the number of a's will be the count of a's by the times that the string fits
    # in infinite string
    else:
        return number_a


s= 'bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc'
n = 649606239668
print(repeatedString(s, n)) #162401559918

s = 'aab'
n = 882787
print(repeatedString(s, n)) #588525

s = 'abcac' #abcacabcac
n = 10
print(repeatedString(s, n)) #4

s = 'aba' #abaabaabaa
n = 10
print(repeatedString(s, n)) #7

s = 'aba' #aba aba aba aba
n = 11
print(repeatedString(s, n)) #7

s = 'a'
n = 1000000000000
print(repeatedString(s, n)) #1000000000000

s = 'aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce'
n = 731869010806
print(repeatedString(s, n)) #168329872486

s = 'ceebbcb'
n = 817723
print(repeatedString(s, n)) #0

s = 'gfcaaaecbg'
n = 547602
print(repeatedString(s, n)) #164280

