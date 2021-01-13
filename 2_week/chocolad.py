n = int(input())
m = int(input())
k = int(input())
if (k % n == 0 and k <= n * (m - 1)) or (k % m == 0 and k <= m * (n - 1)):
    print('YES')
else:
    print('NO')
