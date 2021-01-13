n = int(input())
max1 = n
i = 0
while n != 0:
    if n > max1:
        max1 = n
        i = 0
    if n == max1:
        i += 1
    n = int(input())
print(i)
