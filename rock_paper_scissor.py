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
 


"""
# Another method for the same

import random as r


l=r.randint(0,2)
#print(l)


p=int(input("""Enter the choice
               0 rock
               1 paper
               2 sessior """))

if p==0:
    print('Your Choice is rock')
elif p==1:
    print('Your Choice is paper')
elif p==2:
    print('Your Choice is sessior')

    
    
if l==0:
    print('Computer Choice is rock')
elif l==1:
    print('Computer Choice is paper')
elif l==2:
    print('Computer Choice is sessior')
    



if p==l:
    print('Game Draw!!!')
elif p==0 and l==2:
    print('You win the game!!!')
elif l==0 and p==2:
    print('You loss the game!!!')
elif l>p:
    print('You loss the game!!!')
elif p>l:
    print('You win the game!!!')


"""
