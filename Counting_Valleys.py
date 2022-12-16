def countingValleys(n, s):
	res,i=0,0
	for e in range(n):
		if s[e]=='U':
			res+=1
			if res==0:
				i+=1
		else:
			res-=1	
	print(i)		
	return

countingValleys(8,'UDDDUDUU')			
countingValleys(12,'DDUUDDUDUUUD')	
