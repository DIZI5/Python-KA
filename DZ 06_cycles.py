# А
# star = int(input("Enter size: "))
# for i in range(star):
#     print(' ' * i, '*' * star, sep="")
#     star -= 1



# Б
# star = int(input("Enter size: "))
# i = 1
# while i <= star:
#     print('*' * i, sep="")
#     i += 1
#     if i > star:
#         break



# В
# star = int(input("Enter size: "))
# space = 0
# while star > 0:
#     print(' ' * space, '*' * star, sep="")
#     space += 1
#     star -= 2



# Г
# star = int(input("Enter size: "))
# star = star // 2
# space = star
# i = 1
# while space > 0:
#     space -= 1
#     print(' ' * space, '*' * i, sep="")
#     i += 2



# Д
# space = 0
# star = int(input("Enter size: "))
# number = star
# i = 0
# flag = True
# while i < number:
#     i += 1
#     print(' ' * space, '*' * star, sep="")
#     if star == 1:
#         flag = False
#     if flag:
#         star -= 2
#         space += 1
#     else:
#         star += 2
#         space -= 1



# Е
# space = 8
# star = 1
# number = 9
# i = 0
# flag = True
# while i < number:
#     i += 1
#     print('*' * star, ' ' * space, '*' * star, sep="")
#     if star == 5:
#         flag = False
#     if flag:
#         star += 1
#         space -= 2
#     else:
#         star -= 1
#         space += 2



# Ж
# star = int(input("Enter size: "))
# i = 1
# f = star // 2
# while i <= star:
#     if i == 0:
#         break
#     else:
#         print('*' * i, sep="")
#         i += 1
#         if i > f:
#             i -= 2
#             while i > 0:
#                 print('*' * i, sep="")
#                 i -= 1



# З
# star = int(input("Enter size: "))
# space = star
# f = star // 2
# i = 1
# while space > 0:
#     if i == 0:
#         break
#     else:
#         space -= 1
#         print(' ' * space, '*' * i, sep="")
#         i += 1
#         if i > f:
#             i -= 1
#             while space < star:
#                 i -= 1
#                 if i == 0:
#                     break
#                 else:
#                     space += 1
#                     print(' ' * space, '*' * i, sep="")
                


# И
# star = int(input("Enter size: "))
# for i in range(star):
#     print('*' * star, ' ' * i, sep="")
#     star -= 1



# К
# star = int(input("Enter size: "))
# space = star
# i = 1
# while space > 0:
#     space -= 1
#     print(' ' * space, '*' * i, sep="")
#     i += 1