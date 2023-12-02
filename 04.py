start = 10
end = 20

if start > end:
    start, end = end, start

i = start
print("Print all:", end="")
i = end
while i <= end:
    print(i, end="\t")
    i += 1

print()
print("Print reverse: ", end="")
i = end
while i >= start:
    print(i, end="\t")
    i -= 1

print("\nPrint % 7: ", end="")
i = start
while i <= end:
    if i % 7 == 0:
        print(i, end="\t")
    i += 1

counter = 0
i = start
while i <= end:
    if i % 5 == 0:
        counter += 1
    i += 1
else:
    print("\nNumber of % 5: ", counter)



start = 1
end = 20
if start > end:
    start, end = end, start

i = 1

while start <= end:
    if start % 3 == 0 and start % 5 == 0:
        print("#{} - Fizz Buzz".format(i))
    elif start % 5 == 0:
        print("#{} - Buzz".format(i))
    elif start % 3 == 0:
        print("#{} - Fizz".format(i))
    else:
        print("#{} - {}".format(i, start))

    start += 1
    i += 1