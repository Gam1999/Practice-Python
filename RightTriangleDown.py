Input = int(input("Enter the number of rows: "))
i = 0
for i in range(Input):
    print(' '*((i-1)+1) + "*"*(Input-(i+1)+1))