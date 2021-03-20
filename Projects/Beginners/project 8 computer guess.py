
#   THE GUESS COMPIUTER GAME
# CREATE A COMPUTER GUESS GAME:

import random

# simple step one
def guess_game(num):
    random_num = random.randint(1,num)
    guess = 0
    while(guess != random_num):
        guess = int(input("Enter a number: "))
        print(guess)
print(guess_game(15))

# more addition to the game
# CREATE A COMPUTER GUESS GAME:

import random

def guess_game(num):
    random_num = random.randint(1,num)
    guess = 0
    while(guess != random_num):
        guess = int(input("Enter a number: "))
        if guess>random_num:
            print("You guessed a too high number...try again")
        elif guess<random_num:
            print("your guess is too low.......try again")
    print(f"you just guesed {random_num} =correctly")
print(guess_game(15))




# computer Guess Game ---> time for computer to guess the number
# CREATE A COMPUTER GUESS GAME:
 
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low   # or even low
        feedback = input(f"Is {guess} too high (H) or too low (L) or correct (C) ??").lower()
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1
    print(f"The Computer gussed it right !!! its {guess}")
computer_guess(100)
