print('\nthis program will check whether the number is palindrome or not.\n')
print('btw palindrome is number which when reversed gives the same number\n')
print('Eg: 12321\n')
m = int(input('Write your number here: '))
n = int(str(m) [::-2])  #[::-1] is used to reverse the number 
if n == m:
    print ('This number is palindrome.')
else:
    print ('This number is not palindrome.')
#print(n)