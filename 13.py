# _-/ Task 1 \-_
# print('''
#     \033[30m\"Don\'t compare yourself with anyone in this world… \033[0m
#     \033[31mif\033[0m you \033[31mdo so\033[0m, you are insulting yourself.\" \033[0m
#     Bill Gates
#       ''')



# _-/ Task 2 \-_
# def display_even_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)

# start_num = int(input("Введіть початкове число: "))
# end_num = int(input("Введіть кінцеве число: "))

# display_even_numbers(start_num, end_num)



# _-/ Task 3 \-_
# def display_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         print(symbol * side_length)
#         for _ in range(side_length - 2):
#             print(symbol + ' ' * (side_length - 2) + symbol)
#         print(symbol * side_length)

# side = int(input("Введіть довжину сторони квадрата: "))
# fill = input("Заповнити квадрат? (True або False): ").lower() == 'true'
# symbol_used = input("Введіть символ для заповнення: ")

# display_square(side, symbol_used, fill)



# _-/ Task 4 \-_
# def find_minimum(a, b, c, d, e):
#     return min(a, b, c, d, e)

# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# num3 = int(input("Введіть третє число: "))
# num4 = int(input("Введіть четверте число: "))
# num5 = int(input("Введіть п'яте число: "))

# minimum = find_minimum(num1, num2, num3, num4, num5)
# print("Мінімальне число:", minimum)



# _-/ Task 5 \-_
# def calculate_product_in_range(start, end):
#     if start > end:
#         start, end = end, start
    
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
#     return product

# lower_limit = int(input("Введіть нижню межу діапазону: "))
# upper_limit = int(input("Введіть верхню межу діапазону: "))

# result = calculate_product_in_range(lower_limit, upper_limit)
# print("Добуток чисел у діапазоні:", result)



# _-/ Task 6 \-_
# def count_digits(number):
#     return len(str(number))

# num = int(input("Введіть число: "))
# digit_count = count_digits(num)
# print("Кількість цифр у числі:", digit_count)



# _-/ Task 7 \-_
def is_palindrome(number):
    number_str = str(number)
    reversed_number_str = number_str[::-1]
    return number_str == reversed_number_str

num = int(input("Введіть число: "))
if is_palindrome(num):
    print("True")
else:
    print("False")