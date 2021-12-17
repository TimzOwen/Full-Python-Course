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
    
 
 

 ## MADLIBS GAME
    
# Loop back to this point once code finishes
loop = 1
while (loop < 10):
# All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
# Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
# Loop back to "loop = 1"
    loop = loop + 1
