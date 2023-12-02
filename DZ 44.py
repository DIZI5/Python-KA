print("Введіть дату початку підрахування")
day1 = int(input("Введіть день першої дати: "))
month1 = int(input("Введіть місяць першої дати: "))
year1 = int(input("Введіть рік першої дати: "))
print("")

print("Введіть дату кінця підрахування")
day2 = int(input("Введіть день другої дати: "))
month2 = int(input("Введіть місяць другої дати: "))
year2 = int(input("Введіть рік другої дати: "))

if year1 > year2 or (year1 == year2 and month1 > month2) or (year1 == year2 and month1 == month2 and day1 > day2):
    day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap = False
while year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            leap = True
            break
        else:
            break
    else:
        leap = True
        break

days_count = 0
while day1 != day2 or month1 != month2 or year1 != year2:
    days_count += 1
    day1 += 1

    if day1 > days_in_month[month1]:
        if month1 == 2 and leap:
            if day1 > 29:
                day1 = 1
                month1 += 1
        else:
            day1 = 1
            month1 += 1

    if month1 > 12:
        month1 = 1
        year1 += 1

print(f"Між датами {days_count} днів")