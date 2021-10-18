a = float(input())
b = float(input())
s = 0.5 * a * b
print(s)


s = float(input())
v1 = float(input())
v2 = float(input())
t = s / (v1 + v2)
print(float(t))


a = float(input())
if a == 0:
    print('There is no inverse number')
else:
    print(a ** (-1))


f = float(input())
c = 5/9 * (f - 32)
print(c)


n = float(input())
if n <= 2:
    print(10.5 * n)
elif n > 2:
    print(4 * (n - 2) + (10.5 * 2))


n = float(input())
a = int(n)
c = (n - a) * 10
print (int(c))


n = float(input())
a = int(n)
print(n - a)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('The lowest number =', min(a, b, c, d, e))
print('The biggest number =', max(a, b, c, d, e))


a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print((a+b+c)-max(a, b, c)-min(a, b, c))
print(min(a, b, c))


num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
if (max(a, b, c) - min(a, b, c) == (a + b + c) - max(a, b, c) - min(a, b, c)):
    print('The number is interesting')
else:
    print('The number is not interesting')





