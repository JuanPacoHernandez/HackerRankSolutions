def birthday(s, d, m):
    #Count init, it means the number of ways that Lily could divide the chocolate bar
    c=0
    #This is for special cases when lenght of choco bar is one
    if sum(s)==d:
        print(1)
        return
    #for loop to check in all the size of choco bar, until to fit size of segment
    for i in range(len(s)-m+1):
        #sub list from de choco bar (mother list) 
        ls=[]
        #for loop makes a sub list upon the size given by "m"
        for j in range(m):
            #index i from every square from mother list, index j from every square 
            #from sublist
            ls.append(s[j+i])   
        #after extract sublist from mother list, verify if a segment from choco bar 
        #meets the sum required    
        if sum(ls)==d:
            #count increased by one, then takes another new sublist
            c+=1
    print(c)
    return 
			
#mes longitud del segmento
#dia suma del segmento
#s=[1,2,1,3,2]
#birthday(s,3,2)#2
s=[4]
birthday(s,4,1)#1
#s=[2,2,2,1,3,2,2,3,3,1,4,1,3,2,2,1,2,2,4,2,2,3,5,3,4,3,2,1,4,5,4]
#birthday(s,10,4)#7
#s=[2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
#birthday(s,18,7)#3