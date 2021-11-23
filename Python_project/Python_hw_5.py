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

# list_count_five = [45, 38, 2, 14, 0, 17, 60, 95, 115, 314, 105, 208, 18, 28, 76]    # todo 7)
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

# list_divide_1 = []    # todo 9)
#
#
# def func_generation(list_count_five, n):
#     for i in range(0, len(list_count_five), n):
#         a = list_count_five[i:i + n]
#         list_divide_1.append(a)
#         yield a
#
#
# print(list(func_generation(list_count_five, 5)))

# print(list_divide_1)
# list_1 = list_divide_1 [0]
# print(list_1)
# list_2 = list_divide_1 [1]
# print(list_2)
# list_3 = list_divide_1 [2]
# print(list_3)

# def split_even_odd(list_count_five):    # todo 10)
#     even_list = []
#     odd_list = []
#     for i in list_count_five:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             i % 2 != 0
#             odd_list.append(i)
#     print("Even lists: ", even_list)
#     print("Odd lists: ", odd_list)

#
# split_even_odd(list_count_five)

# stars_5 = [list_1, list_2, list_3]    # todo 11
# print('stars_5 =', stars_5)
#
#
# sum_stars_5 = [sum(list_1), sum(list_2), sum(list_3)]    # todo 12
# print('The sum of lists = ', sum_stars_5)
#
# list_sum_more_100 = []    # todo 13)
# list_sum_less_100 = []
#
#
# def split_into_two_lists(sum_stars_5):
#
#     for i in sum_stars_5:
#         if i >= 100:
#             list_sum_more_100.append(i)
#         elif i < 100:
#             list_sum_less_100.append(i)
#         else:
#             print("No lists")
#     return list_sum_more_100, list_sum_less_100
#
#
# print(split_into_two_lists(sum_stars_5))
# print('The list where sum of elements more than 100 = ', list_sum_more_100)
# print('The list where sum of elements less than 100 = ', list_sum_less_100)

u_age = 30
sum_save_month = 100
sum_save_all = [10000, 20000, 30000, 50000, 100000]
item_1 = sum_save_all[0]
item_2 = sum_save_all[1]
item_3 = sum_save_all[2]
item_4 = sum_save_all[3]
item_5 = sum_save_all[4]


def u_salary_ages(age, sum_month, sum_all):
    total_days = item_1 / sum_save_month
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30

    if 18 <= u_age <= 70 and item_1:
        print('If you want to save up', item_1, 'dollars,', 'it will take you:')
        print('years = ', years, 'months =', months, 'days =', days)

    elif 18 <= u_age <= 70 and item_2:
        total_days = item_2 / sum_save_month
        print('If you want to save up', item_2, 'dollars,', 'it will take you:')
        print('years = ', years, 'months =', months, 'days =', days)


print(u_salary_ages(u_age, sum_save_month, sum_save_all))