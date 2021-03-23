
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

