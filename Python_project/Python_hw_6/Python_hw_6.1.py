import csv
file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_hw_6/'
# file_name = 'empty.csv'                                                             # todo (f = open('test.txt', 'w')
# file_path_name = file_path + file_name

f = open('empty.csv', 'w')      # todo 1

f_1 = open('digits.csv', 'w')      # todo 2
with open('digits.csv', 'w') as digits_csv:
    for i in range(0, 150):
        digits_csv.write(str(i))
        digits_csv.write('\n')
