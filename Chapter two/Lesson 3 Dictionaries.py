# LESSON 4
# DICTIONARIES
# Used when we want to store data with Key-value pair

students = {
    "name":"John doe",
    "Age":20,
    "is_student":True
}
print(students)
print(students["name"])
# print(students["Name"]) # Key error
print(students.get("Age"))
print(students.get("age","0 Ages : a default ")) # asign default value
students["name"] = "Timz" # updating values to a dictionary
print(students["name"])
students["graduation year"] = 2020   # adding new key-value pair 
print(students)


# challenge
# output is user inputs a number and translates the number to words

phone = input("Phone: ") # get user inpput and store in phone
numbers_dict = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
} # define your dictionary with key-value pair
new_phone = " "
for num in phone:
    new_phone += numbers_dict.get(num," * ") + " "
print(new_phone)


# Challenge two
# Emoji converter:
message = input("> ") # step one: Get user message 
word_split = message.split() # step two: split for iteration 
emoji_converter = {
    "):":"😊",
    ":(":"😢",
    ">":"🚨"
}# moji_converter
output_message = " "
for words in word_split:
    output_message += emoji_converter.get(words,words) + " "
print(output_message)
    
# challenge 3
# create a emoji sensor alerts developers on systems hacks
alert_message = input("How serious is it? >: ")
split_alert = alert_message.split()
alert_dict = {
    "!":"🔴",
    "<:": "⛔",
    ":":"⚡"  
}
final_alert = ""
for alert in split_alert:
    final_alert += alert_dict.get(alert, alert) + " "
print(final_alert)

