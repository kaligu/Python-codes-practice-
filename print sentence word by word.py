#print sentence word by word.py

#	1.output = chethiya
#	2.output = c
#	           h
#	           e
#	           t
#	           h
#	           i
#	           y
#	           a
#	3.output =  chethiya 
#	            kaligu

	1)def greet(*names):
	    for names in names:
	             print(names)
	  greet("chethiya")
	
	2)def greet(names):
	     for names in names:
	             print(names)
	  greet("chethiya")
	
	3)
	def greet(*names):
	    for names in names:
	             print(names)
  greet("chethiya" , "kaligu")
