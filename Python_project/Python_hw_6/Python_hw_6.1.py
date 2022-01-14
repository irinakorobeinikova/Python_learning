import csv
file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_hw_6/'


# f = open('empty.csv', 'w')      # todo 1
#
#
# f_1 = open('digits.csv', 'w')      # todo 2
# with open('digits.csv', 'w') as digits_csv:
#     for i in range(0, 150):
#         digits_csv.write(str(i))
#         digits_csv.write('\n')
#

import names
# f_3 = open('names.csv', 'w')      # todo 3
# user_names = []
#
# with open('names.csv', 'w') as names:
#     for i in range(0, 100):
#         names_f = []
#         name_gen = names.get_full_name()
#         names_f.append(name_gen)
#         user_names.append(names_f)
#
#     writer = csv.writer(f_3)
#     writer.writerows(user_names)
#
# for ii in user_names:
#     print(ii)

import random
import string
# f_4 = open('emails.csv', 'w')      # todo 4
# user_emails = []

# with open('emails.csv', 'w') as emails:
#     for i in range(0, 100):
#         emails_f = []
#         u_emails = (names.get_last_name()).lower() + '.'
#         u_emails += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
#         u_emails += random.choice(string.digits) + random.choice(string.digits) + '@gmail.com'
#
#         emails_f.append(u_emails)
#         user_emails.append(emails_f)
#
#     writer = csv.writer(f_4)
#     writer.writerows(user_emails)
#
# for ii in user_emails:
#     print(ii)
#
#
# f_5 = open('nne.csv', 'w')      # todo 5
# user_data = []
#
# with open('nne.csv', 'a') as nne:
#     for i in range(0, 100):
#         data_f_5 = []
#
#         number = i
#         data_f_5.append(number)
#
#         first_name = names.get_first_name()
#         last_name = names.get_last_name()
#         user_name = first_name + ' ' + last_name
#         data_f_5.append(user_name)
#
#         user_email = (first_name + last_name).lower() + '@gmail.com'
#         data_f_5.append(user_email)
#         user_data.append(data_f_5)
#
#     writer = csv.writer(f_5, lineterminator='\n')
#     writer.writerows(user_data)
#
# with open('nne.csv', 'a') as nne:
#     columns = ['Number', 'Name', 'Email']
#     writer = csv.DictWriter(nne, fieldnames=columns)
#     writer.writeheader()
#

# f_6 = open('combo.csv', 'w')      # todo 11
