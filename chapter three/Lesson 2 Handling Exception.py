
# EXCEPTIONS:
# This are used to manage errors and avoid system crash by hadling error occurance
# Exit Code of 0-->Success no error and Exit code 1-->Error/program crash
# Try Except is used to catch this errors

id_number = int(input("Enter your id number: "))
print(id_number) # Returns valueError incase a user enters value that's not an integer

try:
    id_number = int(input("Enter id: "))
    salary = 20000
    savings = salary/id_number
    print(id_number)
except ZeroDivisionError:
    print("Id number cannot be Zero")
except ValueError:
    print("Not a valid input, try again ! ")


COMMENTS
"Hash tag used for commenting out code or explanation"
"""----multiple line comment--"""
