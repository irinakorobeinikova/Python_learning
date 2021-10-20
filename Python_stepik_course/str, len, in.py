# str
print(('"Python is a great language!", ') + ('said Fred. ') + ('''"I don't ever remember having this much fun before."'''))


first_name = str(input())
last_name = str(input())
print("Hello", first_name, last_name + '!', "You just delved into Python")


team = str(input())
print('Football team', team, 'has a length of', len(team), 'symbols')


city1 = str(input())
city2 = str(input())
city3 = str(input())
a = len(city1)
b = len(city2)
c = len(city3)
if a == min(a, b, c):
    print(city1)
elif b == min(a, b, c):
    print(city2)
elif c == min(a, b, c):
    print(city3)

if a == max(a, b, c):
    print(city1)
elif b == max(a, b, c):
    print(city2)
elif c == max(a, b, c):
    print(city3)


a = str(input())
b = str(input())
c = str(input())
a1 = len(a)
b1 = len(b)
c1 = len(c)
if (2 * b1 - c1 - a1) * (2 * c1 - b1 - a1) * (2 * a1 - b1 - c1) == 0:
    print('YES')
else:
    print('NO')


s = str(input())
if 'blue' in s:
    print('YES')
else:
    print('NO')


s = str(input())
if 'saturday' in s or 'sunday' in s:
    print('YES')
else:
    print('NO')
