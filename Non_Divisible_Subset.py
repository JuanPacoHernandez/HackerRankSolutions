from collections import Counter
import numpy as np
from itertools import combinations

def nonDivisibleSubset(s,k):
    # If the two remainders divided by "k" from any two numbers in the list are added 
    # and result in "k", then those two numbers are even divisible by "k", so they cannot 
    # be in the asked subset. Then we need to find the remainders of every single element
    # in list and add every two combinations to drop those who do not sum "k".
    
    # Getting all remainders
    reminders = [i%k for i in s]
    
    # Finding the frequencies of the remainders
    freq_reminders = dict(Counter(reminders))
    
    keys = list(freq_reminders.keys())
    
    try:
        c = min(freq_reminders[0],1)
    except:
        c = 0
    
    # ODD CASE
    if k%2 != 0:
        comb_odd = list(combinations(keys,2))
        for i in comb_odd:
            if i[0] + i[1] == k:
                c += max(freq_reminders[i[0]],freq_reminders[i[1]])
    
    # EVEN CASE
    if k%2 == 0:
        c += min(freq_reminders[k/2],1)
        comb_even = list(combinations(keys,2))
        for i in comb_even:
            if i[0] + i[1] == k:
                c += max(freq_reminders[i[0]],freq_reminders[i[1]])
    return c
    
    
    
    
    
    """# The keys from the past dictionary represent the remainders and the values are
    # the count of those remainders, thus we need to find the max count between two 
    # values from the reminders
    
    # I list the keys from the dictionary, and sort them to get an easy view
    keys = list(freq_remainders.keys())
    keys.sort()
    
    # I'm gonna stored the max values founded comparing two numbers
    max_values = []
    # I go through the keys list two by two
    for i in range(0,len(keys),2):
        # If i found a single last number, then I added that last key to found the
        # respective value from remainders dictionary
        if i+2 > len(keys):
            max_values.append(freq_remainders[keys[i]])
            break
        max_values.append(max(freq_remainders[keys[i]],freq_remainders[keys[i+1]]))
    # The next sum of the list is the maximum length of the solution subset
    return freq_remainders
    """
   
k = 3
s = [1,2,3,4,5,6]
print(nonDivisibleSubset(s,k))############3

k = 6
s = [ 12 ,6 ,1, 9, 13, 15, 10, 21, 14, 32, 5, 8, 23, 19]
print(nonDivisibleSubset(s,k))   #######8
    
k = 3
s = [1, 7, 2, 4]
print(nonDivisibleSubset(s,k))  #########3

k = 7
s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
print(nonDivisibleSubset(s,k)) #####################11

k = 11
s = [582740017, 954896345, 590538156, 298333230, 859747706, 155195851, 331503493,
     799588305, 164222042, 563356693, 80522822, 432354938, 652248359]
print(nonDivisibleSubset(s,k)) #### 11

k = 9
s = [422346306, 940894801, 696810740, 862741861, 85835055, 313720373]
print(nonDivisibleSubset(s,k)) #### 15
