

'''
Given a string and a non negative int n, return a larger string 
that is n copies of the original string 

string_times("Hi", 2) ---> HiHi
string_times("hey", 3)---> heyheyhey
'''

# step one --> create the function
def string_times(message, times):
    if (times>0):
        final = message * times
    else:
        print("Enter a non negative number")
    return final
print(string_times("Hey",-2))


# simplified solution
def string_times(message, times):
    return message * times
print(string_times("Hey",2))
