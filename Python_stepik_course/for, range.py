for i in range(10):     # todo 7.1.1
    print('Python is awesome!')


text = input()     # todo 7.1.2
num = int(input())
for _ in range(num):
    print(text)


for i in range(6):     # todo 7.1.3
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


x = int(input())     # todo 7.1.4
for i in range(x):
    print('*******************')


text = input()     # todo 7.1.5
for i in range(10):
    print(i, text)


n = int(input())     # todo 7.1.6
for i in range(n + 1):
    print('The square of the number', i, 'equal to', i ** 2)


n = int(input())     # todo 7.1.7
n >= 2
for i in range(n):
    print((n - i) * '*')


m = int(input())     # todo 7.1.8
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, m * (1 + p / 100) ** i)


m = int(input())     # todo 7.2.1
n = int(input())
m <= n
for i in range(m, n+1):
    print(i)


m = int(input())# todo 7.2.2
n = int(input())
for i in range(m, n+1, 1):
    if m < n:
        print(i)
for i in range(m, n-1, - 1):
    if m >= n:
        print(i)


m = int(input())     # todo 7.2.3
n = int(input())
for i in range(m, n-1, - 1):
    if m > n and i % 2 != 0:
        print(i)


m = int(input())     # todo 7.2.4
n = int(input())
m <= n
for i in range(m, n+1, 1):
    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
        print(i)


n = int(input())     # todo 7.2.5
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)