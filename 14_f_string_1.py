# f-String
#  It is new string fromatting mechanism.

letter="Hey my name is {1} and I am from {0}"
# letter="Hey my name is {0} and I am from {1}"
country="India"
name="Golu"

print(letter.format(country,name))
# print(letter.format(name,country))

# Above method is difficult to handle as which argument goes where

print("\n------------------------------------------------------------------------\n")

# To overcome we use f-string 

letter=f"Hey my name is {name} and I am from {country}"
print(letter)
clg="CU"
degree="btech"
print(f"I am doing {degree} from college {clg} ")
fees=45000.3456
print(f"My total fees is for an year is: {fees:.2f}") 
# .2f will print upto two decimal places
print(f"{2*30}")
# it is type string
print(type(f"{2*30}"))

# if you want to use {}  in f-string then use double bracket
# print(f"Good morning {India}") --> give error as india is not defined variable
# for writing india in brackets use double brackets  --> applicable to f-string only
print(f"Good morning {{India}}")
print("Good morning {India}") #--> if use not using f-string then this is valid 

