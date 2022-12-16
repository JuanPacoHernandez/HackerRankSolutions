def timeConversion(s):
	import re
	dis=re.findall('..$',s)
	h=re.findall('^..',s)
	if dis[0]=='PM' and h[0]!='12':
		hour=int(h[0])+12
		s=s.replace(h[0],str(hour))[:-2]
		print(s)
	elif dis[0]=='AM' and h[0]=='12':	
		s=s.replace(h[0],'00')[:-2]
		print(s)
	else:
		print(s[:-2])	
	return
	
a="07:05:45PM"
b="05:17:24AM"
c="12:00:32AM"
d="12:34:23PM"
print(a)
timeConversion(a)	
print(b)
timeConversion(b)	
print(c)
timeConversion(c)	
print(d)
timeConversion(d)	
