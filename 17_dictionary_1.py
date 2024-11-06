# DICTIONARY
# are ordered collection of data items. They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets{}

dic={
    "Golu":"Good person",
    7:"Mera lucky number",
    "Song":"Give relief"
}
print(dic)  # print the whole dictionary
print("\n")
print(dic[7])   # print the correspondance key value
print(dic["Golu"])

print("\n")
for i in dic.keys():
    print(i)   # Print the key
    print(dic[i])   #Print the key's value

print("\n----------------------------------------------------------------------------\n") 

info={'name':'Golu', 'age':21, 'id':5640}
print(info["id"])  
# print(info["college"])  # raise error if key is not present in dictionary
print(info.get('id'))
print(info.get('college'))  # will not raise error if key is not in dictionary
# it will print none

print(info.keys())  # print all the keys of dictionary 
print(info.values()) # print all values of dictionary

for i in info:
    print(f"The value corresponding key {i} is {info[i]}")

print("\n-----------------------------------------------------------------\n")

print(info.items()) 
# print all key with values

for ky, value in info.items():
    print(ky,value)
    print(f"The value corresponding to the key {ky} is value {value}")

