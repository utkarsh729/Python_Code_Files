# final keyword
# The final block is always executed, so it is generally used for doing concluding task like 
# closing file resources or closing database connection or may ending program with delightful message

try:
    l1=[2,4,7]
    index=int(input("Enter the index: "))
    print(f"Value at index {index} is {l1[index]}")
except ValueError:
    print(ValueError)
except IndexError:
    print(IndexError)
except:
    print("Different type of error")
# finally:
#     print("I am also executed")
print("I am also executed")

# uper finally and print statement toh same hua...matlab print bhi toh use kr sakte uske jagah
# toh finally ka kya use??

print("\n-------------------------------------------------------------------\n")

def func1():
    try:
        l1=[2,4,7]
        index=int(input("Enter the index: "))
        print(f"Value at index {index} is {l1[index]}")
        return 1
    except ValueError:
        print(ValueError)
        return 0
    except IndexError:
        print(IndexError)
        return 0
    except:
        print("Different type of error")
        return 0
    finally:
        print("I am also executed")
    print("I am also executed")

#  yaha koi na koi value return ho jayegi toh print execute nahi ho payega...but finally jarur execute hoga
# uske baad value return hogi

print("\nOutside function body")
x=func1()
print(x)

