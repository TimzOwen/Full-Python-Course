
# LESSON 2
# TUPLES
# SIMILAR TO LIST;
# they are immutable, cannot be edited, added 

numbers = (2,4,6,8,10)
numbers[0] # accessing elements
numbers[0] = 10 # Type Error , they cannot be edited / not support item assignemnt


# UNPACKING
numbers = (2,4,6)

# Accessing from indexing and multiplying
mult = (numbers[0]*numbers[1]*numbers[2])
print(mult)# 48 but tedious code

# assign new var 
x = numbers[0]
y = numbers[1]
z = numbers[2]
print(x*y*z)  # 48

# with unpacking 
x,y,z = numbers
print(x*y*z) # 48
