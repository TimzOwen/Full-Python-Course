
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
