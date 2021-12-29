dict_item = {}      # todo (add different type of dict)
dict_item = {
    1: 'Julia',
    2: [1, 2, 3, 4, 5],
    3: {'name': 'Vadim', 'age': 32, 'salary': 10000}
}
# print(3, ':', dict_item[3]['name'], dict_item[3] ['age'])

# x = dict_item.get(3).get('salary')        # todo (get item from dict)
# print(x)

dict_item['city'] = 'Lviv'      # todo (add item to dict)
print(dict_item)