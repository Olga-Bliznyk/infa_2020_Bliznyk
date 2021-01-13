a = int(input())
s = a
i = 1
i_2 = 1
while a != 0:
    a = int(input())
    if s == a:
        i += 1
    elif s != a:
        s = a
        if i > i_2:
            i, i_2 = i_2, i
            i = 0
            i += 1
        else:
            i = 0
            i += 1
print(i_2)
