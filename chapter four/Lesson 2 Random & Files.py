
# GENERATING RANDOM VALUES
# python built in module 
# Google search "python 3 module index"
# Random generates values between 0 and 1 

#use random to generate random values
import random 

for x in range(5):
    print(random.random())  # generate random numbers between values 0-5 in 0-1 range
    
    
# print random int values 

for x in range(4):
    print(random.randint(1,10))


# generate a random piicking from a list
leaders = ["Timz","Owen","Shem","Kiptoo","Salma","Joy","Kirui"]
chosen = random.choice(leaders)
print(chosen)


## Challenge
# create a dice roller 

import random

class Dice:
    
    def roll(self):
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        return num1, num2 # Tis is a tuple (num1,num2) but no need as python already recognize it without braces
dice = Dice()
print(dice.roll())



# #
# FILES AND DIRECTORIES
# absolute path: 
#     c:\Program\program Files\anaconda
#     /usr/local/bin
    
# Relative Path
#     a file with your working IDE 
    
#check if a path Exists
from pathlib import Path

path = Path("fOLDER")
print(path.exists()) # CHECK if a path exists 
path2 = Path("MainServer")
print(path2.mkdir()) # creates an empty directory
path2.rmdir() # remove the directory

# print all directories in a path
path4 = Path() # the current path
print(path4.glob('*.*')) # all files
print(path4.glob('*.csv')) # print all with extensions

# print all files using a for loop
for files in path.glob('*.xls'):
    print(files)
    
    
