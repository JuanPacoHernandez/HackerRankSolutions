def designerPdfViewer(h, word):
	base={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
	#h es una cadena que mediante la siguiente linea pasa a lista de enteros
	h=[int(i) for i in h.split()]
	print(max([h[i] for i in [base[e] for e in word]])*len(word))
	return

	
h='1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
word='abc'
designerPdfViewer(h, word)
h='1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'
word='zaba'
designerPdfViewer(h, word)	

