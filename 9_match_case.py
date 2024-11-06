x=int(input("Enter the number: "))
match x:
    case 0:
        print("X is zero")
    case 7:
        print("X is seven")
        print("My favourite number")
    case _ if x%2==0:
        print("It is even")
    case _ if x>=100:
        print(x," greater then hundred")
    case _ if x!=10:
        print(x," is not 10")
    case _:     #--> default case
        print("Inside default case")
        print("Value of x is: ",x)

# in python we don't use break 
# if one of the following case matches then below cases will not run
# if no case matches then default case will match
# in python default case is always written at the end

y=input("Enter character: ")  #take input in form of string
match y:
    case 'a':
        print("Character is a")
    case "+":
        print("Addition")
    case 1:
        print("It is number")
    case _:
        print("unknow")

print("end")
