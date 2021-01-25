# /usr/bin/python3

###LESSON 1 ###### INTRODUCTION

# print Hello world

print("Hello Python")

# print shapes

print("0---------")
print("  ||||||||")
print("          --}")

# Asterisks with strings
print("Hello Python " * 5)
print("#"*5)




# LESSON 2 ##### 
# Variables --> used to store data in memory of a computer

computers = 40
print(computer)

# update 
computers = 50
print(computers) # now 50
houseRating = 4.5 #floating numbers
is_correct = False or True # boolean values
userName = 'owen' # Strings


# checkpoint:
# create aprogram for a Fuel station for a train station. Assing number of passangers to 30, driver name and if is full or not.
# solution
passangers = 30
driver_name = "Mr John"
is_full = False / True


# #########Lesson 3 
### Getting User Input

withdrawal_amount = input("Enter amount to wothdraw ")
print("Welcome to Central bank, aproved amount is " + withdrawal_amount)

###challenge
# print a person's name, d.o.b , and favorite food from a user input perspective


### Lesson 4
## Convertions and Maths operations
#coversion
int() str() bool() float()
num_users = input("Enter number of users between 100")
computers = 100 / int(num_users) 
print("Collect " + str(computers) + " Computers")
# use type() to check the type of user input or variable assigned

### challenge
# write a program to allow a transportation company to convert lagguage to kg from lbs on their web page and cal price
luggage_lbs = input("enter weight: ")
luggage_kg = luaggage_lbs * 0.45
print(luggae_kg)

luggae_kg = int(luggage_lbs) * 0.45
price = luggage_kg * 25
print(price)


######### Lesson 5
# Strings

Lecture = 'Python for developers'

# escaping character
lecture = "Python's backend is Django"
lecture = 'Python\'s developer course here for free. subscribe'
lecture = ' Pthons course for "Develpopers" '
long_string = """ too long string with multiple line 
    get ready not to get bored
    
    hey 
    
    welcome developer """


# Accessing character
#indexing 0-10, n-1
name = " John Doe "
first_name = name[0]
last_char = name[-1] # last character
print(first_name) # first char

# slicing [index:index]
print(name[0:3]) # 
print(name[0:]) # start to end
print(name[:4]) # prints all upto index 4
print(name[:]) # prints all characters
new_name = name[:] # copys contents of the string to the new-string name

### challenge
# using th variable name computer = "MacBook", what is the ouput of the slice [0:-1] ? Write down before running
computer = "MacBook"
print(computer[0:-1])



#### Lesson 6 Formating Strings
# String contatenation
userName = "John"
sirname = "Doe"
print("Mr " + userName + "[" + sirname + "]" + " is an Engineer")

# F String formating
print(f" Mr {userName} [{sirname}] is an Engineer")

# .format of strings
print("Mr {} [{}] is an Engineer").format(userName, sirname)

# {} format of strings
print("Mr {userName} [{sirname}] is an Engineer", userName, sirName)


# String's Method

# cal total char in a string
myProgram = "Junior developer"
print(len(myProgram)) 
print(myProgram.lower()) # to lower
print(myProgram.upper()) # to uppper
print(myProgram.find('J')) # for more than one char, first index is return, -1 mean no char
print(myProgram.replace("Junior","senior"))
print(myProgram.replace('J','P'))

# check if element/char exist in a char
print("Junior" in myProgram) # returns a boolean value , if misspelled returns false.



#####3 Lesson
# Arithmetic Operations

print(5 + 2) # addition
print(5 -2) # subtraction
print( 5 * 2) # multiplication
print(5 / 2 ) # floating value
print(5/2) # returns only whole numbers
print(5%2) # returns remainder
print(5**2) # returns the power of a number

# incrementing values
i = 5
i = i + 5
print(i) # returns 15
i += 5 # returns same value (augumented opertor) shorter way of increamenting/decrementing value
i -+ 5 # decreament

# Oder of operations
print(5+2*5**2) # BODMAS
# adding parenthesis prioritize its operation

# Math Functions

import math
x = 45.987
print(round(x)) 
print(floor(x))
math......


#Conditional statements
# if statements

# if hot:
    cold outside
    wear a jacket
otherwise
    warm outside
    wear a t-shirt
else
    go  swimming

weather_Cold = True

if waether_Cold:
    print("Cold")
else:
   print("Hot")

