InputNum = int(input('Enter the number of rows: '))
InputCha = str(input('Enter print symbol: '))
for i in range(1,InputNum+1):
    print(' '*(i-1) + InputCha*((2*(InputNum-i))+1))

