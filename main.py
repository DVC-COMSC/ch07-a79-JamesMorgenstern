
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])
largest = 0
num = 0

print ('Sum of rows: ', end=' ')
for i in range(rnum):
    rsum = sum(numbers[i])
    if (rsum > largest):
        largest = rsum
    print (rsum, end = ' ')
print()

print ('Sum of columns: ', end = ' ')
for i in range(cnum):
    csum = 0
    for j in range(3):
        csum += (numbers[j][i])
        if (numbers[j][i] > num):
            num = numbers[j][i]
    print (csum, end = ' ')
print()

print ('The row that has the greatest sum: ', end = ' ')
for i in range(rnum):
    if (largest == sum(numbers[i])):
        print(i)

print ('The greatest number: ', end = ' ')
print (num)
# ******************************
# Make your Code
# ******************************
