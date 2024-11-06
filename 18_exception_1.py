a=input("Enter the number: ")
try:
    print(f"Printing table of {a}: ")
    # if you give string as input then after this line the code will not execute ..it will run except part
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid input")

print("End of program")

 
try:
    num=int(input("Enter the number: "))
    a=[2,3]
    print(a[num])
except ValueError:
    print("Number entered is not integer")
except IndexError:
    print("Index Error")
except:
    print("Different kind of error")
    
    