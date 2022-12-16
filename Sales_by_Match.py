#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paco
"""
def sockMerchant(n, ar):
    from collections import Counter
    socks=dict(Counter(ar))
    # 
    # LIST COMPREHENSION BUT IT MAKES A SLOW SOLUTION
    # pairs=sum([socks[i]//2 for i in socks])
    # 
    pairs=0
    for i in socks:
        pairs += socks[i]//2
    print(pairs)    
    return


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(n, ar)
    