import json

dict_item = {}      # todo (add different type of the dict)
dict_item = {
    1: 'Julia',
    2: [1, 2, 3, 4, 5],
    3: {'name': 'Vadim', 'age': 32, 'salary': 10000}
}
print(dict_item)
# print(3, ':', dict_item[3]['name'], dict_item[3] ['age'])
#
# x = dict_item.get(3).get('salary')        # todo (get item from the dict)
# print(x)
#
# dict_item['city'] = 'Moscow'      # todo (add item to the dict)
# print(dict_item)

# dict_item[1] = 'Georgy'      # todo (change item at the dict)
# print(dict_item)

# del dict_item[2]      # todo (delete item from the dict)
# print(dict_item)

# dict_item.popitem()      # todo (delete the last item from the dict)
# print(dict_item)

# dict_item.clear()     # todo (delete the dict)
# print(dict_item)
#
# dict_item['city'] = 'Moscow'      # todo (get the length of the dict)
# print(dict_item, len(dict_item))

# dict_2 = dict_item      # todo (create a copy of the dict)
# print('dict_2', dict_2)
# dict_2['country'] = 'Russia'
# print('dict_2', dict_2)
# dict_3 = dict_item
# print('dict_3', dict_3)
# dict_4 = dict_item.copy()
# print('dict_4', dict_4)

# for key, value in dict_item.items():        # todo (create a for loop of the dict)
#     print('key:', key, 'value:', value)

# for key in dict_item:
#     print('key:', key)

# for key in dict_item:
#     print('value:', dict_item[key])

# names = ('Vadim', 'Inna', 'Sam')      # todo (create the dict in another way)
# salary = 10000
# dd = dict.fromkeys(names, salary)
# print(dd)

file_path = 'C:/Users/irina/git/Python_learning/Python_project/Python_training/'
file_title = 'Python_json_lesson.json'
full_name = file_path + file_title      # todo (create a json_file)

with open(full_name, 'w') as jf:        # todo (create a json_file of the dict)
    json.dump(dict_item, jf)

with open(full_name, 'r') as jf:        # todo (read a json_file of the dict)
    json_data = jf.read()
    json_object = json.loads(json_data)
    print('json_data', json_data, type(json_data))
    print('json_object', json_object, type(json_object))





