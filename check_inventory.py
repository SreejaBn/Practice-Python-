def check_inventory():
    if book in inventory:
        print ('Available')
    else:
        print ('Not Available')

inventory = ['maths', 'harry potter', 'ruskin bond', 'dictionary']

book = str(input('What is the name of book you are searching for: '))

print (check_inventory())