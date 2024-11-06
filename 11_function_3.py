# RECURSION

def fact(a):
    
    if(a==1 or a==0):
        return 1
    else:
        return a*fact(a-1)
    
print(fact(0))

# To find the nth term in fibonacci series
def fibo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
        

print(fibo(7))
