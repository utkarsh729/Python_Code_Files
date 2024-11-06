# 'is' vs '==' in Python
# In Python, is and == are both comparison operators that can be used to check if two values are equal.
#  However, there are some important differences between the two that you should be aware of.
# The is operator compares the identity of two objects, 
# while the == operator compares the values of the objects.
# This means that is will only return True if the objects being compared are the exact same object in memory,
# while == will return True if the objects have the same value.

a=4  # integer
b="4"  # STRING
print(a is b)
print(a == b)

print('\n')
l1=[1,2,3]
l2=[1,2,3]   
# python create to different list 
print(l1 is l2)
print(l1==l2)

print('\n')
x=7
y=7
print(x is y)
print(x == y)
# One important thing to note is that, in Python, strings and integers,tuple are immutable,
# which means that once they are created, their value cannot be changed so it do not create more then
# one variable having same value 
# This means that, for strings and integers, is and == will always return the same result

t1=(1,5)
t2=(1,5)
print(t1 is t2)
print(t1 == t2)

c=None
d=None
print(c is d)
print(c==d)