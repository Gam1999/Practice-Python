num = []
i = 0
while i >= 0:
    LoopNum = int(input("Enter number: "))
    if LoopNum < 0:
        break
    num.append(LoopNum)
print("Minimum number is",min(num))    
print("Maximum number is",max(num))
