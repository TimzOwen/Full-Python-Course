

# LESSON 1
# FUNCTIONS
# Function is a container that holds pieces of code defined to do a specific task and are reusable
# Always use meaningful variable function names 

def greating():
    print("Welcome user")
    print("Let's get started now")
    
print("Hey this is printed First")
greating() # calliing the Function 
print("Then this after the Function been executed")

# Function parameters(Placeholders for receiving information)

def greating_message(name):
    print(f"Hello {name} !")
    print("Welcome to Python Programming")
greating_message("John")
greating_message("Owen") #takes the parameter you passed in the function

# Multiple parameters
def morning_greeting(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome for breakfast")
    
morning_greeting("Timz", "Owen")



# Keyword Arguments
# used especially where order matters and clarification is very important
def calc_price(total_amount,shipping_cost,discount):
    print("Thank you for shopping with us! Receipt below")
    print(f"Amount ksh: {total_amount} and shipping fee: {shipping_cost} , Discount rate: {discount}%")
calc_price(total_amount=20000, shipping_cost=450, discount=0.05) # keyword arguements


# RETURN STATEMENTS
# Calc square of numbers:
def square_number(number):
     print(number * number)
print(square_number(4)) # returns value and "NONE" by default

# return
def create_account(password, number):
    combined_password = (password * number)
    return combined_password
print(create_account(30,50))




# LESSON 2
# CREATING REUSABLE FUNCTIONS
 
def reusable_emoji(message):
    alert_split = message.split()
    dict_emoji = {
        ":":"✅",
        ">":"🚚",
        "<":"👮"
    }
    output_message = " "
    for warning in alert_split:
        output_message += dict_emoji.get(warning, warning) + " "
    return output_message

message = input("> ")
print(reusable_emoji(message))
