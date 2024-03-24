print ('This program calculates your BMI and tells your weight condition: ')

m = float(input('Enter your height in meters: '))
kg = float(input('Enter your weight in kilograms: '))

BMI = kg/(m**2)
BMI = round(BMI, 2)
if BMI < 18.5:
    print ('Your BMI is', BMI,'. You are in the Underweight category.')

if 18.5 <= BMI < 25:
    print ('Your BMI is', BMI,'. You are in the Normal category.')

if 25 <= BMI < 30:
    print ('Your BMI is', BMI,'. You are in the Overweight category.')
