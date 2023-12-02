import math

# Функція для знаходження НСД (найменшого спільного дільника)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Створення словника для простого дробу
def create_fraction(numerator, denominator):
    # Знаходимо НСД чисельника і знаменника
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    fraction = {"numerator": numerator, "denominator": denominator}
    return fraction


# Функція для скорочення дробу
def simplify_fraction(fraction):
    numerator = fraction["numerator"]
    denominator = fraction["denominator"]
    common_divisor = gcd(numerator, denominator)
    fraction["numerator"] //= common_divisor
    fraction["denominator"] //= common_divisor
    return fraction


# Функція для перетворення неправильного дробу на змішаний
def improper_to_mixed(fraction):
    numerator = fraction["numerator"]
    denominator = fraction["denominator"]
    whole_part = numerator // denominator
    numerator = numerator % denominator
    mixed_fraction = {
        "whole_part": whole_part,
        "numerator": numerator,
        "denominator": denominator,
    }
    return mixed_fraction


# Функція для обчислення суми дробів
def add_fractions(fraction1, fraction2):
    numerator1 = fraction1["numerator"]
    denominator1 = fraction1["denominator"]
    numerator2 = fraction2["numerator"]
    denominator2 = fraction2["denominator"]

    # Знаменник для суми дробів
    common_denominator = denominator1 * denominator2

    # Обчислення чисельника для суми дробів
    new_numerator = (
        numerator1 * denominator2 + numerator2 * denominator1
    )

    # Створення та скорочення результату
    result_fraction = create_fraction(new_numerator, common_denominator)
    result_fraction = simplify_fraction(result_fraction)

    return result_fraction


# Функція для обчислення різниці дробів
def subtract_fractions(fraction1, fraction2):
    numerator1 = fraction1["numerator"]
    denominator1 = fraction1["denominator"]
    numerator2 = fraction2["numerator"]
    denominator2 = fraction2["denominator"]

    # Знаменник для різниці дробів
    common_denominator = denominator1 * denominator2

    # Обчислення чисельника для різниці дробів
    new_numerator = (
        numerator1 * denominator2 - numerator2 * denominator1
    )

    # Створення та скорочення результату
    result_fraction = create_fraction(new_numerator, common_denominator)
    result_fraction = simplify_fraction(result_fraction)

    return result_fraction


# Функція для обчислення добутку дробів
def multiply_fractions(fraction1, fraction2):
    numerator1 = fraction1["numerator"]
    denominator1 = fraction1["denominator"]
    numerator2 = fraction2["numerator"]
    denominator2 = fraction2["denominator"]

    # Обчислення чисельника та знаменника для добутку дробів
    new_numerator = numerator1 * numerator2
    new_denominator = denominator1 * denominator2

    # Створення та скорочення результату
    result_fraction = create_fraction(new_numerator, new_denominator)
    result_fraction = simplify_fraction(result_fraction)

    return result_fraction


# Функція для обчислення частки дробів
def divide_fractions(fraction1, fraction2):
    numerator1 = fraction1["numerator"]
    denominator1 = fraction1["denominator"]
    numerator2 = fraction2["numerator"]
    denominator2 = fraction2["denominator"]

    # Обчислення чисельника та знаменника для частки дробів
    new_numerator = numerator1 * denominator2
    new_denominator = denominator1 * numerator2

    # Створення та скорочення результату
    result_fraction = create_fraction(new_numerator, new_denominator)
    result_fraction = simplify_fraction(result_fraction)

    return result_fraction

# Приклад використання
fraction1 = create_fraction(3, 4)
fraction2 = create_fraction(1, 2)

sum_result = add_fractions(fraction1, fraction2)
difference_result = subtract_fractions(fraction1, fraction2)
product_result = multiply_fractions(fraction1, fraction2)
division_result = divide_fractions(fraction1, fraction2)


print("Сума:", sum_result)
print("Різниця:", difference_result)
print("Добуток:", product_result)
print("Частка:", division_result)