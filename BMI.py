Gender = input("Enter Gender (M/W): ")
if Gender != 'W' and Gender != 'M':
    print(Gender,"is not M or W")
    exit()
YearCurrent = int(input("Enter current year: "))
Birthday = int(input("Enter your birth year: "))
Weight = float(input("Enter your weight (kg): "))
Height = float(input("Enter your height (cm): "))
age = int(YearCurrent-Birthday)
BMI = float((Weight / (Height * Height)) * 10000)

if Gender == 'M':
    BMR = float(66.5 + (13.75*Weight) + (5.003*Height) - (6.755*age))
elif Gender == 'W':
    BMR = float(655.1 + (9.563 * Weight) + (1.850 * Height) - (4.676 * age))
    

print("- - - - - -")
print("Your age =",age)
print("Your BMI = %.3f"%BMI)
print("Your BMR = %.3f"%BMR)