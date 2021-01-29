
# CHAPTER TWO

# Lesson 1
# Lists

myFriends = ["Timz","Owen","Shem","Salma","Joy","Hussein","Juma"]
print(myFriends)
print(myFriends[0]) # Assecing elements
print(myFriends[-1]) # Last item in the list
print(myFriends[2:]) # prints elements from third elements to the last element
print(myFriends[2:4]) # print elements between ranges

# new sliced list does not affect the former original list
print(myFriends[1:3]) # ['Owen', 'Shem']  returns a new created list
print(myFriends) # ['Timz', 'Owen', 'Shem', 'Salma', 'Joy', 'Hussein', 'Juma']
myFriends[0] = "Tim" # editing elements in a list
print(myFriends) 


# challenge
# write a program to return largest values in a list 

numbers = [9,4,6,12,9,4,3,1,8]
largestNumber = numbers[0]
for number in numbers:
    if number>largestNumber:
        largestNumber = number
print(largestNumber)


# LESSON 2
# 2-D Lists
# Each matrix in the row and column are also list in the defined 2-D array List
matrix = [
    [2,4,6],
    [1,3,5],
    [11,22,33]
]
print(matrix[0][0]) # access first element in the list
print(matrix[1][1]) # elements 
matrix[0][1] = 20
print(matrix[0]) # [2,20,6]

#iterate through a the matrix
for x in matrix:
    for i in x:
        print(i,end=" ")
    print()


# Methods in List
numbers = [11,22,33,44,55,66,22]
numbers.append(44) # adding element to the end
numbers.insert(0,99) # adding elements to a specific index
numbers.remove(33) # remove elements
numbers.clear() # removes all elements
numbers.pop() # removes last item
numbers.index(44) # returns index of the first occurance of an item
print(50 in numbers) # checks existance of an element
print(numbers.count(22)) # counts occurance of multiple items in a list
numbers.sort() # sorts the numbers
numbers.reverse() # descending oder
num2 = numbers.copy() # copying from numbers list
                      # copied list doesn't affect the list in numbers list. (independent)
                      
                      
# Challenge
# write a program to remove duplicate elements in a list and arrange the numbers in descending order

numbers = [2,3,4,5,6,2,4,7,8,4,9]
new_list = []

for x in numbers:
    if x not in new_list:
        new_list.append(x)
        new_list.reverse()
print(new_list)

