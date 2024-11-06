# readline()  -->  the readline() methods reads a single line from the file. if want to read multiple lines 
# we can use the loop.
# The readline() reads all the lines of the file and returns them as a list of strings
 

f=open("marks.txt",'r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
f.close()

print('\n--------------------------------------------------------------\n')

f=open("marks.txt","r")  # we have to reopen the file as in previous while the f reached to end of file 
# so to use readline from starting we have close the previous and open it again
i=1
while True: 
    line=f.readline()
    if not line: 
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of sudent {i} in English are: {m1}")
    print(f"Marks of sudent {i} in Maths are: {m2}")
    print(f"Marks of sudent {i} in EVS are: {m3}")
    i=i+1
f.close()
print("\ndone")

# str="12,13,14"
# str2="56,45"
# s=str.split(",")[2]
# print(s)


print('\n--------------------------------------------------------------\n')


# writelines() --> the writelines() method writes a sequence of string to a file. 
# The sequence can be any iterable object, such as a list or tuple.
f=open("about.txt","a")
line=['hello\n',"hi\n","hyy\n","byy\n"]
f.writelines(line)

# the \n character is used to add newline at the end of each string
# as writelines() method does not add new line between the strings in the sequence
# alternative is below

for l in line:
    f.writelines(l)
f.close()
