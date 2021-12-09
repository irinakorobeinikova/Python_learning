counter = 0     # todo 7.3.1
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if a <= b and i**3 % 10 == 4 or i**3 % 10 == 9:
        counter = counter + 1
print(counter)


total = 0     # todo 7.3.2
n = int(input())
for i in range(n):
    num = int(input())
    total = total + num
print(total)


from math import *     # todo 7.3.3
counter = 0
n = int(input())
for i in range(1, n + 1):
    counter = counter + 1/i
print(counter - log(n))


total = 0      # todo 7.3.4
n = int(input())
for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total = total + i
print(total)


total = 1     # todo 7.3.5
n = int(input())
n <= 12
for i in range(1, n + 1):
    if n <= 12:
        total = total * i
print(total)
