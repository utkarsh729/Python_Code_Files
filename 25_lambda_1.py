# LAMBDA function --- a lambda function is a small anonymous function defined without name.
# It is defined using lambda keyword
# lambda arguments: expression 

double = lambda x: x*2
cube = lambda x: x*x*x
avg=lambda x,y,z: (x+y+z)/3
 
print(double(5))
print(double(3.5))
print(cube(3))
print(avg(7,5,3))

# lambda function is often used in situation where a small function is required for short period of time.
# They are commonly used as arguments to higher order function, such as map, filter 

def appl(fun, value):
    return 7+fun(value)

print(appl(cube, 3))
# hum function ko ak function bhi pass kar sakte hai
print(appl(lambda a: a*a, 4))  # here lambda is anonymous function --> no name
