#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""

def utopianTree(i):
	if i % 2 != 0:
		j = i + 1
		k = int(j / 2) + 1
		res = (2 ** k) - 2
		print(res)
		return
	elif i % 2 == 0:
		k = int(i / 2) + 1
		res = (2 ** k) - 1
		print(res)
	else:
		print(1)	
		return

   
utopianTree(0)
utopianTree(1)
utopianTree(2)
utopianTree(4)
utopianTree(9)
