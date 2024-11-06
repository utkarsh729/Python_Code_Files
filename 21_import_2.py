import golu
# sirf import karne se jo module ke andhar code a vo run ho jayega 
# isliye yaha "utkarsh singh welcomes you" doh baar print hoga 
# isse bachne ke liye hum __name__ == __main__ idiom use karte hai

print('\n-----------------------------------------------------------------\n')
golu.welcome()
from golu import hel as h
# print(hel) --> give error because humne hel as h import kiya hai toh h use karna hoga
print(h)

# yaha __main__ ki value golu hai isliye if wala part run nahi hoga 

