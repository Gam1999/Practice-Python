InputNum = int(input('Enter the number of rows: '))
InputCha = str(input('Enter print symbol: '))

i = 0
for i in range(InputNum):
    print(' '*(InputNum-(i+1)) + InputCha*(i+1) + InputCha*(i+0))