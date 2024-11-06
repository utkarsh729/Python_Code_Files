# list methods
l=[2,7,3,9]
print(l)
l.append(1)  # --> add item at the end of list
print(l)
l.sort()  # --> sort list in ascending order
print(l)
l.sort(reverse=True) # --> sort in descending order  
print(l)

names=["Golu","utkarsh","Neha","Ekaa"]
names.reverse() #--> reverse the list items
print(names)
names.reverse()
names.append("Neha")
names.append("Teja")
print(names)
print(names.index("Neha"))  #--> returns the index of first occurrence of item in list
#  give error in item is not present in list

num=[2,6,8,2,5,9,2]
print(num.count(2))  # --> returns the total count of item in list 

print("\n----------------------------------------------------------\n")

n=num  # here we are creating reference of list 
n[0]=0 # so if we change the item in one list 
print(num) # ..the items of other list will also change
print(n)

number=num.copy()  # here we are copying of one list item to another list
print(number)
number[0]=4       # changing list items of one will not change the items in another list
print(number)
print(num)

print("\n----------------------------------------------------------\n")

num.insert(2,899)  # --> insert 899 at index 2 in list and shift other items
print(num)

l1=[4,67,8]
l2=[9,3,12]

l2.extend(l1)  # add items of list l1 to list l2 
print(l2)  
# here l2 changes but below l1 and l2 does not change

k=l1+l2  # --> concatenation of two list
print(k)