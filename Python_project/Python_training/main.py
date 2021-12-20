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


file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_training/'
file_name = 'test.txt'

file_path_name = file_path + file_name
with open(file_path_name, 'w') as txt_file:
    name = 'Irina '
    last_name = 'Korobeinikova'
    full_name = name + last_name

    txt_file.write(full_name)
