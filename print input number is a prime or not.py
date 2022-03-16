#print input number is a prime or not.py

#Complete the code to find if a given number is a prime number? 
#The program will take a positive integer greater than 1 as input and indicate if it is a prime number by saying "prime", and if it is not a prime number saying "not a prime".
#Note there are 3 places in the given code that you need to fix for this code to work properly and give the expected output. 
#For example:

 #   Input	       Result

 #    3            prime

 #     4        not a prime
  
i = int(input())
count = 0
if (i>1):
    for j in range (1,i+1):
      if (i%j == 0):
        count = count+1
if count == 2:
 print("a prime ")
else:
 print('not a prime')
