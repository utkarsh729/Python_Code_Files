#  for loops
name ="Utkarsh"
for n in name:
    print(n,end=",")
    if(n=="a"):
        print("Special")

colors=["Red","Yellow","Blue","Green"]  # --> This is list
print("\n")
for color in colors:
    print(color)
    for c in color:
        print(c)   

# Range function range()

for i in range(7):   # --> will go from 0 to 6
    print(i)   

print("\n")

for i in range(1,8):  # --> will go from 1 to 7
    print(i,i+1)

print("\n")

# range(start, stop, step)
# step --> is the difference between first number and next number

for i in range(0,10,2):
    print(i)

print("\n")
# print reverse number
for i in range(10,0,-1):  # -->will go from 10 to 1  
    print(i)
print("\n")
for i in range(17,-1,-3):
    print(i)

# float value are not allowed in range
# for i in range(3.3,8):  # give error
#     print(i)