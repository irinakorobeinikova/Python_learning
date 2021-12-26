import csv
file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_hw_6/'

f = open('empty.csv', 'w')      # todo 1

f_1 = open('digits.csv', 'w')      # todo 2
with open('digits.csv', 'w') as digits_csv:
    for i in range(0, 150):
        digits_csv.write(str(i))
        digits_csv.write('\n')

f_3 = open('names.csv', 'w')      # todo 3
