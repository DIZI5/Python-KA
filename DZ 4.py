# --- Завдання 1 ---
# age = int(input("Введіть ваш вік: "))

# if age <= 11:
#     print("Ви дитина")
# elif age <= 18:
#     print("Ви підліток")
# elif age <= 60:
#     print("Ви дорослий")
# elif age >= 61:
#     print("Ви пенсіонер")
# else:
#     print("Invalid input!")


# --- Завдання 2 ---
# number = input("Введіть трьохзначне число: ")

# if len(number) != 3:
#     print("Введене число не є трьохзначним.")
# else:
#     if number[0] == number[1] == number[2]:
#         print(f"З троьохзначного числа {number} однаковими числами є {number[0]}, {number[1]} і {number[2]}")
#     elif number[0] == number[1]:
#         print(f"З троьохзначного числа {number} однаковими числами є {number[0]} і {number[1]}")
#     elif number[1] == number[2]:
#         print(f"З троьохзначного числа {number} однаковими числами є {number[1]} і {number[2]}")
#     elif number[0] == number[2]:
#         print(f"З троьохзначного числа {number} однаковими числами є {number[0]} і {number[2]}")
#     else:
#         print(f"Жодне з чисел {number} не є однаковим.")


# --- Завдання 3 ---
# year = int(input("Введіть рік: "))

# if year % 400 == 0:
#     print(year, "є високосним роком.")
# elif year % 4 == 0 and year % 100 != 0:
#     print(year, "є високосним роком.")
# else:
#     print(year, "не є високосним роком.")


# --- Завдання 4 ---
# number = input("Введіть п'ятизначне число: ")

# if len(number) != 5:
#     print("Введіть правильне п'ятизначне число!")
# else:
#     if number == number[::-1]:
#         print(number, "є паліндромом.")
#     else:
#         print(number, "не є паліндромом.")


# --- Завдання 5 ---
# import math

# circumference = float(input("Введіть довжину кола: "))
# perimeter = float(input("Введіть периметр квадрата: "))

# radius = circumference / (2 * math.pi)

# side_length = perimeter / 4

# if side_length >= 2 * radius:
#     print("Коло може поміститися в квадраті.")
# else:
#     print("Коло не може поміститися в квадраті.")


# --- Завдання 6 ---
# count = 0

# print("*-----------------------------------*")
# print("|1. Перша світова війна почалася у: |")
# print("*-----------------------------------*\n")

# print("*------------------*")
# print("|1. 09 лют. 1812 р.|")
# print("|2. 28 лип. 1914 р.|")
# print("|3. 01 вер. 1939 р.|")
# print("*------------------*\n")

# answer = int(input("Введіть вашу відповідь [1-3]: "))

# if answer == 2:
#     count = +2

# print("Ваша відповідь зарахована")

# print("*----------------------------------------------*")
# print("|2. Комп'ютерна Академія ШАГ була заснована у: |")
# print("*----------------------------------------------*\n")

# print("*------------*")
# print("|1. 2002 році|")
# print("|2. 2001 році|")
# print("|3. 1999 році|")
# print("*------------*\n")

# answer_2 = int(input("Введіть вашу відповідь [1-3]: "))

# if answer_2 == 3:
#     count = +2

# print("Ваша відповідь зарахована")

# print("*--------------------------------------------------------------------------*")
# print("|3. Комп'ютерна Академія ШАГ здобула статус Microsoft Certified Partner у: |")
# print("*--------------------------------------------------------------------------*\n")

# print("*------------*")
# print("|1. 2002 році|")
# print("|2. 2005 році|")
# print("|3. 2003 році|")
# print("*------------*\n")

# answer_3 = int(input("Введіть вашу відповідь [1-3]: "))

# if answer_3 == 1:
#     count = +2

# print("Ваша відповідь зарахована")
# print("Вітаю, ви пройшли тест")

# print(f"Ваша сума балів за 3 запитання {count}")


# --- Завдання 7 ---
# hour = int(input("Введіть години: "))
# minute = int(input("Введіть хвилини: "))
# second = int(input("Введіть секунди: "))

# if hour < 0 or hour > 23:
#     print("Некоректне значення годин!")
# elif minute < 0 or minute > 59:
#     print("Некоректне значення хвилин!")
# elif second < 0 or second > 59:
#     print("Некоректне значення секунд!")
# else:
#     print("Введені дані є коректними.")


# --- Завдання 8 ---
# x = float(input("Введіть координату x: "))
# y = float(input("Введіть координату y: "))

# if x == 0 and y == 0:
#     print("Точка знаходиться в початку координат.")
# elif x == 0:
#     print("Точка лежить на вісі Y.")
# elif y == 0:
#     print("Точка лежить на вісі X.")
# elif x > 0 and y > 0:
#     print("Точка знаходиться в першій чверті.")
# elif x < 0 and y > 0:
#     print("Точка знаходиться в другій чверті.")
# elif x < 0 and y < 0:
#     print("Точка знаходиться в третій чверті.")
# else:
#     print("Точка знаходиться в четвертій чверті.")


# --- Завдання 9 ---
# mounth = int(input("Ввеліть номер місяця [1-12]: "))

# match mounth:
#     case 1:
#         print("Січень")
#     case 2:
#         print("Лютий")
#     case 3:
#         print("Березень")
#     case 4:
#         print("Квітень")
#     case 5:
#         print("Травень")
#     case 6:
#         print("Червень")
#     case 7:
#         print("Липень")
#     case 8:
#         print("Серпень")
#     case 9:
#         print("Вересень")
#     case 10:
#         print("Жовтень")
#     case 11:
#         print("Листопад")
#     case 12:
#         print("Грудень")
#     case _:
#         print("Error!")


# --- Завдання 10 ---
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def get_next_date(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] = 29

    if day < days_in_month[month - 1]:
        day += 1
    elif month < 12:
        day = 1
        month += 1
    else:
        day = 1
        month = 1
        year += 1

    return day, month, year


day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік: "))

next_day, next_month, next_year = get_next_date(day, month, year)

print("Наступна дата:", next_day, ".", next_month, ".", next_year)