# ENUMERATE FUNCTION --> is built in function in python that allows you to loop 
# over a sequence(such as list, tuple or string) and get index and value of each element
# in the sequence at the same time

marks=[34,64,23,77,89,95]

for i,num in enumerate(marks):
    print(i,num)

print('\n')
name=["utka","golu","neha","ashu","momo"]

for index,naam in enumerate(name,start=1):   # start the index from one 
    print(index,naam)
    if(index==2):
        print("i am awesome")
    