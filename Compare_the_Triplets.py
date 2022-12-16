def compareTriplets(a, b):
	i=[1 for e in range(len(a)) if a[e]>b[e]]
	j=[1 for e in range(len(a)) if b[e]>a[e]]
	print(sum(i),sum(j))
	return
	
	
a=[17,28,30]
b=[99,16,8]
compareTriplets(a,b)
c=[5,6,7]
d=[3,6,10]
compareTriplets(c,d)
