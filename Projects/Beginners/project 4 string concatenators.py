

# quiz 3

'''
String problem. No loops:
Use + to combine strings ,len(str) is the number of characters in a string ,
str[i:j]  extracts substrings starting at index i running upto but not including index j.

ex: given a string Bob  returns greeting "Hello Bob!"

'''
def hello_name(name):
    return "Hello "+ name + "!"
print(hello_name("Bob"))
print(hello_name("X"))
