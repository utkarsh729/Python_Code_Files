# TUPLEs
# tuple is similar to list 
# Tuples are unchangeable means we can not alter them after creation
# tuples item are separated by commas and enclosed within round brackets ()

tuple1=(3,6,8,1)
tuple2=(7,"Golu",0.4,True)
print(tuple1)
print(tuple2)

t1=(1)
print(type(t1)) # it shows the type int 
print(t1)
t2=(1,)    # tuple of one element
print(type(t2))  
print(t2)

t3=(5,6,1,9,56,78,1,4)
# t3[0]=1   --> give error as we can not change the tuple
# printing tuple items
print(t3[0])
print(t3[1])
print(t3[2])
print(t3[3])

print("\n-----------------------------------------------------\n")



if 10 in t3:
    print("present")
else:
    print("Not present")

tup3=t3[1:5]
print(tup3)
t4=t3
print(t4)
# we can directly copy the one tuple element to other by referencing as we further can't change the
# tuple.....so copy function is not used with tuples

t3=(44,4,4,2,234,4)
print(t3)