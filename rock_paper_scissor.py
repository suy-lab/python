from operator import truediv
import random

def play():
    user = input ("what's your choice   'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r','p','s'])
    

    if user == computer:
        return 'tie'

    # r>s, s>p, p>r 

    if is_win(user,computer):
        return 'you won!!!'

    return 'you lost!!!'    

def is_win(player,opponent):
        # return true if player wins
        # r>s, s>p, p>r
        if(player=='r' and opponent=='s') or (player=='s'and opponent=='p')\
            or (player =='p'and opponent=='r'):
            return True    


y='y'

while(y=='y'):
    y='n'
    print(play())
    y=input("do you want to do more (y/n)")