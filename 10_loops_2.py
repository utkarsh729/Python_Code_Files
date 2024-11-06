#  while loops
#  while loops execute the statements while the condition is true
 
i=0
while(i<3):
    print(i)
    i=i+1

print("Done with loop")
 
i=0
while(i<=10):
    i=int(input("Enter the number: "))
    print(i)

# decrementing while loop
# we can even use else statement with while loop....
# as soon as while condition become false else statement is executed

count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("Inside else after while")

# python don't have do while loop but we can emulate it

k=int(input("Enter the number: "))
print(k)
while(k<10):
    k=int(input("Enter the number: "))
    print(k)
    