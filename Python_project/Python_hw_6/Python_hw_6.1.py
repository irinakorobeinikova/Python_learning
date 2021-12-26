import csv
file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_hw_6/'


f = open('empty.csv', 'w')      # todo 1


f_1 = open('digits.csv', 'w')      # todo 2
with open('digits.csv', 'w') as digits_csv:
    for i in range(0, 150):
        digits_csv.write(str(i))
        digits_csv.write('\n')


import names
f_3 = open('names.csv', 'w')      # todo 3
user_names = []

with open('names.csv', 'w') as names.csv:
    for i in range(0, 100):
        names_f = []
        name_gen = names.get_full_name()
        names_f.append(name_gen)
        user_names.append(names_f)

        writer = csv.writer(f_3)
        writer.writerows(user_names)