for i in range(10):
    print('Python is awesome!')


text = input()
num = int(input())
for _ in range(num):
    print(text)


for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


x = int(input())
for i in range(x):
    print('*******************')


text = input()
for i in range(10):
    print(i, text)


n = int(input())
for i in range(n + 1):
    print('The square of the number', i, 'equal to', i ** 2)


n = int(input())
n >= 2
for i in range(n):
    print((n - i) * '*')


m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, m * (1 + p / 100) ** i)


m = int(input())
n = int(input())
m <= n
for i in range(m, n+1):
    print(i)


m = int(input())
n = int(input())
for i in range(m, n+1, 1):
    if m < n:
        print(i)
for i in range(m, n-1, - 1):
    if m >= n:
        print(i)


m = int(input())
n = int(input())
for i in range(m, n-1, - 1):
    if m > n and i % 2 != 0:
        print(i)