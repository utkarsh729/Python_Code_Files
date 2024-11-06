country=('India',"Bhutan","Nepal","Bsdk","Sri")
# country.append("Ass")  --> give error as we can not change the tuple once created
print(country)
tempC=list(country)  # --> as we cannot change the tuple but we can do it by first changing tuple to list 
tempC.append("China")
tempC.pop(3)
tempC[2]="Ass"
country=tuple(tempC)  # --> converting back to tuple
print(country)

# We can directly concatenate two tuples without converting them to list..as here we are making new tuple
t1=(1,5,2,89)
t2=("Golu",7,"Polu")
# t2.extends(t1)  --> give error as we cannot change the tuple

t3=t1+t2
print(t3)

print("\n----------------------------------------------------------\n")

t4=(35,9,7,9,7,92,2,5,7,40,5,7)
res=t4.count(7)  # --> return total number of occurence of item in tuple
print(res)
print(t4.index(9))  # --> return the index of first occurence of item in tuple
#  give error if the item is not present in tuple

ans=t4.index(7,5,10)  # check the occurence of 7 between index 5 to index 9 and return first occurence
print(ans)

