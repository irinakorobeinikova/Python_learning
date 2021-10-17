#if, else
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


#elif
n, k = int(input()),int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")


a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Equilateral triangle')
elif (a == b != c) or (b == c != a) or (a == c != b):
    print('Isosceles triangle')
else:
    print('Versatile triangle')


a, b, c = int(input()), int(input()), int(input())
if a < b < c or a > b > c:
    print(b)
elif b < a < c or b > a > c:
    print(a)
elif a < c < b or a > c > b:
    print(c)


month = int(input())
if month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    print(28)
else:
    print(31)


weight = int(input())
if weight < 60:
    print('Light weight')
elif 60 <= weight < 64:
    print('First average weight')
elif 64 <= weight < 69:
    print('Average weight')


num1 = int(input())
num2 = int(input())
slash = input()
if slash == ('+'):
    print(num1 + num2)
elif slash == ('-'):
    print(num1 - num2)
elif slash == ('*'):
    print(num1 * num2)
elif slash == ('/') and num2 != 0:
    print(num1 / num2)
elif slash == ('/') and num2 == 0:
    print('You cannot divide by zero!')
else:
    print('Invalid operation')


color1 = input()
color2 = input()
if (color1 == 'red' and color2 == 'blue') or (color2 == 'red' and color1 == 'blue'):
    print('purple')
elif (color1 =='red' and color2 == 'yellow') or (color2 =='red' and color1 == 'yellow'):
    print('orange')
elif (color1 == 'blue' and color2 == 'yellow') or (color2 == 'blue' and color1 == 'yellow'):
    print('green')
elif color1 == color2 and (color1 == 'red' or color1 == 'blue' or color1 == 'yellow'):
    print(color1)
elif color1 == color2 and (color1 != 'red' or color1 != 'blue' or color1 != 'yellow'):
    print('wrong color')
else:
    print('wrong color')


n = int(input())
if n == 0:
   print('green')
elif 1 <= n <= 10 and n % 2:
    print('red')
elif 1 <= n <= 10 and n % 2 == 0:
    print('black')
elif 11 <= n <= 18 and n % 2:
    print('black')
elif 11 <= n <= 18 and n % 2 == 0:
    print('red')
elif 19 <= n <= 28 and n % 2:
    print('red')
elif 19 <= n <= 28 and n % 2 == 0:
    print('black')
elif 29 <= n <= 36 and n % 2:
    print('black')
elif 29 <= n <= 36 and n % 2 == 0:
    print('red')
elif n > 36 or n < 0:
    print('input error')



a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < b1 < a2 < b2:
    print("empty set")
elif a2 < b2 < a1 < b1:
    print("empty set")
elif a1 < a2 < b2 < b1:
    print(a2, b2)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a2 < a1 < b1 < b2:
    print(a1, b1)
elif a1 < b1 == a2 < b2:
    print(b1)
elif a2 < b2 == a1 < b1:
    print(b2)
elif a1 == a2 and b1 == b2:
    print(a1,b1)
elif a1 == a2 < b1 < b2:
    print(a1, b1)
elif a2 < a1 < b1 == b2:
    print(a1,b1)
elif a1 < a2 < b2 == b1:
    print(a2,b2)
elif a1 == a2 < b2 < b1:
    print(a2, b2)



