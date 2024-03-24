y = int(input('Enter year: '))
if y % 4 == 0:
    if y % 100 != 0:
        print ("It's a leap year.")
    if y % 100 == 0:
        if y % 400 == 0:
            print ("It's a leap year")