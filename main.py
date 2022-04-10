import random
from re import X
from telnetlib import DO

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f" guess a number between 1 and {x} :"))
        if guess< random_number:
            print("sorry, guess again. Too low")
        elif guess> random_number:
            print("sorry, guess again. Too high ")
    print(f"yay, congrats. you have guessed the number {random_number} correctily!!! ")            
    print(guess)

def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback !='c':
        if  low != high:
            guess = random.randint(low, high)
        else:
            guess =low   
        feedback=input(f" Is {guess} too high (h), too lower (l), or correct (c)???")
        if feedback == 'h':
            high =guess-1
        elif feedback =='l':
            low = guess+1


x=int(input("enter the upper limit "))
computer_guess(x)
   
print(f"Yay! the computer guessed your number, {guess}, correctily !!!")



    



