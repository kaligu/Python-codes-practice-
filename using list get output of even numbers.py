#X=[2,4,5,1,3,8] using this list get output of even numbers Y=[2,4,8]

x= [2,4,5,1,3,8 ]
y= [y for y in x if (y % 2==0)]
print(y)
