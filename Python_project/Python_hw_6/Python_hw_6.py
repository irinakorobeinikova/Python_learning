import csv
file_path = '/C:/Users/irina/git/Python_learning/Python_project/Python_hw_6/'
file_name = 'digits.csv'

file_path_name = file_path + file_name

with open(file_path_name, 'w') as emp_csv:
    for i in range(0, 150):
        print(i)
