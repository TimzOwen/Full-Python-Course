
# level 2 projects
# ROCK PAPER SCISSORS

# CREATE A ROCK PAPER AND SCISSORS
import random

def play_game():
    user = input("choose:  'r' for rock 'p' for Paper 's' for scissor \n")
    comp_turn = random.choice(['r','p','s'])
    
    if user == comp_turn:
        return ' it\'s a tie '
    # r>s s>p p>r
    if is_win(user, comp_turn):
        return 'You won !!! '
    return 'You lost '
def is_win(player,opponent):
    # return true if player wins 
    # r>s s>p p>r
    if (player == 'r' and opponent == 's') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True                                                                        
print(play_game())
