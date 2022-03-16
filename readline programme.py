#readline programme.py

#Write a Python program to 
#Read the first two lines from a text file named "file1.txt"
#Write the two lines read from "file1.txt" to a new file called "file2.txt"
#Read "file2.txt" and Print the contents.

#teacher answer
fhandle1 = open("file1.txt","r")
fhandle2 = open("file2.txt","w")

str = fhandle1.readline()
fhandle2.write(str)
str = fhandle1.readline()
fhandle2.write(str)

fhandle1.close()
fhandle2.close()

fhandle3 = open("file2.txt")
print(fhandle3.read())
fhandle3.close()

#my answer
	fhandle = open("file1.txt" , 'r')
	f = fhandle.readline()
	ff= fhandle.readline()
	fhandle2 = open("file2.txt" , 'w')
	fhandle2 . write (f)
	fhandle2 . write (ff)
	fhandle.close()
	fhandle2.close()
	fhandle3 = open("file2.txt" , 'r' )
	f3 = fhandle3.read()
	print(f3)
	fhandle3.close()
