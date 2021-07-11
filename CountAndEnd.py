count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
InputText = ''
sentence = ''

while True:
    InputText = input('Enter string: ').strip().lower()
    if InputText == 'end': 
        break
    else: sentence += InputText

for i in range(len(sentence)):
    if sentence[i] >= 'a' and sentence[i] <= 'z':
        index = ord(sentence[i]) -97
        count[index] += 1

print('''******************************
*     Alphabet Counting      *
******************************''')

for i in range(len(count)):
    if count[i] > 0:
        character = chr(ord('a') + i)
        print(character,count[i])
print('******************************')