count = 0
def CountWord(words):
    ans = len(words.split()) 
    return ans


while True:
    end = str(input('Enter text: '))
    if end == 'end':
        break
    count = count + CountWord(end)

AnswerCount = 'Got',count,'words'
print(AnswerCount)