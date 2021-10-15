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