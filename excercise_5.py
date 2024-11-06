import random
print("you are going to play sanke water gun game with computer")
print("you have 3 rounds and you have to win atleast 2 to defeat computer")
print("-----------------chaliye suru karte hai----------------------")
you=0
com=0
for i in range(3):
    print("\n")
    print("------------------Round",i+1)
    print("enter 1 for snake ")
    print("enter 2 for water")
    print("enter 3 for gun")
    
    ch= int(input("What you choose..: "))
    ran=random.randint(1,3)
    if(ch ==1 and ran == 2):
        you = you+1
        print("You won this round")
    elif(ch==2 and ran ==3):
        you=you+1
        print("You won this round")
    elif(ch==3 and ran ==1):
        you=you+1
        print("You won this round")
    elif(ch==ran):
        print("Both choose same..round is draw")
        continue
    else:
        com=com+1
        print("Computer won this round")
    

print("\n")
print("Your score is: ",you)
print("Computer score is: ",com)
if(you>com):
    print("Congratulations you won the game ")
elif(you==com):
    print("Match is draw")
else:
    print("you loose .. computer won")

