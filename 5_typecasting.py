#  Explicit Typecasting  --> done by the programmer
a="1"
b="2"
print(a+b) #give 12 as result 
print(int(a)+int(b))  #give 3 as answer -->typecasting

c="golu"
d="7"
print(c+d)
# print(int(c)+int(d))  # give error as string should be valid for conversion 
# golu can't be converted to interger

# Implicit Typecasting  -->done by the compiler
# python converts a smaller data type to a higher data type to prevent data loss

c=8
d=1.9
print(c+d)
