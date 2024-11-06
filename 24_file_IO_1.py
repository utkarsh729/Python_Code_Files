# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. 
# This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. 
# t mode is used to handle text files. t refers to the text mode.
# There is no difference between r and rt or w and wt since text mode is the default. 
# The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).


#   OPENING A FILE 
f=open("myfile.txt",'r')   
print(f)  # will not print the content of file but print something related to file 


#  READING FROM FILE 
content=f.read()
print(content)

f.close()


# WRITING IN FILE
f=open("myfile.txt","w")    # --> before writing will clear all the previous content from file
f.write("beta humse nhi toh \n kisi se nahi")

f.close()
print("\n------------------------------------------------------------------------\n")

# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it.


with open("myfile.txt",'a') as f:
    f.write("\ndone ho gaya")

with open("myfile.txt",'r') as f:
    con=f.read()
    print(con)