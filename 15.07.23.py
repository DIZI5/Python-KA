# --- /[Task 1]\ ---
# import random

# def double_elements_between_min_max(lst):
#     if not lst:
#         return lst

#     min_index = lst.index(min(lst))
#     max_index = lst.index(max(lst))

#     if min_index > max_index:
#         min_index, max_index = max_index, min_index

#     for i in range(min_index + 1, max_index):
#         lst[i] *= 2

#     return lst

# random_list = [random.randint(1, 100) for _ in range(10)]
# print("Initial list:", random_list)

# result = double_elements_between_min_max(random_list)
# print("List after increasing elements between largest and smallest:", result)



# --- /[Task 2]\ ---
# import random

# def swap_even_odd_elements(lst):
#     for i in range(0, len(lst) - 1, 2):
#         lst[i], lst[i + 1] = lst[i + 1], lst[i]

# random_list = [random.randint(1, 100) for _ in range(10)]
# print("Initial list:", random_list)

# swap_even_odd_elements(random_list)
# print("List after exchanging even and odd elements:", random_list)



# --- /[Task 3]\ ---
# import random

# def find_duplicates(lst):
#     duplicates = []
#     seen = set()

#     for item in lst:
#         if item in seen and item not in duplicates:
#             duplicates.append(item)
#         else:
#             seen.add(item)

#     return duplicates

# random_list = [random.randint(1, 10) for _ in range(15)]
# print("Initial list:", random_list)

# duplicates = find_duplicates(random_list)
# print("Repeating values:", duplicates)



# --- /[Task 4]\ ---
def calculate_sums(matrix):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    total_sum = sum(sum(row) for row in matrix)

    return row_sums, col_sums, total_sum

matrix = [
    [3, 5, 6, 7],
    [12, 1, 1, 1],
    [0, 7, 12, 1]
]

row_sums, col_sums, total_sum = calculate_sums(matrix)

max_width = max(len(str(max(row_sums))), len(str(max(col_sums))), len(str(total_sum))) + 2

for row in matrix:
    print(" ".join(f"{item:{max_width}}" for item in row) + " |", sum(row))

print("-" * (max_width * len(matrix[0]) + 1))

for col_sum in col_sums:
    print(f"{col_sum:{max_width}}", end=" ")

print(f"| {total_sum}")