# LIST
# List are ordered collection of data items
# They store multiple items in a single value
# List items are separated by commas and enclosed within square brackets[].
# List are changeable meaning we can alter them after creation

marks=[50,36,89]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])  # to print single item of list ...use index value
print(marks[2])
# print(marks[3])  # give error as list index out of range

list1=[45,99.23,"Golu",'A',True]
print(list1)        #-->print in list format

for i in list1:
    print(i)   #--> print one item in one line

print(list1[-3]) # negative index
print(list1[len(list1)-3])  #convert into positive index
print(list1[5-3])  #Positve index
print(list1[2])   # all print same

print("\n----------------------------------------------------------\n")
#  check whether an item is present in list

if "Golu" in list1:
    print("It is present")
else:
    print("No")

if 7 in list1:
    print("7 is present")
else:
    print("7 not present in list")

print("\n")

print(list1)  #--> print all the items of list
print(list1[:])  # --> it also print all the element
print(list1[1:])  # --> print items from index 1 to end
print(list1[:4])  # --> print items from starting till index 3
print(list1[2:5])  # --> print items from index 2 from index 4
print(list1[::2])  # --> silicing ...print every second element
print(list1[1:5:3])  

print("\n----------------------------------------------------------\n")

# list comprehension
# it used for creating new list from other iterables like list,tuples,sets,dictionaries 
# and even in array and strings.

list2=[i for i in range(4)]
print(list2)

list2=[i*i for i in range(6)]
print(list2)

list2=[i for i in range(3,15) if i%2==0]
print(list2)

names=["Utkarsh","Golu","Momo","Neha","Ashu"]
list3=[item for item in names if "a" in item]
print(list3)