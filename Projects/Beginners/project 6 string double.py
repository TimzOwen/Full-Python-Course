

# Quiz 5

'''
Given a string, return a string where for every char in the original, there are two charater
Ex:
double_char(The)-->TThhee
double__char(AAbb)--AAAAbbbb

'''

def double__char(stringName):
    final_message = ''
    for characters in stringName:
        final_message += characters * 2
    return final_message
print(double__char('ABC'))


# Quiz number 6
