# int(), +, -, /, *, **
a = int(input())
print(a)
print(a + 1)
print(a + 2)

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(num_1 + num_2 + num_3)

a = int(input())
v = a * a * a
s = 6 * (a * a)
print('Volume =', v)
print('Total surface area =', s)

a = int(input())
b = int(input())
print((3 * ((a + b)**3)) + (275 * (b**2)) - (127*a) - 41)

a = int(input())
print('Following', a, 'digit:', a + 1)
print('For digit', a, 'previous digit:', a - 1)

screen_cost = int(input())
processor_cost = int(input())
keyboard_cost = int(input())
mouse_cost = int(input())
print((screen_cost + processor_cost + keyboard_cost + mouse_cost)*3)

a = int(input())
b = int(input())
c = a + b
print(a, '+', b, '=', c)
c = a - b
print(a, '-', b, '=', c)
c = a * b
print(a, '*', b, '=', c)

a1 = int(input())
d = int(input())
n = int(input())
an = a1 + d * (n - 1)
print(an)

x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep=('---'))

b1 = int(input())
q = int(input())
n = int(input())
bn = b1 * q ** (n - 1)
print(bn)

sm = int(input())
print(sm // 100)

n = int(input())
k = int(input())
print(k // n)
print(k % n)

n = int(input())
print(n % 2 + n // 2)

place = int(input())
print((place + 3) // 4)

min = int(input())
hour = min // 60
min_r = min % 60
print(min, 'minute', '-', 'is', hour, 'hour', min_r, 'minute.')

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Sum =', digit3 + digit2 + digit1)
print('multiply =', digit3 * digit2 * digit1)

num = int(input())
a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = (num // 1000) % 10
print('The figure in the thousands position is equal to', d)
print('The number in the hundreds position is equal to', c)
print('The digit in the tens position is equal to', b)
print('The digit in the position of units is equal to', a)


