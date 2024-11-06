# if...else in one line 
a=88
b=7
print("a") if a>b else print("=") if a==b else print("b")

# print("hello") if a>b --> give error as else is compulsory 
print("hello") if a>b else ""

c=a if a>b else 200
print(c)

hai=True if a<b else False
print(hai)