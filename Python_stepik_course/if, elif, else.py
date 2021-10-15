qwerty1 = input()
qwerty2 = input()
if qwerty1 == qwerty2:
    print('Password is correct')
else:
    print('Password is wrong')


num = int(input())
if num % 2 == 0:
    print('even')
else:
    print('odd')


num = int(input())
digit4 = num % 10
digit3 = (num // 10) % 10
digit2 = (num // 100) % 10
digit1 = (num // 1000) % 10
if digit1 + digit4 == digit2 - digit3:
    print('YES')
else:
    print('NO')


access = int(input())
if access >= 18:
    print('Access is allowed')
else:
    print('Access denied')


num1 = int(input())
num2 = int(input())
num3 = int(input())
if num2 - num1 == num3 - num2:
    print('YES')
else:
    print('NO')


a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b:
    a = b
if c > d:
    c = d
if a < c:
    print(a)
else:
    print(c)


age = int(input())
if age <= 13:
    print('childhood')
if 14 <= age <= 24:
    print('youth')
if 25 <= age <= 59:
    print('maturity')
if age >= 60:
    print('old age')


a = int(input())
b = int(input())
c = int(input())
if a > 0:
    a = a
else:
    a = 0
if b > 0:
    b = b
else:
    b = 0
if c > 0:
    c = c
else:
    c = 0
result = a + b + c
print(result)