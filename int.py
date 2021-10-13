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
print('Following', a, 'number:', a + 1)
print('For number', a, 'previous number:', a - 1)

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



