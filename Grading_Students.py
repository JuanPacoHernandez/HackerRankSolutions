def gradingStudents(grades):
	res=[((i//5)+1)*5 if (((i//5)+1)*5)-i<3 and i>=38 else i for i in grades]
	print(res)
	return
			
		
a=[73,67,38,33]		
gradingStudents(a)

		
