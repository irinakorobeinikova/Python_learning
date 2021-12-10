word = input()     # todo 7.4.1
while word != 'THE END':
    print(word)
    word = input()


word = input()     # todo 7.4.2
while word != 'THE END' and word != 'The end':
    print(word)
    word = input()


text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    total += 1
    text = input()
print(total)