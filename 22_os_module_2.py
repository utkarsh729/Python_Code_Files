import os
folders=os.listdir("formula")
print(folders)  # will print the list of file present in formula folder

for fol in folders:
    print(fol)
    print(os.listdir(f"formula/{fol}"))  # formula ke andhar ke andhar ki file print karega ye 
     
 