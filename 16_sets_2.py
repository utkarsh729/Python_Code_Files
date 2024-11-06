# SETS methods
s1={3,4,7,9}
s2={3,23,9}

#  Union 
print(s1.union(s2))
s3=s1.union(s2)
print(s3)

# sets s1 and s2 remain changed
print(s1)
print(s2)
s1.update(s2)  # update the set s1 and add items of set s2 which is not in set s1
print(s1)

print("\n---------------------------------------------------------------------------\n")

s4={2,4,7,9,1}
s5={3,7,8,5}

# intersection 
print(s4.intersection(s5))
s6=s4.intersection(s5)
print(s6)

print(s4)
print(s5) 
s4.intersection_update(s5)  # update the set s4 ..only item comman in both set are in set set s4 
print(s4)

print("\n---------------------------------------------------------------------------\n")

s7={1,5,9,3,"Golu"}
s8={5,8,0,3}

# Symmetric difference a-b(_)a+b
print(s7.symmetric_difference(s8)) #--> print all items of both sets excepts the comman one 
s9=s7.symmetric_difference(s8)
print(s7)
print(s8)
s7.symmetric_difference_update(s8)   # update the set s7
print(s7)

print("\n---------------------------------------------------------------------------\n")

# isdisjoint()  --> two sets are disjoint if they don't have any element in comman
s10={2,3,5}
s11={44,66,77}
print(s10.isdisjoint(s11))

# issurperset()  --> methods check if all the items of a particular set are present in original set
# it returns true if all the items are present, else it return false

s12={2,4,7,9,1}
s13={4,1,23}
s14={2,9}
print(s12.issuperset(s13))
print(s12.issuperset(s14))

# issubset() --> methods check if all the items of the original set are present in particular set. 
# It return True if all the items are present, else it returns false.

print(s14.issubset(s12))  # s14 ke saare elements s12 mai present hai toh true else false
print(s13.issubset(s12))

print("\n---------------------------------------------------------------------------\n")

# add()--> method is used to add single item in set
s15={2,6,78,3.45,False}
print(s15)
s15.add("Golu")
print(s15)

# remove()/discard() --> method used to remove items from sets  
# The difference between  remove and discard is that, if we try to delete an item 
# which is not present in set, then remove() raises an error whereas discard() does not raise any error
s15.remove(6)
print(s15)
# s15.remove("G")  --> as G is not present in set hence removing will raise error
s15.discard(False)
print(s15)
s15.discard("G")  #--> does not riase any error

print("\n---------------------------------------------------------------------------\n")

# pop() --> method removes the last item of the set but the catch is that we don't know which
# item gets popped as set is unordered
# however we can access the popped item if we assign pop() method to variable

s16={2,6,"Golu",True,4.4,"Ekaa"}
print(s16)
s16.pop()
var= s16.pop()
print("Popped item is: ",var)
print(s16)

#  del --> is used to delete whole set
del s16
# print(s16)  #--> as set s16 is deleted the it will raise error

# clear()  --> methods are used to clear all items of set
s17={3,5,7,"Golu"}
print(s17)
s17.clear()
print(s17)

# Check if used to check whether given item is present in the set or not
s18={4,6,3,"golu",67}
if 3 in s18:
    print("Present")
else:
    print("No ")

if True in s18:
    print("yes")
else:
    print("No")