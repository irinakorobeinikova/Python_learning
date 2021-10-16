num = int(input())
if -1 < num < 17:
    print('Belongs')
else:
    print('Does not belong to')


x = int(input())
if x <= -3 or x >= 7:
    print('Belongs')
else:
    print('Does not belong to')


x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Belongs')
else:
    print('Does not belong to')


x = int(input())
if 1000 <= x <= 9999 and (x % 7 ==0 or x % 17 == 0):
    print('YES')
else:
    print('NO')


a = int(input())
b = int(input())
c = int(input())
if a < b + c and c < a + b and b < a + c:
    print('YES')
else:
    print('NO')




