def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo (n-1) + fibo (n-2)
n = int(input('Enter the size of the series: '))
if n <= 0:
    print('Enter a positive number')
else:
    print('Fibonacci Series:')
    for i in range (n):
        print (fibo(i))