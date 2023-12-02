# --- Завдання 1 ---
# reg = input("Example [21+2]: ")
# if reg.find('+') != -1:
#     numbers = reg.split('+')
#     numbers = [int(number) for number in numbers]
#     print(f"Result: {numbers[0]+numbers[1]}")

# --- Завдання 2 ---
import random

minus = 0
plus = 0
zero = 0

numbers = [random.randint(-50,50) for i in range(10)]
min = min(numbers)
max = max(numbers)

print(numbers)

for number in numbers:
    if number > 0:
        plus += 1
    elif number < 0:
        minus += 1
    elif number == 0:
        zero += 1
print("Max --> ", max)
print("Min --> ", min)
print("Plus --> ", plus)
print("Minus --> ", minus)
print("Zero --> ", zero)