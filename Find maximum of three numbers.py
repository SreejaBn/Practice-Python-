d = int(input("1st number:\n"))
h = int(input('2nd number:\n'))
k = int(input('3rd number;\n'))
if d > h and d > k:
    print (d, ' is greater.')
elif h > d and h > k:
    print (h, ' is greater.')
elif k > h and k > d:
    print(k, ' is greater.')
else:
    print('All are equal.')