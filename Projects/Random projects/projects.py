# 3 Random projects in python

# computer Guess game:
import random as r
num = r.randrange(500)
Guess = 5

while Guess >=0:
    your_guess = int(input("Enter Your Guess number.....\n"))

    def checkGuess(number):
        if your_guess == number:
            print("you win")
        elif your_guess > number:
            print("Too high, go Low...")
        else:
            print("Too Low , Go high....")

    if Guess > 1:
        checkGuess(num)
    elif Guess == 1:
        checkGuess(num)
        print("This is Your Last chance..Play Well \n")
    else:
        print("You lost the Game..... then number was.." + str(num))

    Guess -= 1
    
 
 
    
# 
