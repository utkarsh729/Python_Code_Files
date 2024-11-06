def wish():
    print("good morning")
ut="utkarsh is good boy"

def Gmean(a,b):
    mean=(a*b)/(a+b)
    print("The mean of number is: ",mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

# def isLesser(a,b):  --> will give error as we have not define the body of function

def isLesser(a,b):
    pass    #--> here we can write the body later and this will not give an error
    
wish()   
a=8
b=4
Gmean(a,b)
isGreater(a,b)

c=12
d=16
Gmean(c,d)
isGreater(c,d)
