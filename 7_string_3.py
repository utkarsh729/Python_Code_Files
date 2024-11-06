a="Utkarsh"
# String are immutable
print(len(a))
print(a.upper())  # give string into upper case but the original string does not get change
print(a.lower())  # give string into lower case but the original string does not get change
print(a)

print("----------1-----------")

str="!!!Yo Yo!!!!!"
print(str)
print(str.rstrip("!")) # removes the trailing/back character only
# only removes when trailing character is ending with the given character in bracket
str2="!!yoppppooooo"
print(str2.rstrip("o"))  
str2="!!yopppoooooo!"
print(str2.rstrip("o")) # here will not strip the string as it not ending with "o"

print("-------------2-----------")

str3="Golu is great!! Golu gaand faad dega sabki. #Golu"
print(str3.replace("Golu","Utkarsh")) # replace all the Golu occuring in string with Utkarsh
print(str3)  
print(str3.split(" ")) #splits the string at specified instance 
# and returns the separated string in as list items.
print(str3.split("a"))

print("--------------3-------------")

heading="welcome tO tHe Code"
print(heading.capitalize())  # captitalize the first letter of string and other letter in lowercase
print(len(heading))
print(heading.center(70)) # aligns the string in center as per parameter given by the user
print(len(heading.center(73)))  
 
print("--------------4--------------")

str4="Hello everyone I am here"
print(str4.count("e"))  # return the total time occurence
str5="Golu golu....!!!Golu"
print(str5.count("Golu"))
print(str5.startswith("go"))
print(str5.startswith("ol",6,12))
print(str5.endswith("lu")) # return true or false
print(str5.endswith("go",2,7)) #check string is ending with go in between(2,7) where last 7 not included

print("--------------5----------------")

str6="Momo is good girl. She is very beautiful"
print(str6.find("ishh")) # returns the index of first occurence and returns -1 if not present in string
print(str6.index("is")) # similar to find() but returns exception if not present in string

print("---------------6---------------")

str7="Good morning maam"
print(str7.isalnum())
# return true if the string consist of only alphabets and numeric characters
str8="Goofmorningmaam55"
print(str8.isalnum())

print(str8.isalpha()) 
# return true only for string is consist of alphabets

print("----------------7-----------------")

print(str7.islower())
# return true only if all the letters are present in lowercase
print(str7.isupper())
# return true only if all the letters in string are in uppercase

print("-------------8----------------")

str9="Hello \n everyone"
print(str9.isprintable())
# return true if all the values within the given string is printable, if not then return false
str10="Hello everyone"
print(str10.isprintable())
print(str10.isspace())
# return true only if string contains white space
str11="    "
print(str11.isspace())

print("---------------9----------------")

str12="Welcome to my Code"
print(str12.istitle()) 
# return true only if the first letter of each word of the string is capitalized, esle return false
str13="Welcome To My Code"
print(str13.istitle()) #true
str14="Welcome To My COde"
print(str14.istitle()) #false

print("---------------10----------------")

str15="Good aLl are"
print(str15.swapcase())
# converts lowecase letter to uppercase and uppercase letter to lowercase
str16="hello evErone"
print(str16.title())
# converts first letter of each word in uppercase and rest letter in lowercase

# Check whether given sub string is present in main string
if "ol" in "Golu":
    print("present")
else:
    print("not present")