#  break and continue in loops

for i in range(1,13):
    if(i==11):
        break
    print("7 X",i,"=",7*i)

print("Exit from loop when i is: ",i)
print("\n")
for i in range(1,13):
    if(i==5):
        print("Skip the iteration")
        continue
    print("10 X",i,"=",10*i)

print("Done")

for k in [2,10,23,5,7,8]:
    if(k%2==0):
        continue
    print(k,end=":")

print("\n")

# do-while loop creation
i=0
while True:
    print(i)
    i=i+1
    if(i==10):
        break