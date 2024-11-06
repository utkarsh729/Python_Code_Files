# Write a python to translate a message into secret code language. Use the rules below to translate normal 
# english into secret code 

# CODING
#  --> if the word contain atleast 3 characters, remove the first letter and and append at the end
#  now append three random character at the starting and at the end
#  --> else simply reverse the string

# DECODING
# if the word contains less then three character reverse it
# else..remove three letter from start and end. Now remove the last letter and append to the beginning
import string
import random
str=input("enter the string: ")
print("enter 1 for encode")
print("enter 2 for decode")
print("\n---------------------------------------------------------------------\n")
choice=int(input("enter your choice: "))
if(choice==1):
    if(len(str)>=3):
        c1=str[0]
        str=str[1:]
        str=str+c1
        # str=str[1:]+str[0]
        # print(str)
        i=0
        while(i<3):
            rl=random.choice(string.ascii_letters)
            str=rl+str
            i=i+1
        j=0
        while(j<3):
            rl=random.choice(string.ascii_letters)
            str=str+rl
            j=j+1
        print("encoded string is: ",str)
    else:
        if(len(str)==1):
            print("encoded string is: ",str)
        else:
            c1=str[0]
            str=str[1:]+c1
            print("encoded string is: ",str)

elif(choice==2):
    if(len(str)>=3):
        try:
            str=str[3:]
            l=len(str)
            str=str[0:l-3]
            # str=str[3:-3]
            l=len(str)
            ch=str[l-1]
            str=ch+str[0:l-1]
            print("string after decoding: ",str)
        except:
            print("error while decoding...string is too small to remove three letter from end")
    else:
        if(len(str)==1):
            print("string after decoding: ",str)
        else:
            ch=str[1]
            str=ch+str[0]
            print("string after decoding: ",str)










