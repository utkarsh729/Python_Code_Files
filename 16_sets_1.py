#  SETS --> are unordered collection of data items. They store multiple items in a single variable.
# Sets items are separated by commas and enclosed within curly brackets{}.
# Sets are unchangeable means you cannot change items of the set once created.
# Sets do not contain duplicate items

s1={2,6,79,2,3,True,5.3}  
print(s1)   # 2 will print only once
# there is no guarantee that order is maintained...item occur in random order 
# and hence they cannot be accessed using index numbers

# To make empty set 
s2={}  #-->wrong
print(type(s2))

s2=set()  #--> RIGHT
print(type(s2))

# accessing set elements
for value in s1:
    print(value)