
def miniMaxSum(arr):
	if 1<len(arr)<=10**9:
		print(min(sum(arr)-i for i in arr),max(sum(arr)-i for i in arr))
	return	
	
	
a=[1,2,3,4,5]	
miniMaxSum(a)	
