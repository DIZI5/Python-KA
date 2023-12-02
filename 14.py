#Task 1
def greet_user():
    name = input("Введіть ваше ім'я: ")
    age_valid = False

    while not age_valid:
        try:
            age = int(input("Введіть ваш вік: "))
            if age < 0 or age > 130:
                raise ValueError("Вік повинен бути в межах від 0 до 130")
            age_valid = True
        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, спробуйте ще раз.")

    print(f"Привіт, {name}! Твій вік —> {age}")

greet_user()




#Task 2#1
def greet_formatted(name, age):
    if age < 0 or age > 130:
        return None
    return f"Привіт, {name}! Твій вік — {age}"

def main():
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))

    greeting = greet_formatted(name, age)

    if greeting is None:
        print("Помилка: некоректний вік.")
    else:
        print(greeting)

main()




#Task 2#2
def greet_formatted(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Вік повинен бути в межах від 0 до 130")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as e:
        return f"Помилка: {e}"

def main():
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))

    greeting = greet_formatted(name, age)
    print(greeting)

main()




#Task 3
def main():
    numbers = []
    
    while True:
        try:
            num = float(input("Введіть додатнє число (або 0 для завершення): "))
            if num == 0:
                break
            elif num < 0:
                raise ValueError("Введено від'ємне число")
            numbers.append(num)
        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, спробуйте ще раз.")
    
    if numbers:
        total_sum = sum(numbers)
        print(f"Сума введених чисел: {total_sum}")
    else:
        print("Список чисел порожній.")

try:
    main()
except KeyboardInterrupt:
    print("\nПрограма була припинена користувачем.")
except Exception as e:
    print(f"Невідома помилка: {e}")




#Task 4
def format_greeting_v1(name, age):
    formatted_greeting = f"Привіт, {name}! Твій вік — {age}"
    return formatted_greeting

def main_v1():
    try:
        name = input("Введіть ваше ім'я: ")
        age = int(input("Введіть ваш вік: "))
        if age < 0 or age > 130:
            raise ValueError("Вік повинен бути в межах від 0 до 130")
        
        greeting = format_greeting_v1(name, age)
        print(greeting)
    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, спробуйте ще раз.")

main_v1()



def format_greeting_v2(name, age):
    if age < 0 or age > 130:
        raise ValueError("Вік повинен бути в межах від 0 до 130")
    
    formatted_greeting = f"Привіт, {name}! Твій вік — {age}"
    return formatted_greeting

def main_v2():
    try:
        name = input("Введіть ваше ім'я: ")
        age = int(input("Введіть ваш вік: "))
        
        greeting = format_greeting_v2(name, age)
        print(greeting)
    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, спробуйте ще раз.")

main_v2()