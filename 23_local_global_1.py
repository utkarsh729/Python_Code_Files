# LOCAL and GLOBAL variables
# A local variable is a variable that is defined within a function and it is only accessible within that
# function. It is created when the function is called and destroyed when the function return

# On the other hand, a global variable is a variable that is defined outside the of function
# and is accessbile from within the function in your code

x=7 # global
y=4

def yo():
    x=5
    z=9
    print("inside the function")
    print(x)
    print(y)
    print(z)
yo()
print("\nin main\n")
print(x)  
print(y)
# print(z)  give error as its scope limited to function yo()
print("\n------------------------------------------------------------------------\n")
a=100
print(a)
def change():
    global a  # this will change the value of the global variable a
    a=999
    print(a)
    a=99
    print(a)

change()
print(a)

# an important note changing global variable is not good practice

