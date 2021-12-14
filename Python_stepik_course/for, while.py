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
        total += 1
    num = int(input())
print(total)


n = int(input())     # todo 7.4.7
counter = 0

while n >= 25:
    counter += 1
    n = n - 25
while n >= 10 and n < 25:
    counter += 1
    n = n - 10
while n >= 5 and n < 10:
        counter += 1
        n = n - 5
while n >= 1 and n < 5:
        counter += 1
        n = n - 1
print(counter)


num = int(input())     # todo 7.5.1
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)


num = int(input())     # todo 7.5.2
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end='')


n = int(input())     # todo 7.5.3
max_digit = 0
min_digit = 9
while n != 0:
    last_digit = n % 10
    if last_digit < min_digit:
        min_digit = last_digit
    if last_digit > max_digit:
        max_digit = last_digit
    n = n // 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
