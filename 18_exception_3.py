#  rasing custom error
# in python we can raise custom error by using raise keyword 
n=int(input('enter number between 4 to 7 '))
if(n<4 or n>7):
    raise ValueError("value should be between 4 and 7")

