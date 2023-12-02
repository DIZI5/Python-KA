# # --- ДЗ 1 ---
# # --- Завдання 1 ---
# print("1.Додавання")
# print("2.Віднімання")
# print("3.Множення")
# print("4.Ділення")
# print("")
# action = input("Виберіть число від 1-4: ")

# if action == 1:
#     a = input("Введіть перше число: ")
#     b = input("Введіть перше число: ")
#     print(a, "+", b, "=", int(a) + int(b))

# if action == 2:
#     a = input("Введіть перше число: ")
#     b = input("Введіть перше число: ")
#     print(a, "-", b, "=", int(a) - int(b))

# if action == 3:
#     a = input("Введіть перше число: ")
#     b = input("Введіть перше число: ")
#     print(a, "*", b, "=", int(a) * int(b))

# if action == 4:
#     a = input("Введіть перше число: ")
#     b = input("Введіть перше число: ")
#     print(a, "/", b, "=", int(a) / int(b))


# # --- Завдання 2 ---
# a = int(input("Число: "))
# b = int(input("Відсотки: "))
# print(a * (b * 0.01))


# # --- Завдання 3 ---
# print("area", int(input("Довжина")) * int(input("Висота")), sep=" = ")


# # --- ДЗ 2 ---
# # --- Завдання 1 ---
# grn = int(input("Введіть кількість гривень: "))
# kop = int(input("Введіть кількість копійок: "))

# if kop >= 100:
#     grn += kop // 100
#     kop %= 100

# print(f"Правильна грошова сума: {grn} грн {kop} коп")


# # --- Завдання 2 ---
# mashtab = float(input("Масштаб карти (кількість кілометрів в одному сантиметрі) -> "))
# distance_cm = float(input("Відстань між точками, які зображують населені пункти (см) -> "))

# # Обчислення відстані в кілометрах
# distance_km = distance_cm / 100 * mashtab

# # Виведення результату
# print("Відстань між населеними пунктами:", distance_km, "км.")


# # --- Завдання 3 ---
# seconds = int(input("Введіть кількість секунд: "))

# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# remaining_seconds = (seconds % 3600) % 60

# print("Години:", hours)
# print("Хвилини:", minutes)
# print("Секунди:", remaining_seconds)


# --- Завдання 4 ---
# def format_money(amount):
#     grn = int(amount)  # ціла частина
#     kop = int((amount % 1) * 100)  # дробова частина в копійках

#     formatted_money = f"{grn} грн {kop:02d} коп."  # форматування рядка з грошовим форматом
#     return formatted_money

# number = float(input("Введіть дробове число: "))

# result = format_money(number)
# print("Результат:", result)


# --- Завдання 5 ---
# days = int(input("Введіть кількість днів: "))

# weeks = days // 7  # Визначаємо кількість повних тижнів
# remaining_days = days % 7  # Визначаємо кількість залишкових днів

# print(f"{weeks} тижнів і {remaining_days} днів")


# --- Завдання 6 ---
# print(chr(9556) + (chr(9552) * 50) + chr(9559))

# print(" " * 52)

# print(chr(9553), (" " * 19), "Pory roku", (" " * 18), chr(9553))

# print(" " * 52)

# print(chr(9568) + (chr(9552) * 12) + chr(9574) + (chr(9552) * 12) + chr(9574) + (chr(9552) * 11) + chr(9574) + (chr(9552) * 12) + chr(9571))

# print(" " * 52)

# print(chr(9553), (" " * 3), "Zyma", (" " * 2), end="")
# print(chr(9553), (" " * 2), "Vesna", (" " * 2), end="")
# print(chr(9553), (" " * 2), "Lito", (" " * 2), end="")
# print(chr(9553), (" " * 2), "Osin", (" " * 2), chr(9553))

# print(" " * 52)

# print(chr(9562) + (chr(9552) * 12) + chr(9577) + (chr(9552) * 12) + chr(9577) + (chr(9552) * 11) + chr(9577) + (chr(9552) * 12) + chr(9565))


# --- Завдання 7 ---
# print("Магазин техніки")
# cost = float(input("Введіть вартість одного ноутбука: "))
# amount = int(input("Введіть кількість ноутбуків: "))
# discount = float(input("Введіть знижку у відсотках: "))
# print("")

# all_cost = cost * amount

# a = all_cost - all_cost / 100 * discount

# print("Ваше замовлення:")
# print(f"{amount} ноутбуків на суму {all_cost} грн.")
# print(f"Ціна до сплати з врахуванням знижки становить: {a} грн.")


# --- Завдання 8 ---
# total_sales = float(input("Введіть загальну суму угод менеджера за місяць: "))

# salary = 100 + 0.05 * total_sales

# print("Підсумкова зарплата менеджера: $", salary)

# --- Завдання 9 ---
# file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))
# internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах на секунду: "))

# file_size_bits = file_size_gb * 8 * 1024 * 1024 * 1024
# download_time_seconds = file_size_bits / internet_speed_bps

# hours = int(download_time_seconds // 3600)
# minutes = int((download_time_seconds % 3600) // 60)
# seconds = int(download_time_seconds % 60)

# print("Час завантаження файла:", hours, "годин,", minutes, "хвилин,", seconds, "секунд")


# --- Завдання 10 ---
# start_h = int(input("Enter start h: "))
# start_m = int(input("Enter start m: "))
# start_s = int(input("Enter start s: "))
# print("")

# end_h = int(input("Enter end h: "))
# end_m = int(input("Enter end m: "))
# end_s = int(input("Enter end s: "))

# start_time = start_h * 3600 + start_m * 60 + start_s
# end_time = end_h * 3600 + end_m * 60 + end_s

# result = end_time - start_time
# print("result -->", result //60 * 2, "UAH")


# --- Завдання 11 ---
# distance = int(input("Enter distance :: "))

# A95_value = float(input("Enter A95 ::"))
# A92_value = float(input("Enter A92 ::"))
# A98_value = float(input("Enter A98 ::"))

# A95 = float(input("Enter A95 price :: "))
# A92 = float(input("Enter A92 price :: "))
# A98 = float(input("Enter A98 price :: "))

# resA95 = (A95_value/ 100) * distance * A95
# resA92 = (A92_value/ 100) * distance * A92
# resA98 = (A98_value/ 100) * distance * A98

# print("A95 ---> " , resA95)
# print("A92 ---> " , resA92)
# print("A98 ---> " , resA98)