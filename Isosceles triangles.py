Input = int(input("Enter the number of rows: "))
Input1 = str(input("Enter print symbol: "))
for g in range (Input,0,-1):
     print((g * ' ' + (Input-g) * Input1)+ Input1 +((Input-g) * Input1)+(g * ' ' ))
     
    

    