# --- Завдання 1 ---
# number = int(input("Введіть число: "))
# if number >= 90 and number <= 131:
#     print("Число входить до діапазону [131 - 90]")
# else:
#     print("Число не входить до діапазону [131 - 90]")


# --- Завдання 2 ---
# dollars = float(input("Введіть курс долару: "))
# euros = float(input("Введіть курс євро: "))
# funts = float(input("Введіть курс фунтів: "))
# print("")

# print("1.Виберіть варіант конвертації:")
# print("1.Долари у гривні")
# print("2.Євро у гривні")
# print("3.Фунти у гривні\n")

# action = int(input("Виберіть варіант від 1-3: "))

# if action == 1:
#     print("1.Долари у гривні")
#     print("2.Гривні у долари\n")
#     action_1 = int(input("Виберіть варіант від 1-2: "))

#     if action_1 == 1:

#         amount_usd = float(input("Введіть кількість доларів: "))
#         a = dollars * amount_usd
#         print(f"{amount_usd} доларів у {a} гривнях")

#     if action_1 == 2:

#         amount_uah = float(input("Введіть кількість гривень: "))
#         a = amount_uah / dollars
#         print(f"{amount_uah} гривень у {a} доларах")


# if action == 2:
#     print("1.Євро у гривні")
#     print("2.Гривні у євро\n")
#     action_2 = int(input("Виберіть варіант від 1-2: "))

#     if action_2 == 1:

#         amount_eur = float(input("Введіть кількість євро: "))
#         a = euros * amount_eur
#         print(f"{amount_eur} євро у {a} гривнях")

#     if action_2 == 2:
        
#         amount_uah = float(input("Введіть кількість гривень: "))
#         a = amount_uah / euros
#         print(f"{amount_uah} гривень у {a} євро")


# if action == 3:
#     print("1.Фунти у гривні")
#     print("2.Гривні у фунти\n")
#     action_3 = int(input("Виберіть варіант від 1-2: "))

#     if action_3 == 1:

#         amount_gbp = float(input("Введіть кількість фунтів: "))
#         a = funts * amount_gbp
#         print(f"{amount_gbp} фунтів у {a} гривнях")

#     if action_3 == 2:
        
#         amount_uah = float(input("Введіть кількість гривень: "))
#         a = amount_uah / funts
#         print(f"{amount_uah} гривень у {a} фунтах")


# --- Завдання 3 ---
# number = int(input("Введіть число: "))
# if number >= 90 and number <= 131:
#     print("Число входить до діапазону [131 - 90]")
# else:
#     print("Число не входить до діапазону [131 - 90]")

# if number % 7 and number % 3:
#     print("Число кратне 7 і 3")
# else:
#     print("Число не кратне 7 і 3")


# --- Завдання 4 ---
# cost = float(input("Введіть суму покупки: "))
# if cost >= 100 and cost <= 199:
#     a = cost * 0.03
#     b = cost - a
#     print(f"{b} грн.")

# elif cost >= 200:
#     a = cost * 0.05
#     b = cost - a
#     print(f"{b} грн.")
# else:
#     print("Error")