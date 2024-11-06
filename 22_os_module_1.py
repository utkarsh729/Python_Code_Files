# OS MODULE 
# The os module in Python is a built-in library that provides functions 
# for interacting with the operating system. 
# It allows you to perform a wide variety of tasks,
# such as reading and writing files, interacting with the file system, and running system commands.

import os 

if(not os.path.exists("formula")):  # check whether the floder exits or not 
    os.mkdir('formula')  # make folder in this directory 

# for i in range(1,11):
#     os.mkdir(f"formula/f{i}")   # will make folder inside formula as f1,f2....f10 

# here formula/f --formula is name of folder and f is name of sub folder

for i in range(1,11):
    os.rename(f"formula/f{i}", f"formula/car{i}") # --> will change name from f1,f2...f10 to car1,car2..car10

print(os.getcwd())  # --> return the directory in which currently you are working

