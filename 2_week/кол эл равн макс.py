x = int(input())
max1 = x
n = 1
while x != 0:
    x = int(input())
    if x > max1:
        max1 = x
        n = 0
    if x == max1:
        n += 1
print(n)
