a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = (d * e - b * f) / (d * a - b * c)
y = (e * c - f * a) / (b * c - d * a)
if x % 1 == 0 and y % 1 == 0:
    print(int(x), int(y))
elif x % 1 > 0 and y % 1 == 0:
    print(x, int(y))
elif x % 1 == 0 and y % 1 > 0:
    print(int(x), y)
elif x % 1 > 0 and y % 1 > 0:
    print(x, y)
