def birthdayCakeCandles(ar):
	if 1<len(ar)<=10**5:
		j=0
		ar.sort()
		for i in range(1,len(ar)):
			if ar[-i]==ar[-i-1]:j+=1	
			else: break
	print(j+1)		
	return	

a=[3,2,1,3]
birthdayCakeCandles(a)	
