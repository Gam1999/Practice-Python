uniques = []
numbers = []

status = False
for i in range(20):
    text = 'Enter number #' + str(i+1) + ': '
    InputNum = int(input(text))
    numbers.append(InputNum)
numbers.sort()
uniques.append(numbers[0])
for n in numbers:
    status = False
    for i in range(len(uniques)):
        if uniques[i] == n:
            status = True
            break
    if status == False:
        uniques.append(n)
print('Unique numbers is',*uniques)
count = 0
sum = 0
j = 0
while j <= len(uniques):
    sum += uniques[j]
    j += 2
    count += 1
average = float(sum)/count
print('Average number of even position in list is','{:.2f}'.format(average))