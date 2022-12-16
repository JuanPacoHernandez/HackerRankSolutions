def minimumNumber(n, password):
	numbers="0123456789"
	lower_case="abcdefghijklmnopqrstuvwxyz"
	upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters="!@#$%^&*()-+"
	c=0   
	if any(i in numbers for i in password)==False:c+=1
	if any(i in lower_case for i in password)==False:c+=1
	if any(i in upper_case for i in password)==False:c+=1
	if any(i in special_characters for i in password)==False:c+=1
	print(max(c,6-n))
	return


n=3
pas='Ab1'
minimumNumber(n,pas)
#3

n=11
pas='#HackerRank'
#1
minimumNumber(n,pas)

n=2
pas='12'
#4
minimumNumber(n,pas)

n=2
pas='fe'
#4
minimumNumber(n,pas)

n=3
pas='790'
#3
minimumNumber(n,pas)

n=4
pas='IGEC'
#3
minimumNumber(n,pas)

n=4
pas='06HL'
#2
minimumNumber(n,pas)

n=4
pas='EKZy'
#2
minimumNumber(n,pas)


