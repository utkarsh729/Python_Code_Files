# Importing in Python is the process of loading code from a Python module into the current script.
#  This allows you to use the functions and variables defined in the module in your current script, 
# as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of module.

import math

# Once a module is imported, 
# you can use any of the functions and variables defined in the module by using the dot notation.

print(math.floor(5.566))

res=math.sqrt(9)
print(res)

# you can also import specific function from or variables from a module using from keyword.

from math import ceil,pi

ans=ceil(4.2)*pi     # --> here don't need to use math.ceil and math.pi
print(ans)

from math import *  # --> will import everything from math module ...this is not good approach ..
# may lead to cofusion ... as if to different module  can have same variable and function name

import math as m
# pyhton allows you to rename imported module using the as keyword
print(m.sqrt(56))

from math import ceil,floor as f
print(f(7.890))
print(ceil(7.890))

print(dir(math))
# python has a built-in function called dir that you can use to..
# view names of all the functions and variables defined in the module 
print(math.nan, type(math.nan))
print("\n----------------------------------------------\n")

# import pandas
# print(dir(pandas))

print("\n----------------------------------------------\n")
# from practice import wish, ut
import practice
print("__----___")
practice.wish()
from practice import*
wish()
print(ut)
print(practice)

# import 11_function_1  --> import nahi kr sakte kyuki module ke name mai _ nahi hona chahiye