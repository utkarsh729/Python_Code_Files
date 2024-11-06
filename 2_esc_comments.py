# print("Hee this is
# golu")    --> this gives error you can't broke line like this
#  --> use escape character

print("Hee this is\ngolu")

'''use triple quote
for multi line comment'''

""" You can use triple double 
quote also for multi line comment"""

# to use single or  double quote in statement use \' \"

print("Hello \"Golu\" how are you")
print('Good morning, \'Rhea\', \" Gupta\".')

# Default separator is a space between the values
# you can give your own separator

print("Hello Golu",4,7,"full",sep="~")  # here differnt values are separated by ~
# print("hello",4,6,True,sep=0)    give error as separator must be string
print("hello",4,6,True,sep="0")    
print("Hello Golu",4,7.29,sep="@") 
print("Hello Golu",4,7,sep="~", end="23MAy")  # start next line after writing 23MAy with this line only
print("wedding")  