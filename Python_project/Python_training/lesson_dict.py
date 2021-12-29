dict_item = {}      # todo (add different type of the dict)
dict_item = {
    1: 'Julia',
    2: [1, 2, 3, 4, 5],
    3: {'name': 'Vadim', 'age': 32, 'salary': 10000}
}
# print(3, ':', dict_item[3]['name'], dict_item[3] ['age'])

# x = dict_item.get(3).get('salary')        # todo (get item from the dict)
# print(x)

# dict_item['city'] = 'Lviv'      # todo (add item to the dict)
# print(dict_item)

# dict_item[1] = 'Georgy'      # todo (change item at the dict)
# print(dict_item)

# del dict_item[2]      # todo (delete item from the dict)
# print(dict_item)

dict_item.popitem()      # todo (delete the last item from the dict)
print(dict_item)

