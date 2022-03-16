#Take a number N as input and output the sum of all numbers from 1 to N (including N).

#Sample Input
#     100

#Sample Output
#     5050

#Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
#You can iterate over a range and calculate the sum of all numbers in the range.
#Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.

N = int(input())
y = 0
#your code goes here
x = list(range(1 , N+1))
for n in x:
    y += n
print(y)
