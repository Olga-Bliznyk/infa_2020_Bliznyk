x = int(input())
LastD = x % 10
if LastD == 1 and x != 11:
    print(x, 'korova')
elif 10 <= x <= 20 or 5 <= LastD <= 9 or x == 0 or LastD == 0:
    print(x, 'korov')
else:
    print(x, 'korovy')
