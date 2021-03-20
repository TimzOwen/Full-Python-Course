
'''
return the number of even ints in the given array
the % returns the remainer
ex:
count_evens([2,4,3,5,8])-->3
count_evens([1,2,3,4,5,6,7,8])--4
'''

def count_evens(numbersList):
    count = []
    for nums in numbersList:
        if nums%2==0:
            count.append(nums)
    return len(count)
print(count_evens([2,4,6,8]))
print(count_evens([1,2,3,4,5,6,7,8,9,10]))


# soln 2

def count_evens(numbers):
    counter = 0;
    for nums in numbers:
        if nums%2 == 0:
            counter += 1
    return counter
print(count_evens([2,4,6,8,10]))


