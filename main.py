import sys
print('Введите число от 1 до 10')
a = int(input())

if a > 10:
    sys.exit("error")
if a < 1:
    sys.exit("error")
print('Введите число от 11 до 100')
b = int(input())

c = a*b

if b < 11:
    sys.exit("error")
if b > 100:
    sys.exit("error")
if b > 11:
    print(c)

d = c//10
print(d)
print('Введите число больше чем'), print(d)
z = int(input(''))
x = z//d
print(x)
print(('Ваше счастливое число -'),(x*a))