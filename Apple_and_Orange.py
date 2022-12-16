def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for i in apples if a+i in range (s,t+1)]),sum([1 for j in oranges if b+j in range (s,t+1)]),sep='\n')
    return   

s,t,a,b,apples,oranges=7,11,5,15,[-2,2,1],[5,-6]
countApplesAndOranges(s, t, a, b, apples, oranges)		

