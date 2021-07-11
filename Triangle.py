import math
print("*" *30)
print("*" *8 + "About Triangle" + "*" *8)
print("*" *30)
ASide = int(input("Enter a-side long (cm): "))
BSide = int(input("Enter b-side long (cm): "))
CSide = math.sqrt((ASide*ASide) + (BSide*BSide))
AAngle = math.acos(BSide/CSide)
A = math.degrees(AAngle)
B = 180-A-90
print("A angle is {:.4f}".format(A))
print("B angle is {:.4f}".format(B))
print("c-side is {:.4f}".format(CSide),"cm")
print("*" *30)