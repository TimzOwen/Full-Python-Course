

'''
The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Retuen True true if we sleep in.
sleep_in(False, False)-->True
sleep_in(True, False)-->False
sleep_in(False,True)-->True
'''

# quiz number 1 

# step 1.
# write a function that takes in two parameters
def sleep_in(weekday, vacation):
    if(weekday==False and vacation==True):
        return True
    else:
        return False
print(sleep_in(False,True))


# simplify more
def sleep_in(weekday, vacation):
    if not weekday and vacation:
        return True
    else:
        return False
print(sleep_in(False,True))
