
# Regular Expression 
# Regular expression makes your job easier especially when searching for specific patterns


# QUIZ NUMBER 1


# Example: Phone number validation
#(415-555-4242) ---> Kenya number formart

# sample in function

def isPhoneNumber(text):
    if len(text) != 14:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# search for phone number in a text:
print(isPhoneNumber(message))


# solution in Regex


# Done in regular Expression
# sample phone number text search :
import re

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number.search('my number is 415-255-4040 for official use')
print("phone number found: " + mo.group())

# reduce the compile arguements 
kenya_phon = re.compile(r'\d{3}-\d{3}-\d{6}')
phone = kenya_phon.search("This is the phone number 254-740-354167 to call for help")
print("Help number: " + phone.group())



# perform group matching
# group matching:
# print a phone number in two group matching

# group matching:
# print a phone number in two group matching

import re

phone_number = re.compile(r'(\d{3})-(\d{4}-\d{4})')
final_output = phone_number.search('my number is 254-7403-4167 for any help desk inquiries')
print("Help line number is: " + final_output.group())
print("help line 2: "+ final_output.group(1)) # prints the number 1 from the first brackets of the hyphen.
print("help line 3: " + final_output.group(2)) # this prints the second shift
print("full help line number: " + final_output.group(0)) # 0 prints all the number in the format


# using pipe to find occurance of a pattern in search

import re

names = re.compile(r'timz | owen | ninja')
found_name = names.search("Hi, my name is timz owen the code ninja")
print(found_name.group()) # returns fisrt occurance of a pattern incases where there are more than one occurance


# pipe matching with different patterns
# using pipe to find occurance of a pattern in search

import re

names = re.compile(r'bat(man | tle | ing)')
found_name = names.search("The batman today decide he will be bating before the battle")
print(found_name.group())
print(found_name.group(1))


# matching with question mark.
# check if the match character is there or not.
import re

batRex = re.compile(r'Bat(wo)?man')
mo1 = batRex.search('The adventures of Batman')
print(mo1.group())  # Batman
mo2 = batRex.search("the adventures of Batwoman")
print(mo2.group())  # Batwoman


# matching with question mark.
# check if the match character is there or not.
import re

phone_number = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phone_number.search("The help line is 254-740-3541 for school of Engineering. while that of emergency is 740-3542")
print(mo1.group()) # returns 254-740-3541
mo2 = phone_number.search("new number is 254-6767")
print(mo2.group()) # returns 254-6767

# matching zero or more with the start / asterisk
import re

quiz = re.compile(r'bat(wo)*man')
mo = quiz.search("The is no batman")
mo2 = quiz.search("Neith batwoman is ")
mo3 = quiz.search("The is triple wo for batwowowoman")
print(mo.group())
print(mo2.group())
print(mo3.group())
    # batman
    # batwoman
    # batwowowoman
    
# matching zero or more with the plus (+)
# Must appear at least once else returns false.
import re

quiz = re.compile(r'bat(wo)+man')
mo = quiz.search("The is no batman")
mo == None # use double equal sign to run and no group during printing. Assign to None acmd check its boolean
mo2 = quiz.search("Neith batwoman is ")
mo3 = quiz.search("The is triple wo for batwowowoman")
print(mo)
print(mo2.group())
print(mo3.group())
    # True  
    # batwoman
    # batwowowoman

# matching repetition with curl brackets
# this enables you to match repeated formats

import re

laughter = re.compile(r'(ha){3}')
laughter2 = re.compile(r'(ha){4,}')
laughter3 = re.compile(r'(ha){2,5}')
laughter4 = re.compile(r'(ha){,3}')

laugh = laughter.search("He laughed hahahahaha before repeating hahaha " )
lugh2 = laughter2.search(" the laught haha before hahahahahahahahahaha")
laugh3 = laughter3.search(" so i laughed hahahahahahahahaha then haha and hahahahaha ")
laugh4 = laughter4.search(" now laughin ha ")

print(laugh.group())
print(lugh2.group())
print(laugh3.group())
print(laugh4.group())


# The GREEDY AND NON-GREEDY ? QUESTION MARK
# The greedy question mark returns the longest match in string
# the non-greedy returns the shortest in a match

import re

non_greedy = re.compile(r'(ha){3,6}?')
greedy = re.compile(r'(ha){3,5}')

gree = greedy.search(" haha in hahahahaha ")
non_gre = non_greedy.search(" not haha and hahahahaha ")

print(gree.group())     # hahahahaha
print(non_gre.group())  # hahaha



# find all Method
# this returns all the match character of a string in fom is alist
# while printing do not attache the group () method , only pass in the finadall method and will print automatically
import re

phone = re.compile(r'\d{3}-\d{3}-\d{4}')  # returnsn a list because there is no groups
pn = phone.findall("The number is 255-504-4900 or help line number is 293-384-4949") # has no groups
print(pn)       # ['255-504-4900', '293-384-4949']

# the find all with groups
new_phone = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # this now has groups and returns tuples where each element is a list 
n_phone = new_phone.findall("new 255-440-4040 to old 455-555-4545 number")
print(n_phone)          # [('255', '440', '4040'), ('455', '555', '4545')]




# character classes combination 
# check read me for all its explantion
# What the expression means is, start with numeric from 0-9, then a space or special character then a word.

import re

xmas_re = re.compile(r'\d+\s\w+')
mas = xmas_re.findall(" mr timz owen, 19 years of age, student developer, loves eating 50 chapos, can code till 12:00 am, and cool ")
print(mas)

# defining your own character classes
# involves using square brackets
# Example matching aeiouAEIOU vowels both in capital and small letters

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
words = vowelRegex.findall("My name is TIMZ OWEN from KABARAK UNIVERSITY Oooooh")
print(words)   # ['a', 'e', 'i', 'I', 'O', 'E', 'o', 'A', 'A', 'A', 'U', 'I', 'E', 'I', 'O', 'o', 'o', 'o', 'o']


# Character combination with integer numbers from 0-9
import re

vowelRegex = re.compile(r'[\dAEIOU]')
words = vowelRegex.findall("My name is TIMZ OWEN and phone is 07403541 6740")
print(words)   # ['a', 'e', 'i', 'I', 'O', 'E', 'o', 'A', 'A', 'A', 'U', 'I', 'E', 'I', 'O', 'o', 'o', 'o', 'o']


# matching characters in a range
import re

# matching specific characters in a range (below matches 0-5 and all alphabetic in capital and small letter
vowelRegex = re.compile(r'[a-zA-Z0-5]')
words = vowelRegex.findall("I am TIMZ OWEN  07403541 6740")
print(words)   # ['a', 'e', 'i', 'I', 'O', 'E', 'o', 'A', 'A', 'A', 'U', 'I', 'E', 'I', 'O', 'o', 'o', 'o', 'o']


# The Caret character '^'
# when planced after the character class matches all character that are not in the the char class
# sometimes called matching the negative character class

import re

regX = re.compile('[^aeiou0-4]')
words = regX.findall("My name is Timz @ Gmail 78903")
print(words)    # ['M', 'y', ' ', 'n', 'm', ' ', 's', ' ', 'T', 'm', 'z', ' ', '@', ' ', 'G', 'm', 'l', ' ', '7', '8', '9']



# Caret and Dollar Sign
# $ --> the words searched must end with the matched pattern
# ^ --> the words must start with a certain pattern
# ^ and $  --> start and end with the matched pattern

import re

nameRex = re.compile(r'^\d+$')
test1 = nameRex.search("my name is 0705xyz90") == None # Returns false because there exists the pattern
test2 = nameRex.search("today is date 04/04/20201 and not 05June") == None # Returns False because there exist
test3 = nameRex.search("No Kenyas here with Id number")  == None
print(test2)
print(test1)
print(test3)


wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('12345678900')
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)

# The wildCard Character
# .dot---> the wildcard
# used to match any character except for the new line
# \ --> used to escape characters that include the dot.
import re

atRegx = re.compile(r'.at')
print((atRegx.findall('the hat and cat lives on the flat houses and mat\.')))


# matching everything with DOT-STAR
# '.'-->  matches anything except for the new lines
# '.*' --> Mathces more than one charcater

import re

nameRegx = re.compile(r'FirstName: (.*) LastName: (.*)')
name1 = nameRegx.search('FirstName: Timz  LastName: Owen')
print(name1.groups())
print(name1.group(1))
print(name1.group(2))



# Dot-Star Non-greedy
import re

nameRegx = re.compile(r'<.*?>') # Pattern matches the shortest 
name1 = nameRegx.search('FirstName: <Timz owen> and LastName: is  Owen> ')
print(name1.group())
nameRegxGreedy = re.compile(r'<.*>')    # Matches the longest patter -GREEDY
name2 = name1 = nameRegxGreedy.search('FirstName: <Timz owen> and LastName: is  Owen> ')
print(name2.group())


# Matching new Lines with the DOT-STAR
# 're.DOTALL' as the second argument ot the re.compile
# This will match pattern to the next lines

import re

multilineRegx = re.compile(r'.*')
output = multilineRegx.search('my name is \nTimz and am from \nKabarak ')
print(output.group())   # my name is

multilineRegx2 = re.compile(r'.*',re.DOTALL)
output2 = multilineRegx2.search('my name is \nTimz and am from \nKabarak ')
print(output2.group()) # print all



# REGEX SYMBOLS:

# •	 The ? matches zero or one of the preceding group.
# •	 The * matches zero or more of the preceding group.
# •	 The + matches one or more of the preceding group.
# •	 The {n} matches exactly n of the preceding group.
# •	 The {n,} matches n or more of the preceding group.
# •	 The {,m} matches 0 to m of the preceding group.
# •	 The {n,m} matches at least n and at most m of the preceding group.
# •	 {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# •	 ^spam means the string must begin with spam.
# •	 spam$ means the string must end with spam.
# •	 The . matches any character, except newline characters.
# •	 \d, \w, and \s match a digit, word, or space character, respectively.
# •	 \D, \W, and \S match anything except a digit, word, or space character, respectively.
# •	 [abc] matches any character between the brackets (such as a, b, or c).
# •	 [^abc] matches any character that isn’t between the brackets.



# Case Insensitive Matching:
# This allows you to pass re.IGNORE or re.I as the second arguement to the re.compile method
import re

caseRegx = re.compile(r'kenya', re.I)
case1 = caseRegx.search('KENYA is my country')
case2 = caseRegx.search('I love Kenya')
case3 = caseRegx.search('Napenda kenya')

print(case1.group())    #KENYA
print(case2.group())    #Kenya
print(case3.group())    #kenya


# use re.IGNORECASE
import re

caseRegx = re.compile(r'kenya', re.IGNORECASE)
case1 = caseRegx.search('KENYA is my country')
case2 = caseRegx.search('I love Kenya')
case3 = caseRegx.search('Napenda kenya')

print(case1.group())    #KENYA
print(case2.group())    #Kenya
print(case3.group())    #kenya


# Substituting Strings with the sub() method

# the sub method takes in two argurments (first--> string to replace any matches, second-->regular expression itself)

import re

namesReg = re.compile(r'Timz \w+')
newRegx = namesReg.sub('owen','Timz was eleccted the new chair and Timz refused')
print(newRegx)  # owen eleccted the new chair and owen


# using replaceable symbols in Regex.

import re

namesReg = re.compile(r'Agent (\w)\w*')
newRegx = namesReg.sub(r'\1****','Agent Timz tole Agent Owen that Agent kim was a double Agent')
print(newRegx)  # T**** tole O**** that k**** was a double Agent
