age=int(input("Enter your age: "))
print("Your age is: ",age)

if(age>18):
    print("you can drive")
    print("Congratulations")
# here indentation means it is part of if else statement
else:
    print("you cannot drive")
    print("Try after 18")
print("Yay!")  # it is outside else

# if-elif-esle
num=int(input("Enter the number: "))

if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is zero")
elif(num==7):
    print("My favourite number")
else:
    print("Number is positive")

# nested if-elif-else
number=int(input("Enter the number: "))
if(number<0):
    print("Number is negative")
elif(number>0):
    if(number>100):
        print("Number is greater then 100")
    elif(number==7):
        print("Number is sepecial")
    else:
        print("Number is positive")
else:
    print("Number is zero")