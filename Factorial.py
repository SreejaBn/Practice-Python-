num = int(input('Enter the number here: '))

k = 1

if num == 0:
    print('The factorial of 0 is 1.')
    
elif num < 0:
    print ("Factorial of negetive numbers doesn't exist.")

else:
    for i in range (1, num+1):
        k= k *i

print(k)
