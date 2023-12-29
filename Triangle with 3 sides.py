##When we only know the sides of a triangle
#First we take the value of the sides of the triangle
a = float(input('Enter 1st side: ')) #I took float in case the user may provide with with a decimal value
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))

#Now we need to put the formula
p = (a+b+c)*0.5
r = (p*(p-a)*(p-b)*(p-c))*0.5

#Now simply put print the value
print('Area= ', r)