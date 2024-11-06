# There are four types of argument and return statement
# Default Argument
# Keyword Argument
# Variable length Argument
# Required Argument


# default argument
# #-->function takes these value as default value if value is not provided in the function call
def average(a=7,b=4):   
    print("Average of numbers is: ",(a+b)/2)

average()  # a=7 b=4
average(8,6)  # a=8 b=6
average(3)   #a=3  b=4
average(b=5)  #a=7 b=5

def name(fname, mname="Pal", lname="Singh"):
    print("Hello",fname,mname,lname)

name("Desi")
name("Moti","Lal")
name("Demand",lname="Roy")

# keyword argument
# we can provide arguments with key= value, this way the interpreter recongnizes the arguments 
# by the parameter name

average(b=10,a=5)
name(lname="Pandu", fname="Guddu",mname="Roy")

# Required arguments 
name(fname="Chandra")   # here fname is requride argument as fname don't have default value
name("Chandra")

#  Variable length argument

def adding(*numbers): 
    # here it take number as tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("The sum of numbers is: ",sum)

adding(2,5,7)
adding(4,1)
adding(1,1,11,1,1,1)

print("-------------------------------------------------\n")

# return type function
#  is used return the value back to the calling function
def sum(a,b,c):
    return a+b+c
    return 3
    # phela wala return mana jata hai baaki sab ignore kr diye jaate hai

d=sum(2,3,4)
print("The sum is: ",d)
