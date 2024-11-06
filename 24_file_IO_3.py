# In python, the seek() and tell() functions are used to work with file objects and their positions within file.
# This function are part of the built-in io module 

# seek() function allows you to move the current position within a file to a specific point. 
# The position is specified in bytes, and you can move either forward or backward from the current position.

# tell() functions returns the current position within the file, in bytes. This can be useful for 
# keeping track of your location within the file 

with open("myfile.txt", 'r') as f:
    f.seek(9)  # took the pointer to the 9 place
    print(f.tell()) 
    data= f.read(6)  # read the next 6 bytes after 9
    print(data)
    print(f.tell())

# turncate() if you want to turncate the file to specific size, you can use the turncate function
#  it works with only write and append mode

with open("me.txt",'w') as f:
    f.write("Hello buddy me utkarsh")
    f.truncate(10)    # file size is reduced to 10 byte and original file also reflect this change



with open("me.txt",'r') as f:

    d=f.read()
    print(d)
