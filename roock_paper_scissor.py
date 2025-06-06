import random

l = ['rock', 'paper', 'scissor']

print ('This a rock paper scissor game.')
print ("\nto clear any doubts, as a computer, i don't have a mind of my own and i can't cheat. so even if u type your answer first, i won't change my choice. so, rest assured.")


while True:

    user = input ('What is your choice? \n').lower()
    choice = random.choice(l)
    print (f'My choice is {choice}') 
    if choice == user:
        print ('its a draw. -_-')
    elif (choice == 'rock' and user == 'paper') or (choice == 'paper' and user == 'scissor') or (choice == 'scissor' and user == 'rock'):
        print ('Wow! u got that one.')
    else:
        print ('I won!!! >-<')

    f= input ("Do u want to play again? Type y for yes and n for no.").lower()

    if f != 'y':
        break