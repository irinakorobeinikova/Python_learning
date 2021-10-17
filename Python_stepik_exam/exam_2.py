x = int(input())
if x % 100 == 0:
    print('YES')
else:
    print('NO')


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 + b1 + a2 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')


age = int(input())
gender = input()
if 10 <= age <= 15 and gender == 'f':
    print('YES')
else:
    print('NO')


num = int(input())
if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('wrong')


num = int(input())
if num % 2 != 0:
    print('YES')
elif num % 2 == 0 and 2 <= num <= 5:
    print('NO')
elif num % 2 == 0 and 6 <= num <= 20:
    print('YES')
elif num % 2 == 0 and num > 20:
    print('NO')


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 + b1 == a2 + b2:
    print('YES')
elif a1 - b1 == a2 - b2:
    print('YES')
else:
    print('NO')


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 - a2) * (b1 - b2) == 2 or (a1 - a2) * (b1 - b2) == -2:
    print('YES')
else:
    print('NO')


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 + b1 == a2 + b2:
    print('YES')
elif a1 - b1 == a2 - b2:
    print('YES')
elif a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')




