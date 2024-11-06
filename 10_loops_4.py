# we can use else with loops also


for i in range(5):
    print(i)   
else:                              # --> else part will execute when we are not unable to enter in for loop
    print("Unable to enter in for loop")

print()
#  else part printed after all the sucessful execution of loop
for i in []:
    print(i)
else:
    print("List is empty now")

print()

n=10
while(n>=5):
    print(n)
    n=n-1
else:
    print("n is lesser then 5")

print("\n--------------------------------------------------------------------\n")

for i in range(7):
    print(i)
    if(i==4):
        break
else:
    print("No i")

# in this case else part will not print kyuki loop i=4 pr break ho gaii matlab khatam ho gaii ..
# isliye else part nahi chala kyuki uske baad koi iteration he nahi huii jo check kare ki i ki value
# kya hai ..aur firr decide kare for execute karna hai ya else.