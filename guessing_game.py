import random

print('This is a number guessing game. \nYou have to guess the number that I guessed. \nYou will have a total number of 10 chances to guess the number. \nYou can input the lower and the upper limit. \nThe difference between the lower and the upper limit must be greater than 20.')

while True:
    try:
        low= int(input('Enter the lower limit: '))
        high= int(input('Enter the higher limit: '))
        if high < low:
            print("The upper limit is smaller than the higher limit.")
            continue
        elif high - low < 20:
            print ('The differnce between higher and the lower limit is less than 20. \nEnter again.')
            continue
        break
    except ValueError:
        print('This is a number guessing game. Not word or symbol guessing game!! ヽ(ｏ`皿′ｏ)ﾉ')



number= random.randint(low, high)
print('I have chosen a number.')

t= 5
for i in range(t):
    guess= int(input('Enter your guess: '))
    if guess == number:
        print('Wow!! You guessed the number!! Congratulations!!')
        break
    elif guess - low < 0 or high - guess < 0:
        print ('Are u dumb? Look at your number. (>_<)')
    elif guess < number and number - guess <= 5:
        print ('The number is little low. \nTry again.')
    elif guess < number and number - guess > 5:
        print ('The number is too low.')
    elif guess > number and number - guess >= 5:
        print ('The number is a little high. Try again.')
    elif guess > number and number - guess > 5:
        print ('The number is too high.')  
        
print ("You have exhausted all of your chances and still couldn't find the number. You lost. \nThe Correct number is", number)
