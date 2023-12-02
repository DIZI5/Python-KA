# --- Завдання 1 ---
# expression = input("Введіть арифметичний вираз: ")

# parts = expression.split()
# num1 = float(parts[0])
# operator = parts[1]
# num2 = float(parts[2])

# result = None
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Помилка: ділення на нуль!")
# else:
#     print("Помилка: непідтримувана операція")

# if result is not None:
#     print("Результат:", result)



# --- Завдання 2 ---
import random

n = int(input("Введіть кількість чисел у списку: "))
random_list = [random.randint(-100, 100) for _ in range(n)]

min_element = min(random_list)
max_element = max(random_list)

negative_count = sum(1 for num in random_list if num < 0)
positive_count = sum(1 for num in random_list if num > 0)
zero_count = sum(1 for num in random_list if num == 0)

print("Список випадкових чисел:", random_list)
print("Мінімальний елемент:", min_element)
print("Максимальний елемент:", max_element)
print("Кількість від'ємних елементів:", negative_count)
print("Кількість додатніх елементів:", positive_count)
print("Кількість нулів:", zero_count)