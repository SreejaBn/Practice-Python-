s1 = int(input('Enter marks in subject 1: '))
s2 = int(input('Enter marks in subject 2: '))
s3 = int(input('Enter marks in subject 3: '))

Average = (s1 + s2 + s3)/ 2
print ('Average Grade: ',Average)

if Average >= 90:
    print ('Grade A')
if 80 <= Average < 90:
    print ('Grade B')
if 70 <= Average < 80:
    print ('Grade C')
if Average < 70: 
    print ('Grade D')