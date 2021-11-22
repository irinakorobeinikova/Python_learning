# list_numbers = list(range(30))    # todo 1)
# print(list_numbers)
#
# list_numbers_even = list(range(0, 35, 2))    # todo 2)
# print(list_numbers_even)
#
# list_numbers_odd = list(range(1, 35, 2))    # todo 3)
# print(list_numbers_odd)

# list_even = [0, 1, 35, 48, 25, 65, 24]    # todo 4)
# print(list_even)
#
# for i in list_even:
#     if i % 2 == 0:
#         print('i =', i, 'even')
#
# list_odd = [1, 3, 14, 36, 25, 48, 93]    # todo 5)
# print(list_odd)
#
# for i in list_odd:
#     if i % 2 != 0:
#         print('i =', i, 'odd')
#
# list_for_five = [15, 62, 23, 45, 25, 47, 32, 5]    # todo 6)
# print(list_for_five)
#
# for i in list_for_five:
#     if i % 5 == 0:
#         print('i =', i)

list_count_five = [45, 38, 2, 14, 0, 17, 60, 95, 115, 314, 105, 208, 18, 28, 76]    # todo 7)
# print(list_count_five)
#
# counter = 0
#
# for i in list_count_five:
#     if i % 5 == 0:
#         counter += 1
# print('counter =', counter)

# from random import randint    # todo 8)
# for i in range(10):
#     print(randint(1, 100))

list_divide_1 = []    # todo 9)


def func_generation(list_count_five, n):
    for i in range(0, len(list_count_five), n):
        a = list_count_five[i:i + n]
        list_divide_1.append(a)
        yield a


print(list(func_generation(list_count_five, 5)))

print(list_divide_1)
list_1 = list_divide_1 [0]
print(list_1)
list_2 = list_divide_1 [1]
print(list_2)
list_3 = list_divide_1 [2]
print(list_3)

# def split_even_odd(list_count_five):    # todo 10)
#     even_list = []
#     odd_list = []
#     for i in list_count_five:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             i % 2 != 0
#             odd_list.append(i)
#     print("Even lists:", even_list)
#     print("Odd lists:", odd_list)

#
# split_even_odd(list_count_five)

stars_5 = [list_1, list_2, list_3]    # todo 11
print(stars_5)



