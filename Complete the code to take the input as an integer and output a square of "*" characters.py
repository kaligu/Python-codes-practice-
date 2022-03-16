#Complete the code to take the input as an integer and output a square of "*" characters.py
#  val = int(input())
#       For example, if the input is 2 and 5 respectively:

#       For example:
#     Input      	Result

#       2            **
#                    **
#       5          *****
#                  *****
#                  *****
#                  *****
#                  *****

var=int(input())
for x in range (0,var):
       for y in range (0,var-1):
            print('*' , end= '')
       print('*')
