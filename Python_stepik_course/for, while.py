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


num = int(input()) # todo 7.4.4
while num % 7 == 0:
    print(num)
    num = int(input())


total = 0      # todo 7.4.5
num = int(input())
while num >= 0:
    total += num
    num = int(input())
print(total)


total = 0      # todo 7.4.6
num = int(input())
while num > 0 and num < 6:
    if num == 5: