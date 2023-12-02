# --- /[Task 1]\ ---
# line = ''
# with open(r'Python KA 05.06.2023/practs in lesson/16/output.txt', 'r', encoding='utf-8') as file:
#     line = file.read()

# line = line.split()

# with open(r'Python KA 05.06.2023/practs in lesson/16/input.txt', 'w', encoding='utf-8') as file:
#     for item in line:
#         if len(item) >= 7:
#             file.write(item + ' ')

# print("Successfully completed")



# --- /[Task 2]\ ---
# def readFile(fname):
#     with open(fname, 'r', encoding='utf-8') as file:
#         return file.read()

# def appFile(fname,info):
#     with open(fname, 'w', encoding='utf-8') as file:
#         file.write(info)

# url_read = r'Python KA 05.06.2023/practs in lesson/16/output.txt'
# url_write = r'Python KA 05.06.2023/practs in lesson/16/input.txt'

# text = readFile(url_read)
# appFile(url_write, text)

# print("Successfully completed")



# --- /[Task 3]\ ---
# output = r'Python KA 05.06.2023/practs in lesson/16/input.txt'
# input = r'Python KA 05.06.2023/practs in lesson/16/output.txt'

# with open(input, 'r', encoding='utf-8') as input_file:
#     lines = input_file.read().splitlines()

# with open(output, 'w', encoding='utf-8') as output_file:
#     reversed_lines = reversed(lines)
#     output_file.write("\n".join(reversed_lines))

# print("Successfully completed")



# --- /[Task 4]\ ---
# input_file_path = r'Python KA 05.06.2023/practs in lesson/16/output.txt'
# with open(input_file_path, 'r', encoding='utf-8') as input_file:
#     lines = input_file.readlines()

# last_line_without_comma = None
# for i in range(len(lines) - 1, -1, -1):
#     if "," not in lines[i]:
#         last_line_without_comma = i
#         break

# stars_line = '************\n'

# insert_index = len(lines)
# if last_line_without_comma is not None:
#     insert_index = last_line_without_comma + 1

# lines.insert(insert_index, stars_line)

# output_file_path = r'Python KA 05.06.2023/practs in lesson/16/input.txt'
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     output_file.writelines(lines)

# print("Successfully completed")



# --- /[Task 5]\ ---
# lines = r'Python KA 05.06.2023/practs in lesson/16/output.txt'

# url = r'Python KA 05.06.2023/practs in lesson/16/input.txt'

# user_word = input("Enter letter: ")

# with open(url, 'w', encoding='utf-8') as file:
#     # file.write(lines)
#     counter = 1
#     for line in lines:
#         file.write(f'{counter}. {line}\n')
#         counter += 1

# print("Successfully completed")



# --- /[Task 6]\ ---
# input_file_path = r'Python KA 05.06.2023/practs in lesson/16/output.txt'
# with open(input_file_path, 'r', encoding='utf-8') as input_file:
#     lines = input_file.readlines()

# output_file_path = r'Python KA 05.06.2023/practs in lesson/16/input.txt'
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for line in lines:
#         modified_line = line.replace("*", "@").replace("&", "*").replace("@", "&")
#         output_file.write(modified_line)

# print("Successfully completed")



# --- /[Task 7,8]\ ---
# line = ''
# with open(r'Python KA 05.06.2023/practs in lesson/16/output.txt', 'r', encoding='utf-8') as file:
#     line = file.read()

# def delPunct(line,mark):
#     new_str = ''
#     for li in line:
#         if li not in mark:
#             new_str += li
#     return new_str

# line = line.split()

# with open(r'Python KA 05.06.2023/practs in lesson/16/input.txt', 'w', encoding='utf-8') as file:
#     for item in line:
#         file.write(item + '\n')

# print("Successfully completed")



# --- /[Task 9]\ ---
# file_path = r'Python KA 05.06.2023/practs in lesson/16/output.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()

# character_count = len(content)

# print(f"The number of characters in the file: {character_count}")



# --- /[Task 10]\ ---
file_path = r'Python KA 05.06.2023/practs in lesson/16/output.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)

print(f"The number of lines in the file: {line_count}")