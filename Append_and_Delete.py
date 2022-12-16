#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""

def appendAndDelete(s, t, k):
    c = 0
    for i,j in zip(s,t):
        if i == j:
            c += 1
        else: 
            break
    # CASE A: IF SUM OF LENGTHS IS LESS THAN NUMBER OF 
    # MOVES, IT IT EASILY TO RE-CONSTRUCT SECOND STRING
    if len(s) + len(t) <= k:
        print('Yes')
        return
    # CASE B:
    # LEN(S) - C IS THE NUMBER OF LETTERS TO BE DELETED
    # AND LEN(T) - C IS THE NUMBER OF LETTERS TO BE
    # ADDED, THEN IF 'K' MOVEMENTS LESS THE RESULT OF
    # THIS LAST OPERATION IS EVEN, TO DELETE AND APPEND 
    # IN EVEN NUMBER OF MOVEMENTS, THEN WE CAN TRANSFORM
    # STRING 'S' TO STRING 'T'
    elif (k - len(s) - len(t) + 2 * c) % 2 == 0 and (k - len(s) - len(t) + 2 * c) >= 0:
        print('Yes')
        return
    # ANY OTHER CASE:
    # THERE IS NO OTHER POSSIBLE CASE TO TRANSFORM FROM
    # STRING 'S' TO STRING 'T', SO RETURN 'NO'
    else:
        print('No')
        return

s = 'qwerasdf'
t = 'qwerbsdf'
k = 6
appendAndDelete(s, t, k) # No

s = 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
t = 'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
k = 100
appendAndDelete(s, t, k) # No

s = 'abc'
t = 'def'
k = 6
appendAndDelete(s, t, k) # Yes

s = 'hackerhappy'
t = 'hackerrank'
k = 9
appendAndDelete(s, t, k) # Yes

s = 'aba'
t = 'aba'
k = 7
appendAndDelete(s, t, k) # Yes

s = 'ashley'
t = 'ash'
k = 2
appendAndDelete(s, t, k) # No
