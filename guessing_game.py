import random
print ("""This is a number guessing game. U have to guess the correct number I have chosen.
       You'll get total of 5 chances to guess the number. 
       If u can guess the number within 5 chances, then congrats but if u couldn't, u lose.""")

chances = 5

while True:
    while True:
        try:  #to check the user input
            low = int(input("Write the lower limit of the range: "))
            high = int(input("Write the higher limit of the range: "))

            if high < low:  #checks if the limit is inputed correctly. it only checks after the user ahs successfully inputed the correct value.
                print ("The higher limit is less than the lower limit. Try again.")
                continue
            elif high - low < 20:
                print ("The difference between the higher and the lower limit is less than 20. Try again.")
                continue
            else:
                break

        except Exception:
            print ("The input isn't a number. Try again.")

    comp = random.randint(low, high)

    for rounds in range(chances):
        while True:
            try: #checks if the user has inputed a logical input
                user  = int(input("Enter your guess: "))
                if user > high or user < low: #checks the range of the input
                    print ("Write your guess within the limit.")
                    continue
                else:
                    break
            except Exception:
                print ("Seriously? Just look what u wrote. Try again.")

        if user == comp:
            print ("Great job! u got it.")
            if rounds == 0:
                print ("Incredible!! U guessed it in very first try!")
                break
            else:
                print ("You guessed the number in", rounds+1, "rounds.")
                break
        elif abs(user - comp)<= 2:
            print ("U r almost there.")
        elif abs (user - comp) <=5:
            print ("U r very close.")
        else:
            print("Nice try.") 

    else:
        print (f'''You have used all of your chances. 
            The correct number was {comp}''')
        
    while True:
        again= input ("Do u want to play again? Types yes if u do and no if u don't. ").lower()
        if again == 'yes':
            break
        elif again == 'no':
            exit()
        else:
            print ("Type yes or no.")
