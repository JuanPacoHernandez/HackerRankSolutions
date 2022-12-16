#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def formingMagicSquare(s):
    """
    THIS FUNCTION DETERMINES THE AMOUNT OF MINIMUM STEPS TO SOLVE A MAGIC
    SQUARE, MAGIC SQUARE IS A MATRIX OF 3X3 INTEGERS THAT SUMS '15' IN
    EVERY HORIZONTAL, VERTICAL AND DIAGONAL LINE. 
    
    TO SOLVE IT, IT IS NECESSARY TO KNOW THAT THERES IS ONLY EIGHT SQUARES 
    THAT COMPLY WITH THE PREVIOUS RESTRICTIONS. 
    
    SO, THIS FUNCTION COMPARES THE SQUARE TO TEST WITH EVERYONE OF THE 
    EIGHT SOLVED SQUARES BY OBTAINING THE COST OF EVERYONE OF THE EIGHT 
    SQUARES VERSUS THE SQUARE TO TEST AND THEN DETERMINES THE MINIMUM 
    NUMBER OF COST.

    Parameters
    ----------
    s : SQUARE TO TEST

    Returns
    -------
    PRINT THE MINIMUM STEPS TO GET A MAGIC SQUARE FROM THE SQUARE TO TEST

    """
    # THIS ARE THE EIGHT SQUARES THAT COMPLY WITH THE RESTRICTIONS TO BE 
    # A MAGIC SQUARE
    patterns=[[[8,1,6],[3,5,7],[4,9,2]],[[6,1,8],[7,5,3],[2,9,4]], 
             [[4,9,2],[3,5,7],[8,1,6]],[[2,9,4],[7,5,3],[6,1,8]],
             [[8,3,4],[1,5,9],[6,7,2]],[[4,3,8],[9,5,1],[2,7,6]],
             [[6,7,2],[1,5,9],[8,3,4]],[[2,7,6],[9,5,1],[4,3,8]]]
    # N IS THE COUNTER TO LOOP OVER THE EIGHT MAGIC SQUARES
    n=0
    # COSTS IS THE LIST OF COSTS FOR EVERY COMPARISON BETWEEN EIGHT MAGIC
    # SQUARES AND THE SQUARE TO TEST, THERE WILL BE ONLY EIGHT COSTS 
    costs=[]
    # LOOP OVER THE EIGHT SQUARES
    while n<=7:
        # THIS COUNTER STORES THE COST OF ONE MAGIC SQUARE VERSUS SQUARE 
        # TO TEST
        c=0
        # PARALELL LOOP OVER A MAGIC SQUARE AND SQUARE TO TEST
        for i,j in zip(patterns[n],s):
            for x,y in zip(i,j):
                # ONCE INSIDE THE NUMBERS TO COMPARE, GET ABSOLUTE DIFFERENCE,
                # THIS IS HOW TO CALCULATE THE COST:  SUM(| X - Y |)
                c+=abs(x-y)
        # STORE THE COST IN A LIST OF COSTS        
        costs.append(c)    
        # INCREASE COUNTER TO THE NEXT MAGIC SQUARE
        n+=1 
    # FINALLY, GET THE MINIMUM COST OF A LIST OF COSTS
    print(min(costs))
    return
    
    
    


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]#7
formingMagicSquare(s)
s = [[4,9,2], [3,5,7], [8,1,5]]#1
formingMagicSquare(s)
s = [[4,8,2], [4,5,7], [6,1,6]]#4
formingMagicSquare(s)

