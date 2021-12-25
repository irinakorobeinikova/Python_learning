import names, randomtimestamp as rd

import time
import names

# def test_1(param_1):
#     result = param_1 + 3
#     print('param_1 =', param_1)
#     print('result =', result)
# test_1(5)
#
# for i in range(0, 3):
#     user_name = names.get_full_name()
#
#     print(user_name)
#

    # test_1(i)
    # time.sleep(.500)
    # print('===========================')



# def test_1(param_1):
#     result = param_1 + 3
#     print('param_1 =', param_1)
#     print('result =', result)
# test_1(5)
#
# for i in range(0, 3):
#     user_name = names.get_full_name()
#     print(result)

#
# for i in range(0, 3):
#     user_name = names.get_full_name()
#
#     test_1(user_name)
#     print(user_name)

# def test_1(param_1):
#     result = 'Hello, ' + param_1
#
# one_list_of_name_date = []
# def test_1(u_name, b_date):
#
#     result = [u_name + ' ' + str(b_date)]
#     one_list_of_name_date.append(result)
#     print(one_list_of_name_date)
#
# for i in range(1):
#     user_name = names.get_full_name()
#     gen_date = rd.random_date()

    # test_1(user_name, gen_date)
import random
#
#
# def test_1(u_name, b_date, u_weight):
#     result = 'Hello, ' + u_name + 'you was born ' + str(b_date)
#     current_weight = u_weight
#     print(result)
#     print('Now your current weight =', current_weight)
#
#
# def u_weight():
#     random_int = random.randint(45, 100)
#     return random_int
#
#
# for i in range(0, 3):
#     user_name = names.get_full_name()
#     gen_date = rd.random_date()
#     user_weight = u_weight()
#
#     test_1(user_name, gen_date, user_weight)
import datetime

# x = datetime.datetime.now()
#
# print(x)
from datetime import date

# for a in range(5):
#     print(datetime.date(2011, 5, 3) + datetime.timedelta(a))
#
# from datetime import date
#
# start_date = date(2011, 5, 3)
# end_date = date(2011, 5, 10)
#
# for i in range(start_date.toordinal(), end_date.toordinal())
#
#     a = date.fromordinal(i)
import names
#=====================================================================================================================

file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_training/'     # todo 'How to create a path to the file'
# file_name = 'test.txt'
# file_path_name = file_path + file_name

# with open(file_path_name, 'w') as txt_file:     # todo 'How to write data to a file'
#     name = 'Irina '
#     last_name = 'Korobeinikova\n'
#     full_name = name + last_name
#
#     txt_file.write(full_name)
#
# with open(file_path_name, 'a') as txt_file:     # todo 'How to add (input) data to a file'
#     name = input('name: ')
#     last_name = input('last_name: ')
#     full_name = name + ' ' + last_name + '\n'
#
#     txt_file.write(full_name)
#
# with open(file_path_name, 'a') as txt_file:     # todo 'How to add data to a file'
#     name = 'Vadim '
#     last_name = 'Ksendzov'
#     full_name = name + last_name
#
#     txt_file.write(full_name)

names_list = ['Pavel', 'Alex', 'Julia', 'Sam']
# with open(file_path_name, 'w') as txt_file:     # todo 'How to add data to a file (for)'
#     for i in names_list:
#         txt_file.write(i)
#         txt_file.write('\n')

age_list = ['28', '35', '48', '55']
# with open(file_path_name, 'w') as txt_file:     # todo 'How to add data to a file (join)'
#     txt_file.write('\n'.join(age_list))

# with open(file_path_name, 'r') as txt_file:     # todo 'How to read data'
#     read_f = txt_file.readlines()
#     for i in read_f:
#         print(i.rstrip(), type(i))

import csv


# file_name = 'test.csv'
# csv_file_name = file_path + file_name

# users_list = [      # todo 'How to create data to csv file'
#     ['Vadim', 32],
#     ['Alex', 36],
#     ['Olga', 28]
# ]
#
# with open(csv_file_name, 'w') as cf:
#     writer = csv.writer(cf)
#     writer.writerows(users_list)

#
# users_list_next = [     # todo 'How to generate data to a csv file'
#     ['Peter', 23],
#     ['Alexey', 34],
#     ['Veronika', 22],
#     ['Jon', 39]
# ]
# new_users_list = []
# for item in range(0, 100):
#     for ul_item in users_list_next:
#         name_age = []
#         new_name = ul_item[0] + '_' + str(item)
#         new_age = 10 + item
#         name_age.append(new_name)
#         name_age.append(new_age)
#         new_users_list.append(name_age)
#         # print(name_age)
#
# for ii in new_users_list:
#     print(ii)
#
# with open(csv_file_name, 'w') as cf:    # todo 'How to add data to a csv file'
#     writer = csv.writer(cf)
#     writer.writerows(new_users_list)


# file_name = 'csv_lesson_8.csv'      # todo 'How to create a csv file'
# csv_file_name = file_path + file_name
#
# user_name_list = [      # todo 'How to create data to csv file'
#     ['Kate', 35],
#     ['Alex', 26],
#     ['Pavel', 37]
# ]
#
# second_user_list = []

# with open(csv_file_name, 'a') as csv_f:     # todo 'How to add data to a csv file'
#     writer = csv.writer(csv_f)
#     row_1 = ['Vlas', 25]
#     writer.writerow(row_1)

#===================================================
# file_name = 'csv_lesson_8_headers.csv'      # todo 'How to add headers to the file'
# csv_file_name = file_path + file_name
#
# user_name_list = [
#     ['Kate', 35],
#     ['Alex', 26],
#     ['Pavel', 37]
# ]
#
# second_user_list = []
# with open(csv_file_name, 'w') as cf:
#     columns = ['name', 'age']
#     writer = csv.DictWriter(cf, fieldnames=columns)
#     writer.writeheader()
#     row_2 = {'name': 'Steve', 'age': 30}
#     writer.writerow(row_2)
#==================================

file_name = 'csv_lesson_8_headers.csv'      # todo 'How to add data (dict) to the file'
csv_file_name = file_path + file_name

user_name_list = [
    ['Kate', 35],
    ['Alex', 26],
    ['Pavel', 40]
]

users_dict = [
    {'name': 'Maggy', 'age': 22},
    {'name': 'Roman', 'age': 26},
    {'name': 'Ben', 'age': 34}
]

second_user_list = []
#
# with open(csv_file_name, 'a') as csv_f:
#     columns = ['name', 'age']
#     writer = csv.DictWriter(csv_f, fieldnames=columns)
#     writer.writerows(users_dict)


with open(csv_file_name, 'r') as csv_f:     # todo 'How to read the csv file'
    reader = csv.DictReader(csv_f)
    line_count = 0