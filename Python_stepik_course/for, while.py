word = input()     # todo 7.4.1
while word != 'THE END':
    print(word)
    word = input()


word = input()     # todo 7.4.2
while word != 'THE END' and word != 'The end':
    print(word)
    word = input()


text = input()     # todo 7.4.3
total = 0
while text != 'stop' and text != 'enough' and text != 'quite':
    total += 1
    text = input()
print(total)