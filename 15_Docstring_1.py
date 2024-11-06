# Docstring
# Python docstring are the string literals that appear right after the defination
# of a function, method, class or module
# They are used to document our code.
# We can access these docstring using the doc attribute


def square(n):
    '''Takes n as input and prints the square of n'''  #--> This is not comeent this special type string 
    # called docstring stroed in attribute __doc__
    print(n**2)

square(10)
print(square.__doc__)  # --> print the doc string

print("\n\n")

def number(n):
    print(n)
    '''takes n input and print the number'''  #--> ye docstring nahi hai 
    # ..docstring just function ke baad likhi jaati hai
    print("Done")

number(7)
print(number.__doc__)  # -> will print none as no doc string in number()


# Pyhton comments are description that help programmers better understand the intent 
# and functionality of the program. They are completely ignored by the python interpreter.

print("\n\n--------------------------------------------------------------------------\n\n")
# PEP  --> PEP is a document that provides guidlines and best practices on how to write Pyhton code.
# PEP stands for Python Enhancement Proposal
import this  # print Zen of Python