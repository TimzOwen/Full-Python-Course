
'''
The MADLIBS QUIZ
Use string concatenation (putting strings together) 
Ex: I ama traveling to ____ using ___ and its carrying ____ passegers for  ____ kilometers
    Thank you for watching ________ channel please ________
'''
youtube_channel = ""
print("thank you for watching " +  youtube_channel + "Channel ")
print(f"thank you for watching {youtube_channel}")
print("Thank you for watching {}".format(youtube_channel))


#soln 2:---->Get user input
name = input("Name: ")
coding = input("coding: ")
verb = input("Verb: ")
madlib = "my name is {name} and I love {coding} because it is {verb}".format(name,coding,verb)
print(madlib)


#soln 2:---->Get user input
# f formating
name = input("Name: ")
coding = input("coding: ")
verb = input("Verb: ")
madlib = "my name is {} and I love {} because it is {}".format(name,coding,verb)
print(madlib)


#soln f string
#soln 2:---->Get user input
name = input("Name: ")
coding = input("coding: ")
verb = input("Verb: ")
madlib = f"my name is {name} and I love {coding} because it is {verb}"
print(madlib)

