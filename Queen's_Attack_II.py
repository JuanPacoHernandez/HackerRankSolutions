#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:50:13 2022

@author: m710
"""
    
"""
# Calculating the total available spaces in the board
d1 = c_q - 1
d2 = min(r_q - 1, d1)
d3 = r_q - 1
d4 = min(n - c_q, d3)
d5 = n - c_q
d6 = min(n - r_q, d5)
d7 = n - r_q
d8 = min(d1, d7)
available_spaces = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
"""
    

def queensAttack(n, k, r_q, c_q, obstacles):
    # When the board is 1x1 size, there is only left space for the Queen, then
    # no movement is allowed
    if n == 1:
        return 0
    
    #        d7
    #   d8 \  |  / d6
    #       \ | /
    #        \|/ 
    # d1 -----o----- d5
    #        /|\
    #       / | \
    #   d2 /  |  \ d4
    #        d3
    
    # The next diagonals represent a list of posible positions in that diagonal, according
    # with the diagram at the top, and also their lengths are calculated
    D1 = [(r_q, i) for i in range(c_q - 1, 0, -1)]
    len_D1 = len(D1)
    
    D2 = [(r_q - i, c_q  - i) for i in range(1, min(r_q,c_q))]
    len_D2 = len(D2)
    
    D3 = [(i, c_q) for i in range(r_q - 1, 0, -1)]
    len_D3 = len(D3)
    
    D4 = [(r_q - i, c_q  + i) for i in range(1, min(r_q, (n+1) - c_q))]
    len_D4 = len(D4)
    
    D5 = [(r_q, i) for i in range(c_q + 1, n + 1)]
    len_D5 = len(D5)
    
    D6 = [(r_q + i, c_q  + i) for i in range(1, min((n+1) - r_q, (n+1) - c_q))]
    len_D6 = len(D6)
    
    D7 = [(i, c_q) for i in range(r_q + 1, n + 1)]
    len_D7 = len(D7)
    
    D8 = [(r_q + i, c_q  - i) for i in range(1, min((n+1) - r_q, c_q))]
    len_D8 = len(D8)
    
    # Check if obstacles are in the eight diagonals, if so then re-calculate the 
    # new length of the diagonal considering the obstacle
    for i in obstacles:
        if i in D1:
            len_D1 = len(D1[:D1.index(i)])
        elif i in D2:
            len_D2 = len(D2[:D2.index(i)])
        elif i in D3:
            len_D3 = len(D3[:D3.index(i)])
        elif i in D4:
            len_D4 = len(D4[:D4.index(i)])
        elif i in D5:
            len_D5 = len(D5[:D5.index(i)])
        elif i in D6:
            len_D6 = len(D6[:D6.index(i)])
        elif i in D7:
            len_D7 = len(D7[:D7.index(i)])
        elif i in D8:
            len_D8 = len(D8[:D8.index(i)])          
    
    # Return the sum of the positions considering the obstacles
    return len_D1 + len_D2 + len_D3 + len_D4 + len_D5 + len_D6 + len_D7 + len_D8

n = 8
k = 1
r_q = 4
c_q = 4
obstacles = [(3,5)]
print(queensAttack(n, k, r_q, c_q, obstacles)) #24

n = 5
k = 0
r_q = 4
c_q = 3
obstacles = []
print(queensAttack(n, k, r_q, c_q, obstacles)) #14

n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [(5,5), (4,2), (2,3)]
print(queensAttack(n, k, r_q, c_q, obstacles)) #10

n = 4
k = 0
r_q = 4
c_q = 4
obstacles = []
print(queensAttack(n, k, r_q, c_q, obstacles)) #9

n = 88587
k = 9
r_q = 20001
c_q = 20003
obstacles = [(20001,20002), (20001, 20004), (20000, 20003), (20002, 20003), (20000, 20004), (20000, 20002), (20002, 20004), (20002, 20002), (564,323)]
print(queensAttack(n, k, r_q, c_q, obstacles)) #0




    
    













