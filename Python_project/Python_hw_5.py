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

# import math     # todo 14)
# u_age = int(input('Enter your age '))
# sum_save_month = int(input('Enter your sum of monthly savings '))
# sum_save_all = [10000, 20000, 30000, 50000, 100000]
#
#
# def u_savings(years):     # todo 16)
#     for i in sum_save_all:
#         if 0 < sum_save_month < 10000 and 14 <= u_age <= 70:
#             total = i / sum_save_month
#             years = math.floor(total / 12)
#             months = math.ceil(total % 12)
#             print('If you want to save up', i, 'dollars, it will take you', years, 'years', months, 'month')
#
#         else:
#             print('Enter valid data, please')
#             break
#
#
# u_savings(u_age)
import datetime

import names

# for i in range(0, 71):     # todo 17)
#     user_name_list = names.get_full_name()
#     print('Your name is', user_name_list)

import uuid     # todo 17)

# for i in range(0, 71):
#     file_name_list = str(uuid.uuid4())
#     print(i, 'file_name =', file_name_list)


import names, randomtimestamp as rd    # todo 18)
#
# full_list_of_lists = []
#
# for i in range(5):
#     one_list_of_name_date = []
#     full_list_of_lists.append(one_list_of_name_date)
#
#     name_gen = names.get_full_name()
#     one_list_of_name_date.append(name_gen)
#
#     date_gen = str(rd.random_date())
#     one_list_of_name_date.append(date_gen)
#
# print(full_list_of_lists)

import random     # todo 19)
import string

employees = []

for i in range(70):
    one_list_of_name_date = []
    employees.append(one_list_of_name_date)

    name_gen = names.get_full_name()
    one_list_of_name_date.append(name_gen)

    u_login = random.choice(string.ascii_uppercase)
    u_login += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    u_login += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    one_list_of_name_date.append(u_login)

    password = random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.digits)
    password += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    password += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.punctuation)
    one_list_of_name_date.append(password)

    u_email = random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    u_email += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    one_list_of_name_date.append(u_email)

    date_gen = str(rd.random_date())
    one_list_of_name_date.append(date_gen)

print('The list of employees:', employees)


family = []    # todo 20)
#True = 'married'
#False = 'single'


for i in range(70):
    one_list_of_family = []
    family.append(one_list_of_family)

    u_login = random.choice(string.ascii_uppercase)
    u_login += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    u_login += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    one_list_of_family.append(u_login)

    name_gen = names.get_full_name()
    one_list_of_family.append(name_gen)

    random_bit = random.getrandbits(1)
    random_boolean = bool(random_bit)
    one_list_of_family.append(random_boolean)

print('The list of family:', family)


gender = []     # todo 21)

for i in range(70):
    one_list_of_gender = []
    gender.append(one_list_of_gender)

    name_gen = names.get_full_name()
    one_list_of_gender.append(name_gen)

    u_login = random.choice(string.ascii_uppercase)
    u_login += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    u_login += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    one_list_of_gender.append(u_login)

    female = 0
    male = 1
    num_gender = random.randint(0, 1)
    one_list_of_gender.append(num_gender)

print('The list of gender:', gender)


salary = []     # todo 22)

for i in range(70):
    one_list_of_salary = []
    salary.append(one_list_of_salary)

    u_login = random.choice(string.ascii_uppercase)
    u_login += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    u_login += random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    one_list_of_salary.append(u_login)

    name_gen = names.get_full_name()
    one_list_of_salary.append(name_gen)

    salary_list = list(range(300, 5000))
    salary_gen = random.choice(salary_list)
    one_list_of_salary.append(salary_gen)

print('The list of salary:', salary)


# salary_name_list = []     # todo 23)
#
# for i in range(0, len(salary)):
#     all_salary = salary[i][2]
#     all_names = salary[i][1]
#     if 1500 >= all_salary <= 3000:
#         salary_name_list.append(all_names)
#         #print(all_names, all_salary, '$')
#
# print('salary_name_list', salary_name_list)


men_name_list = []     # todo 24)

# for i in range(0, len(gender)):
#     all_names_gen = gender[i][0]
#     all_gender = gender[i][2]
#     if all_gender == 1:
#         men_name_list.append(all_names_gen)
#         print(all_names_gen, all_gender)
#
# print('men_name_list:', men_name_list)

#
# women_name_list = []     # todo 25)
#
# for i in range(0, len(gender)):
#     all_names_gen = gender[i][0]
#     all_gender = gender[i][2]
#     if all_gender == 0:
#         women_name_list.append(all_names_gen)
#         print(all_names_gen, all_gender)
#
# print('women_name_list:', women_name_list)

#
# single_men_list_family = []     # todo 26)
#
# for i in range(0, len(family)):
#     female = 0
#     male = 1
#     gender_from_gender = gender[i][2]
#     family[i].insert(3, gender_from_gender)
#
#     all_names_gen = family[i][1]
#     marital_status = family[i][2]
#     gender_family = family[i][3]
#
#     if gender_family == 1 and marital_status == False:
#         single_men_list_family.append(all_names_gen)
#
# print(family)
# print('The single men list:', single_men_list_family)
#

# single_women_list_family = []     # todo 27)
#
# for i in range(0, len(family)):
#     female = 0
#     male = 1
#     gender_from_gender = gender[i][2]
#     family[i].insert(3, gender_from_gender)
#
#     all_names_gen = family[i][1]
#     marital_status = family[i][2]
#     gender_family = family[i][3]
#
#     if gender_family == 0 and marital_status == False:
#         single_women_list_family.append(all_names_gen)
#
# print('The single women list:', single_women_list_family)


# full_list = []     # todo 28)
#
# for i in range(0, len(family)):
#     family[i][1] = employees[i][0]     # female = 0, male = 1
#
#     family[i].insert(3, gender[i][2])
#
#     family[i].insert(4, salary[i][2])
#
#     name_from_employees = family[i][1]
#     marital_status_family = family[i][2]
#     gender_from_gender = family[i][3]
#     salary_from_salary = family[i][4]
#
#     if gender_from_gender == 1 and salary_from_salary >= 1500 and marital_status_family == False:
#         full_list.append(name_from_employees)
#         # full_list.append(marital_status_family)
#         # full_list.append(salary_from_salary)
#
# print('The full list:', full_list)


def complete_list(u_name, u_family, u_gender, u_salary):     # todo 29)

    full_list = []
    print('The full list:', full_list)

    for i in range(0, len(family)):
        family[i][1] = employees[i][0]     # female = 0, male = 1

        family[i].insert(3, gender[i][2])

        family[i].insert(4, salary[i][2])

        name_from_employees = family[i][1]
        marital_status_family = family[i][2]
        gender_from_gender = family[i][3]
        salary_from_salary = family[i][4]

        if gender_from_gender == 1 and salary_from_salary >= 1500 and marital_status_family == False:
            full_list.append(name_from_employees)
        # full_list.append(marital_status_family)
        # full_list.append(salary_from_salary)

    complete_list(name_from_employees, marital_status_family, gender_from_gender, salary_from_salary)
