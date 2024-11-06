c1={3:"Neha", 7:"Golu", 1:"Ameesha", 17:"Isha",3:"Geeta"}
# if dictionary have more then one same key aur dono key ki different value ho toh ....
# vo wali value print hogi jo last mai hogi...yaha 3 (key) ki value Geeta hogi
c2={6:"James",19:"Rahul"}

print(c1)
print()
c1.update(c2)  # add dictionary c2 in c1 
print(c1)
c2.clear()  # remove all the keys and values from dictionary
print(c2)

print()

empt={} # -->empty dictionary
print(empt)

print("\n-------------------------------------------------------------\n")

stud1={'name':"Neha", 'roll':5655, "c":715, "age":20}
stud1.pop('name')  # delete the name key value
print(stud1)

stud1.popitem() # removes the last item from dictionary
print(stud1)

del stud1['roll']  #--> delete the correspond key and value
print(stud1)
del stud1     #--> delete the whole dictionary
# print(stud1)   #-->give error as dictionary is deleted
# del stud[20]  --> give error as 20 is not in dictionary 