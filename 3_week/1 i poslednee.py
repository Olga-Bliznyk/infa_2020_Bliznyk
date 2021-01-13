s = input()
a = s.find('f')
b = s.rfind('f')
if a != b:
    print(a, b)
elif a == -1:
    print(' ')
else:
    print(a)
