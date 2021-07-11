x = int(input("Enter number: "))
p = x
xfac = 1
if x >= 0:
    while x > 1:
        xfac *= x
        x -= 1
    print("%d!"%(p),"=",xfac)
else:
    print("Cannot get %d!"%(p))