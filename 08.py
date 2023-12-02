import random

row = 3
col = 4

matrix = [[random.randrange(1, 10) for i in range(col)] for j in range(row)]

for item in matrix:
    for li in item:
        print(li, "  ", end="")
    print('| ', sum(item))
print("-" * (8 * (col + 1)))
totalSum = 0
for i in range(col):
    sum = 0
    for j in range(row):
        sum += matrix[j][i]
    print(sum, "  ", end="")
    totalSum += sum
print('| ', totalSum)