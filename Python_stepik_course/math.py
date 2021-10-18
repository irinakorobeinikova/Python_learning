x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
c = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
from math import *
print(sqrt(c))


r = float(input())
from math import *
s = pi * (r ** 2)
print(s)
c = 2 * pi * r
print(c)


a, b = float(input()), float(input())
from math import *
s_ar = (a + b) / 2
s_geo = sqrt(a * b)
s_gr = (2 * a * b) / (a + b)
s_kv = sqrt((a ** 2 + b ** 2) / 2)
print(s_ar)
print(s_geo)
print(s_gr)
print(s_kv)


from math import *
x = radians(float(input()))
p = sin(x) + cos(x) + tan(x) ** 2
print(p)


x = float(input())
from math import *
print(ceil(x) + floor(x))


import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep = '\n')

