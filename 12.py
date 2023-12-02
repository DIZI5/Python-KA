#Task 2
def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

result = sum_range(a, b)
print(f"Сума всіх чисел у діапазоні від {a} до {b} дорівнює {result}")




#Task 3
def print_stars(n):
    if n > 0:
        print("*", end="")
        print_stars(n - 1)

N = int(input("Введіть кількість зірок (N): "))

print_stars(N)




#Task 6
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def date_difference(year1, month1, day1, year2, month2, day2):
    total_days = 0

    while year1 != year2 or month1 != month2 or day1 != day2:
        total_days += 1
        day1 += 1

        if day1 > days_in_month(year1, month1):
            day1 = 1
            month1 += 1

            if month1 > 12:
                month1 = 1
                year1 += 1

    return total_days

year1 = int(input("Введіть рік першої дати: "))
month1 = int(input("Введіть місяць першої дати: "))
day1 = int(input("Введіть день першої дати: "))

year2 = int(input("Введіть рік другої дати: "))
month2 = int(input("Введіть місяць другої дати: "))
day2 = int(input("Введіть день другої дати: "))

difference = date_difference(year1, month1, day1, year2, month2, day2)
print(f"Різниця між датами: {difference} днів")