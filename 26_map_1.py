# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you 
# to apply a function to a sequence of elements and return a new sequence.
# These functions are known as higher-order functions, as they take other functions as arguments.

# map
# The map function applies a function to each element in a sequence and 
# returns a new sequence containing the transformed elements. 
# The map function has the following syntax: map(function, iterable)
# The function argument is a function that is applied to each element in the iterable argument.
# The iterable argument can be a list, tuple, or any other iterable object.

def cube(x):
    return x*x*x

l1=[3,5,1,2]

# newl1=[]  # empty list
# for i in l1:
#     newl1.append(cube(i)) 
# it is very long process first create empty list then append every element ...

# newl1=list(map(cube,l1)) # return the map object so convert into list
newl1=list(map(lambda x: x*x*x ,l1))  # we can pass lambda function also

print(newl1)


# filter
# The filter function filters a sequence of elements based on a given predicate 
# (a function that returns a boolean value) and 
# returns a new sequence containing only the elements that meet the predicate. 
# The filter function has the following syntax:  filter(predicate, iterable)
# The predicate argument is a function that returns a boolean value 
# and is applied to each element in the iterable argument.
# The iterable argument can be a list, tuple, or any other iterable object.

def greater(a):
    return  a>4

# newl2=list(filter(greater,l1))
newl2=list(filter(lambda y:y>4,l1))

print(newl2)


# reduce
# The reduce function is a higher-order function that applies a function to a sequence 
# and returns a single value. It is a part of the functools module in Python 
# and has the following syntax: reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value. 
# The iterable argument is a sequence of elements, such as a list or tuple.
# The reduce function applies the function to the first two elements in the iterable 
# and then applies the function to the result and the next element, and so on. 
# The reduce function returns the final result.

from functools import reduce
# we have to import reduce for using it

def mysum(x,y):
    return x+y

num=[1,3,2,4,5]

newnum=reduce(mysum,num)  # no need to convert in list and give error if you try to convert
# ismai phele do number ko sum karega firr jo naii list banegi uske doh number sum honge...aise karke
# last mai single value return hogi
print(newnum)

