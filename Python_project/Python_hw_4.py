count = 0   # todo 1)
range_count = 10    # todo 2)
for_count = 0    # todo 3)
run = True    # todo 4)

# while run:  # todo 5)
#     print('Hello Cycle')    # todo 5.1)
#
# while run:  # todo 6)
#     print('Step = ', count)    # todo 6.1)
#     count += 1    # todo 6.2)
#
# while count < range_count:  # todo 7)
#     print('Step = ', count)    # todo 7.1)
#     count += 1  # todo 7.2)

# while count < range_count:    # todo 8)
#     print('Step = ', count)    # todo 8.1)
#     count += 1    # todo 8.2)
#     if count == 3:    # todo 8.3)
#         print('Step =', count, 'If body')

# while run:    # todo 9)
#     print('Step = ', count)   # todo 9.1)
#     count += 1    # todo 9.2)
#     if count == range_count:    # todo 9.3)
#         print('STOP', count)

# for item in range(for_count, range_count):    # todo 10)
#     print('Step =', item)     # todo 10.1)

# for item in range(0, 31):    # todo 11)
#     print('Step =', item)     # todo 11.1)
#     if item == 5:
#         print('item =', item)    # todo 11.2)
#         if item == 10:
#             print('item =', item)    # todo 11.3)
#             if item < 4:
#                 print('item <', item)    # todo 11.4)
#                 if item >=27:
#                     print('item >=', item)    # todo 11.5)

for item in range(0, range_count + 1):    # todo 12)
    print('Step =', item)     # todo 12.1)
    if item == 7:    # todo 12.2)
        inner_count = 0
        print('-- inner_count =', inner_count)
        for inner_item in range(0, item):
            print('--------- Inner_Step =', inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print('inner_count =', inner_count)


for item in range(0, 21):
    print('Stem =', item)
    if 12 > item > 7:















