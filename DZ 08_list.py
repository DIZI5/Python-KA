# _-/ Task 1 \-_
# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     else:
#         return reverse_string(s[1:]) + s[0]

# input_string = input("Введіть рядок: ")
# reversed_string = reverse_string(input_string)
# print("Результат повороту рядка:", reversed_string)



# _-/ Task 2 \-_
# def count_letters_digits(s):
#     letters = 0
#     digits = 0

#     for char in s:
#         if char.isalpha():
#             letters += 1
#         elif char.isdigit():
#             digits += 1

#     return letters, digits

# input_string = input("Введіть рядок: ")
# letter_count, digit_count = count_letters_digits(input_string)

# print("Кількість букв:", letter_count)
# print("Кількість цифр:", digit_count)



# _-/ Task 3 \-_
# def count_occurrences(s, target):
#     count = 0

#     for char in s:
#         if char == target:
#             count += 1

#     return count

# input_string = input("Введіть рядок: ")
# target_char = input("Введіть символ для пошуку: ")

# occurrences = count_occurrences(input_string, target_char)
# print("Кількість входжень:", occurrences)



# _-/ Task 4 \-_
# def count_word_occurrences(s, target_word):
#     words = s.split()
#     count = 0

#     for word in words:
#         if word == target_word:
#             count += 1

#     return count

# input_string = input("Введіть рядок: ")
# target_word = input("Введіть слово для пошуку: ")

# occurrences = count_word_occurrences(input_string, target_word)
# print("Кількість входжень слова:", occurrences)



# _-/ Task 5 \-_
# def replace_word(s, target_word, replacement_word):
#     words = s.split()
#     replaced_words = []

#     for word in words:
#         if word == target_word:
#             replaced_words.append(replacement_word)
#         else:
#             replaced_words.append(word)

#     replaced_string = " ".join(replaced_words)
#     return replaced_string

# input_string = input("Введіть рядок: ")
# target_word = input("Введіть слово для пошуку: ")
# replacement_word = input("Введіть слово для заміни: ")

# replaced_string = replace_word(input_string, target_word, replacement_word)
# print("Результат заміни:", replaced_string)