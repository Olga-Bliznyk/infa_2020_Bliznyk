x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
v = x1 - x
g = y1 - y
if -1 <= v <= 1 and -1 <= g <= 1:
    print("YES")
else:
    print("NO")
