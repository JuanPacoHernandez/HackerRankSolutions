def birthday(s, d, m):
	j,c=0,0
	while (j+m)<len(s):
		ls=[]
		for j in range(j+m):
			ls.append(s[j])
		print(ls,sum(ls))	
		if sum(ls)==d:
			c+=1
			j+=1
	print(c,j)
	return	
			
		
		
	
#mes segmento
#dia suma del segmento
s=[1,2,1,3,2]
birthday(s,3,2)#2
