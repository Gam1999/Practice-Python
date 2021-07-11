InputNumber = int(input("Enter number: "))
binary = []
decimal = InputNumber
 
while decimal > 0:
    binary.append(str(decimal % 2))
    decimal = int(decimal / 2)
 
binary.reverse()

print(f"{InputNumber} is {''.join(binary)} in base 2.")

