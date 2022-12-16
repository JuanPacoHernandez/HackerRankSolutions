def divisibleSumPairs(n, k, ar):
    """
    This function returns number of pairs (i,j) from a list where i<j and i+j
    is divisible by k

    Parameters
    ----------
    n : lenght of the list or array
    k : integer divisor
    ar : list of numbers

    Returns
    -------
    m : number of pairs that satisfies conditions

    """
    m = 0
    for i in range(n-1):
        j = i+1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                m += 1
            j += 1
    return  m
    
	

n,k=6,3
ar=[1, 3, 2, 6, 1, 2]
divisibleSumPairs(n,k,ar)
