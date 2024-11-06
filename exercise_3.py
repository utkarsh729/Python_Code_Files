# Create a program capable of displaying questions to th user like KBC. 
# Use List data type to store the question and their correct answers.
# Display the final amount the person is taking home after playing the game.

ques=["The capital of Uttar Pradesh", "National Bird of India", "Prime Minister of India", "Interpreter/Compiler language"]
amount=10000
opt1=["Lucknow","Patna","Delhi","Chennai"]
opt2=["Tiger","Crow","Peacock","Parrot"]
opt3=["Modi","Rahul","Rakhi","Salmaan"]
opt4=["Java", "C++","Pyhton","R"]
options=[opt1,opt2,opt3,opt4]
correct_ans=["Lucknow","Peacock","Modi","Java"]
j=0
amount=0
k=0
print("\n~~~~~~~~Welcome to Kaun Banega Chutiya~~~~~~~~~~\n")
for i in ques:
    print(i)
    print(options[j])
    j=j+1
    ans=input("Enter your answer: ")
    if ans in correct_ans:
        print("\nBilkul sahi uttar diya aapne")
        amount=5000+amount*2
    else:
        print("\nLondu galat answe hai...Chutiya\n")
        break
    if(k<len(i)-1):
        print("\nNext Question\n")
        k=k+1

print("```````````~~~~~~~~~~~~~~~~~~~~~~~~~``````````````")
print("\nAmount you won: ",amount)
print("\nCongratulations aap sucessfully chutiya ban chuke hai\n")


    