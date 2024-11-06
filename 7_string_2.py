names="Golu, Shubham"
print(len(names))
# len() function is used to find the length of string
fruit="Banana"
len1=len(fruit)
print("banana is",len1," words")
print(fruit[0:4]) 
# index 0 to index 3 will print ..index 4 will not include
print(fruit[1:5])
# printing will start from index 1 to 4
print(fruit[:4])
# here index automatically start from zero
print(fruit[0:-2])
# print(fruit[0:len(fruit)-2]) is same as above ...first calculate the length of fruit then minus 2 from it
# and print till the index one less then that obtain
print(fruit[-3:-1])
nm="harry"
print(nm[-4:-2])
