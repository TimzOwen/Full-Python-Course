

# quiz 4

'''
Given an arrays of ints, return true if 6 appears as either first or last element in the arrays
The arrays will be lenght 1 or more

ex:
first_last6([1,2,6])---> True
first_last6([6,4,3,4,5])-->True
first_last6([4,6,7,8,9])-->False

'''

def first_last6(arraysList):
    if arraysList[0]==6 or arraysList[-1]==6:
        return True
    else:
        return False
print(first_last6([2,6,7,8,9]))
print(first_last6([2,6,7,8,6]))
print(first_last6([6,6,7,8,9]))
