# --- Завдання 1 ---
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# num = start

# while num <= end:
#     if num % 7 == 0:
#         print(num)
#     num += 1


# --- Завдання 2 ---
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# # Всі числа діапазону
# print("Всі числа діапазону:")
# num = start
# while num <= end:
#     print(num, end=" ")
#     num += 1
# print()

# # Всі числа діапазону в спадному порядку
# print("Всі числа діапазону в спадному порядку:")
# num = end
# while num >= start:
#     print(num, end=" ")
#     num -= 1
# print()

# # Всі числа, кратні 7
# print("Числа, кратні 7:")
# num = start
# while num <= end:
#     if num % 7 == 0:
#         print(num, end=" ")
#     num += 1
# print()

# # Кількість чисел, кратних 5
# count = 0
# num = start
# while num <= end:
#     if num % 5 == 0:
#         count += 1
#     num += 1
# print("Кількість чисел, кратних 5:", count)


# --- Завдання 3 ---
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